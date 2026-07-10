###### Cleaning Up User Input ######

##### You should never expect your users to always follow your hopes for clean input.
#### Indeed, users will often violate your intentions as a programmer.
### There are ways to clean up your data.
## In the terminal window, type code format.py.

# Then, in the text-editor, code as follows:

#name = input("What's your name? ").strip()
#print(f"hello, {name}")

#### Notice that we've created, essentially, a "hello world" program.
### Running this program and typing David, it works well!
## However, typing in Malan, David notice how the program doesnt function as inteneded.
# How could we modify our program to clean up this input?

## Modify your code as follows:

#name = input("What's your name? ").strip()
#if "," in name:
#    last,first = name.split(",")
#    name - f"{first} {last}"
#print(f"hello,{name}")

#### Notice how last, first = name.split(",") is run there is a , in the name.
### Then, the name is standardized as first and last.
## Running our code, typing in Malan, David, you can see how this program does clean up at least one scenario where a user types in something unexpected.

#### You might notice that typing in Malan, David with no space causes the compiler to throw an error.
### Since we now know some regular expression syntax,

## Let's apply that to our code:

#import re
#
#name = input("What's your name? ").strip()
#matches = re.search(r"^(.+), (.+)$", name)
#if matches:
#    last, first = matches.groups()
#    name = first + " " + last
#print(f"hallo, {name}")

#### Notice that re.search can return a set of matches that are extracted from the user's input.
### If matches are returned by re.search. Running this program, typing in David Malan notice how the if condition is not run and the name is returned.
## If you run the program by typing Malan, David, the name is also returned properly.

###It just so happens that we can request specific groups back using matches.group.

## We can modify our code as follows:

#import re
#
#name = inpuches.group(2) + " " + matches.group(1)
#print(f"hello, {name}")
#("What's your name? ").strip()
#matches = re.search(r"^(.+), (.+)$", name)
#if matches:
#    name = matches.group(2) + " " + matches.group(1)
#print(f"hello, {name}")

## Notice how, in this implementation, group is not plural (there is no s).

### Our code can be further tightened as follows:

#import re
#
#name = input("What's your name? ").strip()
#matches = re.search(r"^(.+), (.+)$, name)
#if matches:
#    name = matches.group(2) + " " + matches.group(1)
#print(f"hello, {name}")

#### Notice how group(1) and group(2) are concatenated together with a space.
### The first group is that which is left of the comma.
## The second group is that which is right of the comma.

#### Recognize still that typing in Malan, David with no space will still break our code.

### Therefore, we can make the following modifications:

#import re
#
#name = input("What's your name? ").strip()
#matches = re.search(r"^(.+), *(.+)$", name)
#if matches:
#    name = matches.group(2) + " " + matches.group(1)
#print(f"hello, {name}")

##### Notice the addition of the * in our validation statement.
#### This code will now accept and properly process Malan, David.
### Further, it will poroperly handle David, Malan with many spaceds in front of it Davis'.

### It's very common to utlize re.search as we have in the previous examples, where matches is on a line of code after.

## However, we can combine these statements:

import re

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")

#### Notice how we combine two lines of our code. The walrus := operator assigns a value from right to left and allows us to ask a boolean question at the same time.
### Turn your head sideways and you'll see why this is called a walrus operator.
