class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    def dar_like(self):
        self.likes += 1

    @property
    def likes(self):
        return self.likes

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    def dar_like(self):
        self.likes += 1

    @property
    def likes(self):
        return self.likes

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()

vingadores = Filme("maicon", 2011, 1.38)
print(vingadores.nome)