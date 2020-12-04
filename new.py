import os
def draw_board(board):
    os.system('cls')
    print ("-------------")
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
    print("-------------")


def player_input(player):
    if player:
        x = int(input('Ходит х, выбирите место:'))
        if 1 <= x <= 9:
            board[x-1] = 'X'
            return False
    else:
        x = int(input('Ходит о, выбирите место:'))
        if 1 <= x <= 9:
            board[x-1] = 'O'
            return True
def check(board):
    for i in range(3):
        if any([str(board[0+i*3]) == str(board[1+i*3]) == str(board[2+i*3]),
                str(board[0]) == str(board[4]) == str(board[8]),
                str(board[2]) == str(board[4]) == str(board[6]),
                str(board[i]) == str(board[i+3]) == str(board[i+6])]):
            return True

def winer(player):
    if player:
        return 'O'
    else:
        return 'X'

board = [i+1 for i in range(9)]
player = True
print('Правила игры:')
print('по очереди вводите цифры')
print('от 1 до 9 иначе игрок ')
print('набравший другую цифру будит ходить заново')
input('Нжмите Enter для продолжения')
while True:
    draw_board(board)
    player = player_input(player)
    if check(board):
        os.system('cls')
        print('Выйграл:', winer(player))
        break
print(input('Нажмите Enter для завершения'))
