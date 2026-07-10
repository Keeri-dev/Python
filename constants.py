###### Constants ######

##### Some languages aloow you to create variables that are unchangeable, called "constants"

#### In the text ediotr window, code as follows:

#MEOWS = 3
#
#for _ in range(MEOWS):
#    print("meow")

###### Notice MEOWS is our constant in this case. Constants are typically denoted by capital variable names and are placed at the top of our code.
##### Though this looks like a constant, in reality, Python actually has no mechanism to prevent us from changing that value within our code!
#### Instead, you're on the honor system: if a variable name is written in all caps, just don't change it!

#### One can create a class "constant", now in quotes because we know Python doesnt quite support "constants".

### In the text editor window, code as follows:

class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")


cat = Cat()
cat.meow()

#### Because MEOWS is defined outside of any particular class method, all of them have access to that value via Cat.MEOWS.