from choose_random_numbers import chooseRandomNumbers
from generate_random_number import generateRandomNumber
from generate_random_character import generateRandomCharacter
from remove_duplicated_itens_on_list import removeDuplicatedItensOnList
from generate_random_special_character import generate_random_special_character

passwordRange = int(input("Digite o número de caracteres da senha (6 ou mais): "))

password = ""
indexList = list(range(passwordRange))
toLowerCaseLetter = True

letterPositions = chooseRandomNumbers(indexList, 2, 4)

indexList = removeDuplicatedItensOnList(indexList, letterPositions)

specialCharPositions = chooseRandomNumbers(indexList, 1, 2)

for i in range(passwordRange):
    if i in letterPositions:
        word = generateRandomCharacter()

        if toLowerCaseLetter == True:
            word = word.lower()
            toLowerCaseLetter = False
        else:
            word = word.upper()
        
        password += word

    elif i in specialCharPositions:
        password += generate_random_special_character()
    else:
        password += generateRandomNumber()

print(password)