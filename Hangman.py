import random
def hangman():
    words = ["Alert", "train", "river", "house", "chair" ,"Angle","Aware" ,"Black",
"Agent","Badly","Blame"]
    word=random.choice(words)
    guessed_letter=[] #guess letter should be stored in list
    attempt=6

    print("Welcome To The Game:")
    print("choose the correct word from the list given below")
    print(words)
    print("_ " * len(word))

    #the loop will run untill the attempts are more than 0
    while attempt>0:
        guess=input("guess a letter: ").lower()  
        if len(guess) !=1 or not guess.isalpha():  #Input should be only a alphabet 
            print("Enter a single letter")
            continue

        if guess in guessed_letter:
            print("You Already Guessed the Letter")  #Not to repeat the guessed letter
            continue

        guessed_letter.append(guess) #If the user's input letter is right print correct
        if guess in word:
            print("correct")

        else:
            attempt-=1
            print(f"wrong!!, Attempts Lefts:{attempt}") #It tells the number of attempts left

        progress = [letter if letter in guessed_letter else "_" for letter in word] #list comprehnsion it checks the every letter enter by the user and if the letter is correct it remove (_) and show the letter 
        print(" ".join(progress))

        if "_" not in progress:
            print(f"You guessed the right word it was {word}") #if you guess the right word it shows that word and break the loop
            break
        
    else:
        print(f"The game is over The word was:{word}") #If the user is failed to guess than the game is over and all attmpts are used


hangman() #to run the game or functiom




