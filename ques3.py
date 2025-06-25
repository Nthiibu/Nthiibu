#inputs and print array elements using a loop
elements = []

num_elements = int(input("Enter the number of elements: "))

for i in range(num_elements):
    element = input(f"Enter element {i + 1}: ")
    elements.append(element)

print("You entered:")
for element in elements:
    print(element)