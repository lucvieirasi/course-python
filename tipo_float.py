""""
Tipo Float

Tipo Real . Decimal

Casas Decimais
OBS: O separador de casas decimais na programacao é ponto e náo a virgula.
"""
# Errado do ponto de vista do Float,mas gera uma tupla.
valor = 1,44
print(valor)
print(type(valor))

# Certo, do ponto de vista do Float.
valor = 1.44
print(valor)
print(type(valor))

# é possível fazer dupla atribuicao
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))