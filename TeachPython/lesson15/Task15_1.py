dct = {1:1, 2:2, 3:{2:22, 3:{1:111, 2:222, 3:{0:1111, 1:2222, 2:3333}}, 1:11}, 6:522}
lst = []

def rec_dict(d, x = int(input())):
    for k, v in d.items():
        if k == x:
            lst.append(v)
        if type(v) == dict:
            rec_dict(v, x)

rec_dict(dct)
print(lst)