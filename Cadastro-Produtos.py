import matplotlib.pyplot as plt

#1 Criação das funções e listas antes do while, para o phyton reconhecer as funções que existem.
lista_produtos = []

def cadastro(): # Função que faz o usuário cadastrar seu produto.
    produto_nome = str(input('Digite o nome do produto que deseja cadastrar: '))
    produto_quantidade = int(input('Digite a quantidade do produto: '))
    produto_preco = float(input('Digite o preço do produto: '))
    sublista = [produto_nome, produto_quantidade, produto_preco]
    lista_produtos.append(sublista)
    print('Produto cadastrado com sucesso!')

def excluir_cadastro(): # Função que analisa se determinado produto está dentro da lista para remoção, se estiver, será apagado, se não, será alertado.
    excluir_produto = str(input('Digite o nome do produto que deseja excluir: '))
    produto_encontrado = False # Aqui utilizei a logica false, pois essa variavel anda com excluir_produto, ou seja,
    for produto_excluir in lista_produtos:
        if excluir_produto == produto_excluir[0]:
            lista_produtos.remove(produto_excluir)
            print('Produto removido com sucesso!')
            produto_encontrado = True
            break
    if produto_encontrado == False:
        print('Este produto não está dentro da lista!')
        
def excluir_produtos_lista(): # Função que exclui todos os produtos da lista.
    lista_produtos.clear()
    print('Produtos removidos da lista com sucesso!')

print('Bem vindo ao sistema de cadastro de produtos! Oque você deseja fazer? (Digite o número da ação que deseja realizar.)')
while True:
    # Criação do menu: (Com while)
    print("\n-------------------------------------------")
    print('1. VER PRODUTOS | 2. CADASTRAR PRODUTO | 3. EXCLUIR PRODUTO  | 4. LIMPAR LISTAS DE PRODUTOS | 5. SAIR ')

    menu_escolha = str(input(' '))
    if menu_escolha == "1":
        print('Exibindo a lista de produtos:')
        if not  lista_produtos:
            print("Nenhum produto foi cadastrado ainda!")
        else:
            for numero, produto_ofc in enumerate(lista_produtos, start=1):
                print(f"{numero} - {produto_ofc[0]} | Quantidade: {produto_ofc[1]} | Preço: {produto_ofc[2]}") # Aqui, foi criado uma sintaxe que permite o usuário visualizar melhor a lista de produtos.
    elif menu_escolha == "2":
        cadastro()
    elif menu_escolha == "3":
        print('Qual produto deseja remover da lista?')
        for numero, produto_ofc in enumerate(lista_produtos, start=1):
            print(f"{numero} - {produto_ofc[0]} | Quantidade: {produto_ofc[1]} | Preço: {produto_ofc[2]}")
        excluir_cadastro() 
    elif menu_escolha == "4":
        excluir_produtos_lista()
    elif menu_escolha == "5":
        print('Saindo do sistema... Obrigado!')
        break
    else:
        print('Digite o número da ação corretamente!')


#1. Planejar o que é um produto (nome, codigo, quantidade, preço)
#2. Criar armazenamento dos produtos (lista, listas de listas, dicionários)
#3. Criação do menu do sistema: 1 - Ver produtos 2 - Cadastrar produto 3 - Excluir produto 4 - Limpar lista 5 - 
#4. Função para cadastrar os produtos (pedir dados do produto, criar produto, adicionar na lista)
#5. Função para ver os produtos (percorrer todos os produtos e mostrar na tela)
#6. Função para excluir produtos (pedir nome do produto e depois remover da lista)
#7. Função para apagar todos os produtos.
#8. Conectar tudo no menu (ler a opção e chamar a função correta.)