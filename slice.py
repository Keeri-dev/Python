###### Slice ######

# slice is a command that allows us to take a list and tell the compiler where we want the compiler to consdier the start of the list and the end of the list.

# For example, modify your code as follows:

#import sys
#
#if len(sys.argv) < 2:
#    sys.exit("Too few arguments")
#
#for arg in sys.argv:
#     print("hello, my name is", arg)

### Notice that if you type python name.py David Carter Rongxin into the terminal window,
## the compiler will output not just the intended output of the names, but also hello, my name is name.py.
# How then could we ensure that the compiler ignores the first element of the list where name.py is currently being stored?

## slice can be employed in our code to start the list somewhere different!

# Modify your code as follows:

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)

## Notice that rather than starting the list at 0, we use square bracket to tell the compiler to start at 1 and go to the end using the 1: argument.
# Running this code, you'll notice that we can improve our code using relatively simple synatax.

