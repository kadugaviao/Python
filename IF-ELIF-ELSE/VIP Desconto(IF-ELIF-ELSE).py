categoria = input('Digite sua categoria: ').upper()
valorCompra = float(input('Digite o valor total da compra: '))
percentual = 0

if categoria == 'REGULAR' and valorCompra > 100:
    valorCompra = valorCompra * 0.95
    print('Você recebeu 5 porcento de desconto. O valor da compra ficou: R$', valorCompra)
elif categoria == 'REGULAR':
    print('Você não ganhou desconto. Valor de compra: ', valorCompra)
elif categoria == 'VIP' and valorCompra > 500:
    valorCompra = valorCompra * 0.80
    print('Você recebeu 20 porcento de desconto. Valor da compra: ', valorCompra)
elif categoria == 'VIP' and valorCompra > 100:
    print('Você recebeu 10 porcento de desconto. Valor de compra: ', valorCompra)
elif categoria == 'PLATINUM' and valorCompra > 500:
    valorCompra = valorCompra * 0.75
    print('Você recebeu 25 porcento de desconto. Valor de compra: ', valorCompra)

