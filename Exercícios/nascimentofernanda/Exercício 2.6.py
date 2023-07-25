# 2.6	Crie um programa que leia 3 palavras do teclado e imprima essas palavras:
# •	Na forma padrão (separadas por espaço);
# •	Separadas por hífen (-);
# •	Separadas por espaço e terminadas em ponto de exclamação.

print("Por favor, digite uma palavra")
palavra_um=input()
print("Por favor, digite uma palavra")
palavra_dois=input()
print("Por favor, digite uma palavra")
palavra_tres=input()

print(palavra_um, palavra_dois, palavra_tres)
print(palavra_um, palavra_dois, palavra_tres, sep="-")
print(palavra_um, palavra_dois, palavra_tres, end="!")
