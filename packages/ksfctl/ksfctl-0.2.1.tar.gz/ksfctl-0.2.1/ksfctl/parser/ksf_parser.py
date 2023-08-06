from collections import defaultdict
from pathlib import Path


class KsfObject:
    obj = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.__init__(*args, **kwargs)
        obj.obj[obj.id] = obj
        return obj

    def __init__(self, file, module, name, level, comment=None):
        self.export = False
        self.file = file
        self.module = module
        self.name = name
        self.level = level
        self.comment = comment
        self.id = ""

    def __eq__(self, other):
        if self.id is None or other.id is None:
            raise SyntaxError("Ksf对象的Id不允许为空")
        return self.id == other.id

    def __hash__(self):
        if self.id is None:
            raise SyntaxError("Ksf对象的Id不允许为空")
        return hash(self.id)

    def update_export_symbol(self):
        pass


class KsfFile:
    def __init__(self, file):
        self.file = file
        self.elements = []
        self.includes = []
        self.level = 1

    def add_enum(self, enum):
        self.elements.append(enum)

    def add_interface(self, interface):
        self.elements.append(interface)

    def add_struct(self, struct):
        self.elements.append(struct)

    def add_const(self, const):
        self.elements.append(const)

    def add_include(self, inc, inc_file_name):
        self.includes.append((inc, inc_file_name))


class KsfEnumMember(KsfObject):
    def __init__(self, file, module, enum, name, value, comment=''):
        super().__init__(file, module, name, 3, comment)
        self.enum = enum
        self.value = value

        self.id = '.'.join([self.module, self.enum, self.name])


class KsfEnum(KsfObject):
    def __init__(self, file, module, name, member, comment=None):
        super().__init__(file, module, name, 2, comment)
        self.member = []
        for m in member:
            ksf_enum_member = KsfEnumMember(file, module, name, m['name'], m['value'], m['comment'])
            self.member.append(ksf_enum_member)

        self.id = '.'.join([self.module, self.name])

    def update_export_symbol(self):
        self.export = True


class KsfField(KsfObject):
    def __init__(self, file, module, struct, tag, is_required, value_type, name, default, comment=None):
        super().__init__(file, module, name, 3, comment)
        self.struct = struct
        self.tag = tag
        self.is_required = is_required
        self.value_type = value_type
        self.default = default

        self.id = '.'.join([self.module, self.struct, self.name])

    def update_export_symbol(self):
        """
        更新导出符号, 需要更新所有依赖的结构体
        :return:
        """
        for obj_type in self.value_type.get_no_native_obj():
            obj_type.update_export_symbol()


class KsfStruct(KsfObject):
    def __init__(self, file, module, name, variable, comment=None):
        super().__init__(file, module, name, 2, comment)
        self.key_fields = []
        self.variable = {}
        for v in variable:
            value_type = KsfType.create(module, v['value_type'])
            ksf_field = KsfField(file, module, name, v['tag'], v['is_required'], value_type, v['name'],
                                 v['default'] if 'default' in v else None, v['comment'])
            self.variable[ksf_field.id] = ksf_field

        self.id = '.'.join([self.module, self.name])

    def add_key(self, arg: list):
        self.key_fields = arg

    def update_export_symbol(self):
        """
        更新导出符号, 需要更新所有依赖的结构体
        :return:
        """
        self.export = True
        for v in self.variable.values():
            for obj_type in v.value_type.get_no_native_obj():
                obj_type.update_export_symbol()


class KsfVariable(KsfObject):
    def __init__(self, file, module, interface, operator, value_type, name, index):
        super().__init__(file, module, name, 4, None)
        self.interface = interface
        self.operator = operator
        self.value_type = value_type
        self.index = index

        self.id = '.'.join([self.module, self.interface, self.operator, self.name])


