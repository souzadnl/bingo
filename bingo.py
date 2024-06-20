import random
import sys

def criar():
    numeros = []
    for numero in range(1, 76):
        numeros.append(numero)
    return numeros
    
    
def sortear(numeros, numeros_sorteados):
    if(numeros==[]):
        print("Acabaram os números!")
        sys.exit()
    else:
        numero_sorteado = random.choice(numeros)
        if(numero_sorteado>=1 and numero_sorteado<=15):
            print("Letra B")
        elif(numero_sorteado>=16 and numero_sorteado<=30):
            print("Letra I")
        elif(numero_sorteado>=31 and numero_sorteado<=45):
            print("Letra N")
        elif(numero_sorteado>=46 and numero_sorteado<=60):
            print("Letra G")
        elif(numero_sorteado>=61 and numero_sorteado<=75):
            print("Letra O")
        
        print(numero_sorteado)
        numeros_sorteados.append(numero_sorteado)
        numeros.remove(numero_sorteado)
    return numeros, numeros_sorteados


def verificar_se_bateu(lista_sorteados):
    while(True):
        resposta = input("\nHouve um vencedor? Digite S para sim ou N para não.\n")
        try:
            if(resposta == "S" or resposta == "s"):
                print("Muito bem. Aqui está a lista de números sorteados para garantir que ninguém comeu bola!")
                for numero in lista_sorteados:
                    print(numero)
                return verificar_vencedor()
                  
                
            elif(resposta == "N" or resposta == "n"):
                print("Muito bem, vamos continuar\n")
                return True
            else:
                print("Inserção inválida!\n")
        except:
            print("Inserção inválida!\n")
            
            
def verificar_vencedor():          
    while(True):
        houve_vencedor = input("\nA pessoa ganhou mesmo? Digite S para sim ou N para não.\n")  
        try:
            if(houve_vencedor == "S" or houve_vencedor == "s"):
                print("PARABÉNSS. Finalizando o jogo\n")
                return False
                
            elif(houve_vencedor == "N" or houve_vencedor == "n"):
                print("Certo, então vamos continuar\n")
                return True
                
            else:
                print("Inserção inválida!\n")
        
        except:
            print("Inserção inválida!\n")
    
print("Bem-Vindo ao Bingão!")
continuar = True
numeros = criar()
numeros_sorteados = []
input("Aperte ENTER para sortear um número!")

while continuar:
    numeros, numeros_sorteados = sortear(numeros, numeros_sorteados)
    continuar = verificar_se_bateu(numeros_sorteados)


