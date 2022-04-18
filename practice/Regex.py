import re

ejemplo1 = re.compile("[a-z]")
cadena1 = "ejemplo1"
print(f"""\tREGEX FUNCTIONS
RE: {ejemplo1}
string: {cadena1}
""")
"""match() determine if the RE matches at the 
beginning of the string"""
print("function match() :", ejemplo1.match(cadena1))
"""search() sacan through a string looking for any
location where the RE matches"""
print("function search() : ", ejemplo1.search(cadena1))
"""findall() find all substrings where the RE
matches, and returns them as a list"""
print("function findall() : ", ejemplo1.findall(cadena1))
"""finditer() find all substrings where the RE matches
and returns them as an iterator"""
example_iterator = ejemplo1.finditer(cadena1)
print("function finditer() : ", example_iterator)
print("iterator:")
for item in example_iterator:
    print(item)

ejemplo2 = re.compile("[a-z]+")
cadena2 = "esto,es.el{{ejemplo[2"
print(f"""\tEJEMPLO2
RE: {ejemplo2}
string: {cadena2}
""")
"""group() return the string matched by RE
start() return the starting position of the match
end() return the ending position of the match
span() return a tuple containing the (start, end) positions
of the match
"""
match_group = ejemplo2.match(cadena2)
print("group match: ", match_group.group())
print("start match: ", match_group.start())
print("end match: ", match_group.end())
print("span match: ", match_group.span())
print("function findall():", ejemplo2.findall(cadena2))
example_iterator2 = ejemplo2.finditer(cadena2)
print("function finditer() : ", example_iterator2)
print("iterator:")
for item in example_iterator2:
    print(item)