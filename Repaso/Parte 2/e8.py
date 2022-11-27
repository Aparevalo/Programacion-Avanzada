def dolares(precio):
    return (precio[:precio.find('.')], 'dolares y', precio[precio.find('.')+1:], 'centavos.')


print(dolares(input("Introduce el precio del producto con dos decimales:  ")))
