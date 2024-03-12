def main():
    # Expression in @ +-*/ @ format
    expression = input("Expression: ")
    result = calculate(expression)
    print(result)


def calculate(f: str) -> float:
    x, sign, y = f.split(" ")
    
    match sign:
        case "+":
            return float(x) + float(y)
        case "-":
            return float(x) - float(y)
        case "*":
            return float(x) * float(y)
        case "/":
            return float(x) / float(y)
    

main()