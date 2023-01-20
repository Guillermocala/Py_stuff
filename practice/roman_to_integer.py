# ROMAN TO INTEGER 
# problem from leetcode
symbols = {
    "I":1, "V":5, "X":10, "L":50,
    "C":100, "D":500, "M":1000
}
# PUT THE ROMAN NUMBER HERE DOWN =================
s = "MCMXCIV"
i = 0
sum = 0
while i < len(s):
    print("iteracion: ", s[i])
    if i != len(s) - 1:
        if s[i] == "I" and (s[i + 1] == "V" or s[i + 1] == "X"):
            if s[i + 1] == "V":
                sum += 4
            elif s[i + 1] == "X":
                sum += 9
            i += 1
        elif s[i] == "X" and (s[i + 1] == "L" or s[i + 1] == "C"):
            if s[i + 1] == "L":
                sum += 40
            elif s[i + 1] == "C":
                sum += 90
            i += 1
        elif s[i] == "C" and (s[i + 1] == "D" or s[i + 1] == "M"):
            if s[i + 1] == "D":
                sum += 400
            elif s[i + 1] == "M":
                sum += 900
            i += 1
        else:
            sum += symbols[s[i]]
    else:
        sum += symbols[s[i]]
    i += 1
print(sum)