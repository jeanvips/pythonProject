import re
s = input()
print(re.sub(r"(\b\w+\b)\W+\b\1", r"\1", s))