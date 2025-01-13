produtos = []


def cadastrar_produto():
    nome = input("Nome do produto: ")
    descricao = input("Descrição do produto: ")
    while True:
        try:
            valor = float(input("Valor do produto: "))
            if valor < 0:
                print("O valor não pode ser negativo.")
            else:
                break
        except ValueError:
            print("Valor inválido. Digite um número.")
    disponivel = input("Disponível para venda (S/N): ").lower()
    if disponivel not in ("S", "N"):
        print("Resposta inválida. Use 'S' para sim ou 'N' para não.")
        return
    produtos.append(
        {"nome": nome, "descricao": descricao, "valor": valor, "disponivel": disponivel}
    )
    listar_produtos()


def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    produtos_ordenados = sorted(produtos, key=lambda produto: produto["valor"])

    print("\nListagem de Produtos:")
    print("-" * 20)
    print("{:<20} {:<10}".format("Nome", "Valor"))
    print("-" * 20)
    for produto in produtos_ordenados:
        print("{:<20} {:<10.2f}".format(produto["nome"], produto["valor"]))

    while True:
        opcao = input("Deseja cadastrar um novo produto? (S/N): ").lower()
        if opcao == "S":
            cadastrar_produto()
            break
        elif opcao == "N":
            break
        else:
            print("Resposta inválida. Use 'S' para sim ou 'N' para não")


while True:
    print("\nMenu:")
    print("1. Cadastrar produto")
    print("2. Listar produtos")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        break
    else:
        print("Opção inválida.")
