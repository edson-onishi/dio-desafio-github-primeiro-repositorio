texto = input("digite um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end='')

print()        

# range (stop) -> rage object
# range (star, stop[,step]) -> range object

print(list(range(4)))


for numero in range(0, 51, 5):
    print(numero, end="")