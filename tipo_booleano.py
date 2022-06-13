""""
Tipo Booleano

Algebra Booleana, criada por George Boole

2 Consctantes, verdadeiro ou falso, True => Verdadeiro e False => Falso.

Obs: Sempre com a inicial maiuscula.
Errado: true, false
Certo: True, False
"""

ativo = True

print(ativo)

""""
Operacoes Basicas:
"""
# Negacao (not):
""""
Fazendo a negacao, se o valor booleano for verdadeiro o resultado será falso,
se for falso o resultado será verdadeiro, ou seja semrpe ao contrario.
"""
print (not ativo)
logado = False
# Out (or)
""""
É uma operacao binaria, ou seja depende de dois valroes ou um ou outro deve ser verdadeiros.

True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""
print (ativo or logado)

# E (and)
""""
Também é uma operacao binaria, ou seja, depende de dois valores. Ambos, os valores
devem ser verdadeiros.
True and True -> True
True and False -> False
False and True -> False
False and False -> True
"""
