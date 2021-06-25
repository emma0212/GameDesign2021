#Emma Hoffman
#06/14/2021
# Learn how to open files

import os
import sys
import time
# print("Hi...... Allow me to guess your name")
# time.sleep(3)
# print("..almost there")
# print("... Yes, you are Emma")
# time.sleep(2)
# #os.system('cls')
# file=input("Please enter file name and extension of the file. Ex file.txt :")
# #check if file exists
# if os.path.exists(file):
#PENCIL= open(file, 'r')
#print(PENCIL.read())
#PENCIL.close()
# else:
#print("File not found, it most likely does not exist")
BOOK=open("asdfre.txt", 'w')
BOOK.write("\n you are amazing")
time.sleep(1)
BOOK.close()
#try to put score into file