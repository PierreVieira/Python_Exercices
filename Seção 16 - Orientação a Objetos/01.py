from typing import Any


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


pessoa = Pessoa('Pierre', 19, 1.83)
pessoa.idade += 1
pessoa.ver_dados()
