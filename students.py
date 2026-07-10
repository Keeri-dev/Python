###### CSV ######

##### CSV stands for "comma seperated values".
#### In your terminal window, type code students.csv. Ensure your new CSV file looks like the following:
### See "students.csv"

##### Let's create a new program by typing code students.py and code as folows:

#with open("students.csv") as file:
#    for line in file:
#        row = line.rstrip().split(",")
#        print(f"{row[0]} is in {row[1]}")

##### Notice that rstrip removes the end of each line in our CSV file.
#### split tells the compiler where to find the end of each of our values in our CSV file.
### row[0] is the first element in each line of our CSV file.
## row[1] is the second element in each line in our CSV file.

##### The above code is effective at dividing each line or "record" of our CSV file.
#### However, it's a bit cryptic to look at if you are unfamiliar with this type of syntax.
### Python has bulit-in ability that could further simplify this code.

## Modify your code as follows:

#with open("students.csv") as file:
#    for line in file:
#        name, house = line.rstrip().split(",")
#        print(f"{name} is in {house}")

##### Notice that the split function actually returns two values:
#### The one before the comma and the one after the comma.
### Accordingly, we can rely upon that functionationaly to assign two variables at once instead of one!

#### Imagine that we would again like to provide this list as sorted output?

### You can modify your code as follows:

#students = []
#
#with open("students.csv") as file:
#    for line in file:
#        name, house = line.rstrip().split(",")
#        students.append(f"{name} is in {house}")
#
#for student in sorted(students):
#    print(student)

#### Notice that we create a list called students.
### We append each string to this list.
## Then, we output a sorted version of our list.

##### Recall that Python allows for a dictionaries where a key can be associated with a value.

#### This code could be further improved:

#students = []
#
#with open("students.csv") as file:
#    for line in file:
#        name, house = line.rstrip().split(",")
#        student = {}
#        student["name"] = name
#        student["house"] = house
#        students.append(student)
#
#for student in students:
#    print(f"{student['name']} is in {student['house']}")

####  Notice that this produces the desired outcome, minus the sorting of students.

### Unfortunately, we cannot sort the students as we had prior because each student is now a dictionary inside of a list.
## It would be helpful if Python could sort the students list of student dictionaries that sort this list of dictionaries by the student's name.

##### We can improve our code to illustrate this as follows:

#students = []
#
#with open("students.csv") as file:
#    for line in file:
#        name, house = line.rstrip().split(",")
#        student = {"name": name, "house": house}
#        students.append(student)
#
#for student in students:
#    print(f"{student['name']} is in {student['house']}")

#### Notice that this produce the desired outcome, minus the sorting of students.
### Unfortunately, we cannot sort the studetns as we had prior because each student is now a dictionary inside of a list.
## It would be helpful if Python could sort the students list of student dictionaries that sort this list of dictionaries by the student's name.

## To implement this in our code, make the following changes:

#students = []
#
#with open("students.csv") as file:
#    for line in file:
#        name, house = line.rstrip().split(",")
#        students.append({"name": name, "house": house})
#
#def get_name(student):
#    return student["name"]
#
#for student in sorted(students, key=get_name):
#    print(f"{student['name']} is in {student['house']}")

##### Notice that sorted needs to know how to get in the key of each student.
#### Python allows for a parameter called key where we can define on what "key" the list of students will be sorted.
### Therefore, the get_name function simply returns the key of student["name"].
## Running this program, you'll now see that the list is now sorted by name.

##### Still, our code can be further improved upon.
#### It just so happens that if you're only going to use a function like get_name once, you can simplify your code in the manner presented below.

### Modify your code as follows:

#students = []
#
#with open("students.csv") as file:
#    for line in file:
#        name, house = line.rstrip().split(",")
#        students.append({"name": name, "house": house})
#
#for student in sorted(students, key=lambda student: student["name"]):
#    print(f"{student['name']} is in {student['house']}")

