import random


dif_level_values = {"1": "50", "2": "100", "3": "1000"}


print("Игра - Угадай число")
dif_level = input("Выберите уровень сложности: \n1 - от 1 до 50\n2 - от 1 до 100\n3 - от 1 до 1000\n")


print(f"Я загадал число от 1 до {dif_level_values[dif_level]}. Угадай!")
guess_number = random.randint(1, int(dif_level_values[dif_level]))

while True:
    count_try = 0

    while (number := int(input("Ваша попытка:"))) != guess_number:
        count_try += 1

        if number < guess_number:
            print("Загаданное число больше. Попробуй еще раз!\n")
        else:
            print("Загаданное число меньше. Попробуй еще раз!\n")
        
    print(f"Отлично! Ты угадал(а) за {count_try} попыток 🎉")

    finish = input("\nХотите сыграть еще раз? (да/нет): ").strip().lower()
    if finish not in ["да", "yes", "y", "д"]:
        print("Игра окончена. До встречи! 👋")
        break




