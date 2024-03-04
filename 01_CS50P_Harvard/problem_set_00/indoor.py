def main():
    phrase = input("What would you like to say? ")
    indoor = indoor_voice(phrase)
    print(indoor)


def indoor_voice(text: str) -> str:
    return text.lower()


main()