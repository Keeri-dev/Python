## Following convention, let's create a new test program by typing code test_calculator.py.

# Modify your code in the text editor as follows:

#from calculator import square
#
#def main():
#    test_square()
#
#def test_square():
#    if square(2) != 4:
#        print("2 squared was not 4")
#    if square(3) != 9:
#        print("3 squared was not 9")
#
#if __name__ == "__main__":
#    main()

###### Notice that we're importing the square function from square.py on the first line of code.
##### By convention, we're creating a function called test_square. Inside that function, we define some conditions to test.

#### In the console window, type python test_calculator.py. You'll notice that nothing is being outputted.
### It could be that everything is runnig fine! Alternatively, it could be that out test funstion did not discover one of the "corner cases" that could produce an error.
## Right now, our code tests two conditions. If we wanted to test many more conditions, our test code could easily become bloated.
# How could we expand our test capabilities without expanding our test code?


###### Assert ######

## Python's assert command allows us to tell the compiler that something, some assertion, is true.

# We can apply this to our code as follows:

#from calculator import square
#
#def main():
#    test_square()
#
#def test_square():
#    assert square(2) == 4
#    assert square(3) == 9
#
#if __name__ == "__main__":
#    main()

# Notice that we're definitively asserting what square(2) and square(3) should equal. Our code is reduced from four test lines down to two.

# We can purposely break our calculator code by modifying it as follows:

#def main():
#    x = int(input("What's x? "))
#    print("x squared is", square(x))
#
#def square(n):
#    return n + n
#
#if __name__ == "__main__":
#    main()

# Notice that we have changed the * operator to a + in the square function.

##### Now running python test_square.py in the console window, you'll notice that an AssertionError is raised by the compiler.
#### Essentially, this is the compiler telling us that one of our conditons was not met.

### One of the challenges that we're now facing is that our code could become even more burdensome if we wanted to provide more descriptive error output to our users.

## Plausibly, we could code as follows:

#def main():
#    test_square()
#
#
#def test_square():
#    try:
#        assert square(2) == 4
#    except AssertionError:
#        print("2 squared is not 4")
#    try:
#        assert square(3) == 9
#    except AssertionError:
#        print("3 squared is not 9")
#    try:
#        assert square(-2) == 4
#    except AssertionError:
#        print("-2 squared is not 4")
#    try:
#        assert square(-3) == 9
#    except AssertionError:
#        print("-3 squared is not 9")
#    try:
#        assert square(0) == 0
#    except AssertionError:
#        print("0 squared is not 0")
#
#
#if __name__ == "__main__":
#    main()

### Notice that runnig this code will produce multiple errors. However, it's not producing all the errors above.
## This is a good illustration that it's worth testing multiple cases such that you might catch situations where there are coding mistakes.
# The above code illustrates a major challenge: How could we make it easier to test your code without dozens of lines of code like the above?


###### pytest ######

##### pytest is a third- party library that allows you to unit test your program.
#### That is, you can test functions within your program.

### To utilize pytest please type pip install pytest into your console window.

## Before applying pytest to our own program,

# Modify your function as follows:

#from calculator import square
#
#
#def test_assert():
#    assert square(2) == 4
#    assert square(3) == 9
#    assert square(-2) == 4
#    assert square(-3) == 9
#    assert square(0) == 0

###### Notice how the above code asserts all the conditions that we want to test.
##### pytest allows us to run our program directly thru it, such that we can more easily view the results of our test conditions.

#### In the terminal window, type pytest test_calculator.py. You'll immediately notice that output wil be provided.
### Notice the red F near the top of the output, indicating that something in your code failed.
## Further, notice that the red E provides some hints about the errors in your calculator.py program.
# Based upon the ouput, you can imagine a scernario where 3 * 3 has outputted 6 instead of 9.

# Based on the results of this test, we can go correct our calculator.py code as follows:

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


if __name__ == "__main__":
    main()
