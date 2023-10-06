lst = ["abab", "xx", "aaaaaaaa", "abcbab"]
print(sorted(lst, key = lambda x: (-len(set(x)), x)))