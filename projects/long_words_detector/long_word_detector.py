from format_list_to_str import format_list_to_string

def detect_long_word(text:str):
    words = text.split()
    long_words = []

    for word in words:
        if len(word) > 10:
            long_words.append(word)

    return format_list_to_string(long_words)