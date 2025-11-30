def calculate_power(base, exponent):
  """
  Calculates the power of a given number.

  Args:
    base: The base number.
    exponent: The exponent (n-th power).

  Returns:
    The result of base raised to the power of exponent.
  """
  if exponent == 0:
    return 1
  elif exponent < 0:
    # Handle negative exponents by calculating the reciprocal of the positive exponent
    return 1 / calculate_power(base, -exponent)
  else:
    result = 1
    for _ in range(exponent):
      result *= base
    return result

# Get input from the user
try:
  num_base = float(input("Enter the base number: "))
  num_exponent = int(input("Enter the exponent (n-th power): "))

  # Calculate and print the result
  power_result = calculate_power(num_base, num_exponent)
  print(f"{num_base} raised to the power of {num_exponent} is: {power_result}")

except ValueError:
  print("Invalid input. Please enter valid numbers.")