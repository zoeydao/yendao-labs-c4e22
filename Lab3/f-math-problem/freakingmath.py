from random import *

def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(0, 10)
    y = randint(0, 10)
    op = choice(['+','-','*','/'])
    error = random.randint(-1,1)
    r = eval(x,op,y) + error
    return [x,y,op,r]

def check_answer(x, y, op, result, user_choice):
    print(user_choice)
    return True
