"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""
import re
import sys

entrada = input('Digite o seu CPF: ')
cpf_enviado_usuario = re.sub(r'[^0-9]', '', entrada)

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()


nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_1 = 10

resultado_1 = 0
for digito_1 in nove_digitos:
    resultado_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = resultado_1 * 10 % 11
digito_1 = digito_1 if digito_1 <= 9 else 0


nove_numeros = cpf_enviado_usuario[0:9]
nove_numeros_junto_com_primeiro = nove_numeros + cpf_enviado_usuario[9]
resultado_2 = 0
contagem_regressiva = 11

for numeros in nove_numeros_junto_com_primeiro:
    resultado_2 += int(numeros) * contagem_regressiva
    contagem_regressiva -= 1

resultado_2 = resultado_2 * 10 % 11
resultado_2 = resultado_2 if resultado_2 < 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{resultado_2}'

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'CPF {cpf_enviado_usuario} enviado pelo usuário é válido')
else:
    print('CPF inválido')