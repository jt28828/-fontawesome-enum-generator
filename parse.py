import json
from http.client import HTTPResponse
from typing import TextIO, Dict
from urllib import request

from platforms.cpp import as_cpp_enum
from platforms.csharp import as_csharp_enum
from platforms.java import as_java_enum
from platforms.python import as_python_enum
from platforms.typescript import as_typescript_enum


def read_icons_json() -> Dict:
    """Opens the icons.json and converts into a json object"""
    json_file: HTTPResponse = request.urlopen(
        "https://raw.githubusercontent.com/FortAwesome/Font-Awesome/master/metadata/icons.json")
    
    file_contents = json_file.read()
    return json.loads(file_contents)


def print_first():
    icon_json = read_icons_json()
    # Generate all the enums
    as_csharp_enum(icon_json)
    as_typescript_enum(icon_json)
    as_python_enum(icon_json)
    as_java_enum(icon_json)
    as_cpp_enum(icon_json)


print_first()
