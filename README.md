# Sistema de Cadastro de Produtos em Python

Projeto simples desenvolvido em Python para cadastro e gerenciamento de produtos de pequenos mercados.

O sistema permite cadastrar produtos, visualizar a lista de produtos cadastrados, excluir produtos específicos e limpar toda a lista.

## Funcionalidades

- Visualizar produtos
- Cadastrar novo produto
- Atualizar produto existente
- Excluir produto por ID
- Limpar toda a lista de produtos
- Exibir gráfico de produtos (quantidade)
- Sair do sistema
- Estrutura do Projeto

## Divisão dos arquivos
O projeto está dividido em múltiplos arquivos para melhor organização:
- SistemaCadastro.py → Arquivo principal com o menu e execução do sistema.
- exibicao.py → Responsável por exibir produtos e gerar gráficos.
- menuFuncoes.py → Contém funções de cadastro, atualização e exclusão.
- validacoes.py → Funções para validação de dados (nome, preço, quantidade).
- README.md → Documentação do projeto.

## Estrutura de Dados
Os produtos são armazenados em uma lista de dicionários:

lista_produtos = [
    {
        "id": 1,
        "nome": "Produto Exemplo",
        "quantidade": 10,
        "preco": 5.99
    }
]

- Cada produto possui um ID único
- O ID é incremental e não é reutilizado automaticamente após exclusão

## Bibliotecas utilizadas
O sistema utiliza a biblioteca:

- matplotlib

Para gerar gráficos com base na quantidade de produtos cadastrados.

## Tecnologias 

- Python
- Git (Envio de commits, push e sincronia com repositório) 
- Github
- JSON (Para salvar arquivos após ser fechado, evitando as informações ficarem salvas apenas na memória.)


## Como Executar

1. Clone o repositório ou baixe os arquivos
2. Instale as dependências (caso você não possua as bibliotecas utilizadas):

- pip install matplotlib

3. Execute o arquivo principal:

- python SistemaCadastro.py

# Projeto desenvolvido como prática de lógica de programação em Python.
Projeto desenvolvido por: *Vinícius Ribeiro Lins.*