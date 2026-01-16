def generate_and_separate_squares():
    """
    Gets a number range from the user, creates a list of squares,
    and separates them into odd and even lists.
    """
    try:
        start_num = int(input("Enter the starting number of the range: "))
        end_num = int(input("Enter the ending number of the range (inclusive): "))

        # 1. Create the list of all squares using a list comprehension
        # We add 1 to end_num because range() is exclusive of the stop value.
        all_squares = [i**2 for i in range(start_num, end_num + 1)]
        print(f"\nAll squares in range {start_num}-{end_num}: {all_squares}")

        # 2. Separate odd and even squares using list comprehensions
        # Check if a number (x) is even (x % 2 == 0) or odd (x % 2 != 0)
        even_squares = [x for x in all_squares if x % 2 == 0]
        odd_squares = [x for x in all_squares if x % 2 != 0]

        print(f"\nOdd squares: {odd_squares}")
        print(f"Even squares: {even_squares}")

    except ValueError:
        print("Invalid input. Please enter integers only.")

# Run the function to start the program
generate_and_separate_squares()
