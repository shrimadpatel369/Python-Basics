a = int(float(input("Enter any one number:")))
b = int(a**0.5)
limit = b + 1
is_prime = True  

if a <= 1:
    is_prime = False
else:
    for i in range(2, limit):
        if a % i == 0:
            is_prime = False
            break  

if is_prime:
    print(a, "is a prime number")
else:
    print(a, "is not a prime number")
