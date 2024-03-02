def greet(input):
    if "hello" in input:
        return "Hello, there!"
    else:
        return "I'm not sure what you mean"


answer = greet("hello, computer")
print("Hm,", answer)