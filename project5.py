def print_mirrored_right_triangle(rows):
    """
    Prints a mirrored right-angled triangle pattern.

    Args:
        rows (int): The number of rows in the triangle.
    """
    for i in range(1, rows + 1):
        # Print spaces
        for j in range(rows - i):
            print(" ", end="")
        # Print stars
        for k in range(i):
            print("*", end="")
        print()  # Move to the next line

if __name__ == "__main__":
    try:
        num_rows = int(input("Enter the number of rows for the mirrored right-angled triangle: "))
        if num_rows <= 0:
            print("Please enter a positive integer for the number of rows.")
        else:
            print_mirrored_right_triangle(num_rows)
    except ValueError:
        print("Invalid input. Please enter an integer.")