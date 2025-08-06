# hidden_tests_00_python_02.py

def hidden_test_exo1(x, y, sum_result):
    errors = []
    if x != 8 or y != 2:
        errors.append("x should be 8 and y should be 2.")
    if sum_result != x + y:
        errors.append("sum_result is incorrect.")
    return "✅ All tests passed for exercise 1!" if not errors else "❌ " + "\n".join(errors)
