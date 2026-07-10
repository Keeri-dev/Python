###### Generators and Iterators ######

##### In Python, there's a way to protect against your system running out of resources the problems they are addressing become too large.
#### In the United States, it's customary to "count sheep" in one's mind when one is having a hard time falling asleep.

### In the text editor window, type code sleep.py and

## code as follows:

#n = int(input("What's n? "))
#for i in range(n):
#    print("🐑" * i)

### Notice how this program will count the number of sheep you ask of it.

##### We can make our program more sophisticated by adding a main function by coding as follows:

#def main():
#    n = int(input("What's n? "))
#    for i in range(n):
#        print("🐑" * i)
#
#
#if __name__ == "__main__":
#    main()

##### Notice how a main function is provided.

###### We can call a sheep function by modifying our code as follows:

#def main():
#    n = int(input("What's n? "))
#    for i in range(n):
#        print(sheep(i))
#
#
#def sheep(n):
#    return "🐑" * n
#
#
#if __name__ == "__main__":
#    main()

##### Notice how the main fucntion does the iteration.

###### We can provide the sheep function more abilities.

#### In the text editor window, code as follows:

#def main():
#    n = int(input("What's n? "))
#    for s in sheep(n):
#        print(s)
#
#
#def sheep(n):
#    flock = []
#    for i in range(n):
#        flock.append("🐑" * i)
#    return flock
#
#
#if __name__ == "__main__":
#    main()

##### Notice how we create a flock of sheep and return the flock.

###### Executing our code, you might try different numbers of sheep such as 10, 1000, and 10000.
##### What if you asked for 100000 sheep, your program might completely hang or crash.
#### Because you've attempted to generate a massive list of sheep, your computer may be struggling to complete the computation.

###### The yield generator can solve this problem by returnig a small bit of the results at a time.

##### In the text editor window, code as follows:

def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    for i in range(n):
        yield "🐑" * i


if __name__ == "__main__":
    main()

##### Notice how yield provides only one value at a time while the for loop keeps working.
