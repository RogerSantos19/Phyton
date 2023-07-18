print("Pense num número de 1 a 10")
resposta = input("... hmm. Seu número é ímpar? (S/N)").upper()
if resposta == "S":
    resposta = input("Esse número é maior que 5? (S/N)").upper()
    if resposta == "S":
        resposta = input("Espera... Seu número é o 7? (S/N)").upper()
        if resposta == "S":
            print("Eu sabia que era 7!")
        else:
            print("Então seu número é o 9!!")
    else:
        resposta = input("Espera... Seu número é menor que 3? (S/N)").upper()
        if resposta == "S":
            print("Eu sabia que era 1!")
        else:
            resposta = input("Seu número é o 5? (S/N)").upper()
            if resposta == "S":
                print("Eu sabia que era 5!")
            else:
                print("Então seu número é o 3!!")
else:
    resposta = input("Esse número é maior que 6? (S/N)").upper()
    if resposta == "S":
        resposta = input("Espera... Seu número é o 8? (S/N)").upper()
        if resposta == "S":
            print("Eu sabia que era 8!")
        else:
            print("Então seu número é o 10!!")
    else:
        resposta = input("Espera... Seu número é menor que 4? (S/N)").upper()
        if resposta == "S":
            print("Eu sabia que era 2!")
        else:
            resposta = input("Seu número é o 6? (S/N)").upper()
            if resposta == "S":
                print("Eu sabia que era 6!")
            else:
                print("Então seu número é o 4!!")