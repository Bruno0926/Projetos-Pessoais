#projeto número 1.
import random

def jogo():
    palavras = ["banana", "uva", "maracuja", "melancia", "laranja", "abacate"]
    escolhida = random.choice(palavras)

    # print(escolhida)
    num = 6

    letras = ["_" for letra in escolhida]
    # print(letras)

    letras_erradas = []

    print("voce tem 6 tentativas!")

    while num > 0:

        print(" ".join(letras)) # mostra o progresso da palavra durante o programa. Esta expressão pega a lista "letras" e une seus elementos em uma única string, colocando um espaço " " entre cada elemento da lista.

        print("tentativa numero", num, ":")
        letra_digitada = input().lower()

        if letra_digitada in escolhida:
            indice = 0
            for letra in escolhida:
                if letra_digitada == letra:
                    letras[indice] = letra
                indice += 1
        else:
            num -= 1
            letras_erradas.append(letra_digitada)
            print("letras erradas: ", len(letras_erradas)) 

        if "_" not in letras:
            print("VOCE VENCEU O JOGO!")
            break
        
    print("palavra certa: ", escolhida)
   
if __name__ == "__main__":
    jogo()
    print("PROGRAMA ENCERRADO! ")






























