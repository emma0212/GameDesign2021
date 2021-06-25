#Emma Hoffman
#started with Zoya Iyer code
myFruit=['blueberries, apples, mango, strawberries']
myStates=["California, Texas, Colorado, Wyoming"]

convert=("fill")
print(myFruit)
varChoice=0
def menu():
    print("Animal Menu")
    print("1-insert")
    print("2-find")
    print("3-remove")
    print("4-reorder")
    print("5-sort")
    print("6-exit")
    print("Enter either 1, 2, 3, 4, 5, or 6", end=" ")
    varChoice=int(input())
    return varChoice


def gamePause():
    print("Do you wish to go back to menu?")

varChoice=menu()
while varChoice !="ex":
    if varChoice == 1:
        convert= True       #boolean Variable is True or False
    while convert:
        print("insert fruit of your choice")
        ani=input()
        myFruit.append(ani)
        print(myFruit)
        convert=gamePause()
if varChoice ==2:
    convert= True
    while convert:
        print("write an item you wish to find from your list")
        fin=input
        if fin in myFruit:
            print("The item has been found")
        else:
            print("The item you wished for could not be found")
            convert=gamePause()
if varChoice == 3:
    convert= True
    while convert:
        print("choose a fruit to remove")
        dele=input()
        dele=dele.remove
        convert=gamePause()
if varChoice == 4:
    convert= True
    while convert:
        print("Write the fruit in the order you want it")
        myFruit.reverse()
        print(myFruit)
        convert=gamePause()
if varChoice == 5:
    convert=True
    while convert:
        print("choose either myFruit or myStates")
        objects=myFruit or myStates    
        input.sort
        print(objects)
        convert=gamePause()

    varChoice=menu()
print("goodbye")