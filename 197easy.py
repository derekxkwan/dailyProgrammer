#python3
import random

def checkDigit(multi, total):
    #check for maximal result of i*multi where 0<=i<=9 and i*multi <= total
    #has to be a solution since 0*multi = 0 <= total
    for i in reversed(range(10)):
        digitResult = i*multi
        if digitResult <= total:
            newTotal = total - digitResult
            return i, newTotal

def generateISBN():
    #maximal isbn val is where sum(1.. 10) * 9 = 495/11 = 45
    randMult = random.randint(0,45)
    totSum = 11*randMult
    #now to decompose, it's easier to start from big numbers and work downward
    numStr = ""
    for j in reversed(range(10)):
        #reversed range is 9-0, want 10-1
        newDigit, totSum = checkDigit((j+1), totSum)
        numStr = numStr + str(newDigit) 
    return numStr

def checkISBN(numCheck):
    numCheck = str(numCheck).translate("-").strip()
    if len(numCheck) != 10:
        print("incorrect number of digits")
        return False
    else:
        total = 0
        for k, digit in enumerate(numCheck):
            #since len(numCheck) == 10, k is 0-9
            multiplier = 10-k
            total = total + multiplier*int(digit)
        return total % 11 == 0
