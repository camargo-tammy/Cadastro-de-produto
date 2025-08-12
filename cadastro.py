def formartar_nome(nome):
    return nome.strip().title()

def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    categoria = input("Digite a categoria do produto: ")
    return (formartar_nome(nome), preco, categoria)

def salvar_produto(produto):
    with open("produtor.txt", "a", encoding="utf-8") as arquivo:
        linha = f"{produto[0]};{produto[1]};{produto[2]}\n"
        arquivo.write(linha)
def listar_produtos():
    try:
        with open("produtos.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                nome, preco, categoria = linha.strip().split(";")
                print(f"Produto: {nome} | Preço: R${preco} | Categoria: {categoria}")
    except FileNotFoundError:
        print("Nenhum produto cadastrado ainda.")

while True:
    print("\n1 - Cadastrar produto")
    print("2 - Listar produtos")    
    print("0 - Sair")
    opcao = input("Escolha: ")
    
    if opcao == "1":
        produto = cadastrar_produto()
        salvar_produto(produto)
    elif opcao == "2":
        listar_produtos()
    elif opcao == "0":
        break








