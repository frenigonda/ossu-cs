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