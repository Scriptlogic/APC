t1 = (10, 20, 30, 40)
t2 = (30, 40, 50, 60)

merged = t1 + t2

result = ()

for num in merged:
    if num not in result:
        result = result + (num,)

print("Merged tuple:", result)