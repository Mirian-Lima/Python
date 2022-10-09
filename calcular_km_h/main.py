velocidade = float(input("Qual a velocidade do carro: "))
placa = str(input("Digite o número da placa: "))
if velocidade > 80:
    multa = 5
    velocidade = (velocidade - 80) * multa
    print("Você ultrapassou a velocidade!\nO valor da multa é:",velocidade,"\nNúmero do veículo multado",placa)
else:
    print("Dirija com cuidado!\nVeículo sem multa",placa)
    




