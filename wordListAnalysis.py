
def load_words(path):
    words = open(path, "r").read().split()


def print_duplicated_letter_words(words, min_duplicated=3):
    for word in words:
        for letter in "abcdefghijklmnopqrstuvqxyzQWERTYUIOPASDFGHJKLZXCVBNM":
            if word.count(letter) >= min_duplicated:
                print(word)
                # If the word is five letters and it has three duplicates, then we no longer need to search for duplicates.
                if min_duplicated >= 3:
                    break
            

if __name__ == "__main__":
    words = load_words("realwords.csv")
    
    print_duplicated_letter_words(words)
