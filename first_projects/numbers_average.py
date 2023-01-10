"""
Crea una aplicación que calcule el promedio de los números en una lista dada por el usuario. La aplicación debería permitir al usuario ingresar los números de la lista uno por uno y luego mostrar el promedio de todos los números ingresados.
"""

import os
os.system("cls")

from statistics import mean

user_numbers = []
restart = False

while True:
    number = input("Enter a number to calculate the average, or enter 'done' to finish: ")
    if (number == "done"):
        break
    elif ('& C:/Users/quiba/AppData/Local/Programs/Python/Python311/python.exe "c:/Users/quiba/Documents/Machine Learning/Python/Projects/first_projects/numbers_average.py"' in number):
        restart = True;
        break

    try:
        user_numbers.append(int(number))
    except ValueError:
        print("Please enter a valid integer")   
    

if (len(user_numbers) > 0 and restart == False):
    print("The average of the numbers you entered is: ", mean(user_numbers))
elif (restart):
    exec(open("./numbers_average.py").read())
else:
    print("You didn't enter any number")