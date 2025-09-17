n1 = int(input("Digite o 1° número: "))
n2 = int(input("Digite o 2° número: "))
n3 = int(input("Digite o 2° número: "))

if (n1 > n2) and (n1 > n3) and (n2 < n3): # 1° 2° 3°
    print(n1, n2, n3)
else:
    if (n2 > n1) and (n2 > n1) and (n1 < n3): #3° 2° 1°
        print(n3, n1, n2)
    else:
        print(n2, n3, n1) 
        