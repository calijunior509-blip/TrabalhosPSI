lista = []

limite = int(input("Quantas notas quer inserir: "))

for i in range(limite):
    while True:
        try:
            nota = float(input(f"Que nota teve? {i+1}ª nota: "))

            lista.append(nota)
            print("inseriu a nota:", nota)
            break
        except ValueError:
            print("Digite um número.")

while True:
    decisao = input("O que quer fazer agora? (media / max / min / sair): ").lower()

    if decisao == "media":
        media = sum(lista) / len(lista)
        print("a média é:", media)

    elif decisao == "max":
        print("a maior nota é:", max(lista))

    elif decisao == "min":
        print("a menor nota é:", min(lista))

    elif decisao == "sair":
        print("ok.")
        break

    else:
        print("por favor insira apenas as opções indicadas.")

