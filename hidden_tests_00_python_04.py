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



def hidden_test_exo3(result1, result2, numbers):
    errors = []
    if numbers != [6, 9]:
        errors.append("You must test the function with numbers 4 and 7.")
    if result1 is not True:
        errors.append("`result1` must be True for 6.")
    if result2 is not False:
        errors.append("`result2` must be False for 9.")
    return "✅ Exercise 3 passed!" if not errors else "❌ Errors:\n- " + "\n- ".join(errors)



def hidden_test_exo4(limit, num_primes):
    errors = []
    if limit != 20:
        errors.append("`limit` must be equal to 20.")
    expected = [2, 3, 5, 7, 11, 13, 17, 19]
    if num_primes != expected:
        errors.append("`primes` must contain the prime numbers up to 20.")
    return "✅ Exercise 4 passed!" if not errors else "❌ Errors:\n- " + "\n- ".join(errors)
