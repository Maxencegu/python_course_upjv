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
