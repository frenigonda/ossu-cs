name = input("What's your name? ")

match name:
    case "Harry" | "Hemione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherine")
    # default case
    case _:
        print("Who?")