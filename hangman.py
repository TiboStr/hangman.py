import random
import functions as f
playgame = True
while playgame:

    WORD = random.choice(open("hangmanwords.txt").read().split("\n")) # the word that has to be guessed
    tries = 0
    temp_word = "*" * len(WORD)
    guess = ""
    guessed_chars = []


    name = str(input("Enter your name\n> "))
    print("Hello " + name + ", you're playing the game 'hangman'. You have 10 tries to guess a randomly chosen word of " 
                + str(len(WORD)) + " characters. GLHF!")


    while "*" in temp_word and guess != WORD and tries < 10:
        guess=""
        while len(guess) != len(WORD) and len(guess) != 1 or guess in guessed_chars:
            guess = (str(input("Guess a character or try to guess the " + str(len(WORD)) + " letter word. (These are the characters that you have already tried : " + str(guessed_chars) + ")\n> ")))
            print(guess)    
        

        if (guess == WORD):
            print("Congratiulations, " + name + " you guessed the correct word in " + str(tries) + "tries!!")
          

        elif guess in WORD:
            print("Your guess was correct!")
            temp_word = f.replace_char_in_word(guess, WORD, temp_word)
            print(temp_word)
        
        else:
            guessed_chars.append(guess)
            tries+=1
            f.draw_image(tries)

    if tries == 10:
        print("You lose, the word was " + WORD + ". Better luck next time!") 
    answer = str(input("Play again? (y/n)\n> "))
    playgame = answer.lower() == "y"

