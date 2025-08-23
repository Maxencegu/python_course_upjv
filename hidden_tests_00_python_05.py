# hidden_tests_00_python_05.py

def hidden_test_exo1(p1, Person):
    errors = []
    if not isinstance(p1, Person):
        errors.append("p1 must be an instance of Person.")
    if p1.name != "Alice":
        errors.append("p1.name must be 'Alice'.")
    if p1.age != 25:
        errors.append("p1.age must be 25.")
    return "✅ Exercise 1 passed!" if not errors else "❌ Errors:\n- " + "\n- ".join(errors)


def hidden_test_exo2(p1, Person, message):
    errors = []
    if not isinstance(p1, Person):
        errors.append("p1 must be a Person instance.")
    if message != "Hello, my name is Alice":
        errors.append("message must be 'Hello, my name is Alice'.")
    return "✅ Exercise 2 passed!" if not errors else "❌ Errors:\n- " + "\n- ".join(errors)


def hidden_test_exo3(p1, p2, ages, result):
    errors = []
    if (p1.name, p1.age) != ("Alice", 26):
        errors.append("p1 must be Alice, 26.")
    if (p2.name, p2.age) != ("Bob", 30):
        errors.append("p2 must be Bob, 30.")
    if ages != [26, 30]:
        errors.append("ages list must be [26, 30].")
    if result != 28:
        errors.append("the average must be 28.")
    return "✅ Exercise 3 passed!" if not errors else "❌ Errors:\n- " + "\n- ".join(errors)

