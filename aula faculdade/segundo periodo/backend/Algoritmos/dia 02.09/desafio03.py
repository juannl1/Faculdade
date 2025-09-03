p = True
q = False

condicao1 = not(p and q)
condicao2 = (not p) or (not q)

print(f"not (p and q) <=> (not p ) or (not q): ", condicao1 == condicao2)


