#python3

class prioQ:
    def __init__(self):
        self.queue = []

    def enqueue(self, name, pA, pB):
        isStr = type(name) is str
        isNum = type(pA) is int or type(pA) is float
        isNum2 = type(pB) is int or type(pB) is float
        if isStr and isNum and isNum2: 
            self.queue.append((name, pA, pB))
        else:
            print("wrong datatypes")
    
    def dequeueA(self):
        toDQ = [0]
        for i, tup in enumerate(self.queue):
            if i > 0:
                isHigher = self.queue[i][1] > self.queue[toDQ[0]][1]
                isEqual = self.queue[i][1] == self.queue[toDQ[0]][1]
                if isHigher:
                    toDQ = [i]
                elif isEqual:
                    toDQ.append(i)
        self.queue.pop(toDQ[0])


    def dequeueB(self):
        toDQ = [0]
        for i, tup in enumerate(self.queue):
            if i > 0:
                isHigher = self.queue[i][2] > self.queue[toDQ[0]][2]
                isEqual = self.queue[i][2] == self.queue[toDQ[0]][2]
                if isHigher:
                    toDQ = [i]
                elif isEqual:
                    toDQ.append(i)
        self.queue.pop(toDQ[0])
    
    def count(self):
        return len(self.queue)

    def clear(self):
        self.queue = []
