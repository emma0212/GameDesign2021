#Emma Hoffman
#started with Maria Suarez code
#lists and their functions
#indexing a list always starts in 0
from typing import Counter


myNumber=[45,20,12,2]
myFruit=["apples", "berries","mango", "banana"]
print(myFruit)
myFruit.append("blueberries")
for fruit in myFruit: #for each element in y our array get the value
    print(fruit, end= " , ")
print() 
counter=len(myFruit)    #len of Array is 1 more than last index
#for loop limits your Array order
for x in range (0,counter-1):
    print(myFruit[x], end= " , ")
print(myFruit[counter-1])
myFruit[1]="merries"
print(myFruit[1:3])
if"berries" in myFruit:
    print("Yessir")
else:
    print("Get yourself some berries")
counter=len(myFruit)
