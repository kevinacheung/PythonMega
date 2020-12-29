import datetime
mynow = datetime.datetime.now()
#print("The time is " + str(mynow))

mynumber = 10
mytext = "Hello"
#print(mytext + " " + str(mynumber))

x = 15
y = 2
z = 1111
#print(x, y, z)

temperatures = [91, 88, 75]
studentgrades = {"Ann":91, "Bob":88, "Chris":75}
studsum = sum(studentgrades.values())
studlen = len(studentgrades.values())
print("The sum is " + str(studsum) + " and the count is " + str(studlen) + " and the average is " + str(studsum/studlen))

print("Why is Github integration so hard???")