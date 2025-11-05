d = {}

texto = 'pedro cândido rodrigues da silva'


for i in texto:
    if i not in d:
        d[i] = texto.count(i)

print(d)