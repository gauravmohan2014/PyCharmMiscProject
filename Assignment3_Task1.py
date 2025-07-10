def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

x = int(input("Enter a number: "))
sample_num = factorial(x)
print("Factorial of", x,  "is:", sample_num)