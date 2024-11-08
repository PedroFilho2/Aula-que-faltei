import random

palavras = ["arthur", "mouse", "sao paulo", "cadeira", "carro", "ze raimundo", "computador", "php", "javascript"]
palavraEscolhida = random.choice(palavras)

letraEscolhida = ["_"] * len(palavraEscolhida)
quantidadeErros = len(palavraEscolhida) - 1 
meusErros = 0
letrasErradas = []

print("A palavras sorteada tem " + str(len(palavraEscolhida))+ " letras")

while "_" in letraEscolhida and meusErros < quantidadeErros:
    print("Palavra:"+" ".join(letraEscolhida))
    print("Letras erradas: " + ", ".join(letrasErradas))
    letraInformada = input("INFORME UMA LETRA: ").lower()
    if letraInformada in palavraEscolhida:
       for i in range(len(palavraEscolhida)):
           if palavraEscolhida[i] == letraInformada:
               letraEscolhida[i] = letraInformada
    else:
        letrasErradas.append(letraInformada)
        meusErros +=1
        print("ERRRRRRRROU....")