def showWinner(winner):
    result = ""
    
    if winner == "player":
        result = "Você venceu!"
    elif winner == "pc":
        result = "Você perdeu!"
    else:
        result = "Empate!"
    return result