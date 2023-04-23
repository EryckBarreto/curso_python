"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""

variavel = 'Olá Mundo'
print(variavel[5])
print(variavel[-4])
print(variavel[4:8]) # se quero pegar o final, coloco um a mais, no caso queria pegar o 7, aí precisei colocar o 8
print(variavel[4:]) # se quero ir até o fim, pode emitir o fim
print(variavel[:5]) # posso emitir o inicio para indicar que quero que comece do início
print(len(variavel))
print(len(variavel[4:]))
print(variavel[0:9:2]) # passo, quantidade de catactere que pula
print(variavel[::-1]) # nesse caso inverte a string


