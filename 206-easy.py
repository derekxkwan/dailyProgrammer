#python 3
opStr = input("input operator string: ")
term0 = input("input starting term: ")
termF = input("input ending term no.: ")

def getNthTerm(recurRel, firstTerm, n):
    firstTerm = int(firstTerm)
    n = int(n)
    print("Term 0: %i" %(firstTerm))
    for i in range(int(n)):
        for oper in recurRel.split():
            operStr = str(firstTerm) + oper
            firstTerm = eval(operStr)
        print("Term %i: %i" %(i+1, firstTerm))
        
getNthTerm(opStr, term0, termF)
