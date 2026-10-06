from pywebio.input import input as web_input
from pywebio.output import put_text
from pywebio import start_server
import random
WORD_FILE = 'word.txt'

def load_words():
    words = {}
    try:
        with open(WORD_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    en, cn = line.split(' : ')
                    words[en.strip()] = cn.strip()
    except FileNotFoundError:
        pass
    return words

def save_words(words_dict):
    with open(WORD_FILE, 'w', encoding='utf-8') as f:
        for en, cn in words_dict.items():
            f.write(f"{en} : {cn}\n")

def add_word():
    en = web_input("Please enter a word: ").strip()
    cn = web_input("Please enter the explanation of this word: ").strip()
    words = load_words()
    if en in words:
        put_text("This word already exists")
        return
    words[en] = cn
    save_words(words)
    put_text("Successfully saved")

def delete_word():
    words = load_words()
    if not words:
        put_text("No words to delete")
        return
    word = web_input("Please enter a word you want to delete: ")
    if word in words:
        del words[word]
        save_words(words)
        put_text("Deleting successfully")
    else:
        put_text("Deleting unsuccessfully, word not found")

def review_words_English_to_Chinese():
    words = load_words()
    if not words:
        put_text("No words, please add some words before starting")
        return
    word_list = list(words.items())
    right = 0
    total = len(word_list)
    random.shuffle(word_list)
    for en, cn in word_list:
        put_text(f"What is the explanation of: {en}")
        ans = web_input("Please enter your answer: ")
        if ans == cn:
            put_text("Correct!")
            right += 1
        else:
            put_text(f"Wrong! The answer is: {cn}")
    put_text(f"Correct rate is: {right} / {total}")

def review_words_Chinese_to_English():
    words = load_words()
    if not words:
        put_text("No words, please add some words before starting")
        return
    word_list = list(words.items())
    right = 0
    total = len(word_list)
    random.shuffle(word_list)
    for en, cn in word_list:
        put_text(f"How to spell: {cn}")
        ans = web_input("Please enter your answer: ")
        if ans == en:
            put_text("Correct!")
            right += 1
        else:
            put_text(f"Wrong! The answer is: {en}")
    put_text(f"Correct rate is: {right} / {total}")

def show_all():
    words = load_words()
    if not words:
        put_text("No words")
        return
    put_text("All the words: ")
    for en, cn in words.items():
        put_text(f"{en} : {cn}")

def main():
    while True:
        put_text("\n==== My words test tool ====")
        put_text("1. adding a new word: ")
        put_text("2. deleting a word: ")
        put_text("3. Checking all the words: ")
        put_text("4. English -> Chinese review")
        put_text("5. Chinese -> English review")
        put_text("6. Quit")
        choices = web_input("Please enter a number of the functions: ")
        if choices == '1':
            add_word()
        elif choices == '2':
            delete_word()
        elif choices == '3':
            show_all()
        elif choices == '4':
            review_words_English_to_Chinese()
        elif choices == '5':
            review_words_Chinese_to_English()
        elif choices == '6':
            put_text("Quit and your words are saved automatically")
            break
        else:
            put_text("Error number")

if __name__ == "__main__":
    start_server(main, port=8080)
