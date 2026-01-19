'''
give python code for checking perfect number or not
'''
def is_perfect_number(n):
    if n < 1:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n
a = 28
if is_perfect_number(a):
    print(f"{a} is a perfect number")
else:
    print(f"{a} is not a perfect number")
a = 12
if is_perfect_number(a):
    print(f"{a} is a perfect number")
else:
    print(f"{a} is not a perfect number")
a = 6
if is_perfect_number(a):
    print(f"{a} is a perfect number")
else:
    print(f"{a} is not a perfect number")
    