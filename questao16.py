valor = float(input("Digite o valor da presta��o: "))
tempo = int(input("Digite o tempo de atraso: "))
taxa = float(input("Digite o valor da taxa de atraso: "))


prestac = valor + (valor *(taxa/100) * tempo)

print("O valor da presta��o em atraso � R$ %.2f" %prestac)
