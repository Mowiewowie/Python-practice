print("Hello World!")

#regular comments

"""
this
is a
multiline
comment
"""

#variables are dynamically typed
string = "string"
integer = 10
strnumber = "10"
print(type(string))
print(type(integer))

#however it won't automatically convert it
try:
    print(strnumber - 5) #will break code
except TypeError:
    print("we had a type error!")
finally:
    print("That broke the code")

#you'd need to cast it
print(int(strnumber) - 5)

#lists (Python lists are mutable!)
myList = [1, 2, 3, 4, 5]
myList.append(6)
myList.insert(1, 1.5)
myList.pop()
myList.pop(2)

print("my list has these:")
for x in myList:
    print(x)
    
#list sort and reverse
sortList = [7, 1, 2, 6, 3, 4, 5]
sortList.sort()
sortList.reverse()


print("sortList has these:")
for x in sortList:
    print(x)
    
#copying lists, using list1 = list2 is only a reference pointer
list1 = ["a", "b", "c"]
list2 = list1.copy()

#tuples sizes and values are immutable
fruits = ("apple", "banana", "cherry")
print(fruits[1])
(green, yellow, red) = fruits #unpacking tuples

try:
    fruits[1] = "grapes"
except:
    print("tuples are immutible!")
finally:
    convertedToList = list(fruits)
    convertedToList[1] = "grapes"
    print(convertedToList[1])