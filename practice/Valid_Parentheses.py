# Guillermo Cala
# from leetcode

# Given a string s containing just the characters '(', ')', 
# '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the 
# same type.

# Theory: https://fjmduran.com/blog/algoritmia-stack-parentesis 
# El algoritmo usando una pila sería:
# 1- Vamos recorriendo el string
# 2- Comprobamos si el carácter en el que nos encontramos es de 
#    cierre o de apertura.
# 3- Si es un carácter de apertura guardamos su carácter de 
#    cierre en la pila.
# 4- Si es un carácter de cierre lo comparamos con el último 
#    valor de la pila.
# 5- Si son iguales, continuo, si son diferente el string dado 
#    no es válido.
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    if len(s) % 2 == 1:
        return False
    else:
        op_apertura = "({["
        op_cierre = ")}]"
        apertura = 0
        cierre = 0
        index = 0
        stack = []
        while index < len(s):
            if s[index] in op_apertura:
                apertura += 1
                if s[index] == "(":
                    stack.append(")")
                elif s[index] == "{":
                    stack.append("}")
                elif s[index] == "[":
                    stack.append("]")
                else:
                    return False
            elif s[index] in op_cierre:
                cierre += 1
                # si la pila esta vacia pues falso porque estamos
                # en operador de cierre
                if not stack or s[index] != stack.pop():
                    return False
            else:
                return False
            index += 1
        return True if apertura == cierre else False

s = "(){}}{"
print(isValid(s))