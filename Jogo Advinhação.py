# Eduardo Alves Martin N*8 1*E
import random
import os

erros=1
sorteado=random.randrange(0,100)
jogador=int(input("digite seu numero!") )
while (sorteado!=jogador):
    os.system('cls')
if(sorteado>jogador):
    print("ERRO, o número é maior")
elif(sorteado<jogador):
    print("ERRO, o número é menor")
erros += 1
jogador=int(input("Digite seu número: "))
print("Número" + str(jogador) + ",você acertou em: " + str(erros+1) + "tentativas")
