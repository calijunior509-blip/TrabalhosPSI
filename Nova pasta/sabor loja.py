from loja import adicionar_produto
from loja import listar_produtos
from loja import atualizar_stock
from loja import remover_produto
from loja import procurar_produto


def menu():
    while True:
        print("===== MENU =====")
        print("1 - Adicionar produto")
        print("2 - Listar produtos")
        print("3 - Procurar produto")
        print("4 - Atualizar stock")
        print("5 - Remover produto")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            codigo = input("Código: ")
            nome = input("Nome: ")
            preco = float(input("Preço: "))
            stock = int(input("Stock: "))
            adicionar_produto(codigo, nome, preco, stock)

        elif opcao == "2":
            listar_produtos()

        elif opcao == "3":
            codigo = input("Código do produto: ")
            procurar_produto(codigo)

        elif opcao == "4":
            codigo = input("Código do produto: ")
            novo_stock = int(input("Novo stock: "))
            atualizar_stock(codigo, novo_stock)

        elif opcao == "5":
            codigo = input("Código do produto: ")
            remover_produto(codigo)

        elif opcao == "0":
            print("Programa terminado.")
            break

        else:
            print("Opção inválida.\n")


menu()
