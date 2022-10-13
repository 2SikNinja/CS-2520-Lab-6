#Authors: Peter Nguyen
#Assignment: Lab #6
#Completed (or last revision): 10/11/2022

# #Task 1
# strings = input("Enter three strings separated by a comma and space: ")
# stringList = strings.split(", ")
# concatenate = strings.replace(", ","#")
# largestChar = max(list(strings))
# for string in stringList:
#     empty = ""
#     for letter in string:
#         empty = max(list(string))
#     print("The largest character for the string", string, "is:", empty)
# print("The largest character out all the strings is:", largestChar)
# print(concatenate)


#Task 2








# #Task 3
# names = ("Jack","Ada","Lev","Kay","Winny")
# ages = [20,18,22,16,20]
# #seperate names and ages for the additional case
# #names = ("Jeffery","Demarcus","Jason","Kim","David","Pat","Jielson","Manson")
# #ages = [22,17,18,21,25,16,17,19]
# nameAgePair = tuple(zip(names,ages))
# enumerate(nameAgePair)
# print(nameAgePair)
# youngestIndex = ages.index(min(ages))
# youngestPerson = names[youngestIndex]
# print(youngestPerson, "is the youngest at age",min(ages))
# average = sum(ages)/len(ages)
# print("Average age is:",average)
# newNames = [i for i in names if ages[names.index(i)]>average]
# newAges = [i for i in ages if i>average]
# newNameAgePair = tuple(zip(newNames,newAges))
# print(newNameAgePair)
