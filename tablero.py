import random

def display_board(board):
    print("-------------")
    for row in board:
        print("|", end=" ")
        for item in row:
            print(item, end=" | ")
        print("\n-------------")

def is_valid_move(board, row, col):
    if row < 0 or row > 2 or col < 0 or col > 2:
        return False
    if board[row][col] != 0:
        return False
    return True

def is_game_over(board):
    # VALIDAR FILAS
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != 0:
            return True, row[0]
    # VALIDAR COLUMNAS
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0:
            return True, board[0][col]
    # CHECKEAR TABLERO Y DAR DIAGNOSTICO
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return True, board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return True, board[0][2]
    # VALIDACION DE FILAS
    for row in board:
        for item in row:
            if item == 0:
                return False, None
    return True, None

def get_player_move(board):
    while True:
        try:
            row = int(input("Ingrese la fila (0-2): "))
            col = int(input("Ingrese la columna (0-2): "))
            if is_valid_move(board, row, col):
                return row, col
            else:
                print("movimiento invalido intente nuevamente.")
        except ValueError:
            print("movimiento invalido intente nuevamente.")

def get_computer_move(board):
    for row in range(3):
        for col in range(3):
            if is_valid_move(board, row, col):
                board[row][col] = 2
                if is_game_over(board)[0]:
                    board[row][col] = 0
                    return row, col
                board[row][col] = 0
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if is_valid_move(board, row, col):
            return row, col

def play_game():
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    display_board(board)
    while not is_game_over(board)[0]:
        row, col = get_player_move(board)
        board[row][col] = 1
        display_board(board)
        if is_game_over(board)[0]:
            break
        print("Turno de la computadora:")
        row, col = get_computer_move(board)
        board[row][col] = 2
        display_board(board)
    if is_game_over(board)[1] == 1:
        print("Felicitaciones ha ganado")
    elif is_game_over(board)[1] == 2:
        print("Lo siento te gano la computadora")
    else:
        print("Empate")


play_game()