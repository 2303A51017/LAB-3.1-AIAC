'''
give python code for palindrome number or not
'''
def is_palindrome_number(num):
    # Convert the number to string
    str_num = str(num)
    # Check if the string is equal to its reverse
    return str_num == str_num[::-1]
# Example usage
number = 124
if is_palindrome_number(number):
    print(f"{number} is a palindrome number.")
else:
    print(f"{number} is not a palindrome number.")
