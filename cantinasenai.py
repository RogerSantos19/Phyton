
'''
Delicias = ["COD:100 coxinha top da casa top R$10,00 ","COD:101cocalith R$9,00","COD:102picanhadolula R$5"]
for i in Delicias:
    print(i) 

c100 == 10
c101 == 9
c102 == 5

produtos = int(input("o que deseja ? "))
while produtos not in Delicias
'''

print("********** BEM VINDO A LANCHONETE DO PAI ***********")
Delicias = ["COD:100 Coxinha da casa top R$10,00 ","COD:101 Coca Lith R$9,00","COD:102 picanha do lula CONFIA R$5",    "COD:103 X-Salada R$3,50"]
for i in Delicias:
    print(i) 
produtos = {
    100: {"descricao": "Coxinha top da casa","valor": 10.00},
    101: {"descricao":"Coca Lith", "valor": 9.00},
    102: {"descricao":"Picanha |Do Lula", "valor": 5.00},
    103: {"descricao":"X-Salada", "valor": 3.50},
}
total = 0
while True:
    codigo = int(input("Digite o código do produto desejado: "))
    if codigo in produtos:
        produto = produtos[codigo]
        total += produto["valor"]
        print(f"Produto: {produto['descricao']}")
        print(f"Valor: R$ {produto['valor']:.2f}")
    else:
        print("Opção inválida!")
        continue
    while True:
        opcao = input("Deseja pedir mais alguma coisa? (S/N): ").lower() 
        if opcao== "n":
            print(f"Total a pagar: R$ {total:.2f}")
            break
        elif opcao == "s":
            break
        else:
            print("opcao invalida")
            continue
    if opcao== "n":
        break
    print(f"Valor: R$ {produto['valor']:.2f}")


 




