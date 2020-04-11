print("\nIs raining? algorithm(answer yes or no)")
key = input("Is raining?: ")
if key == "Yes" or key == "yes" or key == "YES":
    key = input("Have umbrella?: ")
    if key == "No" or key == "no" or key == "NO":
        print("Wait a while")
        key = input("Is raining?: ")
        while key == "Yes" or key == "yes" or key == "YES":
            print("Wait a while")
            key = input("Is raining?: ")
#no hay necesidad de colocar los respectivos else
#porque siempre conducen a la misma linea
print("Go outside")
