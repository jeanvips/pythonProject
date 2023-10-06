s1 = "АГТЦТЦАГЦТ"
s = list(s1)
for i in range(len(s) - 1):
    if (s[i] == "А" and s[i + 1] == "Г") or (s[i] == "Г" and s[i + 1] == "А"):
        s[i], s[i + 1] = s[i + 1], s[i]
st = ""
for i in s:
    st += i
s3 = ""
for i in range(len(st)):
    if (st[i:].startswith("ТЦ") == True) or (st[i:].startswith("ЦТ") == True):
        s3 +=  s[i] + "АГ"
    else:
        s3 += st[i]
print(s3)