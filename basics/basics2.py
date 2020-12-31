#The Basics: Operations with Data Types
monday_temperatures = [91, 88, 75]
monday_temperatures.append(81)
value = monday_temperatures.index(88)
#print(value)
#print(monday_temperatures.pop())

#more information on indexing
#positive, negative, slicing with brackets
#dictionaries do not use indexing, need keys

#The Basics: Functions and Conditionals
def mean(value):
    if isinstance(value, dict):
        the_mean = sum(value.values())/len(value.values())
    else:
        the_mean = sum(value)/len(value)
    return the_mean

#print(mean([4,5,6]))
#student_grades = {"Mary":91, "Sim":88, "John":75}
#print(mean(student_grades))

#The Basics: Processing User Input
def weather_check(temperature):
    if temperature > 65:
        return "The weather is WARM"
    else:
        return "The weather is COLD"

#user = float(input("Enter the temperature: "))
#print(weather_check(user))

#firstname = input("What is your first name?")
#lastname = input("What is your last name?")
#message1 = "Hello %s %s!" % (firstname, lastname)
#message2 = "Good bye {} {}!".format(firstname, lastname)
#print(message1)
#print(message2)

#The Basics: Loops
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

#for key, value in phone_numbers.items():
#    print("{} has as phone number {}".format(key, value))

while True:
    username = input("Enter username: ")
    if username == 'pypy':
        break
    else:
        continue
