"""
Crea una aplicación que calcule la suma de los números primos en un rango dado por el usuario. Por ejemplo, si el usuario ingresa el rango de 1 a 10, la aplicación debería mostrar la suma de los números primos en ese rango (que sería 17).
"""

def is_prime(number):
    if number == 1: return False
    for i in range(2, number):
        if (number % i == 0):
            return False
    return True

def sum_of_primes(interval):
    total_sum = 0
    for i in range(interval[0], interval[1] + 1):
        if (is_prime(i)):
            total_sum += i
    return total_sum

input_interval = [int(input("Enter the beggining of the interval: ")), 0]
input_interval[1] = int(input("Enter the end of the interval: "))
print("the sum of the prime numbers in that closed interval is: ", sum_of_primes(input_interval))



