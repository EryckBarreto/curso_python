# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool

print(1 + 1)
print('a' + 'b') # poliformismo, concatenou a e b
# print('1' + 1) # não daria certo pq concatena str com str e não int com str

print(int('1'), type(int('1'))) # conversão do tipo
print(int('1') + 1) # exemplo de conversão na soma 
print(float(1.2) + 1) # exemplo float
print(bool('')) # string vazia é considerada falsa
print(bool(" ")) # string não vazia é considerada verdadeira
print(str(11) + 'b') # exemplo str