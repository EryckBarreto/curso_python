import random

nove_digitos = ''

for i in range(9):
    nove_digitos += str(random.randint(0, 9))


contador_regressivo_1 = 10

resultado_1 = 0
for digito_1 in nove_digitos:
    resultado_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = resultado_1 * 10 % 11
digito_1 = digito_1 if digito_1 <= 9 else 0


nove_numeros = nove_digitos[0:9]
nove_numeros_junto_com_primeiro = nove_numeros + nove_digitos[9]
resultado_2 = 0
contagem_regressiva = 11

for numeros in nove_numeros_junto_com_primeiro:
    resultado_2 += int(numeros) * contagem_regressiva
    contagem_regressiva -= 1

resultado_2 = resultado_2 * 10 % 11
resultado_2 = resultado_2 if resultado_2 < 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{resultado_2}'

print(cpf_gerado_pelo_calculo)