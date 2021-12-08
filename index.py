import math

class Pessoas:

    def __init__(self, nome, salario, opcao_de_poupanca, tempo_pagar):
        self.nome = nome
        self.salario = salario
        self.opcao_de_poupanca = opcao_de_poupanca
        self.tempo_pagar = tempo_pagar
        self.informacoes_pessoa = []

    def add_informacoes_pessoa(self, informacoes_pessoa):
        self.informacoes_pessoa.append(informacoes_pessoa)

class Produto():

    def __init__(self, nome_produto, valor):
        self.nome_produto = nome_produto
        self.valor = valor
        self.informacoes_produto = []

    def add_informacoes_produto(self, informacoes_produto):
        self.informacoes_produto.append(informacoes_produto)


class Poupanca():

    def __init__(self, valor_a_guardar, ):
        self.valor_a_guardar = valor_a_guardar
        self.informacoes_poupanca = []

    def add_informacoes_poupanca(self, informacoes_poupanca):
        self.informacoes_poupanca.append(informacoes_poupanca)

class Informacoes():

    def __init__(self):
        self.lista_informacoes = []

    def add_lista_informacoes(self, lista_informacoes):
        self.lista_informacoes.append(lista_informacoes)


def pede_informacoes_pessoa(add_informacoes_pessoa:Pessoas) -> Pessoas:
    nome = input("Qual o seu nome?")
    salario = math.floor(float(input("Qual o seu salario?")))
    print("Você pretende guardar dinheiro como?")
    opcao_de_poupanca = input("1 - Mensalmente  2 - Semanalmente  3 - Anualmente  ")
    tempo_pagar = math.floor(float(input("Em quantos meses quer compras o produto?")))
    add_informacoes_pessoa(nome, salario, opcao_de_poupanca, tempo_pagar)
    #return Pessoas(nome=nome, salario=salario, opcao_de_poupanca=opcao_de_poupanca, tempo_pagar=tempo_pagar)



def pede_informacoes_produto(add_informacoes_produto:Produto) -> Produto:
    nome_produto = input("Qual o nome do produto que deseja comprar?")
    valor = math.floor(float(input("Qual o valor do produto que deseja comprar?")))
    add_informacoes_produto(nome_produto, valor)
    #return Produto(nome_produto=nome_produto, valor=valor)


def tipo_pagamento(informacoes_pessoa:Pessoas, informacoes_produto:Produto):

        if informacoes_pessoa.opcao_de_poupanca == "1":
            poupanca = Poupanca(valor_a_guardar = informacoes_produto.valor / informacoes_pessoa.tempo_pagar)
            print("O valor que precisa guardar mensalmente é: " + str("{0:.2f}".format(poupanca.valor_a_guardar)))


        elif informacoes_pessoa.opcao_de_poupanca == "2":
            poupanca = Poupanca(valor_a_guardar = informacoes_produto.valor / informacoes_pessoa.tempo_pagar)
            print("O valor que precisa guardar semanalmente é: " + str("{0:.2f}".format(poupanca.valor_a_guardar)))


        elif informacoes_pessoa.opcao_de_poupanca == "3":
            poupanca = Poupanca(valor_a_guardar = informacoes_produto.valor / informacoes_pessoa.tempo_pagar)
            print("O valor que precisa guardar anualmente é: " + str("{0:.2f}".format(poupanca.valor_a_guardar)))


        else:
            print("Está não é opção válida!")


#def junta_informacoes(add_lista_informacoes:Informacoes,informacoes_pessoa:Pessoas,informacoes_produto:Produto,informacoes_poupanca:Poupanca):
    #add_lista_informacoes.append[informacoes_pessoa, informacoes_produto, informacoes_poupanca]

pede_informacoes_pessoa(add_informacoes_pessoa = Pessoas)
pede_informacoes_produto(add_informacoes_produto = Produto)
tipo_pagamento(informacoes_pessoa=Pessoas, informacoes_produto=Produto)






