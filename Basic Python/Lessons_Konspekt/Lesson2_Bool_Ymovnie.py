and

True and True   # True
True and False  # False
False and True  # False
False and False # False

or

True or True   # True
True or False  # True
False or True  # True
False or False # False

not

not True  # False
not False # True


color = "red"

match color:
    case "red":
        print("Color is red")
    case "green":
        print("Color is green")
    case "blue":
        print("Color is blue")
    case _:
        print("Color is unknown")