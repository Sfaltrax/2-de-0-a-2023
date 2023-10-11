x = 0
NumberOf2 = 0
for x in range(2024):
    print(x, end=" ")
    NumberOf2 += str(x).count("2")
    print(NumberOf2)
    x += 1
print(f'Le chiffre "2" apparaît {NumberOf2} fois dans les nombres de 0 à 2023')