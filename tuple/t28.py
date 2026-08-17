t = (10, 20, 10, 30, 20, 10, 40)

checked = ()

for num in t:
    if num not in checked:
        print(num, "=", t.count(num))
        checked = checked + (num,)