import math

class Pessoas:

    def __init__(self, nome, salario, opcao_de_poupanca, tempo_pagar):
        self.nome = nome
        self.salario = salario
        self.opcao_de_poupanca = opcao_de_poupanca
        self.tempo_pagar = tempo_pagar
        self.pessoa = []
        self.produto = []
        self.poupanca = []
        self.dados = []

    def add_pessoa(self, pessoa):
        self.pessoa.append({pessoa})

    def add_produto(self, produto):
        self.produto.append(produto)

    def add_poupanca(self, poupanca):
        self.poupanca.append(poupanca)

    def add_dados(self, dados):
        self.dados.append(dados)

class Produto():

    def __init__(self, nome_produto, valor):
        self.nome_produto = nome_produto
        self.valor = valor


class Poupanca():

    def __init__(self, valor_a_guardar, ):
        self.valor_a_guardar = valor_a_guardar


def pede_informacoes_pessoa(add_pessoa:Pessoas) -> Pessoas:
    nome = input("Qual o seu nome?")
    salario = math.floor(float(input("Qual o seu salario?")))
    print("Você pretende guardar dinheiro como?")
    opcao_de_poupanca = input("1 - Mensalmente  2 - Semanalmente  3 - Anualmente  ")
    tempo_pagar = math.floor(float(input("Em quantos meses quer compras o produto?")))
    add_pessoa({'nome' : nome, 'salario' : salario, 'opcao_de_poupanca' : opcao_de_poupanca, 'tempo_pagar' : tempo_pagar})
    #return Pessoas(nome=nome, salario=salario, opcao_de_poupanca=opcao_de_poupanca, tempo_pagar=tempo_pagar)



def pede_informacoes_produto(add_produto:Produto) -> Produto:
    nome_produto = input("Qual o nome do produto que deseja comprar?")
    valor = math.floor(float(input("Qual o valor do produto que deseja comprar?")))
    add_produto(nome_produto, valor)
    #return Produto(nome_produto=nome_produto, valor=valor)


def tipo_pagamento(pessoa:Pessoas, produto:Produto):

    for opcao in pessoa:
        if  opcao == "1":
            poupanca = Poupanca(valor_a_guardar = produto.valor / pessoa.tempo_pagar)
            print("O valor que precisa guardar mensalmente é: " + str("{0:.2f}".format(poupanca.valor_a_guardar)))


        elif pessoa.opcao_de_poupanca == "2":
            poupanca = Poupanca(valor_a_guardar = produto.valor / pessoa.tempo_pagar)
            print("O valor que precisa guardar semanalmente é: " + str("{0:.2f}".format(poupanca.valor_a_guardar)))


        elif pessoa.opcao_de_poupanca == "3":
            poupanca = Poupanca(valor_a_guardar = produto.valor / pessoa.tempo_pagar)
            print("O valor que precisa guardar anualmente é: " + str("{0:.2f}".format(poupanca.valor_a_guardar)))


        else:
            print("Está não é opção válida!")


#def junta_informacoes(pessoa:Pessoas,produto:Pessoas,poupanca:Pessoas):
    #add_dados[pessoa, produto, poupanca]

pede_informacoes_pessoa(add_pessoa = Pessoas)
pede_informacoes_produto(add_produto = Produto)
tipo_pagamento(pessoa=Pessoas, produto=Pessoas)






