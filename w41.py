def is_prime(n):
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime.
    
    for i in range(2, n):
        if n % i == 0:
            return False  # If divisible by any number other than 1 and itself, not prime.
    
    return True  # Number is prime.

number = int(input("Enter a number: "))

if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
