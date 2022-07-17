class elevador:
    def __init__(self):
        self.__qtd_andares = None
        self.__andar_atual = None
        self.__qtd_pessoas = None
        self.__capacidade = None

        @property
        def qtd_andares(self):
            return self.__qtd_andares

        @property
        def andar_atual(self):
            return self.__andar_atual

        @property
        def qtd_pessoas(self):
            return self.__qtd_pessoas
       
        @property
        def capacidade(self):
            return self.__capacidade

        @qtd_andares.setter
        def qtd_andares(self, qtd_andares):
            self.__qtd_andares = qtd_andares

        @andar_atual.setter
        def andar_atual(self, andar_atual):
            self.__andar_atual = andar_atual
           

        @qtd_pessoas.setter
        def qtd_pessoas(self, qtd_pessoas):
            self.__qtd_pessoas = qtd_pessoas

        @capacidade.setter
        def capacidade(self, capacidade):
            self.__capacidade = capacidade
       
        def subir(self):
            if self.__andar_atual + 1 <= self.__qtd_andares:
                self.__andar_atual += 1
                print(f'Subindo... Andar atual {self.__andar_atual}')
            else:
                print('Já estamos no ultimo andar')

        def descer(self):
            if self.__andar_atual - 1 > 0:
                self.__andar_atual -= 1
                print(f'Descendo... Andar atual {self.__andar_atual}')
            else:
                print('Já estamos no térreo')

        def entrar(self, qtd):
            if self.__qtd_pessoas + qtd <= self.__capacidade:
                self.__qtd_pessoas += qtd
                print(f'Quantidade de pessoas no elevador: {self.__qtd_pessoas}')
            else:
                print('Capacidade esgotada')

        def sair(self, qtd):
            if self.__qtd_pessoas - qtd >= 0:
                self.__qtd_pessoas -= qtd
                print(f'Quantidade de pessoas no elevador: {self.__qtd_pessoas}')
            else:
                print('Não a pessoas o suficiente para remover')
