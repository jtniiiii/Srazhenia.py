'''
1 игрок - символ х
2 игрок - символ 0

поле из 9 клеток: 3 ряда по 3 клетки

игроки ходят по очереди
ход - игрок ставит свой символ в любую свободную клетку
пустая клетка - если в нее не походил другой игрок

победа:
    занять любой горизонтальный ряд символави одного игрока
    занять любую вертикальную колонну символави одного игрока
    занять любую диогональ символави одного игрока
ничья - свободные клетки кончились, а победитель не выявлен

победа и ничья прекращают игру
'''
# глобальные константы
EMPTY = '.'
PLAYER_1 = 'X'
PLAYER_2 = '0'


def get_field() -> list:
    ''' Возвращает игровое поле из 9 клеток, заполненых EMPTY '''
    return [EMPTY] * 9

def draw_field(field: list) -> None:
    ''' Выводит на экран поле в 3 ряда по 3 клетки в каждом '''
    for i in range(0, 7, 3):
        print(field[i], field[i + 1], field[i + 2])

def make_turn(flield: list, player: str) -> None:
    ''' 
    Спрашивает, в какую клетку поля поставить player
    Проверить есть ли такая клетка на поле
    Свободна ли выбронная клетка на поле
    Если проверки пройдены, заменить клетку на player
    '''
    pass

def main():
    ''' Главная функция '''
    field = get_field()
    draw_field(field)
    turn = 1
    while turn <= 9: # TODO: при  победе одного из игроков вый...
        ''' Переделать кусок. Если turn не четный, плеер 1, если четны - плеер 2. Короче просто проверка'''
        make_turn(field, PLAYER_1)
        turn += 1
        make_turn(field, PLAYER_2)
        turn += 1
    else:
        print('Игра окончена, Ничья!')

main()