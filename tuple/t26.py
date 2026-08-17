t1 = (10, 20, 30, 40, 50)
t2 = (30, 40, 50, 60, 70)

common = ()

for num in t1:
    if num in t2:
        common = common + (num,)

print("Common elements:", common)