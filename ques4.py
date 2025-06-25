import random
# inputs and print array elements using a loop
num_elements = int(input("Enter the number of elements: "))
elements = []

for i in range(num_elements):
    element = random.randint(1, 100)  # random numbers between 1 and 100
    elements.append(element)

print("You entered:")
for element in elements:
    print(element)

print(f"Sum of the elements: {sum(elements)}")