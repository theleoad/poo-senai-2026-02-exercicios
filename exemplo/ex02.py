# EXEMPLO (não vale nota): um exercício entregue, para você ver o formato.
#
# Enunciado: crie a função dobro(n), que DEVOLVE (return) o dobro de n.
#
# No fim, rode e cole a saída do terminal embaixo da linha # SAÍDA:, cada linha
# começando com #, MESMO QUE SEJA UM ERRO. Depois salve e envie pelo site do GitHub.
# Conta como entregue: arquivo alterado (uma tentativa de verdade) + saída colada.

def dobro(n):
    return n * 2


print(dobro(4))
print(dobro("10" + 1))

# SAÍDA:
# 8
# Traceback (most recent call last):
#   File "C:\Users\aluno\poo-senai-2026-02-exercicios\exemplo\ex02.py", line 14, in <module>
#     print(dobro("10" + 1))
#                 ~~~~~^~~
# TypeError: can only concatenate str (not "int") to str
