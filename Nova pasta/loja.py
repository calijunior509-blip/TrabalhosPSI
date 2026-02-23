
produtos = []


def adicionar_produto(codigo, nome, preco, stock):
    produto = (codigo, nome, preco, stock)
    produtos.append(produto)
    print("Produto adicionado \n")


def listar_produtos():
    if not produtos:
        print("Não existem produtos registados.\n")
        return

    print("\nLista de Produtos:")
    for p in produtos:
        print(f"Codigo: {p[0]} | Nome: {p[1]} | Preço: {p[2]}€ | Stock: {p[3]}")
    print()


def procurar_produto(codigo):
    for p in produtos:
        if p[0] == codigo:
            print(f"Produto encontrado: {p}\n")
            return
    print("Produto não encontrado.\n")


def atualizar_stock(codigo, novo_stock):
    for i in range(len(produtos)):
        if produtos[i][0] == codigo:
            produto = produtos[i]
            produtos[i] = (produto[0], produto[1], produto[2], novo_stock)
            print("Stock atualizado com sucesso!\n")
            return
    print("Produto não encontrado.\n")


def remover_produto(codigo):
    for p in produtos:
        if p[0] == codigo:
            produtos.remove(p)
            print("Produto removido com sucesso!\n")
            return
    print("Produto não encontrado.\n")


