# If  =  É um  bloco de código que irá executar apenas se a condição for verdadeira.

age = int(input("Quantos anos você tem?: "));

if age >= 18:
    print("Você é um adulto!");
elif age < 0:
    print("Você não nasceu ainda!");
else:
    print("Você é uma criança!");