"""
Crea una aplicación que permita al usuario ingresar una cadena de texto y luego muestre la cadena de texto invertida. Por ejemplo, si el usuario ingresa "hola", la aplicación debería mostrar "aloh".
"""
def invert_string (original_string):
    reversed_string = ""

    for i in range(len(original_string) - 1, -1, -1):
        reversed_string += original_string[i]
    return reversed_string

input_string = input("Enter some string and I will give it back to you but inverted: ")
print(invert_string(input_string))


