my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
_len = len(my_list)
i = 0
my_list_new = []
while i < _len:
    if my_list[i] > -1:
        if my_list[i] == 0:
            i = i + 1
            continue
        else:
            my_list_new.append(my_list[i])
            i = i + 1
    else:
        break
print('Все числа:',my_list)
print('Все положительные числа (до первого отрицательного):', my_list_new)
