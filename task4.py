'''
give python code to check whether a number is prime, composite or neither
'''
def check_number_type(n):
    if n <= 1:
        return "neither prime nor composite"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "composite"
    return "prime"
a = 7
result = check_number_type(a)
print(f"{a} is {result}")
a = 10
result = check_number_type(a)
print(f"{a} is {result}")
a = 1
result = check_number_type(a)

print(f"{a} is {result}")
