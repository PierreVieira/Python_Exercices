class Televisao:
    def __init__(self):
        self._volume = 20
        self._canal_atual = 1

    @property
    def volume(self):
        return self._volume

    @property
    def canal_atual(self):
        return self._canal_atual

    @volume.setter
    def volume(self, value):
        self._volume = value

    @canal_atual.setter
    def canal_atual(self, value):
        self._canal_atual = value


class ControleRemoto:
    def __init__(self, tv: Televisao):
        self._tv = tv

    def aumentar_volume(self):
        if self._tv.volume < 100:
            self._tv.volume += 1

    def diminuir_volume(self):
        if self._tv.volume > 0:
            self._tv.volume -= 1

    def mudar_canal(self, canal: int):
        if canal > 0:
            self._tv.canal_atual = canal

    def aumentar_canal(self):
        if self._tv.canal_atual < 100:
            self._tv.canal_atual += 1

    def diminuir_canal(self):
        if self._tv.canal_atual > 1:
            self._tv.canal_atual -= 1


tv = Televisao()
controle_remoto = ControleRemoto(tv)
print(tv.__dict__)
for c in range(15):
    controle_remoto.aumentar_volume()
print(tv.__dict__)
