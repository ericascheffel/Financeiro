"""Esta programação calcula os descontos de INSS, descontos com dependentes
e o valor devedor ao Imposto de Renda"""

#Calcula o INSS

salario = in (input("digite o valor do salario Bruto"))

def INSS (salario, Desc_INSS):
    return (salario * 20 / 100)

print ("O desnconto de INSS é: " , INSS (salario , Desc_INSS))
