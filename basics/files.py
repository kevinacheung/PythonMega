myfile = open("texts/fruits.txt")
content = myfile.read()
myfile.close()

#print(content)

#alternate way that is more streamlined to open and close a file
with open("texts/fruits.txt") as myfile:
    content = myfile.read()

#print(content)

with open("texts/vegetables.txt", "w") as myfile:
    myfile.write("celery\nbroccoli\neggplant\n")
    myfile.write("spinach")



# Imported Modules