class KsfOperator(KsfObject):
    def __init__(self, file, module, interface, name, return_type, variable, comment=None):
        super().__init__(file, module, name, 3, comment)
        self.export = False
        self.interface = interface
        self.return_type = KsfType.create(module, return_type)

        self.input = {}
        self.output = {}
        self.ordered_var = []

        index = 1
        for v in variable:
            value_type = KsfType.create(module, v['value_type'])
            ksf_variable = KsfVariable(file, module, interface, name, value_type, v['name'], index)
            if v['is_output']:
                self.ordered_var.append((ksf_variable.name, True))
                self.output[ksf_variable.name] = ksf_variable
            else:
                self.ordered_var.append((ksf_variable.name, False))
                self.input[ksf_variable.name] = ksf_variable

            index += 1

        self.id = '.'.join([self.module, self.interface, self.name])

    def update_export_symbol(self):
        """
        更新导出符号：
        1.更新自身的export标记为导出
        2.更新接口的export标记为导出
        3.更新所有依赖的结构体标记为导出
        :return:
        """
        self.export = True
        KsfObject.obj[f"{self.module}.{self.interface}"].export = True
        for obj in self.return_type.get_no_native_obj():
            obj.update_export_symbol()

        for v in self.input.values():
            for obj in v.value_type.get_no_native_obj():
                obj.update_export_symbol()

        for v in self.output.values():
            for obj in v.value_type.get_no_native_obj():
                obj.update_export_symbol()


class KsfInterface(KsfObject):
    def __init__(self, file, module, name, operator, comment=None):
        super().__init__(file, module, name, 2, comment)
        self.depend_fields = defaultdict(set)
        self.operator = {}

        for o in operator:
            ksf_operator = KsfOperator(file, module, name, o['name'], o['return_type'], o['variable'], o['comment'])
            self.operator[ksf_operator.name] = ksf_operator

        self.id = '.'.join([self.module, self.name])

    def update_export_symbol(self):
        """
        更新导出符号, 递归更新所有方法的符号
        :return:
        """
        self.export = True
        for o in self.operator.values():
            o.update_export_symbol()


class KsfConst(KsfObject):
    def __init__(self, file, module, name, value_type, value, comment=''):
        super().__init__(file, module, name, 2, comment)
        self.export = False
        self.value_type = KsfType.create(module, value_type)
        self.value = value

        self.id = '.'.join([self.module, self.name])

    def update_export_symbol(self):
        """
        更新导出符号, 递归更新所有方法的符号
        :return:
        """
        self.export = True


class KsfType:
    def __new__(cls, *args, **kwargs):
        if cls is KsfType:
            raise TypeError("KsfType is abstract")

        obj = object.__new__(cls)
        obj.__init__(*args, **kwargs)
        return obj

    def __init__(self, module, name):
        self.module = module
        self.name = name

    @staticmethod
    def create(curr_module, type_def):
        if type_def['type'] == 'class':
            if type_def['module'] is None:
                type_def["module"] = curr_module
        else:
            type_def["module"] = curr_module

        if type_def["type"] == "map":
            return KsfMapType(type_def["module"], type_def["name"], type_def["key_type"], type_def["value_type"],
                              type_def)
        elif type_def["type"] == "vector":
            return KsfVectorType(type_def["module"], type_def["name"], type_def["value_type"], type_def)
        elif type_def["type"] == "class":
            return KsfStructType(type_def["module"], type_def["name"], type_def)
        elif type_def["type"] == "array":
            return KsfArrayType(type_def["module"], type_def["name"], type_def["element_type"], type_def)
        elif type_def["type"] == "native":
            return KsfBuildInType(**type_def)
        else:
            raise SyntaxError("未知类型")

    def get_no_native_obj(self):
        return []

    def __getitem__(self, item):
        return self.__dict__[item]


class KsfBuildInType(KsfType):
    def __init__(self, **kwargs):
        super().__init__(None, kwargs['name'])
        self.__dict__.update(kwargs)


class KsfMapType(KsfType):
    def __init__(self, module, name, key_type, value_type, flags):
        self.__dict__.update(flags)
        super().__init__(module, name)
        self.key_type = KsfType.create(module, key_type)
        self.value_type = KsfType.create(module, value_type)

    def get_no_native_obj(self):
        return self.key_type.get_no_native_obj() + self.value_type.get_no_native_obj()


class KsfVectorType(KsfType):
    def __init__(self, module, name, element_type, flags):
        self.__dict__.update(flags)
        super().__init__(module, name)
        self.value_type = KsfType.create(module, element_type)

    def get_no_native_obj(self):
        return self.value_type.get_no_native_obj()


