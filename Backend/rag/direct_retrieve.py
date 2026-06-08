import os

BASE_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "knowledge_base"
)

def load_file(filename):

    if not filename:
        print("ERROR: Empty filename received!")
        return ""

    path = os.path.join(BASE_DIR, filename)

    print("Loading:", path)

    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    print("FILE NOT FOUND:", path)
    return ""


def get_design_context(room, style, color):

    print("ROOM =", room)
    print("STYLE =", style)
    print("COLOR =", color)

    style_map = {
        "modern": "modern_design.txt",
        "minimal": "minimalistic_design.txt",
        "luxury": "luxury_design.txt",
        "cozy": "cozy_design.txt"
    }

    color_map = {
        "white": "white_color.txt",
        "beige": "beige_color.txt",
        "grey": "grey_color.txt",
        "brown": "brown_color.txt",
        "midnight blue": "midnight_blue_color.txt",
        "forest green": "forest_green_color.txt",
        "wine red": "wine_red_color.txt"
    }

    furniture_file = f"{style}_{room}_furniture.txt"

    print("ROOM FILE =", f"{room}_design.txt")
    print("STYLE FILE =", style_map.get(style))
    print("COLOR FILE =", color_map.get(color))
    print("FURNITURE FILE =", furniture_file)

    print("\n")

    room_context = load_file(f"{room}_design.txt")
    style_context = load_file(style_map.get(style, ""))
    color_context = load_file(color_map.get(color, ""))
    furniture_context = load_file(furniture_file)

    print("\n")

    return f"""{room_context}. {style_context}. {color_context}. Furnitures like {furniture_context}"""