#students = ["Hermoine", "Harry", "Ron"]

#print(students[0])
#print(students[1])
#print(students[2])
# We then print the student who is at the 0th location,"Hermoine".Each of the other students is printed as well.


# We can use a loop to iterate over the list. Improve code as follows
#students = ["Hermoine", "Harry", "Ron"]

#for student in students:
    #print(student)
# Notice that for each student in students list, it will print the student as intended.




#### Length
### Utilize len as a way of checking the length of the list called students.
## Imagine that you dont simply want to print the name of the student but also thier postion in the list
# To accomplish this, you can edit your code as follows

#students = ["Hermoine", "Harry", "Ron"]

#for i in range(len(students)):
    #print(i + 1, students[i])

#### Executing this code results in not only getting the position of each student plus one using i + 1,
### but also prints the name of each student.
## len allows you to dynamically see how long the list of the students is regardless of how much it grows.


##### Dictionaries
#### dict or dictionaries is a data stucture that allows you to associates a key with a value
### Where a list is a list of multiple values, a dict associates a key with a value
## Considering the houses of Hogwartsl, we might assign specific students to specific houses

# We could use list alone to accomplish this :
# students = ["Hermoine", "Harry", "Ron", "Draco"]
#houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

### Notice that we can promise that we'll always keep these lists in order.
## The individual at the first position of students is associated with the house at the first position of the houses list
# However this can become quite cumbersome as our list grows



# We can better our code using a dict as follows:
#students = {
    #"Hermoine": "Gryffindor",
    #"Harry": "Gryffindor",
    #"Ron": "Gryffindor",
    #"Draco": "Slytherin",
#}
#print(students["Hermoine"])
#print(students["Harry"])
#print(students["Ron"])
#print(students["Draco"])
## Notice how we use {} to create a dictionary.
# Where list uses numbers to iterate thru the list, dict allows us to use words


# We can improve the code as follows:
#students = {
#   "Hermoine": "Gryffindor",
#    "Harry": "Gryffindor",
#    "Ron": "Gryffindor",
#    "Draco": "Slytherin",
#}
#for student in students:
#    print(student)
### Executing this code, the for loop will only iterate thru all the keys,
## resulting in a list oof the names of the students.
# How could we print out both values and keys?


# Modify your code as follows:

#students = {
#    "Hermoine": "Gryffindor",
#    "Harry": "Gryffindor",
#    "Ron": "Gryffindor",
#    "Draco": "Slytherin",
#}
#for student in students:
#    print(student, students[student])

## Notice how students[student] will go to each students key and find the value of their house.
# Execute your code, and you'll notice how the output is a bit messy.


# Clean up the print function by improving our code as follows:

#students = {
#    "Hermoine": "Gryffindor",
#    "Harry": "Gryffindor",
#    "Ron": "Gryyffindor",
#    "Draco": "Slytherin",
#}
#for student in students:
#    print(student, students[student], sep=", ")

# Notice how this creates a clan separation of a , between each item printed
## What if we have more info about our students?
# How could we associate more data with each of the students?

## You can imagine wanting to have lots of data associated with multiple keys.
# Enhance your code as follows:

#students = [
#    {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
#    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
#    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
#    {"name": "Draco", "house": "Slyhterin", "patronus": None},
#]

### Notice how this code creates a list of dicts. The list called students has four dicts within it:
## One for each student.
# Notice that Python has a special None designation where there is no value associated with a key.


## Now, you have access to a whole hsot of interesting data about these students.

# Now, further modify your code as follows:

#students = [
#    {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
#    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
#    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
#    {"name": "Draco", "house": "Slyhterin", "patronus": None},
#]
#for student in students:
#    print(student["name"], student["house"], student["patronus"], sep=", " )

# Notice how the for loop will iterate thru each of the dicts inside the list called students