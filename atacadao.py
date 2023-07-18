preco = float ( input("digite o preço:"))
quantidade =int( input ("quantidade de produtos:"))
total = preco * quantidade
print(f"total da compra:")
quantidade = float ( input(quantidade,))
if quantidade  >= 0 and quantidade <=9:    
    print("voce tem 0% de desconto:")
elif quantidade  >= 10 and quantidade <=99:  
    print("voce tem 5% de desconto:")
    desconto = 0,5
elif quantidade  >= 100 and quantidade <=999:  
    print("voce tem 10% de desconto:")
    desconto = 0,10
elif quantidade  >= 1000 and quantidade <=9999999:  
    print("voce tem 15% de desconto:")
    desconto = 0,15 
totaldesc = total - (total*desconto)
print("total do desconto:")
