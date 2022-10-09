soma = 1
subtracao = 2
multiplicacao = 3
divisao = 4
usuario = int(input("Digite 1/2/3/4:"))
numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite o segundo número: "))
while soma != usuario:
    if usuario == soma:
        print("Opção inválida")
    break
else:
    print("A soma é:",numero_1+numero_2)

while subtracao != usuario:
    if usuario == subtracao:
        print("Opção inválida")
    break    
else:
    print("A subtração é: ",numero_1 - numero_2)
while multiplicacao != usuario:    
    if usuario == multiplicacao:
        print("Opção inválida")
    break    
else:
    print("A multiplicação é:",numero_1  * numero_2)
while divisao != usuario:
    if usuario == divisao:
        print("Opção inválida")
    break    
else:
    print("A divisão é: ",numero_1 // numero_2)







