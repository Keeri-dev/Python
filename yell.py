###### map ######

##### Early on, we began with procedural programming.
#### We later revealed Python is an object oriented programming language.

##### We saw hints of functional programming, where functions have side effects without a return value.
#### We can illustrate this in the text editor window, type code yell.py and

### code as follows:

#def main():
#    yell("This is CS50")
#
#
#def yell(word):
#    print(word.upper())
#
#
#if __name__ == "__main__":
#    main()

#### Notice hwo the yell funtion is simply yelled (all caps).

##### Wouldnt it be nice to yell a list of unlimited words?

#### Modify your code as follows:

#def main():
#    yell(["This", "is", "CS50"])
#
#
#def yell(words):
#    uppercased = []
#    for word in words:
#        uppercased.append(word.upper())
#    print(*uppercased)
#
#
#if __name__ == "__main__":
#    main()

##### Notice we accumulate the uppercse words, iterating over each of the words and uppercasing them.
#### The uppercse list is printed utilizing the * to unpack it.

##### Removing the brackets, we can pass the words in as arguments.

#### In the text editor window, code as follows:

#def main():
#    yell("This", "is", "CS50")
#
#
#def yell(*words):
#    uppercased = []
#    for word in words:
#        uppercased.append(word.upper())
#    print(*uppercased)
#
#
#if __name__ == "__main__":
#    main()

##### Notice how *words allow for many arguments to be taken by the function.

#### map allows you to map a funtion to a sequence of values.

### In pratice, we can code as follows:

#def main():
#    yell("This", "is", "CS50")
#
#
#def yell(*words):
#    uppercased = map(str.upper, words)
#    print(*uppercased)
#
#
#if __name__ == "__main__":
#    main()

##### Notice how map takes two arguments. First, it takes a function we want applied to every element of a list.
#### Second, it takes that list itslef, to which we'll apply the aforementioned funxtion.
### Hence, all words in words will be handed to the str.upper function and returned uppercased.

