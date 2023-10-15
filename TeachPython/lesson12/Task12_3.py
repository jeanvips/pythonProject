def funct(s):
    str = s.split(",")
    lst_range = [i.split("-") for i in str]
    lst_range = [[int(i) for i in j] for j in lst_range]
    lst = []
    for i in lst_range:
        for j in range(i[0], i[1] + 1):
            lst.append(j)
    return lst
s = "1-2,4-4,3-6"
print(funct(s))