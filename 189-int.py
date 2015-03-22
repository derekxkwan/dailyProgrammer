#python 3
import sys
import re


vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
def romanToNums(inp):
    retNum = 0
    for i in reversed(range(len(inp))):
        if i < len(inp)-1:
            if vals[inp[i]] < vals[inp[i+1]]:
                retNum = retNum - vals[inp[i]]
            else:
                retNum = retNum + vals[inp[i]]
        else:
            retNum = retNum + vals[inp[i]]
    print(retNum)

def numsToRoman(inp):
    retStr = ""
    for i in reversed(range(len(inp))):
        checkNum = int(inp[i])*pow(10, len(inp)-1-i)    
        if checkNum == 4:
            retStr = retStr + "IV"
        elif checkNum == 9:
            retStr = retStr + "IX"
        elif checkNum >=0 and checkNum <= 8:
            remain = checkNum
            addStr = ""
            if checkNum >= 5:
                addStr = "V"
                remain = checkNum-5
            for i in range(remain):
                addStr =  addStr + "I"
            retStr = retStr + addStr
        elif checkNum == 40:
            retStr = "XL" + retStr
        elif checkNum == 90:
            retStr = "XC" + retStr
        elif checkNum >= 10 and checkNum <= 90:
            remain = int(checkNum/10)
            addStr = ""
            if checkNum >= 50:
                addStr = "L"
                remain = checkNum-5
            for i in range(remain):
                addStr = addStr + "X"
            retStr = addStr + retStr
        elif checkNum == 400:
            retStr = "CD" + retStr
        elif checkNum == 900:
            retStr = "CM" + retStr
        elif checkNum >= 100 and checkNum <= 900:
            remain = int(checkNum/100)
            addStr = ""
            if checkNum >= 500:
                addStr = "D"
                remain = checkNum-5
            for i in range(remain):
                addStr = addStr + "C"
            retStr = addStr + retStr
        else:
            for i in range(int(checkNum/1000)):
                retStr = "M" + retStr
    print(retStr)

numStr = sys.argv[1]
numStr = numStr.strip()



nums = re.findall(r'\d+', numStr)
if len(nums) > 0:
    numsToRoman(numStr)
else:
    romanToNums(numStr)
