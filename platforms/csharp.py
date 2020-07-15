from typing import Dict, TextIO

from utils.file import write_enum
from utils.string import to_pascal_case


def read_template() -> str:
    template_file: TextIO = open("./file_templates/csharp-enum.cs", "r")
    return template_file.read()


def as_enum_row(key: object, json: object) -> str:
    enum_name = to_pascal_case(key)
    hex_val = f"0x{json[key]['unicode']}"
    return f"    {enum_name} = {hex_val},\n"


def as_csharp_enum(icon_json: Dict):
    enum_template = read_template()
    enum_rows = ""
    for key in icon_json:
        enum_rows += as_enum_row(key, icon_json)
    
    updated_enum = enum_template.replace("<<Contents>>", enum_rows)
    write_enum(updated_enum, "FontAwesomeCodes.cs")
