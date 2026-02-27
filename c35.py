def is_palindrome(number):
    s = str(number)
    reversed_s = s[::-1]
    return s == reversed_s
user_input = input("Enter a number to check if it is a palindrome: ")
if is_palindrome(user_input):
    print(f"The number {user_input} is a palindrome.")
else:
    print(f"The number {user_input} is not a palindrome.")