##### Notie how we use a lamda function, an anonymous function, that says "Hey Python,"
#### here is a function that has no name: Given a student, access their name and return that to the key.

#### Unfortunately, our code is a bit fragile. Suppose that we changed our CSV file such that we indicated where each student grew up.
### What would be the impact of this upon our program?

## First, mdofiy your student.csv file.(done)
# Notice how running our program now will produce a number of errors/

#### Now that we're dealing with homes instead of houses, modify your code as follows:

#students =[]
#
#with open("students.csv") as file:
#        for line in file:
#          name, home = line.rstrip().split(",")
#          students.append({"name": name, "home": home})
#
#for student in sorted(students, key=lambda student: student["name"]):
#    print(f"{student['name']} is in {student['home']}")

#### Notice that running our program stil doesnt work properly.
### Can you guess why?

###### The ValueError: too many values to unpack error produced byt he compiler is a result of the fact that we previously created this program expecting the CSV file to split using a comma (,).
##### We could spend more time addressing this, but indeed someone else has already developed a way to "parse" (that is, to read) CSV files!

###### Python's built in csv library caomes with an object called a reader.
##### As the name suggests, we can use a reader to read our CSV file despite the extra comma in "Number Four, Privet Drive".
#### A reader works in a for loop, where each iteration the reader gives is another row from our CSV file.
### This row itself is a list, example, is the first element of the given row,
## while row[1] is the second element.

#import csv
#
#students = []
#
#with open("students.csv") as file:
#    reader = csv.reader(file)
#    for row in reader:
#        students.append({"name": row[0], "home": row[1]})
#
#for student in sorted(students, key=lambda student: student["name"]):
#    print(f"{student['name']} is from {student['home']}")

#### Notice that our program now works as expected.


##### Up until this point,we've been relying upon our program to specifically decide what parts of our CSV file are the names and what parts are the homes.
#### It's better design, though, to bake this directly into our CSV file by editing it as follows(done)
### Notice how we are explicitly saying in our CSV file that anything reading it should expect there to be a name value and a home value in each line.

## We can modify our code to use a part of the csv library called DictReader to treat our CSV file with even more flexibility:

#import csv
#
#students = []
#
#with open("students.csv") as file:
#    reader = csv.DictReader(file)
#    for row in reader:
#        students.append({"name": row["name"], "home": row["home"]})
#
#for student in sorted(students, key=lambda student: student["name"]):
#    print(f"{student['name']} is in {student['home']}")

##### Notice that we have replaced reader with DictReader, which returns one dictionary at a time. Also, notice that the compiler will directly access the row dictionary,
#### getting the name and home of each student. This is an example of coding defensively.
### As long as the person designing the CSV file has inputted the correct header info on the first line, we can access that info using our program.

### Up until this point, we have been reading CSV files.
## What if we want to write to a CSV file?

##### To begin, let's clean up our files a bit. First, delete the students.csv file by typing rm students.csv in the terminal window.
#### This command will only work if you're in the same folder as your students.csv file.

### Then, in students.py, modify your code as follows:

#import csv
#
#name = input("What's your name? ")
#home = input("Where's your home? ")
#
#with open("students.csv", "a") as file:
#    writer = csv.DictWriter(file, fieldnames=["name", "home"])
#    writer.writerow({"name": name, "home": home})

##### Notice how we're leveraging the built-in funtonality of DictWriter, which takes two parameters:
#### the file being written to and the fieldnames to write.
### Further, notice how the writerow function takes a dictionary as its parameter.
## Quite literallt, we're telling the compiler to write a row with two fields called name and home.
# Note that there are many types of files that you can read from and write to.



####### Returning back to students.py we can modify our code as follows, addressing some missed opportunities related to @classmethods:


class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()

##### Notice that get_student is removed and a @classmethod called get is created.
#### This method can now be called without having to create a student first.

