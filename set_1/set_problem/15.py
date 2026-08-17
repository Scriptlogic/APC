# 15. Check whether two sets have no common elements

set1 = {1, 2, 3}
set2 = {4, 5, 6}

if set1.isdisjoint(set2):
    print("Sets have no elements in common")
else:
    print("Sets have common elements")