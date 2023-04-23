"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""

# str_numero_cpf = input('Digite o número do seu CPF: ')
# apenas_numeros = []

# for caractere in str_numero_cpf:
#     if caractere.isdigit():
#         apenas_numeros.append(int(caractere))

# primeiros_nove_digitos = apenas_numeros[0:9]

# a, b, c, d, e, f, g, h, i = primeiros_nove_digitos
# a = a * 10
# b = b * 9
# c = c * 8
# d = d * 7
# e = e * 6
# f = f * 5
# g = g * 4
# h = h * 3
# i = i * 2

# resultado = ((a + b + c + d + e + f + g + h + i) * 10) % 11

# if resultado > 9:
#     print('Resultado é 0.')
# else:
#     print(f'Resultado é {resultado}.')

    
cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado_1 = 0
for digito_1 in nove_digitos:
    resultado_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = resultado_1 * 10 % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)