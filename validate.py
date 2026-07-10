######  Regular Expressions ######

##### Regular expressions or "regexes" will enable patterns within our code.
#### For example, we might want to validate that an email address is formatted correctly.
### Regular expressions will enable us to examine expressions in this fashion.

## To begin, type code validate.py in the terminal window.

# Then, code as follows in the text editor:

#email = input("What's your email? ").strip()
#
#if "@" in email:
#    print("Valid")
#else:
#    print("Invalid")

#### Notice that strip will remove whitespace at the beginning or end of the input.
### Running this program, you'll see that as long as an @ symbol is inputted, the program will regard the input as valid.

##You can imagine, however, that one could input @@ alone and the inout could be regarded as valid.
# We could regard an email address as having at least one @ and a . somewhere within it.

# Modify your code as follows:

#email = input("What's your email? ").strip()
#
#if "@" in email and "." in email:
#    print("Valid")
#else:
#    print("Invalid")

## Notice that while this works as expected, our user could be adversarial, typing simply @. would result in the program returning valid.

# We can improve the logic of our program as follows:

#email = input("What's your email? ").strip()
#
#username, domain = email.slipt("@")
#
#if username and "." in domain:
#    print("Valid")
#else:
#    print("Invalid")

##### Notice how the strip method is used to determine if username exists and if . is inside the domain variable.
#### Running this program, a standard email address typed in by you could be considered valid.
### Typing in malan@harvard alone, you'll find that the program regards this input as invalid.

## We can be even more precise, modifying our code as follows:

#email = input("What's your email? ").strip()
#
#username, domain = email.slipt("@")
#
#if username and "." in domain.endswitch(".edu"):
#    print("Valid")
#else:
#    print("Invalid")

##### Notice how the endswitch method will check to see if domain contains .edu.
#### Still, however, a nefarious user could still break our code. For example, a user could type in malan@.edu and it would be considered valid.

### Indeed, we could keep iterating upon this code ourselves.
## However, it turns out that Python has an existing library called re that has a number of built-in funtions that can validate user inputs agianst patterns.

#### One of the most versatile functions within the library re is search.
### The search library follows the signature re.search(patter, string, flags=0).

## Following this signature, we can modify our code as follows:

#import re
#
#email = input("What's your email? ").strip()
#
#username, domain = email.slipt("@")
#
#if re.search("@", email):
#    print("Valid")
#else:
#    print("Invalid")

## Notice this doesnt increase the functionality of our program at all. In fact, it's somewhat a step back.

##### We can further our program's functionality. However, we need to advance our vocab around valdation.
#### It turns out that in the world of regular expressions there are certain symbols that allow us to identify patterns.
### At this point, we have only been checking for specfic pieces of text like @.
## It so happens that many special symbols can be passed to the compiler for the purpose of engaging in validation.

# A non-exhaustive list of those patterns is as follows:
# . any character except a new line
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetition
# {m} m repetition
# {m,n} m-n repetitions

## Implementing this inside of our code, modify yours as follows:

#import re
#
#email = input("What's your email? ").strip()
#
#if re.search(".+@.+", email):
#    print("Valid")
#else:
#    print("Invalid")

##### Notice that we dont care what the username or domain is. What we care about is the pattern.
#### .+ is used to determine if anything is to the right of the email address.
### Running your code, typing in malan@, you'll notice that the input is regarded as invalid as we would hope.

## Had we used a regular expression .*@.* in our code above, see lecture 7 for visual.

##### Notice the depiction of the state machine of our regular expression. On the left, the compiler begins evaluting the statement from left to right.
#### Once we reach q1 or question 1, the compiler reads time and time again based on the expression handed to it.
### Then, the state is changed looking now at q2 or the second question being validated.
## Again, the arrow indicates how the expression will be evaluated time and time again based upon our programming.
# Then, as depicted by the circle the final state of state machine is reached

### The re and re.search functions and ones like them look for patterns.

## Continuing our improvement of this code, we could improve our code as follows:

#import re
#
#email = input("What's your email? ").strip()
#
#if re.search(".+@.+.edu", email):
#    print("Vaild")
#else:
#    print ("Invalid")

### Notice, however, that one could type in malan@harvard?edu and it would be considered valid.
## Why is this the case?
# You might recognize that in the language of validation, a . means any character!

## We can modify our code as follows:

#import re
#
#email = input("What's your email? ").strip()
#
#if re.search("r.+@.+\.edu", email):
#    print("Vaild")
#else:
#    print ("Invalid")

## Notice how we utilize the "escape character" or \ as a way of regarding the . as part of our string instead of our validation expression.
# Testing your code, you will notice that malan@harvard.edu is regarded as valid, where malan@harvard?edu is invalid.

##### Now that we're using escape characters, it's a good time to introduce "raw string".
#### In Python, raw strings are strings that dont format special characters- instead, each character is taken at face-value.
### Imagine \n, for example. We've seen in an earlier lecture how, in a regualr string, however, \n is treated not as \n, the special character, but as a single n.
## Placing an r in front of a string tells the Python interpreter to treat the string as a raw string, simliar to how palcing an f in front of a string tells Pythn interpreter to treat the string as a format string:

#import re
#
#email = input("What's your email? ").strip()
#
#if re.search(r"^.+@.+\.edu$", email):
#    print("Valid")
#else:
#    print("Invalid")

