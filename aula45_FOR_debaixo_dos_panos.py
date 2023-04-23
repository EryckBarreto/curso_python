"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# texto = iter('Luiz') # __iter__()

# print(next(texto))

# for letra in texto
texto = 'Luiz' # iterável
# iterador = iter(texto) # iterador

# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    (print(letra))
