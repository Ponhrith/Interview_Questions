firstNum = 1
secondNum = 100
amount = 0

for betNum in range (firstNum, secondNum+1):
    if betNum > 1:
        for primeNum in range (2, betNum):
            if betNum % primeNum == 0:
                break
        else:
            print(betNum)
            amount = amount + 1
print("The amount of prime number is:", amount)


# amount = 0
#  for num in range (100, 200):
#      if all(num%i !=0 for i in range (2,num)):
#          print(num)
        #  amount = amount + 1
# print(amount)