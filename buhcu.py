"""
Imprime los números del 1 al 100, pero con las siguientes condiciones:
Para los múltiplos de 3, imprime "Fizz".
Para los múltiplos de 5, imprime "Buzz".
Para los múltiplos de tanto 3 como 5, imprime "FizzBuzz".
Si el número no es múltiplo de 3 ni de 5, imprime el número tal como es
"""

for i in range(1,100+1):
    if i % 3 != 0 and i % 5 != 0: 
        print(i)
    elif i % 3 == 0 and i % 5 == 0: 
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print("Fizz")
