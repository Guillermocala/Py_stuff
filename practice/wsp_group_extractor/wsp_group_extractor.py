# Guillermo Cala 21/01/2023

# este script esta hecho con la finalidad de extraer
# los numeros de un grupo determinado de whatsapp
# y colocarlos en un archivo excel .xlsx
# el script se alimenta de un .txt que recibe un outerHTML
# de los integrantes del grupo

from openpyxl import Workbook

print("\t\tEXTRACTOR DE CONTACTOS...")

with open('data.txt') as data:
    lista = data.readlines()

outer_html = ''.join(map(str, lista))

answer_string = outer_html[(outer_html.find(">") + 1):-8]

numbers_list = answer_string.split(",")

new_excel = Workbook()

ws = new_excel.active

for i in range(len(numbers_list)):
    cellRef = ws.cell(row=(i+1), column=1)
    cellRef.value = numbers_list[i]

# This operation will overwrite existing files without warning.
new_excel.save('numbers_list.xlsx')

print("\nExcel creado exitosamente con", len(numbers_list), "contactos")