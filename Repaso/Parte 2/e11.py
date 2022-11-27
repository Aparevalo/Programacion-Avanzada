
def product(producto,precio,unidades):
    print('{producto}: {unidades:3d} unidades x {precio:9.2f}$ = {total:11.2f}$'.format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))

product(input('Introduce el nombre del producto: '),float(input('Introducde el precio unitario: ')),int(input('Introduce el número de unidades: ')))

