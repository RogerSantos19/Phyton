
'''Tem gente que fala rápido demais, mal dá pra entender, seria bom se a gente pudesse diminuir a velocidade ou até colocar umas pausas entre as palavras...

Crie um arquivo chamado velocidade.py e escreva um programa em Python que mostre uma mensagem digitada pelo usuário, mas substituindo os espaços em branco por reticências "...".

Exemplo:

Mensagem: Não vejo a hora de ir embora
Saída: Não...vejo...a...hora..de...ir...embora
'''
'''
frase = input("digite sua mensagem:").replace(" ","...")
print(frase)
'''
'''
valor = input("digite alguma coisa:").replace("E","Z")
print(valor)
'''


idade =int( input ("digite sua idade"))
if idade  < 16:    
    print("nao vota")
elif idade  >= 18 and idade <=70:  
    print("voto obrigatorio")
else:
    print("voto opcional")

