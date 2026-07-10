# Implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything,
prompt = input("What is Answer to the Great Question of Life, the Universe and Everything?")
prompt= prompt.strip()

# Make it case-sensitive
prompt = prompt.lower()

# Outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two
if prompt == "42":
    print("Yes")
elif prompt == "forty-two":
    print("Yes")
elif prompt == "forty two":
    print("Yes")

# Otherwise output No
else:
    print("No")
