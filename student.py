###### Object-Oriented Programming ######

##### There are different paradigms of programming. As you learn other languages, you will start recognizing patterns like these.
#### Up until this point, you have worked procedurally step-by-step.
### Object Oriented programming (OOP) is a compelling solution to programming-related probelms.
## To begin, type code students.py in the terimnal window and

# Code as follows:

name = input("Name: ")
house = input("House: ")
print(f"{name} from {house}")

### Notice that this program follows a procedural, step-by-step paradigm:
## Much like you've seen in prior parts of this course.

#### Drawing on our work from previous weeks, we can create functions to abstract away parts of this program.

#def main():
#    name = get_name()
#    house = get_house()
#    print(f"{name} from {house}")
#
#
#def get_name():
#    return input("Name: ")
#
#
#def get_house():
#    return input("House: ")
#
#
#if __name__ == "__main__":
#    main()

##### Notice how get_name and get_house abstract away some of the needs of our main function.
#### Further, notice how the final lines of the code above tell the compiler to run the main function.

##### We can further simplify our program by storing the student as a tuple.
#### A tuple is a sequence of values unlike a list, a tuple cant be modified.

#### In spirit, we are returning two values.

#def main():
#    name, house = get_student()
#    print(f"{name} from {house}")
#
#
#def get_student():
#    name = input("Name: ")
#    house = input("House: ")
#    return name, house
#
#
#if __name__ == "__main__":
#    main()

#### Notice how get_student returns name, house.

#### Packing that tuple, such tha we're able to return both items to a variable called student,

### We can modify the code as follows:

#def main():
#    student = get_student()
#    print(f"{student[0]} from {student[1]}")
#
#
#def get_student():
#    name = input("Name: ")
#    house = input("House: ")
#    return (name, house)
#
#
#if __name__ == "__main__":
#    main()

#### Notie that (name, house) explicitly tells anyone reading our code that we're returning two values within one.
### Further, ntoicehow we can index into tuples using student[0] or student[1].

#### tuples are immutable, meaning we cannot change those values.

### Immutablility is a way by which we can program defensively.

#def main():
#    student = get_student()
#    if student[0] == "Padma":
#        student[1] = "Ravenclaw"
#    print(f"{student[0]} from {student[1]}")
#
#
#def get_student():
#    name = input("Name: ")
#    house = input("House: ")
#    return name, house
#
#
#if __name__ == "__main__":
#    main()

#### Notice that this code produces an error. Since tuples are immutable, we're not able to reassign the value of student[1].

### If we wanted to provide our fellow programmers flexibility, we could utlize a list as folllows.

#def main():
#    student = get_student()
#    if student[0] == "Padma":
#        student[1] = "Ravenclaw"
#    print(f"{student[0]} from {student[1]}")
#
#
#def get_student():
#    name = input("Name: ")
#    house = input("House: ")
#    return [name, house]
#
#
#if __name__ == "__main__":
#    main()

##### Note the lists are mutable. That is, the order of house and name can be switched by a programmer.
#### You might decide to utilize this in some cases where you want to provide more flexibility at the cost of the security of your code.
### After all, if the order of those values is changeable, programmers that work with you could make mistakes dow the road.

#### A dictionary could also be utilized in this implementation.

### Recall that dictionaries provide a key-value pair.

#def main():
#    student = get_student()
#    print(f"{student['name']} from {student['house']}")
#
#
#def get_student():
#    student = {}
#    student["name"] = input("Name: ")
#    student["house"] = input("House: ")
#    return student
#
#
#if __name__ == "__main__":
#    main()

##### Notice in this case, two key-value pairs are returned. An advantage of this approach is that we can index into this dictionary using the keys.

#### Still, our code can be further improved. Notic that there is an unneeded variable.
### We can remove student = {} because we dont need to create an empty dictionary.

#def main():
#    student = get_student()
#    print(f"{student['name']} from {student['house']}")
#
#
#def get_student():
#    name = input("Name: ")
#    house = input("House: ")
#    return {"name": name, "house": house}
#
#
#if __name__ == "__main__":
#    main()

##### Notice we can utilize {} braces in the return statement to create the dictionary and return at all in the same line.

#### We can provide our special case with Padma in our dictionary version of oue code.

