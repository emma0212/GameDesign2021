#Emma Hoffman
#starting from Maya Desai code
#while loop is a loop that repeats until condition is met
#if statement --> branching or selection base on conditions
# functions a piece of code that we create to prevent repetition starts with a def keyword
#program will demonstrate use of () capitalization function
#capitalize () first letter of string and make other letters lowercase
txt= "time after time"
x= txt.capitalize
print(x)
name1= "time"
name2= "after"
name3= "time"
print(name1.capitalize() + name2.capitalize() + name3.capitalize())
print("Menu")
print("1 - level 1")
print("2 - level 2")
print("3 - scores")
print("4 - exit game")
print("what do you choose?")
choice=(int(input()))
print(type(choice))
if choice == 1:
    print("Start Level 1")
    print("What is your name")
    txt=input()
    x=txt.capitalize()
    print(x)
if choice == 2:
    print("Start Level 2")
    print("Whatis your favorite color?")
    txt=input()
    x=txt.center(45)
    print(x)
if choice == 3:
    print("Start Level 3")
    print("Menu")
    print("3")
if choice == 4:
    print("goodbye")
