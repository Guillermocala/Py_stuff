import re
print("ingrese caracteres y se comprobara si hay alguna letra")
numero = input("ingrese: ")
if re.search('[a-z]', numero.lower()) == None:
    print("no se encontro letras")
else:
    print("hay letras")