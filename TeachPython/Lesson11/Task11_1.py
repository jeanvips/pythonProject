import calendar, locale
locale.setlocale(locale.LC_ALL, "ru")
y = int(input("Введите год: "))
for m in range(1, 13):
    c = calendar.monthcalendar(y, m)
    week_1 = c[0]
    week_3 = c[2]
    week_4 = c[3]
    if week_1[calendar.THURSDAY]:
        fd = week_3[calendar.THURSDAY]
    else:
        fd = week_4[calendar.THURSDAY]
    print(f"{calendar.month_name[m]}: {fd}")