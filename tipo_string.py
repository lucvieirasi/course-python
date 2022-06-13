"""
Tipo string
Em Python, um dado é considerado do tipo string semrpe que:
- Estiver entre Áspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Esiver entre áspas duplas ->  "uma string", "234", "a", "True", "42.3"
- Estiver entre áspas simples triplas -> ''uma string'', ''234'', ''a'', ''True'', ''42.3''
- Estiver entre aspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''
"""
nome = 'Greek University'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina Jolie'
print(nome)
print(type(nome))

nome = """ Angelina
Jolie"""
print(nome)
print(type(nome))

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
nome = 'Geek University'
print(nome[0:4]) #Slice de string

print(nome[5:15]) #Slice de string
print(nome.split()[0])