n = int(input('Fatorial de: '))

cont = 0
f = 1
for cont in range (1, n+1):
    f = f * cont
    cont = cont + 1

print(f)
