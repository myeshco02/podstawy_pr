def is_binary(binary_number):
    """Checks if the given string is a valid binary number."""
    return all(char in '01' for char in binary_number)