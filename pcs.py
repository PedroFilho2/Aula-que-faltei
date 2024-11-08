import random

def trocar_pcs(pcs_novos, pcs_velhos):
    random.shuffle(pcs_novos)
    random.shuffle(pcs_velhos)
    
    troca = zip(pcs_novos, pcs_velhos)
    return troca

def exibir(troca):
    print("Resultado do sorteio:")
    for pc_novo, pc_velho in troca:
        print(f"Quem usava o PC {pc_novo} vai usar o PC {pc_velho}.")

pcs_novos = [14, 15, 16, 17, 18, 19, 20, 24, 25, 26, 27, 28, 29, 30]
pcs_velhos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 21, 22, 23, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]

troca = trocar_pcs(pcs_novos, pcs_velhos)
exibir(troca)
