def main():
    #Get user input & strip & convert to lowercase
    user_input = input("How would you like to greet the patron? ").strip().lower()
    payout = value(user_input)
    print(payout)

def value(greeting):
#If they say hello, give $0
    if greeting == "hello":
        return("$0")

    #if string is not just "hello", split string up to isolate greeting word, then match each case to their respective payouts
    else:
        greet_word, dump1 = greeting.split(" ", 1)
        match greet_word:
            case "hello,":
                return("$0")
            case "hello":
                return("$0")
            case "how":
                return("$20")
            case _:
                return("$100")

if __name__ == "__main__":
    main()

