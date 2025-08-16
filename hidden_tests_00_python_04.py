# hidden_tests_00_python_04.py

def hidden_test_exo1(name, message):
    errors = []
    if name != "Alice":
        errors.append("`name` must be 'Alice'.")
    expected = "Hello, Alice!"
    if message != expected:
        errors.append(f"`message` must be '{expected}'.")
    return "✅ Exercise 1 passed!" if not errors else "❌ Errors:\n- " + "\n- ".join(errors)


def hidden_test_exo2(num_1, num_2, num_3, total):
    errors = []
    if (num_1, num_2, num_3) != (5, 10, 15):
        errors.append("`num_1, num_2, num_3` must be 5, 10, 15 respectively.")
    if total != num_1 + num_2 + num_3:
        errors.append("`total` must be equal to the sum of num_1, num_2, num_3.")
    return "✅ Exercise 2 passed!" if not errors else "❌ Errors:\n- " + "\n- ".join(errors)



def hidden_test_exo3(the_values):
    errors = []
    expected = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    if the_values != expected:
        errors.append("`values` must contain the sequence [2, 4, ..., 20].")
    return "✅ Exercise 3 passed!" if not errors else "❌ Errors:\n- " + "\n- ".join(errors)



def hidden_test_exo4(limit, num_primes):
    errors = []
    if limit != 20:
        errors.append("`limit` must be equal to 20.")
    expected = [2, 3, 5, 7, 11, 13, 17, 19]
    if num_primes != expected:
        errors.append("`primes` must contain the prime numbers up to 20.")
    return "✅ Exercise 4 passed!" if not errors else "❌ Errors:\n- " + "\n- ".join(errors)
