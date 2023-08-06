from ksfctl.parser.ksf_parser import *
from ksfctl.parser.ksf_yacc import generate

class OrmParser:
    def __init__(self, ast, repl_ns_dict, repl_inc_dir, destination, **kwargs):
        self.__dict__.update(kwargs)
        self.ast = ast

        Path(destination).mkdir(parents=True, exist_ok=True)
        self.dest_path = Path(destination)
        self.repl_ns_dict = repl_ns_dict  # 命名空间替换字典
        self.repl_inc_dir = repl_inc_dir  # 头文件替换字典

    def __getattr__(self, name):
        if name.startswith('with_') and not hasattr(self, 'name'):
            return False
        return super().__getattr__(name)

    @staticmethod
    def endl():
        return '\n'

    @staticmethod
    def get_column_widths(lst):
        # 创建一个空列表来保存每列的最大宽度
        column_widths = [0] * len(lst[0])

        # 遍历列表中的所有元素，找到每列的最大宽度
        for item in lst:
            for i, value in enumerate(item):
                column_widths[i] = max(column_widths[i], len(value))

        return column_widths

    def add_include(self, header):
        """添加头文件"""
        if header in self.inc_native:
            self.inc_native[header] = True
        elif header in self.inc_depends:
            self.inc_native[header] = True

    def enable_push(self, operator_name):
        """启用推送函数"""
        if not self.push_functions or operator_name in self.push_functions:
            return True
        return False

    def enable_async_rsp(self, operator_name):
        """启用异步响应"""
        if not self.push_functions or operator_name not in self.push_functions:
            return True
        return False

    def get_repl_headfile(self, header):
        if header[1:-1] in self.repl_inc_dir:
            return f'"{self.repl_inc_dir[header[1:-1]]}"'
        return header

    def get_module(self, module):
        if module in self.repl_ns_dict:
            return self.repl_ns_dict[module]
        return module

    def get_full_name(self, module, name):
        return f"{self.get_module(module)}::{name}"

    def get_ns_begin(self, module, with_endl=True):
        """获取命名空间开始，将::替换为{"""
        ns = self.get_module(module)
        braces = ""
        for ns_simple in ns.split('::'):
            braces += f'namespace {ns_simple} {{{self.endl() if with_endl else " "}'
        return f"{braces}"

    def get_ns_end(self, module, with_endl=True):
        """获取命名空间结束，有多少::就有多少}"""
        ns = self.get_module(module)
        braces = ""
        for ns_simple in ns.split('::'):
            braces = f'}} {f"// namespace {ns_simple}{self.endl()}" if with_endl else ""}{braces}'
        return f"{braces}"

    def parse_header(self, with_ksf):
        output = ""
        for header in self.inc_ordered[0]:
            if self.inc_native[header]:
                output += "#include " + header + "\n"

        output += "\n"

        if with_ksf:
            for header in self.inc_ordered[1]:
                if self.inc_native[header]:
                    output += "#include " + header + "\n"
        return output

    @staticmethod
    def get_type_id(curr_module, value_type):
        return f"{curr_module if value_type['module'] is None else value_type['module']}.{value_type['name']}"

    def is_movable_type(self, module, value_type):
        """判断是否是可以进行std::move的类型"""
        if value_type['type'] == 'native':
            return value_type['name'] == 'string'
        elif isinstance(value_type, KsfStructType):

            if hasattr(value_type, 'module'):
                class_full_name = value_type['module'] + "." + value_type['name']
            else:
                class_full_name = module + "." + value_type['name']

            return class_full_name not in self.ast.enums
        elif isinstance(value_type, KsfVectorType):
            return True
        elif isinstance(value_type, KsfMapType):
            return True
        else:
            return False

    def parse_type(self, module, value_type: KsfType, is_wrap=False):
        if isinstance(value_type, KsfBuildInType):
            if value_type.name == 'string':
                self.add_include(f"<string>")
                return 'std::string'
            elif value_type.name == 'int':
                if value_type.bit == 8:
                    return f'{"unsigned char" if value_type.unsigned else "char"}'
                return f'{"u" if value_type.unsigned else ""}int{value_type.bit}_t'
            elif value_type.name == 'float':
                return value_type.name
            elif value_type.name == 'double':
                return value_type.name
            elif value_type.name == 'bool':
                return value_type.name
            else:
                raise SyntaxError(f"不支持解析的字段类型[{value_type}]")
        elif isinstance(value_type, KsfStructType):
            if value_type.module is not None and module != value_type.module:
                return self.get_module(value_type['module']) + "::" + value_type.name + ("Wrap" if is_wrap else "")
            else:
                return value_type.name + ("Wrap" if is_wrap else "")
        elif isinstance(value_type, KsfVectorType):
            if value_type.is_ordered and not value_type.is_hashed and not value_type.is_unique_member:
                true_type = 'std::vector'
                self.add_include('<vector>')
            elif value_type.is_ordered and not value_type.is_hashed and value_type.is_unique_member:
                true_type = 'std::set'
                self.add_include('<set>')
            elif not value_type.is_ordered and value_type.is_hashed and value_type.is_unique_member:
                true_type = 'std::unordered_set'
                self.add_include('<unordered_set>')
            else:
                raise SyntaxError(f"不支持解析的字段类型[{value_type}]")

            return f"{true_type}<{self.parse_type(module, value_type.value_type, is_wrap=is_wrap)}>"
        elif isinstance(value_type, KsfMapType):
            if not value_type.is_ordered and value_type.is_hashed and value_type.is_unique_member:
                true_type = 'std::unordered_map'
                self.add_include('<unordered_map>')
            elif value_type.is_ordered and not value_type.is_hashed and value_type.is_unique_member:
                true_type = 'std::map'
                self.add_include('<map>')
            else:
                raise SyntaxError(f"不支持解析的字段类型[{value_type}]")
            return f"{true_type}<{self.parse_type(module, value_type.key_type, is_wrap=is_wrap)}, {self.parse_type(module, value_type.value_type, is_wrap=is_wrap)}>"

        raise SyntaxError(f"不支持解析的字段类型[{value_type}]")

    def parse_comment_above(self, comment, tab=None):
        if comment is None or comment == '':
            return ''

        if tab is None:
            tab = self.curr_tab

        comment_lines = comment.split('\n')
        if len(comment_lines) == 1:
            return f"{tab}//{comment}\n"
        else:
            import re
            matches = re.findall(r"\s+\*\s+(.*)\n", f"/*{comment}*/")
            comment_str = f'{tab}/**\n'

            # 将每行注释内容拼接为Python风格的注释
            for match in matches:
                comment_str += f"{tab} * {match}\n"
            comment_str += f'{tab} */\n'
            return comment_str

    def parse_comment_line(self, comment):
        if comment is None or comment == '':
            return ''

        comment_lines = comment.split('\n')
        if len(comment_lines) == 1:
            return f"//{comment}"
        else:
            raise SyntaxError("不支持的注释方式")

    def parse_value(self, value):
        return value['value'] if value['is_number'] else f'"{value["value"]}"'

    def parse_const(self, curr_module, ksf_const: KsfConst):
        if ksf_const.value_type['name'] == 'string':
            return f"{self.parse_comment_above(ksf_const.comment)}{self.curr_tab}constexpr const char *{ksf_const.name} = {self.parse_value(ksf_const.value)};\n\n"
        return f"{self.parse_comment_above(ksf_const.comment)}{self.curr_tab}constexpr {self.parse_type(curr_module, ksf_const.value_type)} {ksf_const.name} = {self.parse_value(ksf_const.value)};\n\n"

    def parse_enum_member(self, ksf_enum_member: KsfEnumMember):
        return f"{self.curr_tab}{ksf_enum_member.name} = {ksf_enum_member.value}"

    def parse_enum_to_str(self, ksf_enum_member: KsfEnumMember):
        return f"case {ksf_enum_member.name}: return \"{ksf_enum_member.name}\";"

    def parse_str_to_enum(self, ksf_enum_member: KsfEnumMember):
        return f"if (s == \"{ksf_enum_member.name}\") {{ e = {ksf_enum_member.name}; return 0; }}"

    def parse_default_var(self, name, value_type, default):
        if default is None:
            if value_type['name'] == 'int':
                return f'''if ({name} == 0) '''
            elif value_type['name'] == 'float':
                return f'if (ksf::KS_Common::equal(0.0f, {name})) '
            elif value_type['name'] == 'double':
                return f'if (ksf::KS_Common::equal(0.0, {name})) '
            elif value_type['name'] == 'bool':
                return f'if ({name})'
            elif value_type['name'] == 'string':
                return f'if ({name}.empty())'
            else:
                return ''

        # 特殊处理一下bool型
        if default['is_bool']:
            return f'if ({"" if default["value"] else "!"}{name})'
        elif default['is_number']:
            if value_type['name'] == 'float':
                return f'if (ksf::KS_Common::equal({name}f, {default["value"]})) '
            elif value_type['name'] == 'double':
                return f'if (ksf::KS_Common::equal({name}, {default["value"]})) '
            return f'if ({name} == {default["value"]}) '
        elif default['is_enum']:
            return f'if ({name} == {default["value"]}) '
        else:
            return f'if ({name} == "{default["value"]}") '

    def parse_variable(self, curr_module, ksf_var: KsfField):
        def parse_default_var(value_type, default):
            if default is None:
                if value_type.name == 'int':
                    return '0'
                elif value_type.name == 'float':
                    return '0.0f'
                elif value_type.name == 'double':
                    return '0.0'
                elif value_type.name == 'bool':
                    return 'true'
                elif value_type.name == 'string':
                    return '""'
                else:
                    return None

            # 特殊处理一下bool型
            if default['is_bool']:
                return f'{"true" if default["value"] else "false"}'
            elif default['is_number'] or default['is_enum']:
                return f'{default["value"]}'
            else:
                return f'"{default["value"]}"'

        default_var = parse_default_var(ksf_var.value_type, ksf_var.default)
        comment = self.parse_comment_line(ksf_var.comment)

        return comment, self.parse_type(curr_module,
                                        ksf_var.value_type), ksf_var.name, f' = {default_var};' if default_var is not None else ';'

    def add_lines(self, lines, tab=0):
        space = ' ' * (4 * tab)

        return f"\n".join(space + line for line in lines.split("\n"))


# 测试用例
if __name__ == '__main__':
    file_path = [
        'example/enum_simple.ksf',
        'example/const_definition.ksf',
        'example/struct_simple.ksf'
    ]

    include_dirs = ['../../']

    destination_dir = '../../../gen'

    push_functions = {}

    export_symbols = {}

    sdk_invoke = {}

    sdk_export = {}

    parser = create_parser(file_path, {}, {}, include_dirs, destination_dir, push_functions, export_symbols, flags={'with_current_priority': True})
