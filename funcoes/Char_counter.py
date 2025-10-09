def char_counter(word = ""):
    wordLengh = len(word)
    return wordLengh

word = str(input("Digite uma palavra: "))

print(f"Essa palavra tem {char_counter(word)} caracteres.")