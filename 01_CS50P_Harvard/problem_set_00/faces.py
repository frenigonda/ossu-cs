def main():
    text = input("How are you today? ")
    result = convert(text)
    print(result)


def convert(text: str) -> str:
    replace = text.replace(":)", "🙂").replace(":(", "🙁")
    return replace


main()