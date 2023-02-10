import random

def start_game():
    print("\nЛаскаво просимо в гру 'Вгадай число'!")
    print("\nЯ загадав натуральне число від 1 до 100.")
    print("Спробуй вгадати його за мінімальну кількість спроб.\n")

    # загадуємо число
    number = random.randint(1, 100)
    guess = None
    tries = 0

    # ігровий цикл
    while guess != number:
        guess = int(input("Ваш варіант: "))
        if guess < number:
            print("Загадане число більше.")
        elif guess > number:
            print("Загадане число меньше.")
        tries += 1

    print("\nВітаємо, ви вгадали число!", number)
    print("Кількість ваших спроб становить:", tries)

# запускаєм игру
if __name__ == '__main__':
    start_game()
