class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()
    
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes}.'



class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} - {self._likes}.'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} - {self._likes}.'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self.programas = programas

    def tamanho(self):
        return len(self.programas)

vingadores = Filme("vingadores - guerra infinita", 2018, 160)

tmp = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Filme('demolidor', 2016, 2)
atlanta = Serie("atlanta", 2018, 2)

tmp.dar_like()
vingadores.dar_like()
demolidor.dar_like()
tmp.dar_like()
demolidor.dar_like()
vingadores.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmp]

playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

for programa in playlist_fim_de_semana.programas:
    print(programa)

print('Fim do Código')