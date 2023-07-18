def main(): 
    reais = reais_to_float(input("Quanto deu a conta? "))
    percent = percent_to_float(input("Qual a porcentagem da gorgeta? "))
    tip = reais * percent
    print(f"Deixe R${tip:.2f}")

def reais_to_float(d):
    d = (d.replace("R$","",).replace(",",".",))
    try:
     d = float(d)
    except:
       print("valor informado nao é numerico")
       quit()
    return d

def percent_to_float(p):
    p = float (p.replace("%","")) /100
    return p 
main()