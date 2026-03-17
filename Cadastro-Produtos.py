import matplotlib.pyplot as plt

#1 Criação das funções e listas antes do while, para o phyton reconhecer as funções que existem.
lista_produtos = []

def cadastro(): # Função que faz o usuário cadastrar seu produto.
    produto_nome = verificar_nome_produto()
    if produto_nome == "0":
        return
    produto_quantidade = verificar_quantidade_inteiro()
    produto_preco = verificar_preco_float()
    sublista = [produto_nome, produto_quantidade, produto_preco]
    lista_produtos.append(sublista)
    print('Produto cadastrado com sucesso!')

def atualizar_cadastro(): # Função que atualiza os status de um produto, quantidade e preço ( se quiser atualizar o preço )
    atualizar_produto = str(input('Digite o nome do produto que deseja atualizar(0 para voltar ao menu): '))
    if atualizar_produto == "0":
        return
    atualizar_encontrado = False 
    for produto_atualizar in lista_produtos:
        if atualizar_produto == produto_atualizar[0]:
            atualizar_quantidade = verificar_quantidade_inteiro()
            atualizar_preco = verificar_preco_float()
            produto_atualizar[1] = atualizar_quantidade
            produto_atualizar[2] = atualizar_preco
            print('Produto atualizado com sucesso!')
            atualizar_encontrado = True
            break
    if atualizar_encontrado == False:
        print('Produto não encontrado!')

def excluir_cadastro(): # Função que analisa se determinado produto está dentro da lista para remoção, se estiver, será apagado, se não, será alertado.
    excluir_produto = str(input('Digite o nome do produto que deseja excluir(0 para voltar ao menu): '))
    if excluir_produto == "0":
        return
    produto_encontrado = False # Aqui utilizei a logica false, pois essa variavel é como um marcador para servir para a condição ter um pause, por isso há a existencia do break ali. Que será ativado quando o produto for encontrado. (true)
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

def exibir_grafico(): # Função que faz um gráfico (com mathplotlib) baseado no nome do produto e quantidade dele,
    nome_produto = []
    quantidade_produto = []
    
    for produto1 in lista_produtos:
        nome_produto.append(produto1[0])
        quantidade_produto.append(produto1[1])
    plt.bar(x = nome_produto, height = quantidade_produto)
    print('Exibindo o gráfico baseado no nome e quantidade do produto!')
    plt.show()

# Funções de validações ( Nome do produto, Quantidade, Preço e Exclusão. )

def verificar_nome_produto():
    while True:
        verificar = (input('Digite o nome do produto aqui: ')).strip() # Strip para remover espaços antes e depois da string.
        if verificar == "0":
            return
        elif any(char.isalpha() for char in verificar):
            print('Nome do produto validado!')
            return verificar
        else:
            print('Nome inválido, insira novamente em letras.')

def verificar_quantidade_inteiro():
    while True:
        try:
           verificar_inteiro = int(input('Digite a quantidade do produto aqui: '))
           return verificar_inteiro
        except ValueError as erro0:
            print(f'Quantidade inválida, use apenas números! {erro0}')

def verificar_preco_float():
    while True:
        try:
            verificar_float = float(input('Digite o preço do produto aqui: '))
            return verificar_float
        except ValueError as erro1:
            print(f'Preço invalidado!, Digite em números e com . ao invés de , ! {erro1}')

            

print('Bem vindo ao sistema de cadastro de produtos! Oque você deseja fazer? (Digite o número da ação que deseja realizar.)')
while True:
    # Criação do menu: (Com while)
    print("\n-------------------------------------------")
    print('1. VER PRODUTOS | 2. CADASTRAR PRODUTO | 3. ATUALIZAR CADASTRO  | 4. EXCLUIR CADASTRO | 5. LIMPAR LISTA DE PRODUTOS | 6. EXIBIR GRÁFICO | 7. SAIR ')

    menu_escolha = str(input('-> '))
    if menu_escolha == "1":
        print('Exibindo a lista de produtos:')
        if not lista_produtos:
            print("Nenhum produto foi cadastrado ainda!")
        else:
            for numero, produto_ofc in enumerate(lista_produtos, start=1):
                print(f"{numero} - {produto_ofc[0]} | Quantidade: {produto_ofc[1]} | Preço: R$ {produto_ofc[2]:.2f}") # Aqui, foi criado uma sintaxe que permite o usuário visualizar melhor a lista de produtos.
    elif menu_escolha == "2":
        cadastro()
    elif menu_escolha == "3":
        for numero, produto_ofc in enumerate(lista_produtos, start=1):
                print(f"{numero} - {produto_ofc[0]} | Quantidade: {produto_ofc[1]} | Preço: R$ {produto_ofc[2]:.2f}")
        atualizar_cadastro()
    elif menu_escolha == "4":
        print('Qual produto deseja remover da lista?')
        for numero, produto_ofc in enumerate(lista_produtos, start=1):
            print(f"{numero} - {produto_ofc[0]} | Quantidade: {produto_ofc[1]} | Preço: R$ {produto_ofc[2]:.2f}")
        excluir_cadastro() 
    elif menu_escolha == "5":
        excluir_produtos_lista()
    elif menu_escolha == "6":
        exibir_grafico()
    elif menu_escolha == "7":
        print('Saindo do sistema... Obrigado!')
        break


#1. Planejar o que é um produto (nome, codigo, quantidade, preço)
#2. Criar armazenamento dos produtos (lista, listas de listas, dicionários)
#3. Criação do menu do sistema: 1 - Ver produtos 2 - Cadastrar produto 3 - Excluir produto 4 - Limpar lista 5 - 
#4. Função para cadastrar os produtos (pedir dados do produto, criar produto, adicionar na lista)
#5. Função para ver os produtos (percorrer todos os produtos e mostrar na tela)
#6. Função para excluir produtos (pedir nome do produto e depois remover da lista)
#7. Função para apagar todos os produtos.
#8. Conectar tudo no menu (ler a opção e chamar a função correta.)