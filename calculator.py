print("=== Калькулятор v1.0 ===")
finish = "да"

try:
    def calculate(a, b, op):
        match op:
            case "+":
                return a + b
            case "-":
                return a - b
            case "*":
                return a * b
            case "/":
                return a / b
            case "**":
                return a ** b


    while finish == "да":
        a = int(input("Введите первое число:"))
        operation = input("Введите операцию (+ , - , * , / , **):")
        b = int(input("Введите второе число:"))

        if operation not in ['+', '-', '*', '/', '**']:
            raise ValueError("Следует указать операцию из предложенных")
        
        
        print(calculate(a, b, operation))
        finish = input("Хотите продолжить? (да/нет):")
except ZeroDivisionError:
    print("Ошибка деления на ноль.")
except ValueError:
    print("Некорректный ввод данных")

