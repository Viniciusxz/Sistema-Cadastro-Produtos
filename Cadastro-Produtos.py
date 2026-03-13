#0 Criação do menu: (Com while)
while True:
    print('Bem vindo ao sistema de cadastro de produtos! Oque você deseja fazer? (Digite o número da ação que deseja realizar.)')
    print('1. VER PRODUTOS | 2. CADASTRAR PRODUTO | 3. EXCLUIR PRODUTO  | 4. LIMPAR LISTAS DE PRODUTOS | 5. SAIR ')

    menu_escolha = str(input(' '))

    lista_produtos = []

    if menu_escolha == "1":
        print('Exibindo a lista de produtos...')
        print(lista_produtos)
    if menu_escolha == "2":
    if menu_escolha == "3":
    if menu_escolha == "4":
    if menu_escolha == "5":
        print('Saindo do sistema...')
        break


#1. Planejar o que é um produto (nome, codigo, quantidade, preço)
#2. Criar armazenamento dos produtos (lista, listas de listas, dicionários)
#3. Criação do menu do sistema: 1 - Ver produtos 2 - Cadastrar produto 3 - Excluir produto 4 - Limpar lista 5 - 
#4. Função para cadastrar os produtos (pedir dados do produto, criar produto, adicionar na lista)
#5. Função para ver os produtos (percorrer todos os produtos e mostrar na tela)
#6. Função para excluir produtos (pedir nome do produto e depois remover da lista)
#7. Função para apagar todos os produtos.
#8. Conectar tudo no menu (ler a opção e chamar a função correta.)