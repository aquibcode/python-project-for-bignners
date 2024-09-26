# Get input from the user
n = int(input("Enter a number to calculate its factorial: "))

# Initialize the result to 1 (factorial of 0 is 1)
result = 1

# Calculate the factorial using a for loop
for i in range(1, n + 1):
    result *= i

# Print the result
print(f"The factorial of {n} is {result}")
