nome = "Edson"
idade = 28
profissao = "Programador"
liguagem = "Python"

dados = {"nome": "Edson", "idade": 28}

print("Nome: %s idade: %d" % (nome, idade))
print("Nome: {} idade: {}".format(nome, idade))
print("Nome: {1} idade: {0}".format(idade, nome))
print("Nome: {1} idade: {0} Nome: {1} {1}".format(idade, nome))
print("Nome: {nome} idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} idade: {age} {name} {name} {age}".format(age=idade, name=nome))
print("Nome: {nome} idade: {idade}".format(**dados))
