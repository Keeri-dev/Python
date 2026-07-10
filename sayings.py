###### Making Your Own Libraries ######

##### You have the ability as a Python programmer to create your own library!
#### Imagine situations where you want to re-use bits of code time and time again or even share them with others!
### We haev been writing lots of code to say "hello" so far in this course.
## Let's create a package to allow us to say "hello" and "goodbye".

# In your terminal window, type code sayings.py.

# In the text editor, code as follows:

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

## Notice that this code in and of itself doesnt do anything for the user.
# However, if a programmer were to import this package into their own program, the ablities created by the functions above could be implemented in their code.

### Let's see how we could implement code utilzing this package that we created.
## In the terminal window, type code say2.py.
