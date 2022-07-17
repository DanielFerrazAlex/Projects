print('----Validador de CPF (Apenas os números)----')

while True:

    cpf = input('Digite um CPF: ')
    novo_cpf = cpf[:-2]
    reverso = 10
    total = 0
    while len(cpf) != 11 or not cpf.isnumeric() or cpf == cpf[::-2]:
        print(f'Algo deu errado!')
        cpf = input('Digite seu CPF novamente: ')

    for i in range(19):
        if i > 8:
            i -= 9

        total += int(novo_cpf[i]) * reverso
        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0
            novo_cpf += str(d)

    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    if cpf == novo_cpf and not sequencia:
        print(f'O CPF: {cpf} é válido')
    else:
        print(f'O CPF: {cpf} é Inválido')
