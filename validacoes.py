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
           if verificar_inteiro >= 0:
               return verificar_inteiro
           else:
               print('Quantidade inválida, não use números negativos!')
        except ValueError as erro0:
            print(f'Quantidade inválida, use apenas números! {erro0}')

def verificar_preco_float():
    while True:
        try:
            verificar_float = float(input('Digite o preço do produto aqui: '))
            if verificar_float >= 0:
                return verificar_float
            else:
                print('Preço inválido! Não é permitido preço negativo.')
        except ValueError as erro1:
            print(f'Preço invalidado!, Digite em números e com . ao invés de , ! {erro1}')