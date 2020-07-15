import os


def create_if_not_exists():
    """Creates the output directory if required"""
    if not os.path.exists("./output"):
        os.mkdir("./output")


def write_enum(enum_string: str, filename: str):
    file_path = f"./output/{filename}"

    create_if_not_exists()
    
    # Delete the file if already exists to prevent errors
    if os.path.exists(file_path):
        os.remove(file_path)
    
    file = open(file_path, "x")
    file.write(enum_string)
    file.close()
