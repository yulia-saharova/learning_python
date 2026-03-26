print("=== Калькулятор v1.0 ===")
finish = "да"


def calculate(a: float, b: float, op: str) -> float:
        match op:
            case "+":
                return a + b
            case "-":
                return a - b
            case "*":
                return a * b
            case "/":
                if b == 0:
                    raise ZeroDivisionError("Деление на ноль невозможно!")
                return a / b
            case "**":
                return a ** b
            case _:
                raise ValueError(f"Неизвестная операция: {op}")


while True:
    try:
        a = float(input("Введите первое число:").strip())
        operation = input("Введите операцию (+ , - , * , / , **):").strip()
        b = float(input("Введите второе число:").strip())
        
        result = calculate(a, b, operation)
        print(f"Результат: {result}")

    except ZeroDivisionError as e:
        print(f"❌ Ошибка: {e}")
    except ValueError as e:
        print(f"❌ Ошибка: {e} (проверьте, что ввели число и правильную операцию)")
    except Exception as e:
        print(f"❌ Неизвестная ошибка: {e}")

    finish = input("\nХотите продолжить? (да/нет): ").strip().lower()
    if finish not in ["да", "yes", "y", "д"]:
        print("Калькулятор завершён. До встречи! 👋")
        break

