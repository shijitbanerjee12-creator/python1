def decimal_to_binary(decimal_num):
    """
    Converts a decimal number to its binary representation.

    Args:
        decimal_num: An integer representing the decimal number.

    Returns:
        A string representing the binary equivalent of the decimal number.
    """
    if decimal_num == 0:
        return "0"

    binary_digits = []
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_digits.append(str(remainder))
        decimal_num //= 2


    return "".join(binary_digits[::-1])

# Example usage
number = 28
binary_representation = decimal_to_binary(number)
print(f"The binary representation of {number} is: {binary_representation}")

number = 15
binary_representation = decimal_to_binary(number)
print(f"The binary representation of {number} is: {binary_representation}")

number = 0
binary_representation = decimal_to_binary(number)
print(f"The binary representation of {number} is: {binary_representation}")