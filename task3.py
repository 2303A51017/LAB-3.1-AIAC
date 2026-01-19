'''
a=153
display as armstrong number
a=370
display as armstrong number
a=123
display as not armstrong number
'''
def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == n
a = 153
if is_armstrong(a):
    print(f"{a} is an Armstrong number")
else:
    print(f"{a} is not an Armstrong number")
a = 370
if is_armstrong(a):
    print(f"{a} is an Armstrong number")
else:
    print(f"{a} is not an Armstrong number")
a = 123
if is_armstrong(a):
    print(f"{a} is an Armstrong number")
else:
    print(f"{a} is not an Armstrong number")
    