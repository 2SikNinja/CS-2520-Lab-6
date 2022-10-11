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


#Task 3

j=0
names = ("Jack", "Ada", "Lev", "Kay", "Winny")
ages = [20, 18, 22, 16, 20]
n = len(names)
tupleList = names[0],names[1],names[2],names[3],names[4]
tupleLists = ((n,n+1),)*n
tupleLists = tupleList[0], tupleList[1], tupleList[2], tupleList[3], tupleList[4], 
print(tupleLists)
print(len(tupleLists[0][1]))
print(tupleList)
tup1 = (123, "abc", 4.5, ("in", 2), "end")
print(tup1)
tup2 = tuple ("bar")
atp = (1, 2, 3)
tup1 = atp[0], atp[1], atp[-1]
tup3 = tup1 + tup2
print(tup3)



# for i in names:
#     for k in names:
#         tupleList
#     j+=1
# print(tupleList)