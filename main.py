from typing import List
# Skeleton code for even_list
def even_list(int_list: List[int]) -> List[int]:
    """
    Determines if a number is even and return an even list.
    Args:
    int_list: A list of integer.
    Returns:
    A list of even integers.
    """
    even_numbers = []
    for num in int_list:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

# Skeleton code for sum_of_squares_of_even
def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    """
    Computes the sum of the squares of all even numbers in a list of integers.
    Args:
    even_int_list: A list of even integers.
    Returns:
    The sum of the squares of all even numbers in the list.
    """
    sum_of_squares = 0
    for num in even_int_list:
        square = num ** 2
        sum_of_squares += square
    return sum_of_squares

# Main function
def main():
# Example list
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_int_list = even_list(int_list)
    output = sum_of_squares_of_even(even_int_list)
    print(output)
# Boilerplate code
if __name__ == "__main__":
    main()