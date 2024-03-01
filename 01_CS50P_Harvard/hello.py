# Ask user for their name
name = input("What's your name? ")

# Remove whitespaces
name = name.strip()

# Capitalize name
# name = name.capitalize()

# Capitalize all words in a str
name = name.title()

# We can chain methods
# name = input("What's your name? ").strip().title()

# Say hello to user
print("Hello, " + name)
print("Hello,", name)
print(f"Hello, {name}")

print("Hello, ", end="")
print(name)

print("Hello,", name, sep=" ")

# Split name into first name and last name
first, last = name.split()

print(f"Hello, {last}")