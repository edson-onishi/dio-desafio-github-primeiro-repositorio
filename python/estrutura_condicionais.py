MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Digite sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior ide idade, pode tirar a CNH")

if idade < MAIOR_IDADE:
    print("ainda não pode tirar a CNH.")


if idade >= MAIOR_IDADE:
    print('maior de idade, pode tirar a CNH.') 
else:
    print("AInda não pode  tirar a CNH")           


if idade >= MAIOR_IDADE:
    print('maior de idade, pode tirar a CNH.') 
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teoricas , mas nao pode fazer aulas praticas.") 
else:
    print("Ainda não pode tirar a CNH")       