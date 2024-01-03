def newton_sqrt_string(number_str, initial_guess='1', tolerance=0.0001):
    def to_int(s):
        # Convert string representation to an integer equivalent
        if '.' in s:
            integer, decimal = s.split('.')
            return int(integer + decimal)
        else:
            return int(s)

    parts = number_str.split('+')

    if len(parts) == 1:  # Real number
        real_part = number_str
        imaginary_part = '0'
    else:  # Complex number
        real_part = parts[0]
        imaginary_part = parts[1][:-1]

    guess_real = initial_guess

    while True:
        next_guess_real = str((to_int(guess_real) + to_int(real_part)) // (2 * to_int(guess_real)))

        # Convergence check by looking at the difference between squares
        diff = abs(to_int(next_guess_real) ** 2 - to_int(real_part))
        if diff <= to_int(str(tolerance).replace('.', '')):
            break
        guess_real = next_guess_real

    if imaginary_part == '0':
        return f"{next_guess_real}"
    else:
        guess_imaginary = '0'

        while True:
            next_guess_imaginary = str(
                (to_int(guess_imaginary) + to_int(imaginary_part)) // (2 * to_int(next_guess_real))
            )

            # Convergence check for the imaginary part
            diff_imaginary = abs(to_int(next_guess_imaginary) ** 2 - to_int(imaginary_part))
            if diff_imaginary <= to_int(str(tolerance).replace('.', '')):
                break
            guess_imaginary = next_guess_imaginary

        return f"{next_guess_real}+{next_guess_imaginary}i"

# Example usage:
float_number_str = "8.7"
complex_number_str = "4.2+3.6i"

float_result = newton_sqrt_string(float_number_str)
print(f"The square root of {float_number_str} is approximately {float_result}")

complex_result = newton_sqrt_string(complex_number_str)
print(f"The square root of {complex_number_str} is approximately {complex_result}")
