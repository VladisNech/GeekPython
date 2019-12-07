def game():
    import random
    number = random.randint(1, 100)
    # print(number)
    # задаем переменные и создаем список
    user_number = None
    count = 0
    levels = {1: 10, 2: 5, 3: 3}
    max_count = levels[int(input('Введите уровень сложности от 1 до 3 - '))]
    # Вводим пользователей
    user_count = int(input('Введите количество пользователей - '))
    users = []
    for i in range(user_count):
        user_name = input(f'Введите имя пользователя {i + 1} - ')
        users.append(user_name)

    is_winner = False
    winner_name = None
    # начинаем цикл
    while not is_winner:
        # Считаем попытки
        count += 1
        if count > max_count:
            print('Все пользователи проиграли')
            break
        # Логика подбора чисел
        print(f'Попытка № {count}')
        for number_enum, user in enumerate(users, 1):
            print(f'Ход пользователя №{number_enum} {user}')
            user_number = int(input('Введите число - '))
            if user_number == number:
                is_winner = True
                winner_name = user
                break
            elif user_number > number:
                print('Загаданное число меньше')
            else:
                print('Загаданное число больше')
    else:
        print(f'Пользователь {winner_name} выиграл')
