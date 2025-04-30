with open("fileee.txt","w") as file:
    file.write("This is the file about India.")
file.close()

#split file

with open("fileee.txt","r" ) as file2:
    file02 = file2.readlines()
    for line in file02:
        line2 = line.split()
        print(line2)
file.close()

file = open("New.txt", "x")
import os
os.remove("New.txt")
