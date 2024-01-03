def sum_string_digits(str1, str2):
    # Make sure both strings are of equal length
    len1, len2 = len(str1), len(str2)
    if len1 != len2:
        raise ValueError("Input strings must have the same length")

    # Initialize the sum
    result = ''

    # Iterate through each pair of corresponding digits and add them
    for digit1, digit2 in zip(str1, str2):
        # Check if both characters are digits
        if digit1.isdigit() and digit2.isdigit():
            # Add the digits without using int function
            digit_sum = str(ord(digit1) - ord('0') + ord(digit2) - ord('0'))
            result += digit_sum
        else:
            raise ValueError("Input strings must contain only digits")

    return result

# Example usage
str1 = "126"
str2 = "456"
result = sum_string_digits(str1, str2)
print(result)
