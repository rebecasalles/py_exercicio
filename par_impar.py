cont_par = 0
cont_impar = 0

for i in range(5):
    valor = int(input('Digite o valor: '))
    valor = valor % 2
    if valor > 0: 
       cont_impar += 1
    else:
        cont_par += 1

print('Total de valores pares: {}, Total de valores ímpares: {}'.format (cont_par, cont_impar))