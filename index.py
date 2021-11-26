import math

class Pessoas:

    def __init__(self, nome, salario, opcao_de_poupanca, tempo_pagar):
        self._nome = nome
        self.salario = salario
        self.opcao_de_poupanca = opcao_de_poupanca
        self.tempo_pagar = tempo_pagar


class Produto():

    def __init__(self, nome_produto, valor):
        self.nome_produto = nome_produto
        self.valor = valor


class Poupanca():

    def __init__(self, valor_a_guardar):
        self.valor_a_guardar = valor_a_guardar


def pede_informacoes_pessoa() -> Pessoas:
    nome = input("Qual o seu nome?")
    salario = math.floor(float(input("Qual o seu salario?")))
    print("Você pretende guardar dinheiro como?")
    opcao_de_poupanca = input("1 - Mensalmente  2 - Semanalmente  3 - Anualmente  ")
    tempo_pagar = math.floor(float(input("Em quantos meses quer compras o produto?")))
    return Pessoas(nome=nome, salario=salario, opcao_de_poupanca=opcao_de_poupanca, tempo_pagar=tempo_pagar)


def pede_informacoes_produto() -> Produto:
    nome_produto = input("Qual o nome do produto que deseja comprar?")
    valor = math.floor(float(input("Qual o valor do produto que deseja comprar?")))
    return Produto(nome_produto=nome_produto, valor=valor)

def tipo_pagamento(pessoa:Pessoas,produto:Produto):

    if pessoa.opcao_de_poupanca == "1":
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

pessoa1 = pede_informacoes_pessoa()
produto1 = pede_informacoes_produto()
tipo_pagamento(pessoa=pessoa1, produto=produto1)






