numbers = [25, 10, 45, 5, 45, 30]
unique_numbers = list(set(numbers))
unique_numbers.sort()

if len(unique_numbers) >= 2:
    print("Second largest element:", unique_numbers[-2])
else:
    print("List does not have a second largest element.")