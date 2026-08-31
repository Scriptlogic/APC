file = open("Q1.py", "r")

lines = file.readlines()

file.close()

new_file = open("without_comments.py", "w")

for line in lines:
    if not line.strip().startswith("#"):
        new_file.write(line)

new_file.close()

print("Comments removed successfully.")