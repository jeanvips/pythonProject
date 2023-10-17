def signs():
    i, s = 0, -1
    while True:
        i,s = i + 1, -s
        yield i * s
gen = signs()
for i in range(int(input())):
    print(next(gen), end = ',')
