
OPERATIONS = {"+", "-", "*", "/", "**"}


def calculate(a: float, b: float, op: str) -> float:
    """Функция выполняет арифметическую операцию и возвращает результат"""

    match op:
        case "+": return a + b
        case "-": return a - b
        case "*": return a * b
        case "/":
            if b == 0:
                raise ZeroDivisionError("Деление на ноль невозможно!")
            return a / b
        case "**": return a ** b
        case _:
            raise ValueError(f"Неизвестная операция: {op}")


def get_number(txt: str) -> float:
    """Функция запрашивает число"""

    while True:
        try:
            return float(input(txt).strip())
        except ValueError:
            print("Пожалуйста, введите число!")


def main():

    print("=== Калькулятор ===")

    while True:
        try:
            a = get_number("Введите первое число: ")
            operation = input("Введите операцию (+ , - , * , / , **): ").strip()
            b = get_number("Введите второе число: ")

            if operation not in OPERATIONS:
                raise ValueError(f"Неизвестная операция: {operation}")
            
            result = calculate(a, b, operation)

            print(f"Результат: {result:.4f}" if isinstance(result, float) else f"Результат: {result}")  # если вещещственное число, то отображаем 4 знака после запятой
            
        except Exception as e:
            print(f"Ошибка: {e}")
        
        if input("\nПродолжить? (да/нет): ").strip().lower() not in ["да", "yes", "y", "д", "lf"]:
            print("Калькулятор завершён. До встречи!")
            break


if __name__ == "__main__":
    main()