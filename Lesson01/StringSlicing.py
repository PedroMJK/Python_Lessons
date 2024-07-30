# Slicing = Para criar uma sub-string baseado em uma porção fatiada do nome completo
#           indexing[] ou slice();
#           [start:stop:step];


name = "Pedro Monteiro"

fisrt_name = name[0:5];
last_name = name[6:15];
funky_name = name[0:15:2];  # Contará os caracteres de 2 em 2

# Caso o start e o stop seja deixados vazios, python entenderá os ponto de partida e parada como 0.
funky_name_02 = name[::3];  # Contará os caracteres de 3 em 3.

# Para inverter a sring, numa contagem reversa
reversed_name = name[::-1];

print(fisrt_name);
print(last_name);
print(funky_name);
print(funky_name_02);
print(reversed_name);

### Usando slice().

