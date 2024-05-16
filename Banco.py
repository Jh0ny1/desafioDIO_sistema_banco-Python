menu = """
[0] Home
[1] Depositar
[2] Sacar
[3] Extrato



=> """

saldo = 0
extrato = ""
nsaques = 0
Lsaque = 500
Lsaques = 3


while True:
    opcao = input(menu)
    if opcao == "1":
        valor = float(input("Informe o Valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print ("Valor inválido")
    
    elif opcao == "2":
            valor = float(input("Informe o Valor a ser sacado: "))

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > Lsaque

            excedeu_saques = nsaques > Lsaques

            if excedeu_saldo:
                print(f"Saldo Insuficiente, seu Saldo autal é {saldo}.")
            
            elif excedeu_saques:
                print(f"Você execedeu o limite de R${Lsaque}")
            
            elif excedeu_saques:
                print(f"Você ultrapassou o limite de {Lsaque} saques hoje.")
            
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n, confirmado"
                nsaques += 1
            
            else:
                print("Valor inválido, tente denovo.")
    
    elif opcao == "3":
        print("\n==================  EXTRATO  ==================")
        print("Não foram realizadas movimentações ainda" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==================================================")
    elif opcao == "0":
        break
    
    else:
        print("Operação Inválida, tente novamente.")