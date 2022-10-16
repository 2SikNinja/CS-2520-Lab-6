#Authors: Peter Nguyen
#Assignment: Lab #6
#Completed (or last revision): 10/11/2022
import random

#Task 1
strings = input("Enter three strings separated by a comma and space: ")
stringList = strings.split(", ")
concatenate = strings.replace(", ","#")
largestChar = max(list(strings))
for string in stringList:
    empty = ""
    for letter in string:
        empty = max(list(string))
    print("The largest character for the string", string, "is:", empty)
print("The largest character out all the strings is:", largestChar)
print(concatenate)


#Task 2
marker = True
list1 = []
while marker == True:
    floatnum = input("Enter a float, enter ! to stop: ")
    if floatnum == "!": #if the user enters !, stop the input prompt
        break
    list1.append(float(floatnum)) #add every float of the user into a list
print("List 1 is:",list1)
intnum = int(input("Enter an integer: ")) #asking user to enter int
list2 = [round(random.uniform(0,10),1) for i in range(intnum)] #create a list of random floats, the amount equal to int
print("List 2 is:",list2)
if len(list1)<len(list2): #case if list2 is larger insize than list1
    for i in range(len(list1)): #for all values in list one, add then to the end of list 2
        list2.append(list1[i])
    print("The combined list is:",list2)
    print("The last element of the combined list is:",list2[len(list2)-1])
    list2.reverse() #reverse the list2, which is now the combined list
    print("The reversed list is:",list2)
else: #cause if list2 is equal or smaller in size than list1
    for i in range(len(list2)):
        list1.append(list2[i]) #for all values in list two, add them to end of list 1
    print("The combined list is:",list1)
    print("The last element of the combined list is:",list1[len(list1)-1])
    list1.reverse() #reverse the list which is the combined list 1 and 2
    print("The reversed list is:",list1)



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
