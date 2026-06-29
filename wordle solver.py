file_path = 'valid-wordle-words.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()

valid_words = []
valid_chars = set("abcdefghijklmnopqrstuvwxyz")

for line in lines:
    word = line.strip()
    valid_words.append(word)

words = []
values = []
quit = False

while True:
    word = input("Next word: ")
    
    if (word == "q"):
        quit = True
        break

    if (len(word) != 5):
        print("Must be 5 characters long")
        continue

    if not all(char in valid_chars for char in word):
        print("Invalid characters, enter a valid 5-letter word")
        continue


    while True:
        value = input("Value: ")
    
        if (value == "q"):
            quit = True
            break
        
        if (len(value) != 5):
            print("Must be 5 characters long")
            continue
        
        if not all(char in "012" for char in value):
            print("Please enter 0, 1, or 2 for each character")
            continue
        
        break

    if (not quit):
        values.append(value)
        words.append(word)

    print(words)
    print(values)

    for (word, value) in zip(words, values):
        for i in range(5):
            if (value[i] == "0"):
                valid_words = [valid_word for valid_word in valid_words if word[i] not in valid_word]
            elif (value[i] == "1"):
                valid_words = [valid_word for valid_word in valid_words if word[i] in valid_word and word[i] != valid_word[i]]
            elif (value[i] == "2"):
                valid_words = [valid_word for valid_word in valid_words if valid_word[i] == word[i]]
    
    print("\nPossible words:")
    print(valid_words)

    if (len(words) >= 5 or quit):
        break

print("\nPossible words:")
