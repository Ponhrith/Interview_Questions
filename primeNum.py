firstNum = 1
secondNum = 100

for betNum in range (firstNum, secondNum+1):
    if betNum > 1:
        for primeNum in range (2, betNum):
            if betNum % primeNum == 0:
                break
        else:
            print(betNum)


       