class KsfStructType(KsfType):
    def __init__(self, module, name, flags):
        self.__dict__.update(flags)
        super().__init__(module, name)
        if self.name == 'void':
            self.obj_type = None
        else:
            self.obj_type = KsfObject.obj[self.module + "." + self.name]

    def get_no_native_obj(self):
        if self.obj_type is None:
            return []
        else:
            return [self.obj_type]


class KsfArrayType:
    pass


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


class Ksf:
    # natives = {
    #     "string": KsfBuildInType(name='string'),
    #     "int": KsfBuildInType(name='int'),
    #     "uint": KsfBuildInType(name='uint'),
    #     "bool": KsfBuildInType(name='bool'),
    #     "short": KsfBuildInType(name='int'),
    #     "ushort": KsfBuildInType(name='ushort'),
    #     "long": KsfBuildInType(name='long'),
    #     "float": KsfBuildInType(name='float'),
    #     "double": KsfBuildInType(name='double'),
    #     "byte": KsfBuildInType(name='byte'),
    # }

    files = {}

    file2module = defaultdict(list)
    module2file = defaultdict(list)

    enums = {}
    file2enum = defaultdict(list)  # 文件到枚举的映射
    module2enum = defaultdict(list)  # 模块到枚举的映射

    structs = {}
    file2struct = defaultdict(list)  # 文件到结构体的映射
    module2struct = defaultdict(list)  # 模块到结构体的映射

    interfaces = {}
    file2interface = defaultdict(list)  # 文件到接口的映射
    module2interface = defaultdict(list)  # 模块到接口的映射

    consts = {}
    file2const = defaultdict(list)  # 文件到常量的映射
    module2const = defaultdict(list)  # 模块到常量的映射

    all_element = KsfObject
    export_elements = defaultdict(set)  # 导出的元素名和其member的关联，如果member为空则全部导出

    @classmethod
    def add_enum(cls, ksf_enum: KsfEnum):
        cls.enums[ksf_enum.id] = ksf_enum
        cls.file2enum[ksf_enum.file].append(ksf_enum.id)
        cls.module2enum[ksf_enum.module].append(ksf_enum.id)
        cls.files[ksf_enum.file].add_enum(ksf_enum)

    @classmethod
    def add_struct(cls, ksf_struct: KsfStruct):
        cls.structs[ksf_struct.id] = ksf_struct
        cls.file2struct[ksf_struct.file].append(ksf_struct.id)
        cls.module2struct[ksf_struct.module].append(ksf_struct.id)
        cls.files[ksf_struct.file].add_struct(ksf_struct)

    @classmethod
    def add_interface(cls, ksf_interface: KsfInterface):
        cls.interfaces[ksf_interface.id] = ksf_interface
        cls.file2interface[ksf_interface.file].append(ksf_interface.id)
        cls.module2interface[ksf_interface.module].append(ksf_interface.id)
        cls.files[ksf_interface.file].add_interface(ksf_interface)

    @classmethod
    def update_export_symbol(cls, obj_ids: list):
        for obj_id in obj_ids:
            if obj_id in KsfObject.obj:
                KsfObject.obj[obj_id].update_export_symbol()
            else:
                raise SyntaxError('未知的导出元素：' + obj_id)

    @classmethod
    def get_all_export_symbol(cls):
        ids = []
        for obj in KsfObject.obj.values():
            if obj.export and obj.level <= 2:
                ids.append(obj.id)
        return ids

    @classmethod
    def add_struct_key(cls, module, struct, arg):
        cls.structs[module + '.' + struct].add_key(arg)

    @classmethod
    def add_constant(cls, ksf_const: KsfConst):
        cls.consts[ksf_const.id] = ksf_const
        cls.file2interface[ksf_const.file].append(ksf_const.id)
        cls.module2interface[ksf_const.module].append(ksf_const.id)
        cls.files[ksf_const.file].add_const(ksf_const)

    @classmethod
    def add_file(cls, file: Path):
        ksf_file = KsfFile(file)
        cls.files[file.name] = ksf_file

    @classmethod
    def add_include(cls, file: Path, include: Path, inc_file_name: str):
        cls.files[file.name].add_include(include, inc_file_name)
