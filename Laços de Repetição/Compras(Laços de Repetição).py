while True:
    somaProduto = 0
    numProduto = 1

    print('Lojas Tabajara')

    while True:
        produto = float(input('Registre o custo do produto ou digite 0 para sair: '))
        if produto == 0:
            break
        elif produto < 0:
            print('Preço invalido, tente novamente...')
            continue
        somaProduto += produto
        numProduto += 1

    print(f'Total: R${somaProduto:.2f}')

    while True:
        dinheiroFornecido = float(input('Quanto dinheiro foi entregue ao caixa: '))
        if dinheiroFornecido < somaProduto:
            print('Erro na transação, valor fornecido é menor que o total...')
        else:
            troco = dinheiroFornecido - somaProduto
            print(f'Troco: R${troco:.2f}')
            break

    novaCompra = input('Deseja comprar algo mais? (s/n): ').lower()
    if novaCompra == 'n':
        print('Compras finalizadas.')
        break
    else:
        continue