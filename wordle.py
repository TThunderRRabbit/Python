# Landon Porter R. Browning
# 190729
# September 2, 2019

# I have not discussed the Python language code in my program 
# with anyone other than my instructor or the teaching assistants 
# assigned to this course.

# I have not used Python language code obtained from another student, 
# or any other unauthorized source, either modified or unmodified.

# If any Python language code or documentation used in my program 
# was obtained from another source, such as a textbook or website, 
# that has been clearly noted with a proper citation in the comments 
# of my program.
import random
playGame = "YES"
firstGame = "yes"
numberGames = 'notValid'

def toUpperCase(characters):
    for x in range(len(characters)): #function that turns everything to uppercase
        for i in range(len(upperCase)):
            if characters[x] == lowerCase[i]:
                characters[x] = upperCase[i]
upperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
while playGame != "NO": # will keep playing unless the player types 'quit' when asked what the word is
    word = input("Please enter a 5 letter word for the player to guess:")  #asks what the wordToGuess will be
    listWord = list(word) 
    toUpperCase(listWord) #converts the list version of the word to uppercase
    word = '' #so we can convert the uppercase type of list word to string again
    for x in range(len(listWord)): #converts the listword uppercase version to list again
        word += listWord[x]
    if word == "QUIT" and firstGame == "no":
        playGame = "NO"
    if word == "RANDOM": 
        randomNumber = random.random()
        if 0<=randomNumber< 0.2:
            word = "SERIF"
        elif .2<=randomNumber< .4:
            word = "COUCH"
        elif .4<=randomNumber< .6:
            word = "DERBY"
        elif .6<=randomNumber< .8:
            word = "WORLD"
        else: 
            word = "MAGIS"  
    if len(list(word)) == 5: #checks if the word is 5, if not then it will ask again for input of word
        while numberGames == "notValid":
            n = int(input("how many tries would you like?"))
            if n>0: 
                numberGames = 'valid'
            else: 
                print('Please input a number greater than 0.')
        numberGames = 'notValid' #so that when they play again, will still ask for n times
        correct = "no"
        feedback = "-----"
        upperTemporary = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']#added this so that this will be the one that gets modify, not the original uppercase list
        while correct == "no" and n != 0:
            guess = input(f"Guess the word, {n} guess(es) left: {feedback}")    #asks for a guessWord
            listGuess = list(guess) 
            i = 0 
            x = 0
            toUpperCase(listGuess) #turns everylower case to uppercase
            guess = ''
            for x in range(len(listGuess)): #returns it as a string
                guess += listGuess[x]
            blank = ["?", "?", "?", "?", "?"] #this is the one that gets printed   
            given = list(word) #created a variable that will get modified accordingly so our basis will not be changed           
            if guess == "ALPHABET":    
                i = 0
                upperList = ""
                for i in range(len(upperCase)): #creates the string of feedback when alphabet is pressed
                    if upperTemporary[i] != '': #avoids the additional spaces printed if a character is removed from the alphabet
                        upperList += upperTemporary[i] + ' '
                print(upperList) 
            else:   
                for x in range(len(listGuess)): #removes a letter from the list, goes through every letter of the guess  
                    for i in range(len(upperCase)):
                        if listGuess[x] == upperCase[i]:
                            upperTemporary[i] = ""
                for i in range(5): #changes the "?" in the blank list if the letter is in the right position and guessed right
                    if listGuess[i] == given[i]:
                        blank[i] = given[i]
                        given[i] = "checked" #"checked" so that whenever the loop after this checks if a letter is in the wordToGuess but not in the right position, we will not get false positives
                for x in range(5): #compares whether the character is equal to any of the wordToGuess character except its own position 
                    for i in range(5):
                        if x != i and listGuess[x] == given[i]: #compares whether the character is equal to any of the wordToGuess character except its own position 
                            if blank[x] == '?': 
                                blank[x] = "!" 
                                given[i] = "checked" #added this again so that the amount of "!" is equal to the amount of match characters
                if list(word) == blank: #checks if the original word guess is equal to the blank which was updated from "???"
                    correct = "yes"
                    print("Congratulations! You win!")
                    firstGame = "no"                   
                n -= 1 
                if n == 0 and list(word) != blank: #if the amount of tries is used then do this
                    print("SORRY, YOU LOSE!")
                    firstGame = "no"

                elif list(word) != blank: #if there still amount of tries, then do this 
                    i = 0
                    feedback = ""
                    for i in range(5): 
                        feedback += str(blank[i])
                        i += 1
