from calc import eval#, add (import * = import all)

x = int(input("Enter x "))
y = int(input("Enter y "))
op = input("Enter operator + - * / ")

r = eval(x,op,y)
print(x, op, y, "=", r)