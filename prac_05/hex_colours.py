COLOR_NAME = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "Alice Blue": "#f0f8ff", "Alizarin Crimson": "#e32636",
              "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc", "Antique White": "#faebd7",
              "Apricot": "#fbceb1", "Aqua": "#00ffff"}
print(COLOR_NAME)

color = input("Enter color name: ").title()
while color != "":
    try:
        print(color, "is", COLOR_NAME[color])
    except KeyError:
        print("Invalid color name")
    color = input("Enter color name: ").title()