class Pessoa:
    def __init__(self, nome: str, idade: int, altura: float):
        self._nome = nome
        self._idade = idade
        self._altura = altura

    def ver_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Altura: {self.altura}')

    # Getters
    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @property
    def altura(self):
        return self._altura

    # Setters
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @idade.setter
    def idade(self, idade):
        self._idade = idade

    @altura.setter
    def altura(self, altura):
        self._altura = altura


class Agenda:
    def __init__(self, pessoas: list):
        self._pessoas = pessoas

    def armazena_pessoa(self, nome: str, idade: int, altura: float):
        """Armazena uma pessoa com as informações na agenda"""
        pessoa = Pessoa(nome, idade, altura)
        self._pessoas.append(pessoa)

    def remove_pessoa(self, nome):
        """Remove as pessoas com o nome informado da agenda"""
        for pessoa in self._pessoas:
            if pessoa.nome == nome:
                self._pessoas.remove(pessoa)
                break

    def busca_pessoa(self, nome):
        """Informe a posição da agenda em que a pessoa com o nome informado se encontra"""
        for i in range(len(self._pessoas)):
            if self._pessoas[i].nome == nome:
                return i
        return None  # O nome informado não existe

    def _dados_pessoa(self, pessoa):
        print(f'Nome: {pessoa.nome}')
        print(f'Idade: {pessoa.idade}')
        print(f'Altura: {pessoa.altura}')

    def imprime_agenda(self):
        """Imprime os dados de todas as pessoas da agenda"""
        print('\033[1;31m ======== AGENDA ========\033[m')
        for pessoa in self._pessoas:
            self._dados_pessoa(pessoa)
            print('-----------------------------------')
        print('\033[1;31m ========================\033[m')

    def imprime_pessoa(self, index: int):
        self._dados_pessoa(self._pessoas[index])


lista_pessoas = []
while True:
    nome = input(f'Informe o nome: ')
    idade = int(input(f'Informe a idade de {nome}: '))
    peso = float(input(f'Informe o peso de {nome}: '))
    while True:
        resposta = input('Deseja continuar [s/n]? ').upper()
        if resposta == 'S' or resposta == 'N':
            break
    if resposta == 'N':
        break
    lista_pessoas.append(Pessoa(nome, idade, peso))
agenda = Agenda(lista_pessoas)
agenda.imprime_agenda()
agenda.remove_pessoa('Alex')
agenda.imprime_agenda()
agenda.armazena_pessoa('Alex', 23, 58.1)
agenda.imprime_agenda()
print(agenda.busca_pessoa('Pierre'))
