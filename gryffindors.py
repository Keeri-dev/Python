##### And code as follows:

#students = [
#    {"name": "Hermione", "house": "Gryffindor"},
#    {"name": "Harry", "house": "Gryffindor"},
#    {"name": "Ron", "house": "Gryffindor"},
#    {"name": "Draco", "house": "Slytherin"},
#]
#
#gryffindors = []
#for student in students:
#    if student["house"] == "Gryffindor":
#        gryffindors.append(student["name"])
#
#for gryffindor in sorted(gryffindors):
#    print(gryffindor)

##### Notice we have a conditional while we're creating our list.
#### If the student's house is Gryffindor, we append the student to the list of names. Finally, we print all the names.

##### More elegantly, we can simplify this code with a list comprehension as follows:

#students = [
#    {"name": "Hermione", "house": "Gryffindor"},
#    {"name": "Harry", "house": "Gryffindor"},
#    {"name": "Ron", "house": "Gryffindor"},
#    {"name": "Draco", "house": "Slytherin"},
#]
#
#gryffindors = [
#    student["name"] for student in students if student["house"] == "Gryffindor"
#]
#
#for gryffindor in sorted(gryffindors):
#    print(gryffindor)

###### filter ######

##### Using Python's filter function allows us to return a subset of a sequence for which a certain condtition is true.

#### In the text editor window, code as follows:

#students = [
#    {"name": "Hermione", "house": "Gryffindor"},
#    {"name": "Harry", "house": "Gryffindor"},
#    {"name": "Ron", "house": "Gryffindor"},
#    {"name": "Draco", "house": "Slytherin"},
#]
#
#
#def is_gryffindor(s):
#    return s["house"] == "Gryffindor"
#
#
#gryffindors = filter(is_gryffindor, students)
#
#for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
#    print(gryffindor["name"])

##### Notice how a function called is_grfyyindor is created. This is our filtering function that will take a student s, and return True or Flase depending on whether the student's house is Gryffindor.
#### You can see the new filter function takes two arguments. First, it take the function that will be applied to each element in a sequence - in this case, is_gryffindor.
### Second, it takes the sequence to which it will apply the filtering function - in this case, students.
## In gryffindors, we should see only those students who are in Gryffindor.

##### filter can also use lamda funtions as follows:

#students = [
#    {"name": "Hermione", "house": "Gryffindor"},
#    {"name": "Harry", "house": "Gryffindor"},
#    {"name": "Ron", "house": "Gryffindor"},
#    {"name": "Draco", "house": "Slytherin"},
#]
#
#
#gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)
#
#for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
#    print(gryffindor["name"])

#### Notice how the same list of students is provided.

###### Dictionary Comprehensions ######

##### We can apply the same idea behind list_comprehensions to dictionaries.

#### In the text editor window, code as follows:

#students = ["Hermione", "Harry", "Ron"]
#
#gryffindors = []
#
#for student in students:
#    gryffindors.append({"name": student, "house": "Gryffindor"})
#
#print(gryffindors)

##### Notice how all the prior code is simplified intoa single line where the structure of the dictionary is provided for each student in students.

#### We can even simplify further as follows:

#students = ["Hermione", "Harry", "Ron"]
#
#gryffindors = {student: "Gryffindor" for student in students}
#
#print(gryffindors)

#### Notice how the dictionary will be constructed with key-value pairs.


###### enumerate ######

##### We may wish to provide some ranking of each student.

#### In the text editor window, code as follows:

#students = ["Hermione", "Harry", "Ron"]
#
#for i in range(len(students)):
#    print(i + 1, students[i])

#### Notice how each student is enumerated when running this code.

#### Utilizing enumeration, we can do the same:

students = ["Hermione", "Harry", "Ron"]

for i, student in enumerate(students):
    print(i + 1, student)

### Notice how enumerate presents the index and the value of each student.