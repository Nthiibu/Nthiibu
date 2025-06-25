arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
new_length = len(list(set(arr)))
print("New length after removing duplicates:", new_length)