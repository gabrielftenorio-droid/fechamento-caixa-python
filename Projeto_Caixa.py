print("=========================================")
print("  SISTEMA SIMPLES DE FECHAMENTO DE CAIXA ")
print("=========================================")

# Variáveis para acumular os totais do dia
total_recolhido = 0.0
total_esperado = 0.0

# Cadastro de funcionários
continuar = "S"
while continuar.upper() == "S":

    print("\n--- Novo Cadastro ---")
    nome = input("Digite o nome do funcionário: ")
    valor_recolhido = float(input(f"Quanto {nome} recolheu em dinheiro? R$ "))
    valor_esperado = float(input(f"Qual era o valor esperado no sistema? R$ "))

    # Somando aos totais gerais
    total_recolhido = total_recolhido + valor_recolhido
    total_esperado = total_esperado + valor_esperado

    # Calculando a situação do funcionário
    diferenca = valor_recolhido - valor_esperado

    print("\n-----------------------------------------")
    if diferenca == 0:
        print(f"Resultado para {nome}: TUDO CERTO!")
    elif diferenca < 0:
        print(f"Resultado para {nome}: [ALERTA] Falta de R$ {abs(diferenca):.2f} no caixa.")
    else:
        print(f"Resultado para {nome}: [AVISO] Sobra de R$ {diferenca:.2f} no caixa.")
    print("-----------------------------------------")

    # CADASTRAR OUTRO FUNCIONÁRIO
    continuar = input("Deseja cadastrar outro funcionário? (S/N): ")

# =========================================
#   RELATÓRIO FINAL (SAÍDA NA TELA)
# =========================================
print("\n=========================================")
print("          BALANÇO GERAL DO DIA           ")
print("=========================================")
print(f"Total Geral Recolhido: R$ {total_recolhido:.2f}")
print(f"Total Geral Esperado:  R$ {total_esperado:.2f}")

balanco_final = total_recolhido - total_esperado

if balanco_final == 0:
    print("Situação Geral: Tudo batendo perfeitamente!")
elif balanco_final < 0:
    print(f"Situação Geral: Prejuízo/Quebra total de R$ {abs(balanco_final):.2f}")
else:
    print(f"Situação Geral: Superávit/Sobra total de R$ {balanco_final:.2f}")
print("=========================================")
