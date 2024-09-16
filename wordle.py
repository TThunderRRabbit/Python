print("Welcome To Wordle!\nwhere blab lab")
word = input("Please input the five letter word to be guessed:")
list = list(word)
firstLetter = list[0]
secondLetter = list[1]
thirdLetter = list[2]
fourthLetter = list[3]
fifthLetter = list[4]
correct = "no"
while correct == "no":
    guess = input("Please give a 5 letter word")
    if guess == word:
        print("you guessed right!")
        correct = "yes"