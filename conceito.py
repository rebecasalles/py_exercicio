nome = str(input('Digite seu nome: '))
n1 = float(input('Insira sua nota do primeiro bimestre (em número): '))
n2 = float(input('Insira sua nota do segundo bimestre (em número): '))
n3 = float(input('Insira sua nota do terceiro bimestre (em número): '))
n4 = float(input('Insira sua nota do quarto bimestre (em núemero): '))

media = (n1+n2+n3+n4)/4

if media<=59.9:
    print('Olá',nome,',sua nota final é ',media,'e seu conceito é C')
elif media<=79.9:
    print('Olá',nome,',sua nota final é ',media,'e seu conceito é B')
elif media<=80:
    print('Olá',nome,',sua nota final é ',media, 'e seu conceito é A')
