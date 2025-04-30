with open("file.txt","w") as file:
    file.write("This is the file about codingal.")
file.close()

#split file

with open("file.txt","r" ) as file2:
    file02 = file2.readlines()
    for line in file02:
        line2 = line.split()
        print(line2)
file.close()


