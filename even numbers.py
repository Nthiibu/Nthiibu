# This script defines a function to display even numbers between 50 and 80.
def display_even_numbers():
    even_numbers = [num for num in range(50, 81) if num % 2 == 0]
    print("Even numbers between 50 and 80:", even_numbers)

display_even_numbers()