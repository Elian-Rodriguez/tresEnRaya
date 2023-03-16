from typing import List
from tablero import *

from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping():
    return {"status": 200, "message": "Estoy listo"}

@app.post("/listas/")
async def procesar_listas(listas: List[List[int]]):
    board = listas
    print("board recibida")
    display_board(board)
    if len(board) == 3:
        display_board(board)
        if is_game_over(board)[0]:
            pass
        print("Turno de la computadora:")
        row, col = get_computer_move(board)
        board[row][col] = 2
        display_board(board)
        if is_game_over(board)[1] == 1:
            print("Felicitaciones ha ganado")
            return {"status": 200, "message": "Felicitaciones ha ganado","lista":board}
        elif is_game_over(board)[1] == 2:
            print("Lo siento te gano la computadora")
            return {"status": 200, "message": "Lo siento te gano la computadora","lista":board}
        else:
            print("Empate")
        zeros_left = True
        for sublist in board:
            if 0 in sublist:
                zeros_left = True
                break

        if zeros_left:
            print("Aún quedan ceros en la lista.")
        else:
            print("Empate")
            return {"status": 200, "message": "Lo siento se geneto un Empate","lista":board}

        # Retornamos las mismas listas recibidas
        return {"status":200, "message":"Continua Jugando", "lista":board}
    else:
        return {"status":409, "message":"Lista Invalida", "lista":[[0,0,0],[0,0,0],[0,0,0]]}
