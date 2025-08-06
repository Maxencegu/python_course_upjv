# hidden_tests_00_python_02.py
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
