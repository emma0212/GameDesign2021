#Emma Hoffman
#starting from Lucas Williams' code
#while loop is a loop that repeats until condition is met
#if statement --> branching or selection based on conditions
#functions of a piece of code that we create to prevent repetition, starts with a def key

def menu(): #declaring a function
    print("*"*28)
    print("*"," "*6,"Forerunner"," "*6,"*")
    print("*"," "*9,"Menu"," "*9,"*")
    print("*"," "*24,"*")
    print("*"," "*2,"L1- Two Betrayls"," "*4,"*")
    print("*"," "*2,"L2- Sacred Icon"," "*5,"*")
    print("*"," "*2,"L3- The Storm"," "*7,"*")
    print("*"," "*2,"EX- Exit Game"," "*7,"*")
    print("*"*28)
    print("Enter either L1,L2,L3,or EX", end= " ")

menu()  #call function
varChoice = (input()
while varChoice != "EX":
        varChoice = str(input())
print("Goodbye, Have a nice day")