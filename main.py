import random
def hangman():
    words = ["apple", "train", "river", "house", "chair"]
    word=random.choice(words)
    guessed_letter=[]
    attempt=6

    print("Welcome To The Game:")
    print("_ " * len(word))

    while attempt>0:
        guess=input("guess a letter: ").lower()
        if len(guess) !=1 or not guess.isalpha():
            print("Enter a single letter")
            continue
        if guess in guessed_letter:
            print("You Already Guessed the Letter")
            continue
        guessed_letter.append(guess)
        if guess in word:
            print("correct")
        else:
            attempt-=1
            print(f"wrong!! Attempts Lefts:{attempt}")
        progress = [letter if letter in guessed_letter else "_" for letter in word]
        print(" ".join(progress))
        if "_" not in progress:
            print(f"You guessed the right word it was {word}")
            break
    else:
        print(f"The game is over The word was:{word}")


hangman()




