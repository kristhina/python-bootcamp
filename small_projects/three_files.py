import datetime

now = datetime.datetime.now()

filename = now.strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt"

print(filename)

newfile = open(filename, "a")

with open("file1.txt", "r") as file1:
    f1 = file1.readlines()
    newfile.writelines(f1)
    newfile.write("\n")

with open("file2.txt", "r") as file2:
    f2 = file2.readlines()
    newfile.writelines(f2)
    newfile.write("\n")


with open("file3.txt", "r") as file3:
    f3 = file3.readlines()
    newfile.writelines(f3)
    newfile.write("\n")


newfile.close()