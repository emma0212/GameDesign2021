#Emma Hoffman
#started with Maria Suarez code
#lists and their functions
#indexing a list always starts in 0
from typing import Counter
import random

myFruit=["apples", "berries","mango", "banana"]
print(myFruit)
for fruit in myFruit:
    print(fruit, end= " , ")
fruity=("apple, banana, strawberry")
print(fruity)
temp=list(fruity)
temp.insert(1,"blackberry")
fruity=tuple(temp)
print(fruity)



for fruit in myFruit:
    print(fruit, end= " , ")
print()
counter=len(myFruit)    #len of Array is 1 more than last index
#for loop limits your Array order
#finding a random number to be the index to select randint
indx=random.randint(0,counter-1)
print(indx)
print("your lucky fruit is",myFruit[indx] )
word=random.choice(myFruit)
print("your lucky fruit is", word)
input()
#random method choice
word=random.choice(myFruit)
print("Your random fruit is", word)



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
