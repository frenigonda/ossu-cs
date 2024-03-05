def main():
    filename = input("File name: ")
    result = get_extension(filename)
    print(result)


def get_extension(f: str) -> str:
    simplified = f.strip().lower().split(".")
    e = simplified[-1]
    if e == None:
        return f"Error: couln't determine extension: {f}"
    match e:
        case "jpg" | "gif" | "jpeg" | "png":
            return f"image/{e}"
        case "pdf", "zip":
            return f"application/{e}"
        case "txt":
            return "text/plain"
        case _:
            return "application/octet-stream"
    

main()