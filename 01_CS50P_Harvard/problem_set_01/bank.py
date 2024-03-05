def main():
    greeting = input("Hello! ")
    result = process(greeting)
    print(result)


def process(g: str) -> str:
    simplified = g.lstrip().lower()
    
    if simplified.startswith("hello"):
        return "$0"
    elif simplified.startswith("h"):
        return "$20"
    else:
        return "$100"
    

main()