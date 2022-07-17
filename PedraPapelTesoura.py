import random

print('--------------Pedra | Papel | Tesoura----------------')
print('Escreva pedra, Papel ou tesoura')
jogador = input('Qual irá escolher?\n')

computador = random.choice(['Pedra', 'Papel', 'Tesoura'])


if jogador == 'Pedra' and computador == 'Tesoura':
    print(f'Você escolheu {jogador} e seu oponente escolheu {computador}. Parabens você venceu.')
    
elif jogador == 'Pedra' and computador == 'Pedra':
    print(f'Você escolheu {jogador} e seu oponente escolheu {computador}. Empatou.')
    
elif jogador == 'Pedra' and computador == 'Papel':
    print(f'Você escolheu {jogador} e seu oponente escolheu {computador}. Você perdeu.')
    
elif jogador == 'Papel' and computador == 'Pedra':
    print(f'Você escolheu {jogador} e seu oponente escolheu {computador}. Parabens você venceu.')
    
elif jogador == 'Papel' and computador == 'Tesoura':
    print(f'Você escolheu {jogador} e seu oponente escolheu {computador}. Você perdeu.')
    
elif jogador == 'Papel' and computador == 'Papel':
    print(f'Você escolheu {jogador} e seu oponente escolheu {computador}. Empatou.')

elif jogador == 'Tesoura' and computador == 'Papel':
    print(f'Você escolheu {jogador} e seu oponente escolheu {computador}. Parabens você venceu.')
    
elif jogador == 'Tesoura' and computador == 'Pedra':
    print(f'Você escolheu {jogador} e seu oponente escolheu {computador}. Você perdeu.')
    
elif jogador == 'Tesoura' and computador == 'Tesoura':
    print(f'Você escolheu {jogador} e seu oponente escolheu {computador}. Empatou.')
    