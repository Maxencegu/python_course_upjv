# hidden_tests.py
def run_test(exercise):
    if exercise == "exo1":
        return hidden_test_exo1(first_name, age, message)
    elif exercise == "exo2":
        return hidden_test_exo2(a, b, c, total, average)
    else:
        return f"❌ Unknown exercise: {exercise}"

def hidden_test_exo1(first_name, age, message):
    import re
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
