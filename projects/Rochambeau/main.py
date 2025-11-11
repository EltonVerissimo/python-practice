import random

from show_winner import showWinner
from process_winner import processWinner

playerAsset = str(input("Escolha: pedra, papel ou tesoura? "))

listOfAssets = ["pedra", "papel", "tesoura"]

computerAsset = random.choice(listOfAssets)

winner = processWinner(playerAsset, computerAsset)

print("Computador escolheu: " + computerAsset)
print(showWinner(winner))