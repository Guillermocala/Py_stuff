# from leetcode
# incomplete, doesnt pass all testcase

"""
:type strs: List[str]
:rtype: str
"""
strs = ["flower", "flow", "flight"]
index = 1
prefix = ""
first = strs[0]
while index < len(strs):
    temp = ""
    for x, y in zip(first, strs[index]):
        if x == y:
            temp += x
    prefix = temp
    index += 1
print(prefix)