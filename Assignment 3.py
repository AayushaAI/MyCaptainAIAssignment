def fibonacci_upto_20():
    a, b = 0, 1
    print("Fibonacci sequence up to 20 terms:")
    for _ in range(20):
        print(a, end=" ")
        a, b = b, a + b
    print()  # For a new line after the sequence

# Call the function to display the sequence
fibonacci_upto_20()




