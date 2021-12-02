# Name: Quang Le
# Student ID: 1768324


if __name__ == "__main__":
    wall_height = int(input("Enter wall height (feet):\n"))
    wall_width = int(input("Enter wall width (feet):\n"))
    wall_area = wall_height*wall_width
    print("Wall area: {:d} square feet".format(wall_area))
    paint_needed = wall_area/350
    print("Paint needed: {:.2f} gallons".format(paint_needed))
    can_needed = round(paint_needed)
    print("Cans needed: {:d} can(s)".format(can_needed))
    print()
    color = (input("Choose a color to paint the wall:\n"))
    color_price = {"red": 35, "blue": 25, "green": 23}
    color_cost = color_price[color]*can_needed
    print("Cost of purchasing {} paint: ${}".format(color, color_cost))
