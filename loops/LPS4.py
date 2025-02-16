#Escriba un programa que pida dos números enteros y escriba qué números son pares y cuáles impares desde el primero hasta el segundo.

primnum = int(input("Introduce el primer numero: "))
segnum = int(input(f"Introduce un segundo numero mayor que {primnum}: "))

if primnum >= segnum:
    print(f"he dicho que mayor a {primnum} >:(")
for i in range(primnum,segnum+1):
    tipo = "par" if i % 2 == 0 else "impar"
    print(f"{i} es {tipo}")