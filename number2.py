#x = int(input("What's x? "))
#print(f"x is {x}")

#### Fixing a ValueError
### with try: and except:

#try:
#    x = int(input("What's x? "))
#    print(f"x is {x}")
#except ValueError:
#    print("x is not an integer")

#### clean up what try: is actually trying

#try:
#    x = int(input("What's x? "))
#except ValueError:
#    print("x is not an integer")
#
#print(f"x is {x}")

### Get A NameError

#### Fix NameError using else

#try:
#    x = int(input("What's x? "))
#except ValueError:
#    print("x is not an integer")
#else:
#    print(f"x is {x}")

#### Further improve the code. make it reprompt instead of closing the dialoguae with a loop.

#while True:
#    try:
#        x = int(input("What's x? "))
#    except ValueError:
#        print("x is not an integer")
#    else:
#        break
#print(f"x is {x}")

#### Another way to break the loop

#while True:
#    try:
#        x = int(input("What's x? "))
#        break
#    except ValueError:
#        print("x is not an integer")
#
#print(f"x is {x}")

#### make your own function to get info over and over

#def main():
#    x = get_int()
#    print(f"x is {x}")
#
#
#def get_int():
#    while True:
#        try:
#            x = int(input("What's x? "))
#        except ValueError:
#            print("x is not an integer")
#        else:
#            break
#    return x
#
#main()


### Improve code further by shortening

#def main():
#    x = get_int()
#    print(f"x is {x}")
#
#def get_int():
#    while True:
#        try:
#            x = int(input("What's x? "))
#        except ValueError:
#            print("x is not an integer")
#        else:
#          return x
#
#main()

#### return can also break the loop

##### Tighten up code further making it shorter

#def main():
#    x = get_int()
#    print(f"x is {x}")
#
#def get_int():
#    while True:
#        try:
#            return int(input("What's x? "))
#        except ValueError:
#            print("x is not an integer")
#
#
#main()

### Remove else and return and move return into x=

#### One more refinement
#### Change output for integer error ny using pass

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass


main()

### change print under error for pass changes output to to shorter
### Indents are basically order of operation and order also makes it much more readable.

##### Final changes
## add a parameter to get x

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input("prompt"))
        except ValueError:
            pass


main()

#### havent changed fucntionality just makes it more dynamic and useable.
#### You can raise .. exceptions with "raise" keyword as well