def fu(lst):
    lst_min = [i for i in range(len(lst)) if lst[i] == min(lst)]
    lst_max = [i for i in range(len(lst)) if lst[i] == max(lst)]
    return lst_min, lst_max
lst = [1, 2, 3, 4, 1, 2, 3, 4, 1, 4]
print(*fu(lst))