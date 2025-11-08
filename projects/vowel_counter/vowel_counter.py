def vowel_counter(text:str):
    text = text.lower()
    chars = "aeiou"

    vowels_counter = 0

    for char in chars:
        if char in text:
            vowels_counter += 1
    
    return vowels_counter