def get_letter_count_a_z(contents):
    
    letter_count = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }
    
    #letter_count = {}
    all_letters = list(contents)
    
    for letter in all_letters:
        letter = letter.lower()
        if letter in letter_count:
            letter_count[letter] = letter_count[letter]+1

    return letter_count

def get_character_count(contents):
    character_count = {}
    for c in contents:
        c=c.lower()
        if c in character_count:
            character_count[c] = character_count[c]+1
        else:
            character_count[c] = 1
    return character_count

def get_word_count(contents):
    words = contents.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letter_count_a_z = get_letter_count_a_z(text)
    character_count = get_character_count(text)
    print(letter_count_a_z)
    print(character_count)

main()