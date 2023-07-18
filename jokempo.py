''''''
player1 = input ("player1 escolha :pedra, papel, tesoura:").lower() 
player2 = input ("player2 escolha :pedra , papel , tesoura:").lower()
print(player1, player2)
if player1 == "pedra"  and player2 == "pedra":
    print("empate")
if player1 == "tesoura"  and player2 == "tesoura":
    print("empate")
if player1 == "papel"  and player2 == "papel":
    print("empate")
if player1  == "pedra" and player2 == "tesoura":
    print("player1 venceu!")    
if player1  == "papel" and player2 == "pedra":
    print("player1 venceu!")  
if player1  == "tesoura" and player2 == "papel":
    print("player1 venceu!")
if player1  == "pedra" and player2 == "tesoura":
    print("player2 venceu!")    
if player1  == "papel" and player2 == "pedra":
    print("player2 venceu!")  
if player1  == "tesoura" and player2 == "papel":
    print("player2 venceu!")     
    '''