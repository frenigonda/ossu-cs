def main():
    #time in @@:@@ or @:@@ format
    time = input("What time is it? ")
    result = convert(time)
    print(result)


def convert(time):
    hh, mm = time.split(":")
    h = int(hh)
    m = int(mm)
    if h < 0 or h > 23 or m < 0 or m > 59:
        return "Invalid time"
    
    match h:
        case 7 | 8:
            return "Breakfast"
        case 12 | 13:
            return "Lunch"
        case 18 | 19:
            return "Dinner"
        case _:
            return ""


if __name__ == "__main__":
    main()