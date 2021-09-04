x=int(input("Digite um número de 4 algarismos: "))
milhar=x//1000
resto=x%1000
centena=resto//100
resto=resto%100
dezena=resto//10
unidade=resto%10
print("Seu milhar é:",milhar)
print("Sua centena é:",centena)
print("Sua dezena é:",dezena)
print("E sua unidade é:",unidade)