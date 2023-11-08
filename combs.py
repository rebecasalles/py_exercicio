alc = float(input('Digite o valor do álcool: '))
gaso = float(input('Digite o valor da gasolina: '))

cal = alc/gaso
val = cal*100
val = round(val)

if (val<= 75):
    print('Compensa abastecer com o álcool, pois o valor é de ', val,)
else:
    print('Compensa abastecer com a gasolina, pois o valor é de ', val)