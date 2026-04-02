import random

# Константы
YES_ANSWERS = {"да", "yes", "y", "д", "lf"}
DIF_LEVELS = {
    1: {"name": "Лёгкий", "max_num": 50,  "max_attempts": 10},
    2: {"name": "Средний", "max_num": 100, "max_attempts": 8},
    3: {"name": "Сложный", "max_num": 1000, "max_attempts": 6}
}


def get_difficulty():
    """Функция запрашивает уровень сложности и возвращает настройки"""
    
    print("Выберите уровень сложности: ")

    for key, level in DIF_LEVELS.items():
        print(f"{key} — {level['name']} (1–{level['max_num']}, {level['max_attempts']} попыток)")

    while True:
        try:
            choice_level = int(input("\nВаш выбор (1/2/3): ").strip())
            if choice_level in DIF_LEVELS:
                return DIF_LEVELS[choice_level]
            print("Пожалуйста, введите число 1, 2 или 3.")
        except ValueError:
            print("Введите корректное число!")



def play_round(max_number: int, max_attempts: int) -> int:
    guess_number = random.randint(1, max_number)
    count_try = 0

    print(f"Я загадал число от 1 до {max_number}")
    print(f"У тебя {max_attempts} попыток. Удачи!\n")

    while count_try < max_attempts:
        try:
            number = int(input(f"Попытка {count_try + 1}/{max_attempts}: ").strip())
            count_try += 1

            if number == guess_number:
                print(f"Отлично! Ты угадал(а) число {guess_number} за {count_try} попыток")
                return count_try
            elif number < guess_number:
                print("Загаданное число больше. Попробуй еще раз!")
            else:
                print("Загаданное число меньше. Попробуй еще раз!")
        except ValueError:
            print("Пожалуйста, введите целое число!\n")

    # Если попытки закончились
    print(f"\n К сожалению, попытки закончились. Я загадал число: {guess_number}")
    return count_try
            


def main():
    """Главная функция игры"""


    print("Игра - Угадай число")

    best_score = None

    while True:
        level = get_difficulty()
        attempts_used = play_round(level["max_num"], level["max_attempts"])
    
        if best_score is None or attempts_used < best_score:
            best_score = attempts_used
            print(f"Новый лучший результат: {best_score} попыток!")

        again = input("\nХотите сыграть ещё раз? (да/нет): ").strip().lower()
        if again not in YES_ANSWERS:
            print("Игра окончена")
            break

    if best_score:
        print(f"Ваш лучший результат за сессию: {best_score} попыток")
    print("Спасибо за игру! До новых встреч")



if __name__ == "__main__":
    main()




