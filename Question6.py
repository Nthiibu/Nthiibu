user_input = input("Enter numbers separated by spaces: ")

numbers = user_input.split()

unique_numbers = set(numbers)

new_length = len(unique_numbers)

print("New length after removing duplicates:", new_length)