### Asks for height for pyramid

#def main():
#    height = int(input("Height: "))
#    pyramid(height)
#
## Expects one arguement n. and prints a pyramid.
## for loop iterates n times. then prints #s
#def pyramid(n):
#    for i in range(n):
#        print("#" * i)
#
#if __name__ == "__main__":
#    main()

#### How to fix it not making a pyramid.. use print to debug

#def main():
#    height = int(input("Height: "))
#    pyramid(height)
#
#def pyramid(n):
#    for i in range(n):
#        print(i, end=" ")
#        print("#" * i)
#
#if __name__ == "__main__":
#    main()

#### shows i starts at zero in a for loop. fix that
### want to print one more than i to move the hashes add (i + 1).

#def main():
#    height = int(input("Height: "))
#    pyramid(height)
#
#def pyramid(n):
#    for i in range(n):
#        print("#" * (i + 1))
#
#if __name__ == "__main__":
#    main()

#### Now have the intended pyramid by using print to debug.

### Use another tool to debug
### called breakpoint..allows you to specify on what line or lines of code, you want to pause or break exuection of the program.
## set a breakpoint.. to step by step look at the code ..added to main the red dot on the left

def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print("#" * i )

if __name__ == "__main__":
    main()
### click run and debug on the left
### use step into on the top
##paused on line 2 and steps into my own function
#
#### continue same soultion as above.