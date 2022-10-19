print(True and True)
print(True and False)
print(True and False)
print(True or True)
print(True or False)
print(True or False)

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque

print(exp)