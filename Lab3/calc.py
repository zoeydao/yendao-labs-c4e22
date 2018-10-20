def add(x, y):
    r = x + y #function scope => kill variables that are not returned
    return r
#a, b = global scope

# a = int(input("a = "))
# b = int(input("b = "))
# t = add(a,b)
# print(t)

def eval(x,op,y):
    if op == "+":
        return x + y #return stops the function (~break)
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        return x / y

    
# x = int(input("x = "))
# y = int(input("y = "))
# op = input("Operator: ")
# t = eval(x,op,y)
# print(t)