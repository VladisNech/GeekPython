# Урок 4
"""""
Задание №3
Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
name - строка полученная от пользователя,
health = 100,
damage = 50. 
### Поэкспериментируйте со значениями урона и жизней по желанию. 
### Теперь надо создать функцию attack(person1, person2). Примечание: имена аргументов можете указать свои. 
### Функция в качестве аргумента будет принимать атакующего и атакуемого. 
### В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого. 
Функция должна сама работать со словарями и изменять их значения.
"""""

player = {'name': input(),
          'health': 100,
          'damage': 50}

enemy = {'name': input(),
         'health': 200,
         'damage': 40}


def attack(person1):
    if person1 == enemy['name']:
        player['health'] = player['health'] - enemy['damage']
        return player['health']
    elif person1 == player['name']:
        enemy['health'] = enemy['health'] - player['damage']
        return enemy['health']


print(attack(person1=input()))
