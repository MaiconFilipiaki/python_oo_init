class Program:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def imprime(self):
        print(f'{self._nome} - {self.ano} -  {self._likes} likes')


class Filme(Program):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min -  {self._likes} likes'


class Serie(Program):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas -  {self._likes} likes'


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome.title()
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


vingadores = Filme("vingadores - guerra infinita", 2019, 149.0)
vingadores.dar_like()
tmep = Filme("todo mundo em panico ", 1999, 100)
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor = Serie("Demolidor", 2016, 3)
got = Serie("Games of Thrones", 2011, 8)
got.dar_like()
got.dar_like()
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes: {vingadores.likes}')
print(f'Nome: {got.nome} - Ano: {got.ano} - Temporadas: {got.temporadas} - Likes: {vingadores.likes}')

filmes_e_series = [vingadores, got, demolidor, tmep]

playlist_fim_de_semana = Playlist("fim de semana", filmes_e_series)

print(len(playlist_fim_de_semana))

for programa in playlist_fim_de_semana:
    print(programa)


print(demolidor in playlist_fim_de_semana)
