from long_word_detector import detect_long_word

text = str(input("Digite um texto: "))

long_words = detect_long_word(text)

if long_words:
    print(f"Palavras longas encontradas: {long_words}")
else:
    print("Nenhuma palavra longa foi encontrada no texto.")