#def main():
#    student = get_student()
#    if student["name"] == "Padma":
#        student["house"] = "Ravenclaw"
#    print(f"{student['name']} from {student['house']}")
#
#
#def get_student():
#    name = input("Name: ")
#    house = input("House: ")
#    return {"name": name, "house": house}
#
#
#if __name__ == "__main__":
#    main()

#### Notice how, similar in spirit to our previous iterations of this code, we can utilize the key names to index into our student dictionary.


###### Classes ######

##### Classes are a way by which, in object-oriented programming, we can create our own type of data and give them names.
#### A class is like a mold for a type of data - where we can invent our own data type and give them a name.

### We can modify our code as follows to implement our own class called Student:

#class Student:
#    ...
#
#
#def main():
#    student = get_student()
#    print(f"{student.name} from {student.house}")
#
#
#def get_student():
#    student = Student()
#    student.name = input("Name: ")
#    student.house = input("House: ")
#    return student
#
#
#if __name__ == "__main__":
#    main()

#### Notice by convention that Student is capitalized. Further,notice the ... simply means that we'll later return to finish that portion of our code.
### Further, notice that in get_student, we can create a student of class Student using the syntax student = Student().
## Further, notice that we utilize "dot notation" to access attributes of this variable student of class Student.

#### Any time you create a class and you utilize that blueprint to create something, you create what is called an "object" or an "instance".
### In the case of our code, student is an object.

### Further, we can lay some groundwork for the attributes that are expected inside an object whose class is Student.

## We can moify our code as follows:

#class Student:
#    def __init__(self, name, house):
#        self.name = name
#        self.house = house
#
#
#def main():
#    student = get_student()
#    print(f"{student.name} from {student.house}")
#
#
#def get_student():
#    name = input("Name: ")
#    house = input("House: ")
#    student = Student(name, house)
#    return student
#
#
#if __name__ == "__main__":
#    main(

##### Notice that within Student, we standardized the attributes of this class.
#### We can create a function within class Student, called a "method", that determines the behavior of an object of class Student.
### Within this function, it takes the name and house passed to it and assigns these variables to this object.
## Further, notice how the constructor student = Student(name, house) calls this function within the Student class and creates a student.
# self refers to the current object that was just created.

### We can simplify our code as follows:

#class Student:
#    def __init__(self, name, house):
#        self.name = name
#        self.house = house
#
#
#def main():
#    student = get_student()
#    print(f"{student.name} from {student.house}")
#
#
#def get_student():
#    name = input("Name: ")
#    house = input("House: ")
#    return Student(name, house)
#
#
#if __name__ == "__main__":
#    main()

#### Notice how return Student(name, house) simplifies the prvious iteration of our code where the constructer statement was run on its own line.

###### raise ######

##### Object-oriented program encourages you ti encapsusulate all the functionality of a class within the class defintion.
#### What if something goes wrong? What if someone tries to type in something random?
### What if someone tries to create a student without a name ?

## Modify your code as follows:

#class Student:
#    def __init__(self, name, house):
#        if not name:
#            raise ValueError("Missing name")
#        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#            raise ValueError("Invalid house")
#        self.name = name
#        self.house = house
#
#
#def main():
#    student = get_student()
#    print(f"{student.name} from {student.house}")
#
#
#def get_student():
#    name = input("Name: ")
#    house = input("House: ")
#    return Student(name, house)
#
#
#if __name__ == "__main__":
#    main()

##### Notice how we check now that a name is provided and a proper house is designated.
#### It turns out we can create ourownexecptions that alerts the programmer to a potential error created by the user called raise.
### In this case above, we raise ValueError witha specific error message.

#### It just so happens tht Python allows you to create a specific function by which you can print the attributes of an object.

### Modify your code as follows:

#class Student:
#    def __init__(self, name, house, patronus):
#        if not name:
#            raise ValueError("Missing name")
#        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#            raise ValueError("Invalid house")
#        self.name = name
#        self.house = house
#        self.patronus = patronus
#
#    def __str__(self):
#        return f"{self.name} from {self.house}"
#
#
#def main():
#    student = get_student()
#    print(student)
#
#
#def get_student():
#    name = input("Name: ")
#    house = input("House: ")
#    patronus = input("Patronus: ")
#    return Student(name, house, patronus)
#
#
#if __name__ == "__main__":
#    main()

