def main():
    # x = int(input("What's x? "))
    # y = int(input("What's y? "))

    # Still works, the result Z is float
    # x = float(input("What's x? "))
    # y = int(input("What's y? "))
    # z = x + y

    x = float(input("What's x? "))
    y = float(input("What's y? "))

    # Round to 1 digit after the floating point
    z = round(x + y, 1)
    print(z)

    # Alternatively we can format the result string
    # print(f"{z:.1f}")

    a = int(input("What's a? "))
    print("a squared is", square(a))
    print("unspecified sqr is", unspecifiedSquare(5.864))


def square(val: int) -> int :
    # exception on return: TypeError if val isn't numerical
    return val * val
    #  Alternatives:
    #   return val ** 2
    #   return pow(val, 2)

# It's okay to not specify the types like this
def unspecifiedSquare(val):
    # exception on return: TypeError if val isn't numerical
    return val * val

main()