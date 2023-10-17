def odds(lst):
    for i in lst:
        if i % 2:
            yield i
lst = list(map(int, input().split()))
gen = odds(lst)
for i in gen:
    print(i, end = ' ')