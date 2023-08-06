import os

import click
import yaml

from ksfctl.generate.cpp.generator import cpp_gen, cpp_sdk_gen


@click.group(context_settings={'help_option_names': ['-h', '--help']})
@click.pass_context
def cli(ctx):
    pass


help_str = f'''\
ksf文件解析器\n
解析ksf文件到其他语言，目前支持[c++(cpp), python(py), java, node.js(node), go]\n
关键字: \n
module, struct, enum, interface, const, bool, int, long, short, byte, double, float, string, map, vector, using, import, export, require, optional, key, out, false, true\n
基础元素: 以模块(module)为核心，文件包含关系为树状结构，模块包含接口interface，结构struct，枚举enum，常量const等元素\n
适合场景: 用于定义协议，生成对应的代码，用于服务端和客户端的通信\n
'''


@cli.group(name='parse', help=help_str,
           context_settings={'help_option_names': ['-h', '--help']})
@click.pass_context
def parse(ctx):
    pass


@parse.command(name='cpp', context_settings={'help_option_names': ['-h', '--help']})
@click.pass_context
@click.argument('ksf_files', nargs=-1, required=True, type=str)
@click.option('-i', '--include', '--include-path', multiple=True, help='ksf协议文件搜索路径')
@click.option('-d', '--dir', '--dest', 'destination_dir', multiple=False, help='生成的头文件存放的路径')
@click.option('--sdk-export', 'sdk_export', multiple=False, default="ksf_export.h",
              help='[sdk模式生效]生成的sdk导出符号头文件名(默认为ksf_export.h)')
@click.option('--sdk-invoke', 'sdk_invoke', multiple=False, default="ksf_invoke.h",
              help='[sdk模式生效]生成的sdk调用头文件名(默认为ksf_invoke.h)')
@click.option('-f', '--config-file', 'config_file', multiple=False, help='注入的脚本文件yaml')
@click.option('-c', '--config', 'config', multiple=False, help='注入的脚本yaml')
@click.option('--export', 'export_symbols', multiple=True, help='需要导出的结构体或者函数体')
@click.option('--replace_ns', '--replace-ns', multiple=False, help='(将被废弃)替换namespace')
@click.option('--replace-namespace', nargs=2, multiple=True, type=str, help='(推荐)将指定命名空间替换为另一个命名空间')
@click.option('--replace-include-path', nargs=2, multiple=True, type=str, help='(推荐)替换头文件路径')
@click.option('--push-function', multiple=True,
              help='携带push模式的函数名, 用于生成push函数，参数形式为module.interface.operator')
@click.option('--ignore-relative-path', 'ignore_relative_path', is_flag=True, flag_value=True, default=False,
              help='忽略依赖目录')
@click.option('--check-default/--no-check-default', default=True, help='是否打包默认值')
@click.option('--ksf/--no-ksf', 'ksf', is_flag=True, default=False, help='是否ksf内部模块')
@click.option('--json/--no-json', 'json', is_flag=True, default=True, help='是否生成Json格式')
@click.option('--sql/--no-sql', 'sql', is_flag=True, default=False, help='是否生成Sql接口')
@click.option('--rpc/--no-rpc', 'rpc', is_flag=True, default=True, help='是否生成RPC接口')
@click.option('--current-priority/--no-current-priority', 'current_priority', is_flag=True, default=True,
              help='是否优先使用当前目录')
@click.option('--trace/--no-trace', 'trace', is_flag=True, default=False, help='是否需要调用链追踪逻辑')
@click.option('--push/--no-push', 'push', is_flag=True, default=True, help='是否需要推送接口')
@click.option('--param-rvalue-ref/--no-param-rvalue-ref', 'param_rvalue_ref', is_flag=True, default=False,
              help='是否参数使用右值引用')
@click.option('--sdk-mode', 'sdk_mode', is_flag=True, default=False,
              help='启动sdk模式，会生成一个纯结构体的头文件和一个纯rpc的头文件')
@click.option('--verbose', 'verbose', is_flag=True, flag_value=True, default=False, help='是否打印详细信息')
@click.option('--with-ksf', 'ksf', is_flag=True, flag_value=True, default=False, help='ksf内部模块')
@click.option('--unjson', 'json', is_flag=True, flag_value=False, default=True, help='不生成Json格式')
@click.option('--os', 'rpc', is_flag=True, default=True, flag_value=False, help='不生成RPC接口')
@click.option('--currentPriority', 'current_priority', is_flag=True, flag_value=True, default=True,
              help='优先使用当前目录')
@click.option('--without-trace', 'trace', is_flag=True, flag_value=False, default=False, help='不需要调用链追踪')
@click.option('--with-push', 'push', is_flag=True, flag_value=True, default=True, help='需要推送接口')
@click.option('--with-param-rvalue-ref', 'param_rvalue_ref', is_flag=True, flag_value=True, default=False,
              help='参数使用右值引用')
