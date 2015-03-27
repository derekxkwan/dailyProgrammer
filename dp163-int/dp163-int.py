#python 3
import random

playing = True
wordList = dict()
with open('enable1.txt') as f:
    for line in f:
        lineStr = line.strip()
        lineLen = len(lineStr)
        if lineLen in wordList:
            wordList[lineLen].append(lineStr)
        else:
            wordList[lineLen] = []
            wordList[lineLen].append(lineStr)

level = {
    0: {"numWords": 7, "numLetters": 4},
    1: {"numWords": 9, "numLetters": 5},
    2: {"numWords": 12, "numLetters": 6},
    3: {"numWords": 15, "numLetters": 7},
    4: {"numWords": 20, "numLetters": 10}
    }

def playGame():
    diff = input("Select difficulty (0-4): ")
    while int(diff) <0 or int(diff) > 4:
        print("Not a difficulty level")
        diff = input("Select difficulty (0-4): ")
    words = []
    wordIdx = []
    guesses = 4
    guessedWord = False
    wordNum = level[int(diff)]['numWords']
    ltrNum  = level[int(diff)]['numLetters']
    for i in range(wordNum):
        num = random.randint(0, len(wordList[ltrNum])-1)
        while num in wordIdx:
            num = random.randint(0, len(wordList[ltrNum])-1)
        wordIdx.append(num)
        words.append(wordList[ltrNum][num])
    correctWord = random.randint(0, wordNum-1)
    correctWord = words[correctWord]
    print("\n")
    for word in words:
        print(word)
    print("\n")
    while guessedWord == False and guesses > 0:
        promptStr = "Guess (" + str(guesses) + " left)? "
        guess = input(promptStr)
        guess = guess.strip().lower()
        if guess ==  correctWord.lower():
            print(str(ltrNum) + " out of " + str(ltrNum) + " correct")
            guessedWord = True
        elif len(guess) != len(correctWord):
            print("Wrong number of letters... Make guess with " + str(ltrNum) + " letters")
            guesses = guesses - 1
        else:
            numCommon = 0
            for idx, ltr in enumerate(correctWord):
                if guess[idx] == correctWord[idx]:
                    numCommon = numCommon + 1
            print("Wrong...")
            print(str(numCommon) + " out of " + str(ltrNum) + " correct")
            guesses = guesses - 1
    if guessedWord == True:
        print("YOU WIN!")
    else:
        print("You lose...")
    
while playing == True:
    playGame()
    playAgain = input("Want to play again?(y/n)")
    playAgain = playAgain.lower()
    if playAgain == "y":
        playing = True
    else:
        playing = False
