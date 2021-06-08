# Emma Hoffman
# We are going to print multiplication tables
# Using print statements and a variable
# input ---> variable is container that will hold data 
# variables need to have valid name
base = 2
numberBase = "multiplication"
base3= 3.5
#print (base + base3)
print(1 * base)  # multiplication is represented with *
print(2 * base) # division /
print(3 * base)
print(4 * base)
print(5 * base)
print(6 * base)
print(7 * base)
print(8 * base)
print(9 * base)
print(10 * base)
# when we repeat something we should loop with counter
for counter in range (1,11): #initial value that included ending value is not included
    print(counter* base, end="   ")
print()
base =3
#nested for loop
for base in range (2, 10):
    for counter2 in range (1,11): #initial value that included ending value is not included
        print(counter2* base, end="   ")
print()
base= input()
print ("Multiplication Table", base)
for counter2 in range(1,11):   #intital value included and ending value that is not included
    print(base, "x", counter2, "=", counter2 * base)

