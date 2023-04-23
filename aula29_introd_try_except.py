"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""


# numero = input('Vou dobrar o número que você digitar: ')

# print(f'O dobro de {numero} é {float(numero) * 2}')

numero_str = input('Vou dobrar o número que você digitar:')

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2}')
except:
    print('Isso não é um número')

# print(numero_str.isdigit())

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2}')
# else:
#     print('Isso não é um número.')

