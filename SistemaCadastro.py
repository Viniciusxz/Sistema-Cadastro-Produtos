import matplotlib.pyplot as plt
from exibicao import exibicao_produtos
from menuFuncoes import cadastro, atualizar_cadastro, excluir_cadastro, excluir_produtos_lista, salvar_produtos, carregar_produtos
from validacoes import verificar_nome_produto, verificar_preco_float, verificar_quantidade_inteiro

#1 Criação das funções e listas antes do while, para o phyton reconhecer as funções que existem.
lista_produtos = carregar_produtos()

if lista_produtos:
    contador_id = max(produto["id"] for produto in lista_produtos) + 1
else:
   contador_id = 1 


def exibir_grafico(): # Função que faz um gráfico (com mathplotlib) baseado no nome do produto e quantidade dele,1
    nome_produto = []
    quantidade_produto = []
    
    for produto1 in lista_produtos:
        nome_produto.append(produto1["nome"])
        quantidade_produto.append(produto1["quantidade"])
    plt.bar(x = nome_produto, height = quantidade_produto)
    print('Exibindo o gráfico baseado no nome e quantidade do produto!')
    plt.show()

print('Bem vindo ao sistema de cadastro de produtos! Oque você deseja fazer? (Digite o número da ação que deseja realizar.)')
while True:
    # Criação do menu: (Com while)
    print("\n-------------------------------------------")
    print('1. VER PRODUTOS | 2. CADASTRAR PRODUTO | 3. ATUALIZAR CADASTRO  | 4. EXCLUIR CADASTRO | 5. LIMPAR LISTA DE PRODUTOS | 6. EXIBIR GRÁFICO | 7. SAIR ')

    menu_escolha = str(input('-> '))
    if menu_escolha == "1":
        print('Exibindo a lista de produtos:')
        exibicao_produtos(lista_produtos)
    elif menu_escolha == "2":
        contador_id = cadastro(lista_produtos, contador_id)
    elif menu_escolha == "3":
        exibicao_produtos(lista_produtos)
        atualizar_cadastro(lista_produtos)
    elif menu_escolha == "4":
        print('Qual produto deseja remover da lista?')
        exibicao_produtos(lista_produtos)
        excluir_cadastro(lista_produtos) 
    elif menu_escolha == "5":
        excluir_produtos_lista(lista_produtos)
    elif menu_escolha == "6":
        exibir_grafico()
    elif menu_escolha == "7":
        print('Saindo do sistema... Obrigado!')
        break