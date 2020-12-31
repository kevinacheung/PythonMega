# List Comprehensions

temps = [221, 234, 340, 230]
new_temps = [temp / 10 for temp in temps]
#print(new_temps)

temps2 = [221, 234, 340, -9999, 230]
new_temps2 = [temp / 10 if temp!= -9999 else 0 for temp in temps2]
#print(new_temps2)

# Functions with Multiple Arguments
def mean(*args):
    return sum(args)/len(args)

#print(mean(3,4,134))

def find_winner(**kwargs):
    return max(kwargs)
print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))
