print("\n\nSquare plotter")
x = int(input("input the rows: "))
y = int(input("input the columns: "))
answer = ""
cont1 = 0
cont2 = 0
while cont1 < x:
    while cont2 < y:
        answer += "*"
        cont2 += 1
    answer += "\n"
    cont2 = 0
    cont1 += 1
print(answer)
