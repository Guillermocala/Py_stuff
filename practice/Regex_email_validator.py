import re
email_checker = re.compile(r"""
            (\w)+           # accepts any char
            [@]             # after an arroba
            (\w)+           # accepts another sufix
            [.]             # the . of 
            [a-zA-Z]{2,}$   # the end of the email(com, es, org, etc)  
            """, re.VERBOSE)
#shortest form
email_checker_short = re.compile(r"(\w)+[@](\w)+[.][a-zA-Z]{2,}")
correo = input("Ingrese su correo: ")
if email_checker_short.match(correo):
    print("Valido")
else:
    print("Invalido")