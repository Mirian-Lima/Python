
salario = float(input("Digite o seu salário: "))
if salario < 1250:
    aumento = 10 
    print("Su salário antigo é",salario,"\nVocê ganhou 10% de aumento\nO valor do pagamento é: ",salario + (salario * aumento / 100))
    #("O aumento é: ",aumento)
if salario > 1250:
    aumento2 = 15 
    print("Seu salário antigo é: ",salario,"\nVocê ganhou 15% de aumento!\nO valor do pagamento é: ",salario + (salario * aumento2 / 100))
    #print("Parabéns salario aumentou",aumento)

