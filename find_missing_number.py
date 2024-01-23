def missing_number(lst : list) -> list:
    numbers = set(lst)
    output = []
    for i in range(1, lst[-1]):
        if i not in numbers:
            output.append(i)
    return output

lst = [1,2,3,5,6,7,8,9,10,12,13,14]
print(missing_number(lst))