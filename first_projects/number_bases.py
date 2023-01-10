"""
Crea una aplicación que convierta números a diferentes bases numéricas. La aplicación debería permitir al usuario ingresar un número y luego elegir a qué base numérica quiere convertirlo (binario, octal, decimal o hexadecimal).
"""

def create_base(input_base):
    number_bases = {
    "binary": 2,
    "octal": 8,
    "hexadecimal": 16,
    }
    base = {
        "number": "", 
        "symbols": []
    }

    try: 
        base["number"] = number_bases[input_base]
    except KeyError:
        base["number"] = int(input_base)

    for i in range (0, base["number"]):
        if (i <= 9):
            base["symbols"].append(str(i))
        else:
            base["symbols"].append(chr(i + 55))
    
    return base
    
def convert_base (input_number: int, chosen_base: str, sumatory: str = ""):
 
    base = create_base(chosen_base)
    
    if(input_number < base["number"]):
        sumatory += base["symbols"][input_number]
    else:
        quotient = input_number // base["number"]
        sumatory += convert_base(quotient, chosen_base, sumatory) + base["symbols"][input_number % base["number"]]
    return sumatory

user_number = 0
user_base = ""
        
while True:
    user_number = input("Please enter the number: ")

    try:
        user_number = int(user_number)
        break
    except ValueError:
        print("Please enter a valid integer")

while True:
    user_base = input("Now, enter the base you want to convert the number to: (e.g.: any number up to 36, 'binary', 'octal' or 'hexadecimal'): ").lower()

    if(user_base == "binary" or user_base == "octal" or user_base == "hexadecimal" or int(user_base) <= 36):
        break
    else:
        print("Please, enter a valid base: ")

print("The number", user_number, "converted to the","base:", user_base, "is equal to:", convert_base(user_number, user_base))

