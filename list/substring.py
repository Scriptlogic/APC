main_str = input("Enter main string: ")
sub_str = input("Enter substring to search: ")

if sub_str in main_str:
    print(f"'{sub_str}' was found in the main string!")
else:
    print(f"'{sub_str}' was NOT found.")