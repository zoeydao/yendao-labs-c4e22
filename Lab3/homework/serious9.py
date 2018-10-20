def get_even_list(l):
    even_list = []
    for number in l:
        if number % 2 == 0:
            even_list.append(number)
    return(even_list)