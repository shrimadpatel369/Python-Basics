# Define a function to check if a number is a palindrome
def is_palindrome(n):
    # Convert the number to a string
    s = str(n)
    # Reverse the string
    r = s[::-1]
    # Compare the original and reversed strings
    return s == r

# Initialize the largest palindrome and the factors
largest = 0
factor1 = 0
factor2 = 0

# Loop through all pairs of 3-digit numbers
for i in range(100, 1000):
    for j in range(100, 1000):
        # Calculate the product
        product = i * j
        # Check if the product is a palindrome and larger than the current largest
        if is_palindrome(product) and product > largest:
            # Update the largest and the factors
            largest = product
            factor1 = i
            factor2 = j

# Print the result
print("The largest palindrome made from the product of two 3-digit numbers is", largest)
print("The factors are", factor1, "and", factor2)
