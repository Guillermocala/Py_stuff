# Guillermo Cala
# from leetcode

# DESCRIPTION: Write a function to find the longest common prefix 
# string amongst an array of strings.
# If there is no common prefix, return an empty string "".

"""
:type strs: List[str]
:rtype: str
"""
#strs = ["flower", "flow", "flight"]
strs = ["aaa","aa","aaa"]

def longestCommonPrefix(strs):
    index = 1
    prefix = []
    first = strs[0]
    if len(strs) == 1 and len(first) <= 1:
        return first
    else:
        while index < len(strs):
            temp = ""
            equal = True
            for x, y in zip(first, strs[index]):
                if x == y and equal:
                    temp += x
                else:
                    equal = False
            print("temp: ", temp)
            prefix.append(temp)
            index += 1
    return min(prefix, key=len)

print(longestCommonPrefix(strs))
