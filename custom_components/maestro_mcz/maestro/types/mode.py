from enum import Enum

class ModeEnum(Enum):
    manual = 0,
    auto = 1,
    overnight = 2,
    comfort = 3,
    turbo = 4

class TypeEnum(Enum):
    BOOLEAN = "boolean"
    DOUBLE = "double"
    INT = "int"
    STRING = "string"