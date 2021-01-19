myfile = open("texts/fruits.txt")
content = myfile.read()
myfile.close()

#print(content)

#alternate way that is more streamlined to open and close a file
#with open("texts/fruits.txt") as myfile:
#    content = myfile.read()

#print(content)

#with open("texts/vegetables.txt", "w") as myfile:
#    myfile.write("celery\nbroccoli\neggplant\n")
#    myfile.write("spinach")



# Imported Modules
import time
import os
import pandas

while True:
    if os.path.exists("texts/temps_today.csv"):
        data = pandas.read_csv("texts/temps_today.csv")
        print(data.mean()["st1"])
    else:
        print("File doesn't exist")
    time.sleep(10)
