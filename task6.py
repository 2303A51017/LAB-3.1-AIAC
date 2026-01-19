'''
a=8
display even number
a=15
display odd number
a=0 
display even number
a=-4
display negative number
a=9.7
display as not as integer
'''
def check_number(a):
    if not isinstance(a, int):
        return "not an integer"
    elif a < 0:
        return "negative number"
    elif a % 2 == 0:
        return "even number"
    else:
        return "odd number"
a = 8
result = check_number(a)
print(f"{a} is an {result}")
a = 15
result = check_number(a)
print(f"{a} is an {result}")
a = 0
result = check_number(a)
print(f"{a} is an {result}")
a = -4
result = check_number(a)
print(f"{a} is a {result}")
a = 9.7
result = check_number(a)
print(f"{a} is {result}")