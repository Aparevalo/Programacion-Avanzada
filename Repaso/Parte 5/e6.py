"""
Escribir una función que reciba una muestra de 
números en una lista y devuelva su media.
"""
def mean(sample):
    return sum(sample)/len(sample)

print(mean([1, 2, 3, 4, 5]))
print(mean([2.3, 9.7, 9.8, 9.7, 12.9, 13.6]))