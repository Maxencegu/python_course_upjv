# hidden_tests_00_python_01.py
import re

def hidden_test_exo1(first_name, age, message):
    errors = []

    if not isinstance(first_name, str) or first_name.strip() == "":
        errors.append("first_name must be a non-empty string.")
    elif re.search(r'\d', first_name):
        errors.append("first_name must not contain digits.")

    if not isinstance(age, int) or not (16 <= age <= 25):
        errors.append("age must be an integer between 16 and 25.")

    expected_message = f"Hello, my name is {first_name} and I am {age} years old."
    if not isinstance(message, str) or message != expected_message:
        errors.append(f"message is incorrect. Expected: '{expected_message}'")

    if errors:
        return "❌ **Tests failed:**\n" + "\n".join(f"- {e}" for e in errors)
    else:
        return "✅ **Congratulations, all tests passed!**"


def hidden_test_exo2(a, b, c, total, average):
    errors = []
    if (a, b, c) != (5, 10, 15):
        errors.append("Variables a, b, c must be 5, 10, 15 respectively.")
    if total != a + b + c:
        errors.append("Incorrect total value.")
    if average != total / 3:
        errors.append("Incorrect average value.")

    if errors:
        return "❌ **Tests failed:**\n" + "\n".join(f"- {e}" for e in errors)
    else:
        return "✅ **Well done! All tests passed for exercise 2!**"


def hidden_test_exo3(text, length):
    errors = []
    expected_text = "Python for Data Science"
    expected_length = len(expected_text)

    if text != expected_text:
        errors.append(f"text must be exactly: '{expected_text}'.")
    if length != expected_length:
        errors.append(f"length must be {expected_length} (the length of the text).")

    if errors:
        return "❌ **Tests failed:**\n" + "\n".join(f"- {e}" for e in errors)
    else:
        return "✅ **Great! All tests passed for exercise 3!**"


def hidden_test_exo4(number_1, number_2, sum_result, diff_result, prod_result, quot_result, rem_result):
    errors = []

    if number_1 != 7 or number_2 != 3:
        errors.append("Variables number_1 and number_2 must be 7 and 3 respectively.")

    if sum_result != number_1 + number_2:
        errors.append("Incorrect sum_result value.")
    if diff_result != number_1 - number_2:
        errors.append("Incorrect diff_result value.")
    if prod_result != number_1 * number_2:
        errors.append("Incorrect prod_result value.")
    if quot_result != number_1 / number_2:
        errors.append("Incorrect quot_result value (should be division).")
    if rem_result != number_1 % number_2:
        errors.append("Incorrect rem_result value (should be modulo).")

    if errors:
        return "❌ **Tests failed:**\n" + "\n".join(f"- {e}" for e in errors)
    else:
        return "✅ **Well done! All tests passed for exercise 4!**"


def hidden_test_exo5(colors):
    errors = []

    if not isinstance(colors, list):
        errors.append("`colors` must be a list.")
    else:
        expected = ["red", "purple", "green", "yellow"]
        if colors != expected:
            errors.append(f"`colors` list is incorrect. Expected: {expected}")

    if errors:
        return "❌ **Tests failed:**\n" + "\n".join(f"- {e}" for e in errors)
    else:
        return "✅ **Great job! Exercise 5 passed successfully!**"


def hidden_test_exo6(numbers, even_numbers):
    errors = []

    if not isinstance(numbers, list):
        errors.append("`numbers` must be a list.")
    else:
        expected_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if numbers != expected_numbers:
            errors.append(f"`numbers` list is incorrect. Expected: {expected_numbers}")

    if not isinstance(even_numbers, list):
        errors.append("`even_numbers` must be a list.")
    else:
        expected_even = [2, 4, 6, 8, 10]
        if even_numbers != expected_even:
            errors.append(f"`even_numbers` list is incorrect. Expected: {expected_even}")

    if errors:
        return "❌ **Tests failed:**\n" + "\n".join(f"- {e}" for e in errors)
    else:
        return "✅ **Great job! Exercise 6 passed successfully!**"


def hidden_test_exo7(numbers, sum_of_numbers):
    errors = []
    expected_list = [1, 2, 3, 4, 6, 7, 8, 9, 10, 15]

    if numbers != expected_list:
        errors.append(f"List 'numbers' is incorrect. Expected {expected_list}")

    if sum_of_numbers != sum(expected_list):
        errors.append(f"Sum 'sum_of_numbers' is incorrect. Expected {sum(expected_list)}")

    if errors:
        return "❌ **Tests failed:**\n" + "\n".join(f"- {e}" for e in errors)
    else:
        return "✅ **Well done! All tests passed for exercise 7!**"


def hidden_test_exo8(values, squared, average):
    errors = []

    expected_values = [4, 8, 15, 16, 23, 42]
    expected_squared = [16, 64, 100]  # Squares under or equal 200 + appended 100
    expected_average = sum(expected_squared) / len(expected_squared)

    # Check values list unchanged
    if values != expected_values:
        errors.append(f"'values' list must be {expected_values}")

    # Check squared list content
    if sorted(squared) != sorted(expected_squared):
        errors.append(f"'squared' list is incorrect. Expected elements {expected_squared}")

    # Check average
    if not (abs(average - expected_average) < 1e-6):
        errors.append(f"'average' value is incorrect. Expected {expected_average}")

    if errors:
        return "❌ **Tests failed:**\n" + "\n".join(f"- {e}" for e in errors)
    else:
        return "✅ **Excellent! All tests passed for exercise 8!**"



