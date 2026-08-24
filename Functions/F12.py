def is_palindrome(value):
    value = str(value)

    if value == value[::-1]:
        return True
    else:
        return False

value = input("Enter a string or number: ")

print(is_palindrome(value))