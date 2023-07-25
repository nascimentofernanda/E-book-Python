#Crie um programa que diga quantos livros tem em estoque baseado nas entradas do usuário

livros=20
novos_livros=0
print("Digite quantos livros você deseja adicionar à biblioteca")
novos_livros=int(input())
livros=livros+novos_livros

livros = str(livros)
texto=f"Você possui {livros} livros na sua biblioteca"
print(texto)

