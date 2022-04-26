words = open("realwords.csv", "r").read().split()

for word in words:
    for letter in "abcdefghijklmnopqrstuvqxyzQWERTYUIOPASDFGHJKLZXCVBNM":
        if word.count(letter) >= 3:
            print(word)
            break