###### Docstrings ######

##### A standard way of commenting your functions purpose is to use a docstring.

#### In the text editor window, code as follows:

#def meow(n):
#    """Meow n times."""
#    return "meow\n" * n
#
#
#number = int(input("Number: "))
#meows = meow(number)
#print(meows, end="")

#### Notice how the three double quotes designate what the function does.

### You can use docstrings to standardize how you document the features of a function.

## In the text editor window, code as follows:

#def meow(n):
#    """
#    Meow n times.
#
#    :param n: Number of times to meow
#    :type n: int
#    :raise TypeError: If n is not an int
#    :return: A string of n meows, one per line
#    :rtype: str
#    """
#    return "meow\n" * n
#
#
#number = int(input("Number: "))
#meows = meow(number)
#print(meows, end="")

##### Notice how multiple docstring arguments are included. For example, it describes the parameters taken by the function and what is returned by the function.

#### Established tools, such as Sphinx, can be used to parse docstrings and automatically create documentation for us in the form of web pages and PDF files such that you can publish and share with others.