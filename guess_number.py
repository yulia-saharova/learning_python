import random

# Константы
YES_ANSWERS = {"да", "yes", "y", "д", "lf"}
DIF_LEVELS = {1: 50, 2: 100, 3: 1000}


def get_difficulty() -> int:
    print("Выберите уровень сложности: \n1 - от 1 до 50\n2 - от 1 до 100\n3 - от 1 до 1000\n")

    while True:
        try:
            choice_level = int(input("Ваш выбор (1/2/3): ").strip())
            if choice_level in DIF_LEVELS:
                return DIF_LEVELS[choice_level]
            print("Пожалуйста, введите только 1, 2 или 3.")
        except ValueError:
            print("Введите число 1, 2 или 3.")


def play_round(max_number: int):
    guess_number = random.randint(1, max_number)
    count_try = 0

    print(f"Я загадал число от 1 до {max_number}. Угадай!")

    while True:
        try:
            number = int(input("Ваша попытка: ").strip())
            count_try += 1

            if number == guess_number:
                print(f"Отлично! Ты угадал(а) за {count_try} попыток 🎉")
                break
            elif number < guess_number:
                print("Загаданное число больше. Попробуй еще раз!\n")
            else:
                print("Загаданное число меньше. Попробуй еще раз!\n")
        except ValueError:
            print("❌ Пожалуйста, введите целое число!\n")
            


def main():

    print("Игра - Угадай число")

    while True:
        max_num = get_difficulty()
        play_round(max_num)
    
        again = input("\nХотите сыграть ещё раз? (да/нет): ").strip().lower()
        if again not in YES_ANSWERS:
            print("Игра окончена. Спасибо за игру! До встречи!")
            break


if __name__ == "__main__":
    main()




