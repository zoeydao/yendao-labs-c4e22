import random
from calc import eval

def generate_quiz():
    x = random.randint(0, 10)
    y = random.randint(0, 10)
    op = random.choice(['+','-','*','/'])
    error = random.randint(-1,1)
    r = eval(x,op,y) + error
    return [x,y,op,r]

x,y,op,r = generate_quiz()

output = "{0} {1} {2} = {3}".format(x, op, y, r)
print(output)

user_input = input("Y/N? ").upper()

if r == eval(x,op,y):
    if user_input == "Y":
        print("Yay")
    elif user_input == "N":
        print("You're wrong")
else:
    if user_input == "Y":
        print("You're wrong")
    elif user_input == "N":
        print("Yay")
