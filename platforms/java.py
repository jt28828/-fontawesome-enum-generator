from typing import Dict, TextIO

from utils.file import write_enum
from utils.string import to_capitals


def read_template() -> str:
    template_file: TextIO = open("./file_templates/java-enum.java", "r")
    return template_file.read()


def as_enum_row(key: str, json: Dict, is_last: bool) -> str:
    enum_name = to_capitals(key)
    hex_val = f"0x{json[key]['unicode']}"
    
    if is_last:
        row = f"    {enum_name}({hex_val});\n"
    else:
        row = f"    {enum_name}({hex_val}),\n"
    
    return row


def as_java_enum(icon_json: Dict):
    enum_template = read_template()
    enum_rows = ""
    for i, key in enumerate(icon_json):
        enum_rows += as_enum_row(key, icon_json, i == (len(icon_json) - 1))
    
    updated_enum = enum_template.replace("<<Contents>>", enum_rows)
    write_enum(updated_enum, "FontAwesomeCodes.java")
