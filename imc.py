print('Vamos calcular seu IMC?')
nome = input('Digite o seu nome: ')
peso = float(input('Olá, {}, agora digite seu peso (em Kg, Ex: 68.9): ' .format(nome)))
altura = float(input('Digite sua altura (em m, Ex: 1.80): '))

media = peso / (altura * altura)
print('Seu IMC é: {:.1f}'.format(media))

