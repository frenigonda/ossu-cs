def main():
    answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")
    result = think(answer)
    print(result)


def think(a: str) -> str:
    simplified = a.strip().lower()
    
    if simplified == "42" or simplified == "forty two" or simplified == "forty-two":
        return "Yes"
    else:
        return "No"
    

main()