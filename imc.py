nome = str(input('Digite o seu nome: '))
idade = int(input('Digite a sua idade: '))
peso = float(input('Digite o seu peso: '))
alt = float(input('Digite a sua altura: '))

imc = peso/(alt**2)
imc = round(imc)

if imc<18.5:
    print('O seu nome é',nome,',sua idade é',idade,',seu peso é',peso,',o seu imc tem valor',imc,'e está abaixo do peso')
elif imc<=24.9:
    print('O seu nome é ', nome, 'sua idade é ', idade, 'seu peso é ', peso, 'e o seu imc tem valor', imc, 'e está no seu peso ideal')
elif imc<=29.9:
    print('O seu nome é',nome,'sua idade é',idade,'seu peso é',peso,'e o seu imc tem valor',imc,'e está levemente acima do peso')
elif imc<=34.9: 
    print('O seu nome é ', nome, 'sua idade é ', idade, 'seu peso é ', peso, 'e o seu imc tem valor', imc, 'e está em obesidade grau 1')
elif imc<=39.9:
    print('O seu nome é ', nome, 'sua idade é ', idade, 'seu peso é ', peso, 'e o seu imc tem valor', imc, 'e está em obesidade severa')
elif imc<40:
     print('O seu nome é ', nome, 'sua idade é ', idade, 'seu peso é ', peso, 'e o seu imc tem valor', imc, 'e está em obesidade mórbida ')
