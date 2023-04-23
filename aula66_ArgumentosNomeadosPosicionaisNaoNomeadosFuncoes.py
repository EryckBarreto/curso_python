"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y, z):
    # definição
    print(f'{x=} {y=} {z=}', '|', 'x + y + z = ', x + y)

soma(1, 2, 3)
soma(y=2, z=3, x=1)
soma(1, 2, z=5)