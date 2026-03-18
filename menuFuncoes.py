from validacoes import verificar_nome_produto, verificar_preco_float, verificar_quantidade_inteiro
def cadastro(lista_produtos, contador_id): # Função que faz o usuário cadastrar seu produto.
    produto_nome = verificar_nome_produto()
    if produto_nome == "0":
        return
    
    dicionario_produto = {
        "id": contador_id,
        "nome": produto_nome,
        "quantidade":verificar_quantidade_inteiro(),
        "preco":verificar_preco_float()
    } 
    lista_produtos.append(dicionario_produto)
    print('Produto cadastrado com sucesso!')
    return contador_id + 1

def gerar_id(lista_produtos): # Função que permite numerar corretamente os IDs, perfeito em situações de remoção de produto. (Substituição do global.)
    if not lista_produtos:
        return 1
    ids_existentes = [produto["id"] for produto in lista_produtos]
    novo_id = 1
    while novo_id in ids_existentes:
        novo_id += 1
    return novo_id

def atualizar_cadastro(lista_produtos): # Função que atualiza os status de um produto, quantidade e preço ( se quiser atualizar o preço )
    atualizar_produto = int(input('Digite o ID do produto que deseja atualizar(0 para voltar ao menu): '))
    if atualizar_produto == "0":
        return
    atualizar_encontrado = False 
    for produto_atualizar in lista_produtos:
        if atualizar_produto == produto_atualizar["id"]:
            atualizar_quantidade = verificar_quantidade_inteiro()
            atualizar_preco = verificar_preco_float()
            produto_atualizar["quantidade"] = atualizar_quantidade
            produto_atualizar["preco"] = atualizar_preco
            print('Produto atualizado com sucesso!')
            atualizar_encontrado = True
            break
    if atualizar_encontrado == False:
        print('Produto não encontrado!')

def excluir_cadastro(lista_produtos): # Função que analisa se determinado produto está dentro da lista para remoção, se estiver, será apagado, se não, será alertado.
    excluir_produto = int(input('Digite o ID do produto que deseja excluir(0 para voltar ao menu): '))
    if excluir_produto == "0":
        return
    produto_encontrado = False # Aqui utilizei a logica false, pois essa variavel é como um marcador para servir para a condição ter um pause, por isso há a existencia do break ali. Que será ativado quando o produto for encontrado. (true)
    for produto_excluir in lista_produtos:
        if excluir_produto == produto_excluir["id"]:
            lista_produtos.remove(produto_excluir)
            print('Produto removido com sucesso!')
            produto_encontrado = True
            break
    if produto_encontrado == False:
        print('Este produto não está dentro da lista!')
        
def excluir_produtos_lista(lista_produtos): # Função que exclui todos os produtos da lista.
    lista_produtos.clear()
    print('Produtos removidos da lista com sucesso!')
