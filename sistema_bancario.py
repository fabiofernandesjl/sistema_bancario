MENU = """
0. Encerrar
1. Saque
2. Depósito
3. Extrato
"""

OPERATION_CONFIRM = """
Confirmar operação?
1. Sim
2. Não
"""

bank_balance, count_withdrawal = 0, 0
bank_statement = []   # Array para armezenar valores para imprimir extrato
WITHDRAWAL_LIMIT = 500   # Valor limite de saque.
DAILY_LIMIT = 3    # quantidade limite de saque diário.

# Função para ação de depositar na conta
def deposit_function():
    global bank_balance
    print("\n_____________________________________________________\n")
    user_deposit = float(input("Informe o valor do depósito: "))
    
    if(user_deposit <= 0):
        print("Valor informado inválido! Tente novamente.")
        deposit_function()
    
    deposit_confirm = input(f"""
                            \nVocê está depositando R$ {user_deposit:.2f} na sua conta.
                            \n{OPERATION_CONFIRM}
                            \n""")
    
    if(deposit_confirm == "1"):
        bank_balance += user_deposit
        bank_statement.append(f"Depósito: R$ {user_deposit:.2f}") # Adiciona o depósito feito no array de extrato
        print(f"\nDepósito concluído!")
        return bank_balance
    else:
        # new_operation()
        print("Operação cancelada.")


def withdrawal_function():
    # Função para efetuar saque da conta do usuário.
    global bank_balance
    global count_withdrawal
    print("\n_____________________________________________________\n")
    user_withdrawal = float(input("Informe o valor para realizar o saque: "))
    
    if(user_withdrawal <= 0):
        print("Valor informado inválido! Tente novamente.")
        withdrawal_function()
    
    if(user_withdrawal > WITHDRAWAL_LIMIT): # Verifica se o valor informado está dentro do limite de saque.
        print("\nNão foi possivel realizar o saque!\nValor informado acima do limite de saque.")
        withdrawal_function()
    elif(count_withdrawal >= DAILY_LIMIT):  # Verifica se o usuário atingiu o limite diário de saque.
        print("\nNão foi possivel realizar o saque!\nVocê atingiu o limite diario de saque.")
    elif(user_withdrawal > bank_balance): # Verifica se o usuário tem saldo suficiente para realizar o saque.
        print(f"\nSaldo insuficiente!")
    else:
        withdrawal_confirm = input(f"Você está sacando R$ {user_withdrawal:.2f} da sua conta.\n{OPERATION_CONFIRM}")
        if(withdrawal_confirm == "1"):
            bank_balance -= user_withdrawal
            count_withdrawal += 1
            bank_statement.append(f"Saque: R$ {user_withdrawal:.2f}") # Adiciona o saque efetuado no array de extrato
            print("\nsaque realizado com sucesso!")
            return count_withdrawal, bank_balance
        else: 
            print("\nOperação cancelada.")
            

def statement_function():
    print("\n________________________ EXTRATO _____________________________\n")
    print("Nenhuma movimentação efetuada." if not bank_statement else "\n".join(bank_statement))
    print(f"\nSaldo: R$ {bank_balance:.2f}")
    


while(True):
    # Loop infinito para escolha das operações. O loop só irar para caso o usuário digite 0 ou um caractere ou número inválido.
    chosen_operation = input(f"""
                             \n_____________________________________________________
                             \nOlá!
                             \nEscolha qual operação você deseja reliazar:
                             \n{MENU}
                             \n""").strip()
    
    if(chosen_operation == "1"):
        withdrawal_function()
        continue
    elif(chosen_operation == "2"):
        deposit_function()
        continue
    elif(chosen_operation == "3"):
        statement_function()
        continue
    elif(chosen_operation == "0"):
        print("Sessão finalizada! Até logo...")
        break
    else: 
        print("Não consegui identificar essa opção. Selecione novamente a opção correta.")
        break