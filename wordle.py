word = input("Please enter a word for the player to guess:")
feedback = "-----"
correct = "no"
n=6 
while correct == "no" and n != 0:
    guess = input(f"Guess the word, {n} guess(es) left: {feedback}")    
    listGuess = list(guess)
    i = 0
    blank = ["?", "?", "?", "?", "?"]    
    given = list(word)
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
    n -= 1 
    if n == 0 and word != blank:
        print("SORRY, YOU LOSE!")
    elif list(word) != blank: 
        i = 0
        feedback = ""
        while i <= 4: 
            feedback += str(blank[i])
            i += 1
             
    