#### Notice how def_str_(self) provides a mens by which a student is returned when called.
###  Therefore, you can now, as a programmer, print an object, its attributes, or almost anything you desire related to that object.

### __str__ is a built-in method that comes with Python classes. It just so happens that we can create our own methods for a class as well!

## Modify your code as follows:

#class Student:
#    def __init__(self, name, house, patronus=None):
#        if not name:
#            raise ValueError("Missing name")
#        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#            raise ValueError("Invalid house")
#        if patronus and patronus not in ["Stag", "Otter", "Jack Russell terrier"]:
#            raise ValueError("Invalid patronus")
#        self.name = name
#        self.house = house
#        self.patronus = patronus
#
#    def __str__(self):
#        return f"{self.name} from {self.house}"
#
#    def charm(self):
#        match self.patronus:
#            case "Stag":
#                return "🐴"
#            case "Otter":
#                return "🦦"
#            case "Jack Russell terrier":
#                return "🐶"
#            case _:
#                return "🪄"
#
#
#def main():
#    student = get_student()
#    print("Expecto Patronum!")
#    print(student.charm())
#
#
#def get_student():
#    name = input("Name: ")
#    house = input("House: ")
#    patronus = input("Patronus: ") or None
#    return Student(name, house, patronus)
#
#
#if __name__ == "__main__":
#    main()

#### Notice how we define our own method charm. Unlike dictionaries, classes can have built-in functions called methods.
### In this case, we define our charm method where specific cases have specific results.
## Further, notice that Python has the ability to utilize emojis direclty in our code.

#### Before moving forward, let us remove our patronus code.

### Modify your code as follows:

#class Student:
#    def __init__(self, name, house):
#        if not name:
#            raise ValueError("Invalid name")
#        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#            raise ValueError("Invalid house")
#        self.name = name
#        self.house = house
#
#    def __str__(self):
#        return f"{self.name} from {self.house}"
#
#
#def main():
#    student = get_student()
#    student.house = "Number Four, Privet Drive"
#    print(student)
#
#
#def get_student():
#    name = input("Name: ")
#    house = input("House: ")
#    return Student(name, house)
#
#
#if __name__ == "__main__":
#    main()

#### Notice how we have only two methods: __init__ and __str__.


###### Decorators ######

##### Properties can be utilized to harden our code. In Python, we define properties using function "decorators", which begin with @.

#### Modify your code as follows:

#class Student:
#    def __init__(self, name, house):
#        if not name:
#            raise ValueError("Invalid name")
#        self.name = name
#        self.house = house
#
#    def __str__(self):
#        return f"{self.name} from {self.house}"
#
#    # Getter for house
#    @property
#    def house(self):
#        return self._house
#
#    # Setter for house
#    @house.setter
#    def house(self, house):
#        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#            raise ValueError("Invalid house")
#        self._house = house
#
#
#def main():
#    student = get_student()
#    print(student)
#
#
#def get_student():
#    name = input("Name: ")
#    house = input("House: ")
#    return Student(name, house)
#
#
#if __name__ == "__main__":
#    main()


###### Notice how we written @property above a function called house. Doing so defines house as a property of our class.
##### With house as a property, we gain the ability to define how some attributes of our class _house, should be set and retrieved.
#### Indeed, we can now define a function called a "setter", via @house.setter, which will be called whenever the house property is set-for example, with student.hosue = "Gryffindor".
### Here, we've made our setter validate values of house for us. Notice how we raise a ValueError if the value of house is not the Harry Potter houses, otherwise, we'll use house to update the value of _house.
## Why _house and not house? house is a property of our class with functions via which a user attempts to set our class attribute. _house is that class attribute itself.
# The leading underscore,_, indicates to users they need not (and indeed, shouldnt!) modify this value directly. _house should only be set thru the house setter.

##### Notice how the house property simply returns that value of _house, our class attribute that has presumably been validated using our house setter. When a user calls student.house, they're getting the value of _house thru our house "getter".
#### In addition to the name of the house, we can protect the name of our student as well.

### Modify your code as follows:

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Invalid name")
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
