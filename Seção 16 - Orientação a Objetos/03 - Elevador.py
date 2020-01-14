class Elevador:
    def __init__(self, capacidade: int, total_andares: int):
        self.__capacidade = capacidade
        self.__total_andares = total_andares
        self.__andar_atual = 0
        self.__qtde_pessoas = 0

    def entra(self):
        if self.__qtde_pessoas < self.__capacidade:
            self.__qtde_pessoas += 1
        else:
            print(f'\033[0;31m ERRO! Elevador cheio.\033[m')

    def sai(self):
        if self.__qtde_pessoas != 0:
            self.__qtde_pessoas -= 1
        else:
            print(f'\033[0;31m ERRO! O elvador já se encontra vazio.\033[m')

    def sobe(self):
        if self.__andar_atual < self.__total_andares:
            self.__andar_atual += 1
        else:
            print(f'\033[0;31m ERRO! O elevador já encontra-se no último andar!\033[m')

    def desce(self):
        if self.__andar_atual >= 0:
            self.__andar_atual -= 1
        else:
            print(f'\033[0;31m ERRO! O elevador já está no térreo.')


elevador = Elevador(9, 13)
for c in range(10):
    elevador.entra()
print(elevador.__dict__)
