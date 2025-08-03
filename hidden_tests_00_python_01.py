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

