s = int(input('Digite o número que se deseja fazer a tabuada: '))
for n in range (0,11):
    t = n*s
    print(('{} x {} = {}'.format(s,n,t)))