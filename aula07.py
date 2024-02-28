import random
import time
print('Bem vindo ao CASSINO.')
time.sleep(1)
print('Para jogar, basta escolher um número de 0 a 10.')
time.sleep(2.5)
print('Cada jogador terá 3 chances para acertar um número aleatório.')
time.sleep(2.5)
nome1 = input('Digite o nome do Jogador 1: ')
nome2 = input('Digite o nome do Jogador 2: ')
n1 = [3,2,1]
roleta = random.randint(1, 10)
#print(roleta)
for c1 in n1:
    c1 = c1 - 1
    time.sleep(2)
    tentativa = int(input('Vez de {}. Digite seu número: '.format(nome1)))
    if tentativa == roleta:
        print('Parabéns {}, você ganhou!'.format(nome1))
        break
    elif  tentativa != roleta:
        print('Você errou. Você tem mais {} chance(s).'.format(c1))
    if c1 == 0:
        print('Suas chances acabaram {}. Você perdeu'.format(nome1))
        time.sleep(2)
    tentativa2 = int(input('Vez de {}. Digite seu número: '.format(nome2)))
    if tentativa2 == roleta:
        print('Parabéns {}, você ganhou!'.format(nome2))
        break
    elif tentativa != roleta:
        print('Você errou. Você tem mais {} chance(s).'.format(c1))
    if c1 == 0:
        print('Suas chances acabaram {}. Você perdeu'.format(nome2))
        print('O real número escolhido foi {}'.format(roleta))
