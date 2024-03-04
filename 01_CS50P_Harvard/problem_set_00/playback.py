def main():
    speech = input("What's the lecture is about? ")
    slower = slow_speech(speech)
    print(slower)


def slow_speech(text: str) -> str:
    components = text.split(" ")
    return "...".join(components)


main()