def parse_cpp(ctx, ksf_files, include, destination_dir, replace_ns, replace_namespace, replace_include_path,
              push_function, sdk_mode, verbose, sdk_export, sdk_invoke, export_symbols, config_file,
              config, **kwargs):
    ctx.help_option_names += ['-h']
    repl_ns_dict = {}

    def print_verbose(msg):
        if verbose:
            click.echo(msg)

    """命令的描述"""
    print_verbose(f'文件列表: {ksf_files}')

    """将指定命名空间替换为另一个命名空间"""
    if replace_namespace:
        for origin, actual in replace_namespace:
            repl_ns_dict[origin] = actual
            print_verbose(f'将命名空间 {origin} 替换为 {actual}。')
    elif replace_ns:
        for replace_namespace_str in replace_ns.split(";"):
            origin, actual = replace_namespace_str.split("/")
            repl_ns_dict[origin] = actual
            print_verbose(f'将命名空间 {origin} 替换为 {actual}。')
    else:
        print_verbose('未指定任何命名空间的置换。')

    """替换头文件路径"""
    repl_inc_dict = {}
    if replace_include_path:
        for origin, actual in replace_include_path:
            repl_inc_dict[origin] = actual
            print_verbose(f'将头文件路径 {origin} 替换为 {actual}。')
    else:
        print_verbose('未指定任何头文件路径的置换。')

    """生成文件位置"""
    if destination_dir:
        print_verbose(f'生成文件位置: {destination_dir}')
    else:
        destination_dir = os.getcwd()
        print_verbose(f'生成文件位置: {destination_dir}')

    """头文件包含路径"""
    if include:
        print_verbose(f'包含路径: {include}')
    else:
        print_verbose(f'未指定包含路径，将只在当前路径搜索')

    """携带push模式的函数名, 用于生成push函数，参数形式为module.interface.operator"""
    if push_function:
        print_verbose(f'推送模式的函数名: {push_function}')
    else:
        print_verbose(f'无指定推送模式的函数')

    """解析配置文件"""
    if config_file:
        with open(config_file, 'r') as f:
            export_symbols = set()
            configs = yaml.safe_load(f.read())
            # print(configs)
            for config in configs:
                module = config['module']
                if 'namespace' in config:
                    repl_ns_dict[module] = config['namespace']

                for element_type, elements in config['export'].items():
                    if element_type == 'interface':
                        for element in elements:
                            if isinstance(element, dict):
                                for interface, functions in element.items():
                                    if functions is None or len(functions) == 0:
                                        export_symbols.add(f'{module}.{interface}')
                                    else:
                                        for function in functions:
                                            export_symbols.add(f'{module}.{interface}.{function}')
                            else:
                                export_symbols.add(f'{module}.{element}')
                    else:
                        for element in elements:
                            export_symbols.add(f'{module}.{element}')

    """是否检测默认值"""
    print_verbose(f"是否检测默认值：{kwargs['check_default']}")

    """是否ksf内部模块"""
    print_verbose(f"是否ksf内部模块：{kwargs['ksf']}")

    """是否生成Json序列化接口"""
    print_verbose(f"是否生成Json序列化接口：{kwargs['json']}")

    """是否生成Sql接口"""
    print_verbose(f"是否生成Sql接口：{kwargs['sql']}")

    """是否生成RPC接口"""
    print_verbose(f"是否生成RPC接口：{kwargs['rpc']}")

    """是否优先使用当前目录"""
    print_verbose(f"是否优先使用当前目录：{kwargs['current_priority']}")

    """是否需要调用链追踪逻辑"""
    print_verbose(f"是否需要调用链追踪逻辑：{kwargs['trace']}")

    """是否参数使用右值引用"""
    print_verbose(f"是否参数使用右值引用：{kwargs['param_rvalue_ref']}")

    """忽略依赖目录"""
    print_verbose(f"忽略依赖目录：{kwargs['ignore_relative_path']}")

    """解析所有的flags，携带with_头"""
    kwargs_with_prefix = {}
    for k, v in kwargs.items():
        kwargs_with_prefix.update({f'with_{k}': v})

    if sdk_mode:
        """启动sdk模式，会生成一个纯结构体的头文件和一个纯rpc的头文件"""
        if sdk_export:
            print_verbose(f"生成纯结构体头文件：{sdk_export}")

        if sdk_invoke:
            print_verbose(f"生成纯rpc头文件：{sdk_invoke}")

        if export_symbols:
            print_verbose(f"导出头文件：{export_symbols}")

        cpp_sdk_gen(files=ksf_files,
                    repl_ns_dict=repl_ns_dict,
                    repl_inc_dir=repl_inc_dict,
                    include_dirs=include,
                    destination_dir=destination_dir,
                    push_functions=push_function,
                    export_symbols=export_symbols,
                    sdk_invoke=sdk_invoke,
                    sdk_export=sdk_export,
                    flags=kwargs_with_prefix)
    else:
        cpp_gen(files=ksf_files,
                repl_ns_dict=repl_ns_dict,
                repl_inc_dir=repl_inc_dict,
                include_dirs=include,
                destination_dir=destination_dir,
                push_functions=push_function,
                flags=kwargs_with_prefix)


if __name__ == '__main__':
    cli()
    exit(0)

    runner = CliRunner()
    result1 = runner.invoke(cli, ['-h'])
    assert result1.exit_code == 0

    result2 = runner.invoke(cli, ['--help'])
    assert result2.exit_code == 0
