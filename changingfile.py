import time, sys, os

os.system('cls')
file="newfile.txt"
FILE=open(file,'r')
print(FILE.read())
FILE.close()
FILE=open(file, 'r')
contest_list=FILE.readlines()
#print(contest_list)
sorted_List=sorted(contest_list)[::-1]
print(sorted_List)
FILE.close()
#sorted_List=sorted(contest_list, key=lambda x: int(x.split()[4]), reverse=True)
# for line in range [5]:
#     print(sorted_List[line])