## Now we've ensured the Python interpreter wont treat \. as a special character.
#Instead, simply as a \ followed by a . - which, in a regular expression terms, means matching a literal"."

#### You can imagine still how our users could create problems for us!
### For example, you could type in a sentence such as My email address is malan@harvard.edu and this whole sentence would be considered valid.
## We can be evem more precise in out coding

# It just so happens we have more speical symbols at our disposal in validation:

# ^   matches the start of the string
# $   matches the end of the string or just before the newline at the end of the string

## We can modify our code using our added vocab as follows:

#import re
#
#email = input("What's your email? ").strip()
#
#if re.search(r"^.+@.+\.edu$", email):
#    print("Valid")
#else:
#    print("Invalid")

#### Notice this has the effect of looking for this exact pattern matching to start and end of the expression being validated.
### Typing in a sentence such as My email address is malan@harvard.edu. now is regarded as invalid.

## We can propose we can do even better! Even though we are now looking for the username at the start of the string, the @ symbol, and the domain name at the end,
# we could type in as many @ symbols as we wish! malan@@@harvard.edu is considered valid!

### We can add to our vocab as follows:
# []    set of characters
# [^]   complementing the set

### Using these newfound abilities, we can modify our expression as follows:

#import re
#
#email = input("What's your email? ").strip()
#
#if re.search(r"^[^@]+@[^@]+\.edu$", email):
#    print("Valid")
#else:
#    print("Invalid")

##### Notice that ^ means to match at the start of the string.
#### All the way at the end of our expression, $ means to match at the end of the string.
### [^@]+ means any character except an @. Then, we have a literal @.
## [^@]+\.edu means any character except an @ follwed by an expression ending in edu.
# Typing in malan@@@harvard.edu.is now regarded as invalid.

## We can still improve this regular expression further. It turns out there are certain requirements for what an email address can be!
# Currently, our validation expression is far too accomdating. We might only want to aloow for characters normally used in a sentence.

## We can modify our code as follows:

#import re
#
#email = input("What's your email? ").strip()
#
#if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
#    print("Valid")
#else:
#    print("Invalid")

#### Notice that [a-zA-Z0-9_] tells the validation that characters must be between a and z, between A and Z, between 0 and 9 and
### potentially include an _ symbol. Testing the input, you'll find that many potential user mistakes can be indicated.

#### Thankfully, common patterns have been built into regular expressions by hard-working programmers.

### In this case, you can modify your code as follows:

#import re
#
#email = input("What's your email? ").strip()
#
#if re.search(r"^\w+@\w+\.edu$", email):
#    print("Valid")
#else:
#    print("Invalid")

### Notice that \w is the same as [a-zA-Z0-9_]. Thanks, hard-working programmers!

## Here is some addtional patterns we can add to our vocab.

# \d    decimal digit
# \D    not a decimal digit
# \s    whitespace characters
# \S    not a whitespace character
# \w    word character, as well as numbers and the underscore
# \W    not a word character

## Now, we know that there are not simply .edu email addresses.

# We could modify our code as follows:

#import re
#
#email = input("What's your email? ").strip()
#
#if re.search(r"^\w+@\w.+\.(com|edu|gov|net|org)$", email):
#    print("Valid")
#else:
#    print("Invalid")

## Notice that the | has the impact of an or in our expression.

# Adding even more symbols to our vocab, here are some more to consider:

# A|B     either A or B
# (...)   a group
# (?:...) non-capturing version

###### Case Sensitivity ######

#### To illustrate how you might address issues around case sensitivity, where there is a difference between EDU and edu and the like,

### let's rewind our code to the following:

#import re
#
#email = input("What's your email? ").strip()
#
#if re.search(r"^\w+@\w+\.edu$", email):
#    print("Valid")
#else:
#    print("Invalid")

#### Notice how we have removed | statements provided previously.
### Recall that winthin the re.search function, there's a parameter for flags.

## Some built-in flag variables are:
# re.IGNORECASE
# re.MULTILINE
# re.DOTALL

### Consider how you might use these in your code.

## Therefore, we can change our code as follows:

#import re
#
#email = input("What's your email? ").strip()
#
#if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
#    print("Valid")
#else:
#    print("Invalid")

### Notice how we added a third parameter re.ignorecase.
## Running this program with MALAN@HARVARD.ED, the input is now considered valid.

#### Consider the following email address malan@cs50.harvard.edu.
### Using our code above, this would be considered valid.

#### Since there is an addtional ., the program considers this invalid.

#### It turns out that we can, looking at our vocab from before, we can group ideas.
# A|B     either A or B
# (...)   a group
# (?:...) non-caputuring version

#### We can modify our code as follows:

#import re
#
#email = input("What's your email? ").strip()
#
#if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
#    print("Valid")
#else:
#    print("Invalid")

#### Notice how the (\w+|.)? communicates to the compiler that this new expression can be there once or not at all.
### Hence, both malan@cs50.harvard.edu and malan@harvard.edu are considered valid.

##### Interestingly enough, the edits we have done so far ro our code dont fully emcompass all the checking that could be done to ensure a valid email address.
#### Indeed, here is the full expression that one would have to type to ensure that a valid email is inputted:
### ^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$

#### There are other functions within the re library you might find useful.
### re.match and re.fullmatch are ones you might fine exceedingly useful
