t = (10, 20, 30, 40)

print("Original tuple:", t)

lst = list(t)
lst[1] = 50

t = tuple(lst)

print("Modified tuple:", t)