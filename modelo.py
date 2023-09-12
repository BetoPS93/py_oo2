from sympy import re


class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0 

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

vingadores = Filme("vingadores - guerra infinita", 2018, 160)
print(
    f"{vingadores.nome} é um filme lançado em {vingadores.ano} tem duração de {vingadores.duracao} e recebeu {vingadores.likes} likes."
)

atlanta = Serie("atlanta", 2018, 2)
atlanta.dar_like()
atlanta.dar_like()
print(
    f"A série {atlanta.nome} estreiou em {atlanta.ano} e tem {atlanta.temporadas} temporadas e recebeu {atlanta.likes} likes."
)
