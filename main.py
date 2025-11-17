from random import randint


def attack(name: str, role: str) -> str:
    """Возвращает нанесённый урон в зависимости от класса персонажа."""
    if role == 'warrior':
        return f'{name} нанёс урон противнику равный {5 + randint(3, 5)}'
    if role == 'mage':
        return f'{name} нанёс урон противнику равный {5 + randint(5, 10)}'
    if role == 'healer':
        return f'{name} нанёс урон противнику равный {5 + randint(-3, -1)}'
    return ''


def defence(name: str, role: str) -> str:
    """Возвращает количество заблокированного урона по классу персонажа."""
    if role == 'warrior':
        return f'{name} блокировал {10 + randint(5, 10)} урона'
    if role == 'mage':
        return f'{name} блокировал {10 + randint(-2, 2)} урона'
    if role == 'healer':
        return f'{name} блокировал {10 + randint(2, 5)} урона'
    return ''


def special(name: str, role: str) -> str:
    """Возвращает сообщение о применении специального умения."""
    if role == 'warrior':
        return f'{name} применил специальное умение «Выносливость {80 + 25}»'
    if role == 'mage':
        return f'{name} применил специальное умение «Атака {5 + 40}»'
    if role == 'healer':
        return f'{name} применил специальное умение «Защита {10 + 30}»'
    return ''


def start_training(name: str, role: str) -> str:
    """Запускает тренировку персонажа и обрабатывает команды игрока."""
    if role == 'warrior':
        print(f'{name}, ты Воитель — сильный боец ближнего боя.')
    if role == 'mage':
        print(f'{name}, ты Маг — мастер контроля стихий.')
    if role == 'healer':
        print(f'{name}, ты Лекарь — чародей, исцеляющий раны.')

    print('Потренируй навыки персонажа.')
    print('Доступные команды: attack, defence, special.')
    print('Чтобы завершить тренировку, введи: skip.')

    command: str = ''

    while command != 'skip':
        command = input('Введи команду: ')
        if command == 'attack':
            print(attack(name, role))
        if command == 'defence':
            print(defence(name, role))
        if command == 'special':
            print(special(name, role))

    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Запрашивает выбор класса персонажа и возвращает его после подтверждения."""
    role: str = ''
    approve: str = ''

    while approve != 'y':
        role = input('Введи класс персонажа: warrior, mage или healer: ')

        if role == 'warrior':
            print('Воитель — дерзкий и выносливый боец ближнего боя.')
        if role == 'mage':
            print('Маг — повелитель стихий и дальнего боя.')
        if role == 'healer':
            print('Лекарь — заклинатель, способный исцелять раны.')

        approve = input('Нажми (Y) для подтверждения или любую клавишу, чтобы выбрать снова: ').lower()

    return role



if __name__ == '__main__':
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')

    char_name: str = input('...назови себя: ')

    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы: warrior, mage, healer.')

    char_class: str = choice_char_class()

    print(start_training(char_name, char_class))



