def pal():
    n = 0
    while True:
        n += 1
        if str(n) == str(n)[::-1]:
            yield n
gen = pal()
s = int(input())
while True:
    r = next(gen)
    if r > s: break
    print(r, end = ' ')