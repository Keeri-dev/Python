###### Inheritance ######

##### Inheritance is, perhaps, the most powerful feature of object-oriented programming.
#### It just so happens that you can create a class that "inherits" methods, variables, and attributes from another class.
### In the terminal, execute code wizard.py.

### Code as follows:

#class Wizard:
#    def __init__(self, name):
#        if not name:
#            raise ValueError("Missing name")
#        self.name = name
#
#    ...
#
#
#class Student(Wizard):
#    def __init__(self, name, house):
#        super().__init__(name)
#        self.house = house
#
#    ...
#
#
#class Professor(Wizard):
#    def __init__(self, name, subject):
#        super().__init__(name)
#        self.subject = subject
#
#    ...
#
#
#wizard = Wizard("Albus")
#student = Student("Harry", "Gryffindor")
#professor = Professor("Severus", "Defense Against the Dark Arts")
#...

###### Notice that there is a class above called Wizard and a class called Student.
##### Further, notice that there is a class called Professor. Both students and professors have names.
#### Also, both students and professors are Wizard. Within the "child" class Student, Student can inherit from the "parent" or "super" class Wizard as the line super().__init__(name) runs the init method of Wizard.
### Finally notice that the last line of this code create a wizrd called Albus, a student called Harry, and so on.


###### Inheritance and Exceptions ######

##### While we have just introduced inheritance, we have been using this all along during our use of exceptions.

#### It just so happens that expections come in a heirarchy, where there are children, parent, and grandparent classes.
### These are illustrated below:

#BaseException
# +-- KeyboardInterrupt
# +-- Exception
#      +-- ArithmeticError
#      |    +-- ZeroDivisionError
#      +-- AssertionError
#      +-- AttributeError
#      +-- EOFError
#      +-- ImportError
#      |    +-- ModuleNotFoundError
#      +-- LookupError
#      |    +-- KeyError
#      +-- NameError
#      +-- SyntaxError
#      |    +-- IndentationError
#      +-- ValueError
# ...



