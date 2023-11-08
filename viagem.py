dist = float(input('Insira a distância em km: '))
cons = float(input('Insira o consumo do seu carro: '))
combs = float(input('Insira o valor do combustível: '))

quant = dist/cons
val = quant*combs
tot = val*2
tot = round(tot) 

print('O valor total gasto vai ser: ', tot )