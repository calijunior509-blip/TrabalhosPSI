import time




print("            ---criador de palavras passes---")
print("     olá seja bem vindo ao criador de palavras passes")
print("                   é de simples uso")
print("                tem 10 slots de palavras")
print("       pense em 10 palavras que nunca se esqueceria")
print("(como o nome de seu animal de estimação , pai , rua , país , etc)")
print("  e o programa criará uma palavra passe pra si automaticamente")


nome1=input("-qual a primeira palavra: ")
nome2=input("--qual a segunda palavra: ")
nome3=input("---qual a terceira palavra: ")
nome4=input("----qual a quarta palavra: ")
nome5=input("-----qual o quinta palavra: ")
nome6=input("------qual o sexta palavra: ")
nome7=input("-------qual o setima palavra: ")
nome8=input("--------qual o oitava palavra: ")
nome9=input("---------qual o nona palavra: ")
nome10=input("---------qual o decima palavra: ")


print(" a sua palavra passe é "+nome1[0:2]+nome2[0:2]+nome3[0:2]+nome4[0:1]+nome5[0:2]+nome6[1:4]+nome7[0:2]+nome8[0:2]+nome9[0:2]+nome10[0:2])

print("caso não esteja satisfeito podemos fazer mais uma para si")
print("       uma"
      ""
      " um pouco mais dificil de memorizar")

while True:
    decisao = input("quer uma nova palavra passe? (Y/N): ")

    if decisao == "Y" or decisao == "y":
        print("Ok, para a nova senha por favor insira os seguintes dados")

        nome_1 = input("-qual o seu nome: ")
        nome_2 = input("--qual a sua morada: ")
        nome_3 = input("---qual a data que expira o seu cartão de credito: ")
        nome_4 = input("----qual o seu numero favorito: ")
        nome_5 = input("-----qual o seu animal favorito: ")
        nome_6 = input("------qual o meu nome?: ")
        nome_7 = input("-------você sabe o meu nome?: ")
        nome_8 = input("--------você tem medos?: ")
        nome_9 = input("---------se vc estivesse em perigo agora, você poderia correr?: ")
        nome_10 = input("----------qual o nome da rua em que vc vive?: ")

        print("processando informações...")

        senha = (
            nome_1[0:1]
            + str(len(nome_2))
            + nome_3[1:5]
            + nome_4
            + nome_5[0:2]
            + str(len(nome_10))
        )

        print("a sua palavra passe é:", senha)
        break

    elif decisao == "N" or decisao == "n":
        print("Ok")
        break

    else:
        print("Por favor escolha Y ou N.")


print(" se quiser podemos fazer uma palavra passe mais dificil ainda ")
print("farei algumas perguntas simples e responda com apenas uma palavra ")

while True:
    decisao_1=input("pretende criar mais uma palavra passe? (Y/N): ")
    if decisao_1 == "Y" or decisao_1 == "y":
        print("Ok")
        nome__1=input("...nome da sua mãe: ")
        nome__2=input("...nome do seu pai: ")
        nome__3=input("...qual o seu maior medo?: ")
        nome__4=input("...acredita em milagres?: ")
        nome__5=input("...qual o seu maior sonho?: ")
        nome__6=input("...caso vc morresse , quantas pessoas se importariam?: ")
        nome__7=input("...fugiria se não tivesse outra opção?: ")
        nome__8=input("...e se tivesse?fugiria sem saber do que?: ")
        nome__9=input("...nome do que te motiva: ")
        nome__10=input("...o primeiro numero que pensar entre 100 e 1000: ")

        print("processando informações...")

        senha_1 = (
                nome__1[0:1]
                + str(len(nome__3))
                + nome__3[1:5]
                + str(len(nome__4))
                + str(len(nome__5))
                + nome__6[0:1]
                + str(len(nome__7))
                + nome__8[1:5]
                + nome__9[0:3]
                + str(len(nome__10))
        )

        print("a sua senha é:", senha_1)

        break
    elif decisao_1 == "N" or decisao_1 == "n":
        print("Ok , obrigado por usar o meu programa:)")
        print("voce fechou meu programa ")
        print("voce tem 20 segundos")
        print("quando fechado vc não pode fazer nada.")
        for n in range(0, 20,-1):
            print(f"fechando em {n}")
        time.sleep(20)

        quit()
    else:
        print("Por favor escolha Y ou N.")


