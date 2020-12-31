# This code takes user inputs, turns them into sentences 
# then prints the whole long string when you end the program by typing "/end".

def sentencemaker(phrase):
    capitalized = phrase.capitalize()
    interogatives = ("who","how","what","where","why","when")
    if phrase.startswith(interogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

results = []
while True:
    user_input = input("Say something:")
    if user_input == "\end":
        break
    else:
        results.append(sentencemaker(user_input))

print(" ".join(results))

