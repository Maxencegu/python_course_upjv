import re

def hidden_test(first_name, age, message):
    errors = []

    if not isinstance(first_name, str):
        errors.append("first_name must be a string.")
    elif first_name.strip() == "":
        errors.append("first_name must not be empty.")
    elif re.search(r'\d', first_name):
        errors.append("first_name must not contain digits.")

    if not isinstance(age, int):
        errors.append("age must be an integer.")
    elif not (16 <= age <= 25):
        errors.append("age must be between 16 and 25.")

    expected_message = f"Hello, my name is {first_name} and I am {age} years old."
    if not isinstance(message, str):
        errors.append("message must be a string.")
    elif message != expected_message:
        errors.append(f"message is incorrect. It should be: '{expected_message}'")

    if errors:
        return "❌ **Tests failed:**\n" + "\n".join(f"- {e}" for e in errors)
    else:
        return "✅ **Congratulations, all tests passed!**"
