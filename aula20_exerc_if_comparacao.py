primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

int_primeiro_valor = int(primeiro_valor)
int_segundo_valor = int(segundo_valor)

if int_primeiro_valor > int_segundo_valor:
    print(f'{primeiro_valor=} é maior que {segundo_valor=}')
else:
    print(f'{segundo_valor=} é maior que {primeiro_valor=}')

