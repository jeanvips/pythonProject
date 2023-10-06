lst = [[1, 5, 3], [2, 44, 1, 4], [3, 3]]
def fu(p):
    return len(p), p.sort(reverse=True)
print(sorted(lst, key = fu))