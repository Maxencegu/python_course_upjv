# hidden_tests_00_python_03.py

def hidden_test_exo1(my_numbers, the_sum):
    errors = []
    if my_numbers != [1, 3, 4, 5, 6]:
        errors.append("`numbers` must be [1, 3, 4, 5, 6].")
    if the_sum != sum(my_numbers):
        errors.append("`total` must be the sum of all elements in numbers.")
    return "✅ Exercise 1 passed!" if not errors else "❌ Errors:\n- " + "\n- ".join(errors)


def hidden_test_exo2(n, multiples):
    errors = []
    if n != 7:
        errors.append("`n` must be equal to 7.")
    expected = [n * i for i in range(1, 16)]
    if multiples != expected:
        errors.append("`multiples` must contain the multiplication table of 7 from 1 to 15.")
    return "✅ Exercise 2 passed!" if not errors else "❌ Errors:\n- " + "\n- ".join(errors)



def hidden_test_exo3(the_values):
    errors = []
    expected = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    if the_values != expected:
        errors.append("`values` must contain the sequence [2, 4, ..., 20].")
    return "✅ Exercise 3 passed!" if not errors else "❌ Errors:\n- " + "\n- ".join(errors)



def hidden_test_exo4(number_1, number_2, number_3, result_1, result_2, result_3):
    errors = []

    if number_1 != 9:
        errors.append("number_1 should be 9 (divisible by 3 and odd)")
    if number_2 != 6:
        errors.append("number_2 should be 6 (divisible by 3 but even)")
    if number_3 != 10:
        errors.append("number_3 should be 10 (not divisible by 3)")

    if result_1 != "Divisible by 3 and odd":
        errors.append("Expected 'Divisible by 3 and odd' for number_1 = 9")
    if result_2 != "Does not meet the condition":
        errors.append("Expected 'Does not meet the condition' for number_2 = 6")
    if result_3 != "Does not meet the condition":
        errors.append("Expected 'Does not meet the condition' for number_3 = 10")

    if errors:
        return "❌ **Tests failed:**\n" + "\n".join(f"- {e}" for e in errors)
    else:
        return "✅ **Perfect! You've correctly covered all logical conditions.**"
