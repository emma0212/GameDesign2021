# Emma Hoffman
# 6/4/2021
# We are going to print multiplication tables
# Using print statements and a variable
# input ---> from the user
# use the function input ()
# variables need to have valid name
base= int(input())
print (type(base))
print ("Multiplication Table", base)
for counter2 in range(1,11):  #intital value included and ending value that is not included
    print(base, "x", counter2, "=", counter2 * base)
base1= int(input())
print (type(base))
print ("Addition Table", base)
for counter2 in range (1,11): #initial value included and ending value that is not included
    print(base1, "+", counter2, "=", counter2 + base1 )
base2= int(input())
print (type(base))
print ("Subtraction Table", base)
for counter2 in range (1,11): #initial value included and ending value that is not included
    print(base2, "-", counter2, "=", counter2 - base2 )
base3= int(input())
print (type(base))
print ("Division Table", base)
for counter2 in range (1,11): #initial value included and ending value that is not included
    print(base3, "/", counter2, "=", counter2 / base3 )