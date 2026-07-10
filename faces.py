# Implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂

def main():
    text = input()
    print(convert(text))

def convert(str):
    str=str.replace(":)","🙂")
    str=str.replace(":(","🙁")
    return str

main()
# Any :( converted to 🙁. All other text should be returned unchanged.
