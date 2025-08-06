# hidden_tests_00_python_02.py

def hidden_test_exo1(x, y, sum_result):
    errors = []
    if x != 8 or y != 2:
        errors.append("x should be 8 and y should be 2.")
    if sum_result != x + y:
        errors.append("sum_result is incorrect.")
    return "✅ All tests passed for exercise 1!" if not errors else "❌ " + "\n".join(errors)


def hidden_test_exo2():
    errors = []

    try:
        score = 12
        result = ""
        if score >= 10:
            result = "Pass"
        else:
            result = "Fail"
        if result != "Pass":
            errors.append("Expected 'Pass' when score is 12")

        score = 8
        result = ""
        if score >= 10:
            result = "Pass"
        else:
            result = "Fail"
        if result != "Fail":
            errors.append("Expected 'Fail' when score is 8")

    except Exception as e:
        return f"❌ Error during test: {e}"

    return "✅ All tests passed for exercise 2!" if not errors else "❌ " + "\n".join(errors)


def hidden_test_exo3():
    errors = []

    try:
        def get_category(age):
            if age < 18:
                return "Minor"
            elif age <= 65:
                return "Adult"
            else:
                return "Senior"

        if get_category(15) != "Minor":
            errors.append("Expected 'Minor' for age = 15")
        if get_category(30) != "Adult":
            errors.append("Expected 'Adult' for age = 30")
        if get_category(70) != "Senior":
            errors.append("Expected 'Senior' for age = 70")

    except Exception as e:
        return f"❌ Error during test: {e}"

    return "✅ All tests passed for exercise 3!" if not errors else "❌ " + "\n".join(errors)


def hidden_test_exo4():
    errors = []

    def check(number):
        if number % 3 == 0 and number % 2 == 1:
            return "Divisible by 3 and odd"
        else:
            return "Does not meet the condition"

    if check(9) != "Divisible by 3 and odd":
        errors.append("Expected 'Divisible by 3 and odd' for number = 9")
    if check(6) != "Does not meet the condition":
        errors.append("Expected 'Does not meet the condition' for number = 6")
    if check(10) != "Does not meet the condition":
        errors.append("Expected 'Does not meet the condition' for number = 10")

    return "✅ All tests passed for exercise 4!" if not errors else "❌ " + "\n".join(errors)

