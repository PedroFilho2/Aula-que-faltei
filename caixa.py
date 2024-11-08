valor_saque = int(input("Informe o valor do saque"))
while valor_saque == "":
    print("Inválido")

    print(valor_saque%20)
    notas200 = valor_saque / 200
    notas100 = (valor_saque%200) / 100
    notas50 = (valor_saque%100) / 50
    notas20 = (valor_saque%50) / 20
    notas10 = (valor_saque%20) / 10
    notas5= (valor_saque%10) / 5
    print("Notas de 200: " + str(int(notas200)))
    print("Notas de 100: " + str(int(notas100)))
    print("Notas de 50: " + str(int(notas50)))
    print("Notas de 20: " + str(int(notas20)))
    print("Notas de 10: " + str(int(notas10)))
    print("Notas de 5: " + str(int(notas5)))

    valor_saque = int(input("Informe o valor do saque"))