from words import word_list
import random

def get_word():
        word = random.choice(word_list)
        return word.upper()

def game(word):
    word_displayed = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 0  

    print("------------------------\n")
    print("Let's play Hangman !!\n")
    print("Would you like to play in easy, medium or hard mode? \n")

    while tries == 0:
        dificulty = input("Write your dificulty here: ").upper()
        if dificulty == "EASY":
            tries = 10
        elif dificulty == "MEDIUM":
            tries = 7
        elif dificulty == "HARD":
            tries = 4
        else:
            print("That dificulty does not exist :( ")
    
    print("Ok lets start in " + dificulty + " mode, so in short you have " + " " + str(tries) + " tries to guess the word!! \n")
    print("The Start blank word is " + word_displayed + "\n")
    print("Its length is: " + str(len(word)))

    while tries > 0 and guessed == False:
        guess = input("Guess a letter or the actual word here: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Already guessed that one pal!")
                print("Currently the word is " + word_displayed  + " " + str(tries) + " left")
            elif guess not in word:
                print("The letter is not in the word.")
                tries = tries - 1
                guessed_letters.append(guess)
                print("Currently the word is " + word_displayed + " " + str(tries) + " left")
            else:
                print("Good Job ! " + guess + " is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_displayed)
                index = 0
                for letter in word:
                    if letter == guess:
                        word_as_list[index] = guess
                    index = index + 1
                word_displayed = "".join(word_as_list)
                if "_" not in word_displayed:
                    guessed = True
                print("Currently the word is " + word_displayed + " " + str(tries) + " left")

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed that word " + guess)
                print("Currently the word is " + word_displayed + " " + str(tries) + " left")
            elif guess != word:
                print("Good try, but that is not the word!")
                tries = tries - 1
                guessed_words.append(guess)
                print("Currently the word is " + word_displayed + " " + str(tries) + " left")
            else:
                guessed = True
                word_displayed = word

        else:
            print("That was an invalid guess, try again :(")

    print("Current word: " + word_displayed)    
        
    if guessed:
        print("YOU WIN! CONGRATS")
        
    else:
        print("Sorry you run out of tries... maybe next time ! The word was " + word)

word = get_word()
game(word)