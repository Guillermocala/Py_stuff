import re
"""backslashes are not handled in any special way in a
string literal prefixed with 'r'
"""
regex1 = re.compile(r"\d+")
cadena1 = "12 drummers drumming, 11 pipers piping, 10 lords a-leaping"

print(regex1.findall(cadena1))

regex2 = re.compile(r"\w+")
cadena2 = input("Ingrese una cadena: ")
match_object = regex2.match(cadena2)
if match_object:
    print("Match found: ", match_object.group())
else:
    print("No match")