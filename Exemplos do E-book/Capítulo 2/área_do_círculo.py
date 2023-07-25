#Faça um programa que calcule a área de um círculo de acordo com o raio informado pelo usuário

PI=3.14
raio=0
área_do_círculo=0

print("Digite o raio do círculo que deseja calcular a área")
raio=int(input())

área_do_círculo=PI*(raio*raio)

print(f"A área do cículo é: {área_do_círculo}")