def processWinner(playerAsset, computerAsset):
    winner = "empate"

    if playerAsset == "pedra":
        if computerAsset == "papel":
            winner = "pc"
        elif computerAsset == "tesoura":
            winner = "player"
    elif playerAsset == "papel":
        if computerAsset == "tesoura":
            winner = "pc"
        elif computerAsset == "pedra":
            winner = "player"
    elif playerAsset == "tesoura":
        if computerAsset == "pedra":
            winner = "pc"
        elif computerAsset == "papel":
            winner = "player"
    
    return winner