###### Extracting User Input ######

##### So far, we've validated the user's input and cleaned up the user's input.
#### Now, lets extract some specific info from user input.
### In the terminal window, type code twitter.py and

## code as follows in the text editor window:

#url = input("URL: ").strip()
#print(url)

#### Notice that if we type in https://twitter.com/davidjmalan, it shows exaclty what the user typed.
### However, how would we be able to extract just the username and ignore the rest of the URL?

#### You can imagine how we would simply be able to get rid of the beginning of the standard Twitter URL.

### We can attempt this as follows:

#url = input("URL: ").strip()
#
#username = url.replace("https://twitter.com/", "")
#print(f"Username: {username}")

#### Notice how the replace method allows us to find one item and replace it with another.
### In this case, we're finding part of the URL and replacing it with nothing.
## Typing in the full URL https://twitter.com/davidjmalan, the program effectively outputs the username.
# However, what are some shortcomings of this current program?

###### What if the user simply typed twitter.com instead of including the https:// and the like?
##### You can imagine many scernarios where the user may input or neglect to input parts of the URL that would create strange output by this program.

#### To improve this program, we can code as follows:

#url = input("URL: ").strip()
#
#username = url.removeprefix("https://twitter.com/")
#print(f"Username: {username}")

##### Notice how we utilize the removeprefix method. This method will remove the beginning of a string.
#### Regular expressions simply allow us to succinctly express the patterns and goals.
### Within the re library, there is a method called sub. This method allows us to substiute a patterns with something else.
## The signature of the sub method is as follows:

## re.sub(pattern, repl, string, count=0, flags=0)

##### Notice how pattern refers to the regular expression we are looking for.
#### Then, there is a repl string that we can replace the pattern with.
### Finally, there's the string that we want to do the substitution on.

## Implementing this method in our code, we can modify our program as follows:

#import re
#
#url = input("URL: ").strip()
#
#username = re.sub(r"https://twitter.com/", "", url)
#print(f"Username: {username}")

#### Notice how executing this program and inputting https://twitter.com/davidjmalan produces the correct outcome.
### However, there are some problems still present in our code.

#### The protocol, subdomain, adn the possibility that user inputted any part of the URL after the username are all reasons that this code is still not ideal.

### We can further address these shortcomings as follows:

#import re
#
#url = input("URL: ").strip()
#
#username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
#print(f"Username: {username}")

##### Notice how the ^ caret was added to the url. Notice also how the . could be interpreted improperly by the compiler.
#### Therefore, we escape it using a \ to make it \. For the purpose of toelrating both https, we add a ? to the end of https?, making the s optional.
### Further, to accommodate www we add (www\.)? to our code.
## Finally, just in case the user decides to leave out the proctol altogether, the http:// or https:// is made optional (https?://).

#### Still, we're blindly expecting that what the user inputted a url that, indeed, has a username.

### Using our knowledge of re.search, we can further improve code:

#import re
#
#url = input("URL: ").strip()
#
#matches = re.search(r"^https?://(www\.)?\.com/(.+)$", url, re.IGNORECASE)
#if matches:
#    print(f"Username:", matches.group(2))

#### Notice how we're searching for the regular expression above in the string provided by the user.
### In particular, we're capturing that which appears at the end of the URL using (.+)$ regular expression.
## Therefore, if the user fails to input a URL without a username, no input will be presented.

### Even further tightening up on our program, we can utilize our := operator as follows:

import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))

#### Notice that the ?: tells the compiler it doesnt have to capture what is in that spot in our regular expression.

### Still, we can be more explicit to ensure that the username inputted is correct.

## Using Twitter's documentation, we can add the following to our regular expression:

import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_])+)", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))

##### Notice that the [a-z0-9_]+ tells the compiler to only except a-z, 0-9, and _ as part of the regualr expression.
#### The + indicates that we're expecting one or more characters.

