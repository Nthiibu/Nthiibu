numbers = [1, 2, 4, 5, 6, 7, 8, 9, 10]  

last_number = len(numbers) + 1

total_sum = last_number * (last_number + 1) // 2

current_sum = sum(numbers)

missing_number = total_sum - current_sum

print("The missing number is:", missing_number)