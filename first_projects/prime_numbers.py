"""
Have the program find prime numbers until the user chooses to stop asking for the next one.
"""


import os
os.system("cls")

def nextPrimeNumber (somePrimeNumber = 1): 
    nextPrimeNumber = somePrimeNumber + 1
    
    for i in range(2, nextPrimeNumber):
        if(nextPrimeNumber % i == 0):
            nextPrimeNumber += 1
    return nextPrimeNumber    

lastPrimeNumber = 1
while (not input("Press ENTER and I will print the next prime number, press any other key to stop: ")):
    lastPrimeNumber = nextPrimeNumber(lastPrimeNumber)
    print("The next prime number is:", lastPrimeNumber)
else:
    pass