a = float(input("Digite o 1° número: "))
b = float(input("Digite o 2° número: "))
c = float(input("Digite o 2° número: "))

if a > b and b > c:
    print(a,b,c)

elif a > c and c > b:
    print(a,c,b)
elif b>a and a>c:
    print(b,a,c)
elif b>c and c>a:
    print(b,c,a)
elif c>a and a>b:
    print(c,a,b)
else:
    print(c,b,a)
