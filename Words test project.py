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
    en = input("Please enter a word: ").strip()
    cn = input("Please enter the explanation of this word: ").strip()
    words = load_words()
    if en in words:
        print("This word already exists")
        return
    words[en] = cn
    save_words(words)
    print("Successfully saved")

def delete_word():
    words = load_words()
    if not words:
        print("No words to delete")
        return
    word = input("Please enter a word you want to delete: ")
    if word in words:
        del words[word]
        save_words(words)
        print("Deleting successfully")
    else:
        print("Deleting unsuccessfully, word not found")

def review_words_English_to_Chinese():
    words = load_words()
    if not words:
        print("No words, please add some words before starting")
        return
    word_list = list(words.items())
    right = 0
    total = len(word_list)
    random.shuffle(word_list)
    for en, cn in word_list:
        print(f"What is the explanation of: {en}")
        ans = input("Please enter your answer: ")
        if ans == cn:
            print("Correct!")
            right += 1
        else:
            print(f"Wrong! The answer is: {cn}")
    print(f"Correct rate is: {right} / {total}")

def review_words_Chinese_to_English():
    words = load_words()
    if not words:
        print("No words, please add some words before starting")
        return
    word_list = list(words.items())
    right = 0
    total = len(word_list)
    random.shuffle(word_list)
    for en, cn in word_list:
        print(f"How to spell: {cn}")
        ans = input("Please enter your answer: ")
        if ans == en:
            print("Correct!")
            right += 1
        else:
            print(f"Wrong! The answer is: {en}")
    print(f"Correct rate is: {right} / {total}")

def show_all():
    words = load_words()
    if not words:
        print("No words")
        return
    print("All the words: ")
    for en, cn in words.items():
        print(f"{en} : {cn}")

def main():
    while True:
        print("\n==== My words test tool ====")
        print("1. adding a new word: ")
        print("2. deleting a word: ")
        print("3. Checking all the words: ")
        print("4. English -> Chinese review")
        print("5. Chinese -> English review")
        print("6. Quit")
        choices = input("Please enter a number of the functions: ")
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
            print("Quit and your words are saved automatically")
            break
        else:
            print("Error number")

if __name__ == "__main__":
    main()
