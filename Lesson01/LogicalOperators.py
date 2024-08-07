# Operações Lógicas ( and, or, not ) = São usadas para checar se duas ou mais declarações condicionais são verdadeiras.

temp = int(input("Qual é a temperatura lá fora?: "))

if temp >= 0 and temp <= 30:
    print("A temperatura está agradável hoje!")
    print("Vá lá fora!")
elif temp < 0 or temp > 30:
    print("A temperatura não está tão agradável!")
    print("Fique dentro de casa!")
    
    
temp2 = int(input("Qual é a temperatura lá fora?: "))
# irá inverter os valores

if not(temp2 >= 0 and temp2 <= 30):
    print("A temperatura está agradável hoje!")
    print("Vá lá fora!")
elif not(temp2 < 0 or temp2 > 30):
    print("A temperatura não está tão agradável!")
    print("Fique dentro de casa!")