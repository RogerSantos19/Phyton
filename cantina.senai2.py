print("**** Bem vindo à cantina do SENAI ****")
print("**************CARDÁPIO****************")
print("| Código |    Descrição      | Valor |")
print("|  100   |   Cachorro-quente | 9,00  |")
print("|  101   |   Cachorro duplo  | 11,00 |")
print("|  102   |       X-egg       | 12,00 |")

total = 0
cachorroQuente = 9.00
cachorroDuplo = 11.00
xEgg = 12.00
while True:
    pedido = input("Digite um código de produto: ")
    if pedido == "100":
        total = total + cachorroQuente
    elif pedido == "101":
        total = total + cachorroDuplo
    elif pedido == "102":
        total = total + xEgg
    else:
        print("Código inválido!")
        continue
    print(f"voce pediu, {pedido}total a pagar: R${total:.2f}")
    print(f"subtotal da compra: R$ {total:.2f}")
    resposta = ""
    while resposta != "S" and resposta != "N":
        resposta = input("Deseja pedir mais alguma coisa? (S/N)").upper()
        if resposta == "S":
            break
        elif resposta == "N":
            break
        else:
            print("Opção inválida. Digite S ou N!")
            continue
    if resposta == "N":
        break
print(f"voce pediu, {}total a pagar: R${total:.2f}")