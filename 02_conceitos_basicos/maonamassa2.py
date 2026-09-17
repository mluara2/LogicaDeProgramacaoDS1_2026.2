# TODO: Desenvolva seu algoritmo aqui
# 1. Leia o valor da conta (float)
# 2. Leia o número de pessoas (int)
# 3. Calcule o valor por pessoa
# 4. Imprima formatado usando f-string

valor_da_conta = float(input("digite o valor da conta"))
numero_de_pessoas = int(input("digite o numero de pessoas"))
valor_final = valor_da_conta/numero_de_pessoas
print(f"cada um ira pagar , {valor_final:.2f}")
