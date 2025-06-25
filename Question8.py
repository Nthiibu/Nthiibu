# Find all leaders in an array
numbers = [16, 17, 4, 3, 5, 2]
leaders = []

# Check each number one by one
for x in range(len(numbers)):
    is_leader = True
    # Compare with all numbers to its right
    for y in range(x + 1, len(numbers)):
        if numbers[x] <= numbers[y]:
            is_leader = False
            break
    if is_leader:
        leaders.append(numbers[x])

print("Leaders in the array:", leaders)