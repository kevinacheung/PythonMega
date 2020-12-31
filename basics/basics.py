## THE BASICS: Small Program
import datetime
mynow = datetime.datetime.now()
#print("The time is " + str(mynow))

## THE BASICS: Data Types
mynumber = 10
mytext = "Hello"
#print(mytext + " " + str(mynumber))

x = 15
y = 2
z = 1111
#print(x, y, z)
#print(x + y + z)

scores = [91, 88, 75] #list
studentgrades = {"Ann":91, "Bob":88, "Chris":75} #dictionary
studsum = sum(studentgrades.values())
studlen = len(studentgrades.values())
#print("The sum is " + str(studsum) + " and the count is " + str(studlen) + " and the average is " + str(studsum/studlen))

#print("Why is Github integration so hard???")

monday_temp = (71, 83, 77) #tuple is immutable
print(monday_temp)
tues_temp = [71, 83, 77] #list is mutable
tues_temp.append(75)
tues_temp.remove(83)
#print(tues_temp)

mood = "Tatte"
strength = "9.8"
rank = "4"

x = 4
y = 9.8
z = 3
s = x + y + z
print(s)

temperatures = [44.7, 41, "37"]
rainfall = [44.7, 41, "37", [1,2,3]]

student_grades = [9.1, 8.8, 7.5]
max_value = max(student_grades)
print(max_value)

student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
student_grades.count(10.0)

username = "Python3"
print(username.lower())