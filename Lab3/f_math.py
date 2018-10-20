from random import randint

x = randint(0, 10)
y = randint(0, 10)
# result = x + y
# r = randint(result - 3, result + 3)
error = randint(-1,1)
r = x + y + error
output = "{0} + {1} = {2}".format(x, y, r)
print(output)


user_input = input("Y/N? ").upper()
if r == x + y:
    if user_input == "Y":
        print("Yay")
    elif user_input == "N":
        print("You're wrong")
    else:
        print("Invalid")
else:
    if user_input == "Y":
        print("You're wrong")
    elif user_input == "N":
        print("Yay")
    else:
        print("Invalid")      
