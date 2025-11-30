def count_digits(number):
  """
  Calculates the total number of digits in a given integer.

  Args:
    number: The integer for which to count the digits.

  Returns:
    The total number of digits in the integer.
  """
  if number == 0:
    return 1  

  count = 0
  if number < 0:
    number = abs(number)

  while number > 0:
    number //= 10  
    count += 1
  return count
try:
  user_input = int(input("Enter an integer: "))
  num_digits = count_digits(user_input)
  print(f"The number {user_input} has {num_digits} digits.")
except ValueError:
  print("Invalid input. Please enter an integer.")