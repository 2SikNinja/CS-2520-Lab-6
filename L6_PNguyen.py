#Authors: Peter Nguyen
#Assignment: Lab #6
#Completed (or last revision): 10/11/2022
import random

#Task 1
strings = input("Enter three strings separated by a comma and space: ")
stringList = strings.split(", ")
merge = strings.replace(", ","#")
largestCharacter = max(list(strings))
for string in stringList:
    empty = ""
    for letter in string:
        empty = max(list(string))
    print("The largest character for the string", string, "is:", empty)
print("The largest character out all the strings is:", largestCharacter)
print(merge)

# Output for Task 1
# Enter three strings separated by a comma and space: Hello, You, Bye
# The largest character for the string Hello is: o
# The largest character for the string You is: u
# The largest character for the string Bye is: y
# The largest character out all the strings is: y
# Hello#You#Bye

# Enter three strings separated by a comma and space: Peter, Lawrence, Johnny, Anderson, Richard, Johnosn, Lester, Random
# The largest character for the string Peter is: t
# The largest character for the string Lawrence is: w
# The largest character for the string Johnny is: y
# The largest character for the string Anderson is: s
# The largest character for the string Richard is: r
# The largest character for the string Johnosn is: s
# The largest character for the string Lester is: t
# The largest character for the string Random is: o
# The largest character out all the strings is: y
# Peter#Lawrence#Johnny#Anderson#Richard#Johnosn#Lester#Random






#Task 2
marker = True
list1 = []
while marker == True:
    floatnum = input("Enter a float, enter ! to stop: ")
    if floatnum == "!":
        break
    list1.append(float(floatnum)) 
print("List 1 is:",list1)
intnum = int(input("Enter an integer: ")) 
list2 = [round(random.uniform(0,10),1) for i in range(intnum)] 
print("List 2 is:",list2)
if len(list1)<len(list2):
    for i in range(len(list1)):
        list2.append(list1[i])
    print("The combined list is:",list2)
    print("The last element of the combined list is:",list2[len(list2)-1])
    list2.reverse()
    print("The reversed list is:",list2)
else:
    for i in range(len(list2)):
        list1.append(list2[i])
    print("The combined list is:",list1)
    print("The last element of the combined list is:",list1[len(list1)-1])
    list1.reverse()
    print("The reversed list is:",list1)


# Outputs for Task 2
# Enter a float, enter ! to stop: 10.2
# Enter a float, enter ! to stop: 20.1
# Enter a float, enter ! to stop: 15.2
# Enter a float, enter ! to stop: !
# List 1 is: [10.2, 20.1, 15.2]
# Enter an integer: 5
# List 2 is: [3.3, 8.4, 9.6, 1.7, 6.3]
# The combined list is: [3.3, 8.4, 9.6, 1.7, 6.3, 10.2, 20.1, 15.2]
# The last element of the combined list is: 15.2
# The reversed list is: [15.2, 20.1, 10.2, 6.3, 1.7, 9.6, 8.4, 3.3]

# Enter a float, enter ! to stop: 40.2
# Enter a float, enter ! to stop: 60.1
# Enter a float, enter ! to stop: 100.1
# Enter a float, enter ! to stop: 89.9
# Enter a float, enter ! to stop: !
# List 1 is: [40.2, 60.1, 100.1, 89.9]
# Enter an integer: 8 
# List 2 is: [4.7, 3.8, 7.2, 7.3, 1.4, 5.2, 1.4, 8.8]
# The combined list is: [4.7, 3.8, 7.2, 7.3, 1.4, 5.2, 1.4, 8.8, 40.2, 60.1, 100.1, 89.9]
# The last element of the combined list is: 89.9
# The reversed list is: [89.9, 100.1, 60.1, 40.2, 8.8, 1.4, 5.2, 1.4, 7.3, 7.2, 3.8, 4.7]









#Task 3
names = ("Jack","Ada","Lev","Kay","Winny")
ages = [20,18,22,16,20]
nameAgePair = tuple(zip(names,ages))
enumerate(nameAgePair)
print(nameAgePair)
youngestIndex = ages.index(min(ages))
youngestPerson = names[youngestIndex]
print(youngestPerson, "is the youngest at age",min(ages))
average = sum(ages)/len(ages)
print("Average age is:",average)
newNames = [i for i in names if ages[names.index(i)]>average]
newAges = [i for i in ages if i>average]
newNameAgePair = tuple(zip(newNames,newAges))
print(newNameAgePair)

# Outputs for Task 3
# (('Jack', 20), ('Ada', 18), ('Lev', 22), ('Kay', 16), ('Winny', 20))
# Kay is the youngest at age 16
# Average age is: 19.2
# (('Jack', 20), ('Lev', 22), ('Winny', 20))

# (('Peter', 11), ('John', 19), ('Kevin', 20), ('Helen', 17), ('Amy', 26))
# Peter is the youngest at age 11
# Average age is: 18.6
# (('John', 19), ('Kevin', 20), ('Amy', 26))
