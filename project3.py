def calculate_tuple_product(numbers_tuple):
    """
    Calculates the product of all numbers in a given tuple.

    Args:
        numbers_tuple: A tuple containing numerical values.

    Returns:
        The product of all numbers in the tuple, or 0 if the tuple is empty.
    """
    product = 1

    for number in numbers_tuple:
        product *= number
        
    return product
data_tuple_1 = (2, 3, 4, 5)
result_1 = calculate_tuple_product(data_tuple_1)
print(f"The product of the numbers in {data_tuple_1} is: {result_1}") 
data_tuple_2 = (1.5, 2, 4)
result_2 = calculate_tuple_product(data_tuple_2)
print(f"The product of the numbers in {data_tuple_2} is: {result_2}")
data_tuple_3 = (10, 0, 5, 2)
result_3 = calculate_tuple_product(data_tuple_3)
print(f"The product of the numbers in {data_tuple_3} is: {result_3}")
data_tuple_4 = ()
result_4 = calculate_tuple_product(data_tuple_4)
print(f"The product of the numbers in {data_tuple_4} is: {result_4}")
