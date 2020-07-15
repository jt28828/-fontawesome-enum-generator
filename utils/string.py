def to_pascal_case(name: str):
    # Need a special case for 500px
    if name == "500px":
        return "FiveHundredPx"
    else:
        return name.replace("-", " ").title().replace(" ", "")


def to_capitals(name: str):
    # Need a special case for 500px
    if name == "500px":
        return "FIVEHUNDREDPX"
    else:
        return name.replace("-", "_").upper()
