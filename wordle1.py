print("Welcome To Wordle!\nwhere blab lab")
word = input("Please input the five letter word to be guessed:")

list = list(word)

firstLetter = list[0]
secondLetter = list[1]
thirdLetter = list[2]
fourthLetter = list[3]
fifthLetter = list[4]
correct = "no"
toBeGuessed = ["-", "-", "-", "-", "-"]
littleWrong = "!"
soWrong = "?"


while correct == "no":
    guess = input("What is the first letter?")
    if guess == firstLetter:
        toBeGuessed = [firstLetter, "-", "-", "-", "-"]
        updateGuess = ' '.join(toBeGuessed)
        print(updateGuess)
        proceed = "yes"
    elif guess == secondLetter or guess == thirdLetter or guess == fourthLetter or guess == fifthLetter:
        toBeGuessed = [littleWrong, "-", "-", "-", "-"]
        updateGuess = ' '.join(toBeGuessed)
        print(updateGuess)
        proceed = "no"

    else:
        toBeGuessed = [soWrong, "-", "-", "-", "-"]
        updateGuess = ' '.join(toBeGuessed)
        print(updateGuess)
        proceed = "no"


    while proceed == "yes" and correct == "no":
        guess = input("What is the second letter?")
        if guess == secondLetter:
            toBeGuessed = [firstLetter, secondLetter, "-", "-", "-"]
            updateGuess = ' '.join(toBeGuessed)
            print(updateGuess)
            proceed = "no"
            proceedToThird = "yes"
        elif guess == thirdLetter or guess == fourthLetter or guess == fifthLetter:
            toBeGuessed = [firstLetter, littleWrong, "-", "-", "-"]
            updateGuess = ' '.join(toBeGuessed)
            print(updateGuess)
            proceed = "yes"
        else:
            toBeGuessed = [firstLetter, soWrong, "-", "-", "-"]
            updateGuess = ' '.join(toBeGuessed)
            print(updateGuess)
            proceed = "yes"
        
    while proceedToThird == 'yes' and correct == "no":
        guess = input("What is the third letter?")
        if guess == thirdLetter:
            toBeGuessed = [firstLetter, secondLetter, thirdLetter, "-", "-"]
            updateGuess = ' '.join(toBeGuessed)
            print(updateGuess)
            proceedToThird = 'no'
            proceedToFourth = "yes"
        elif guess == fourthLetter or guess == fifthLetter:
            toBeGuessed = [firstLetter, secondLetter, littleWrong, "-", "-"]
            updateGuess = ' '.join(toBeGuessed)
            print(updateGuess)
            proceedToThird = "yes"
        else:
            toBeGuessed = [firstLetter, secondLetter, soWrong, "-", "-"]
            updateGuess = ' '.join(toBeGuessed)
            print(updateGuess)
            proceedToThird = "yes"
    
    while proceedToFourth == 'yes' and correct == "no":
        guess = input("What is the fourth letter?")
        if guess == fourthLetter:
            toBeGuessed = [firstLetter, secondLetter, thirdLetter, fourthLetter, "-"]
            updateGuess = ' '.join(toBeGuessed)
            print(updateGuess)
            proceedToFourth = "no"
            proceedToFifth = 'yes'
        elif guess == fourthLetter or guess == fifthLetter:
            toBeGuessed = [firstLetter, secondLetter, thirdLetter, littleWrong, "-"]
            updateGuess = ' '.join(toBeGuessed)
            print(updateGuess)
            proceedToFourth = "yes"
        else:
            toBeGuessed = [firstLetter, secondLetter, thirdLetter, soWrong, "-"]
            updateGuess = ' '.join(toBeGuessed)
            print(updateGuess)
            proceedToFourth = "yes"
        
    while proceedToFifth == 'yes' and correct == "no":
        guess = input("What is the fifth letter?")
        if guess == fifthLetter:
            toBeGuessed = [firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter]
            updateGuess = ' '.join(toBeGuessed)
            print(updateGuess)
            proceedToFifth = "no"
            print(f"You've got it right! the Word is {updateGuess}!\n want to play again? just type 'yes'")
            correct = "yes"
        else:
            toBeGuessed = [firstLetter, secondLetter, thirdLetter, fourthLetter, soWrong]
            updateGuess = ' '.join(toBeGuessed)
            print(updateGuess)
            proceedToFifth = "yes"

            ##PLEASE DONT MIND THIS, I DIDN'T PROPERLY READ THE INSTRUCTIONS SO I MESSED UP
            #really messed