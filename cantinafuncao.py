print("**** Bem vindo à cantina do SENAI ****")
print("**************CARDÁPIO****************")
print("| Código |    Descrição      | Valor |")
print("|  100   |   Cachorro-quente | 9,00  |")
print("|  101   |   Cachorro duplo  | 11,00 |")
print("|  102   |       X-egg       | 12,00 |")

cardapio = { "100":{"descricao":"Cachorro-quente",
                    "preco":9.00},
             "101":{"descricao":"Cachorro duplo",
                    "preco":11.00},
             "102":{"descricao":"X-egg",
                    "preco":12.00}
}

total = 0
listaDePedidos = []

def validarPedido():
    pedido = input("Digite o código do pedido: ")
    while pedido not in cardapio:
        print("Opção inválida!")
        pedido = input("Digite o código do pedido: ")
  

    print(f"Você pediu: {cardapio[pedido]['descricao']}")
    print(f"Preço: {cardapio[pedido]['preco']}")
    listaDePedidos.append(pedido)
    #return cardapio[pedido]["preco"]

#total +=  validarPedido()    
validarPedido()

resposta = input("Deseja pedir algo mais? (S/N)").lower()
while resposta == "s" or resposta == "sim":
    #total += validarPedido()
    validarPedido()
    resposta = input("Deseja pedir algo mais? (S/N)").lower()
    '''
    print("reree")
    if resposta == "n":
        print("9596")
        break
    else:
        print("opcao invalida!")
    '''
print("Seu pedido:")
for item in listaDePedidos:
    print(f"{cardapio[item]['descricao']} | {cardapio[item]['preco']}")
    total += cardapio[item]['preco']
print(f"Total do pedido: R${total:.2f}")
