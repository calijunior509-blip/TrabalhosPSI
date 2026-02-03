nomes = []

def adicionar_nome():
    nome = input("digite o nome que quer adicionar: ")
    nomes.append(nome)
    print("nome adicionado")

def remover_nome():
    nome = input("digite o nome que quer remover: ")
    if nome in nomes:
        nomes.remove(nome)
        print("nome removido")
    else:
        print("nome não existente")

def lista_nomes():
    if len(nomes) == 0:
        print("Nenhum nome existente.")
    else:
        print("Lista de nomes:")
        for nome in nomes:
            print("-", nome)

def procurar_nome():
    nome = input("que nome quer procurar?: ")
    if nome in nomes:
        print("Nome encontrado")
    else:
        print("Nome não encontrado")

def menu():
    while True:
        print("\n///// Tabela de Nomes /////")
        print("1. Adicionar nome")
        print("2. Remover nome")
        print("3. Listar todos os nomes")
        print("4. Procurar um nome")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_nome()
        elif opcao == "2":
            remover_nome()
        elif opcao == "3":
            lista_nomes()
        elif opcao == "4":
            procurar_nome()
        elif opcao == "5":
            print("A sair ...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
