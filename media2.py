quantidade = int(input("Quantas notas você deseja informar? "))
somaDasNotas = 0

for i in range (0, quantidade, 1):
    nota = float(input(f"Digite a nota {i+1}: "))
    peso = float(input(f"digite o peso da nota {i+1}:"))
    somaDasNotas = somaDasNotas + nota * peso
    somdospesos = somaDasNotas + peso

media = somaDasNotas / quantidade
print(f"A média é: {media:.1f}")