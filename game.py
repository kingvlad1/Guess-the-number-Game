import random

def start_game():
    print("Ласкаво просимо в гру 'Вгадай число'!")
    print("\nЯ загадав натуральне число від 1 до 100.")
    print("Спробуй вгадати його за мінімальну кількість спроб.\n")
    print("Game by kingvlad.")

    # бот агадує число
    number = random.randint(1, 100)
    guess = None
    tries = 0

    # ігровий цикл
    while guess != number:
        guess = int(input("Ваш варіант: "))
        if guess < number:
            print(f"Загадане число більше за {guess}")
        elif guess > number:
            print(f"Загадане число меньше за {guess}.")
        tries += 1

    print("\nВітаємо, ви вгадали число!", number)
    print("Кількість ваших спроб становить:", tries)

# запускаєм игру
if __name__ == '__main__':
    start_game()

#end code
