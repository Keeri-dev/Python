def snake_case():
    camelCases = list(input("camelCase: "))
    int_num = 91
    for camelCase in camelCases:
        if ord(camelCase) < int_num:
            camelCase = camelCase.replace(camelCase, f"_{camelCase}").lower()
        print(camelCase, end="")
snake_case()
print("")

#Line 1: Define the function snake_case()
#Line 2: Take user input, convert to list
#line 3: Setup a number greater than all ASCII capital letters
#Line 3: (A is 65... Z is 90)
#Line 4: Loop through the list in Line 2
#Line 5: ord method returns the dcimal number of the alphabet
#Line 5: if camelCase < int_num (it's a capital letter i.e < 91)
#Line 6: Replace cap. lets to lower add underscore b4 it
#Line 6:(eg A = _a, B = _b etc.)
#Line 7: print the letters in one line
#Line 8: call the snake_case() function
#Line 9: Return the cursor to the next line
