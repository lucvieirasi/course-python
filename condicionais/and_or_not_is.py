"""
Estruturas Loicas: and (e), or (ou), not (nao), is (é)

Operadores unários:
    - not, is
Operadores binários:
    - and, or

    - Para o 'and', ambos os valores precisam ser True.
    - Para o 'or' um ou outro valor precisa ser True.
    - Para o 'not' o valor do booleano é invertido, ou seja se for True vira False, se for False vira True.
"""
ativo = True
logado = True
if ativo is True:
    print('Bem-vindo usuário!')
else:
    print('Sua conta requer ativacao,verifique o seu email!')