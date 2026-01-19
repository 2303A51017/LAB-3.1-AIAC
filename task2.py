'''
a=5
display factorial of a number is 120
'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
a = 5
result = factorial(a)
print(f"Factorial of {a} is {result}")
