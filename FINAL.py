import random
terminate = "PLAY"
notFirstGame = "no"
while terminate != "QUIT":
    word = input("Please enter a word for the player to guess:")
    if word == "QUIT" and notFirstGame == "yes":
        terminate = "QUIT"
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
            word = "JACOB"  
        print(word)
    if len(list(word)) == 5:
        n = int(input("how many tries would you like?"))
        correct = "no"
        feedback = "-----"
        alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        beta = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        while correct == "no" and n != 0:
            guess = input(f"Guess the word, {n} guess(es) left: {feedback}")    
            listGuess = list(guess)
            i = 0 
            x = 0
            while x < len(listGuess):
                i = 0
                while i < len(alpha):
                    if listGuess[x] == beta[i]:
                        listGuess[x] = alpha[i]
                    i += 1
                x += 1
            i = 0
            blank = ["?", "?", "?", "?", "?"]    
            given = list(word)
            if guess == "ALPHABET":
                i = 0
                alphaRray = ""
                while i <= (len(alpha)-1):
                    alphaRray += alpha[i]
                    i+=1
                print(alphaRray) 
            else:   
                x = 0 
                while x < len(listGuess): 
                    i = 0 
                    while i<= (len(alpha)-1):
                        if listGuess[x] == alpha[i]:
                            alpha[i] = ""
                        i += 1
                    x+=1
                i = 0        
                while i<=4:      
                    if listGuess[i] == given[i]:
                        blank[i] = given[i]
                        given[i] = "checked"
                    i += 1
                x = 0
                while x<=4:
                    i = 0 
                    while i<=4:
                        if listGuess[x] == given[i] and x != i:
                            if blank[x] == '?':
                                blank[x] = "!"
                        i +=1    
                    x += 1 
                if list(word) == blank:
                    correct = "yes"
                    print("Congratulations! You win!")
                    notFirstGame = "yes"
                    
                    
                n -= 1 
                if n == 0 and list(word) != blank:
                    print("SORRY, YOU LOSE!")
                    notFirstGame = "yes"

                elif list(word) != blank: 
                    i = 0
                    feedback = ""
                    while i <= 4: 
                        feedback += str(blank[i])
                        i += 1
    elif word == "QUIT":
        begin = "no"