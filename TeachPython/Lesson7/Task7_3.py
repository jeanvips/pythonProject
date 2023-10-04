n, m = int(input("n -->")), int(input("m-->"))
lst = [[j for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        k = int(input("-->"))
        lst[i][j] = k
def spis(lst):
    l = []
    for i in lst:
        for j in i:
            l.append(j)
    a = list(set(l))
    b = sorted(a, reverse = True)
    return b[:3]
print(spis(lst))