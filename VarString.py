# Emma Hoffman
# use different types of variables
# Use Strings functions
# Use while loop
num1 =10
num2 = 3.5
num3= 0xadff7824adf040587eadfb
name= "Colorado"
#       01234567    last index is 7 len=8
# print (type(num1))
# print(type(num2))
# print (type(num3))
# print(type(name))
# String functions
# print(name[2])      #Print the letter at index 2
# print(name[2:7])    # print set of letters from 2 to 6
# numIndex=len(name)
# print(numIndex)
# print (name[3:],end="   ") #print from 3 to end
# for var in range(1,5):
#     print(name[3:numIndex])
#     print(name[3:numIndex-var])
# print("Done")

#concadanation 
name="Peter"
lastName= "Kane"
print(name, " ", lastName)
fullName= name+" " +lastName +"/"
print(fullName)
print("Kane" in fullName)
while "Kane" in fullName:
    print(fullName)
    fullName= "Peter Kane"
print("Done")
#make a game menu then put levels
