from serious11 import is_inside

l1 = [100, 120]
l2 = [140, 60, 100, 200]
l3 = [200, 120]
l4 = [140, 60, 100, 200]

if is_inside(l1,l2) == False and is_inside(l3,l4) == True:
    print('Your function is correct')
else:
    print('Your function is wrong')