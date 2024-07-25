x = 1    # int
y = 2.0  # flot
z = "3"  # str

x = str(x)
y = int(y)  # Isso fará que a variável y se torne um int permanente
z = float(z)

 
print(x)
print(y)
print(z*3)


# Não é possível concatenar string com int, para isso acontecer devesse seguir esse modelo
print("X is "+str(x))
print("Y is "+str(y))
