
x = 0 
i  = 0 
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']6
lol = ""
firstTime = "yes"
n = 0
while n <= 3:
    word = (input())
    wordList = list(word)
    if word == "ALPHABET" and firstTime == "yes":
        i = 0 
        lol = ""
        while i <=((len(alpha))-1):
            lol += str(alpha[i])
            i += 1
        print(lol)
    elif word != "ALPHABET":
        i = 0
        while x <= 4:
            i  = 0 
            while i <=25:
                if wordList[x]== alpha [i]:
                    alpha[i] = ""
                i +=1 
            x +=1
        i = 0 
        
        while i <=((len(alpha))-1):
            lol += str(alpha[i])
            i += 1
        print(lol)
    n +=1