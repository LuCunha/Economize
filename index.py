import math

class Pessoas:

    def __init__(self, nome, salario, opcao_de_poupanca, tempo_pagar):
        self._nome = nome
        self.salario = salario
        self.opcao_de_poupanca = opcao_de_poupanca
        self.tempo_pagar = tempo_pagar

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self.salario

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @salario.setter
    def salario(self, salario):
        self.salario = salario

class Produto(Pessoas):

    def __init__(self, nome, valor):
        super().__init__(nome)
        self.valor = valor

    @property
    def nome(self):
        return self.nome

    @nome.setter
    def nome(self, nome):
        self.nome = nome

    @property
    def valor(self):
        return self.valor

    @valor.setter
    def valor(self, valor_produto):
        self.valor = valor_produto

class Poupanca(Pessoas):

    def __init__(self, valor_a_guardar):
        self._valor_a_guardar = valor_a_guardar

    @property
    def valor_a_guardar(self):
        return self._valor_a_guardar

    @valor_a_guardar.setter
    def valor_a_guardar(self, valor_a_guardar):
        self._valor_a_guardar = valor_a_guardar


def pede_informacoes_pessoa(Pessoas):
    Pessoas._nome = input("Qual o seu nome?")
    Pessoas.salario = math.floor(float(input("Qual o seu salario?")))



def pede_informacoes_produto(Produto):
    Produto._nome = input("Qual o nome do produto que deseja comprar?")
    Produto.valor = math.floor(float(input("Qual o valor do produto que deseja comprar?")))

def tipo_pagamento(Pessoas, Produto, Poupanca):
    print("Você pretende guardar dinheiro como?")
    Pessoas.opcao_de_poupanca = input("1 - Mensalmente  2 - Semanalmente  3 - Anualmente")

    if(Pessoas.opcao_de_poupanca == '1'):
        Pessoas.tempo_pagar = math.floor(float(input("Em quantos meses quer compras o produto?")))
        Poupanca.valor_a_guardar = Produto.valor / Pessoas.tempo_pagar
        print("O valor que precisa guardar mensalmente é: " + str("{0:.2f}".format(Poupanca.valor_a_guardar)))

    elif(Pessoas.opcao_de_poupanca == '2'):
        Pessoas.tempo_pagar = math.floor(float(input("Em quantos semanas quer compras o produto?")))
        Poupanca.valor_a_guardar = Produto.valor / Pessoas.tempo_pagar
        print("O valor que precisa guardar semanalmente é: " + str("{0:.2f}".format(Poupanca.valor_a_guardar)))

    else:
        Pessoas.tempo_pagar = math.floor(float(input("Em quantos anos quer compras o produto?")))
        Poupanca.valor_a_guardar = Produto.valor / Pessoas.tempo_pagar
        print("O valor que precisa guardar anualmente é: " + str("{0:.2f}".format(Poupanca.valor_a_guardar)))





pede_informacoes_pessoa(Pessoas)
pede_informacoes_produto(Produto)
tipo_pagamento(Pessoas, Produto, Poupanca)






