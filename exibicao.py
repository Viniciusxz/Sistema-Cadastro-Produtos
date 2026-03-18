def exibicao_produtos(lista_produtos): # Função que faz o usuário vizualizar todos os cadastros.
    if not lista_produtos:
        print('Nenhum produto foi cadastrado ainda!')
    else:
        for produto_ofc in (lista_produtos):
                print(f"ID - {produto_ofc['id']} | Nome: {produto_ofc['nome']} | Quantidade: {produto_ofc['quantidade']} | Preço: R$ {produto_ofc['preco']:.2f}")
