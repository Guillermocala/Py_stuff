# Guillermo Cala
# from leetcode

# Given a string s containing just the characters '(', ')', 
# '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the 
# same type.

# ======================incomplete=====================
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    if len(s) % 2 == 1:
        return False
    else:
        index = 0
        while index < len(s):
            if s[index] == "(":
                if s[index + 1] == ")":
                    index += 1
                else:
                    return False
            elif s[index] == "{":
                if s[index + 1] == "}":
                    index += 1
                else:
                    return False
            elif s[index] == "[":
                if s[index + 1] == "]":
                    index += 1
                else:
                    return False
            else:
                return False
            index += 1
        return True

s = "())"
print(isValid(s))