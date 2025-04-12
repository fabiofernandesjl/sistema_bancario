# Função para ação de depositar na conta
def deposit_function(bank_balance, bank_statement, count_transaction ,/):
    print("\n_____________________________________________________\n")
    user_deposit = float(input("Informe o valor do depósito: "))
    
    if(user_deposit <= 0):
        print("Valor informado inválido! Tente novamente.")
        return bank_balance, bank_statement
    
    deposit_confirm = operation_confirm()
    
    if(deposit_confirm == "1"):
        bank_balance += user_deposit
        count_transaction += 1
        bank_statement.append(f"Depósito: R$ {user_deposit:.2f}") # Adiciona o depósito feito no array de extrato
        print(f"\nDepósito concluído!")
        return bank_balance, bank_statement, count_transaction
    else:
        # new_operation()
        print("Operação cancelada.")
        return bank_balance, bank_statement, count_transaction
        
    


def withdrawal_function(*, withdrawal_limit, withdrawal_daily_limit, bank_balance, count_withdrawal, bank_statement, count_transaction ):
    # Função para efetuar saque da conta do usuário.
    print("\n_____________________________________________________\n")
    user_withdrawal = float(input("Informe o valor para realizar o saque: "))
    
    if(user_withdrawal <= 0):
        print("Valor informado inválido! Tente novamente.")
        return bank_balance, bank_statement, count_withdrawal, count_transaction

    
    if(user_withdrawal > withdrawal_limit): # Verifica se o valor informado está dentro do limite de saque.
        print("\nNão foi possivel realizar o saque!\nValor informado acima do limite de saque.")
        return bank_balance, bank_statement, count_withdrawal, count_transaction
        
        
    elif(count_withdrawal >= withdrawal_daily_limit):  # Verifica se o usuário atingiu o limite diário de saque.
        print("\nNão foi possivel realizar o saque!\nVocê atingiu o limite diario de saque.")
        return bank_balance, bank_statement, count_withdrawal,count_transaction

        
    elif(user_withdrawal > bank_balance): # Verifica se o usuário tem saldo suficiente para realizar o saque.
        print(f"\nSaldo insuficiente!")
        return bank_balance, bank_statement, count_withdrawal, count_transaction
    

    else:
        withdrawal_confirm = operation_confirm()
        
        if(withdrawal_confirm == "1"):
            bank_balance -= user_withdrawal
            count_withdrawal += 1
            count_transaction += 1
            bank_statement.append(f"Saque: R$ {user_withdrawal:.2f}") # Adiciona o saque efetuado no array de extrato
            print("\nsaque realizado com sucesso!")
            return bank_balance, bank_statement, count_withdrawal, count_transaction
        
        else: 
            print("\nOperação cancelada.")
            return bank_balance, bank_statement, count_withdrawal, count_transaction
            

def statement_function(bank_balance, /, *, bank_statement):
    print("\n________________________ EXTRATO _____________________________\n")
    print("Nenhuma movimentação efetuada." if not bank_statement else "\n".join(bank_statement))
    print(f"\nSaldo: R$ {bank_balance:.2f}")
    

def operation_confirm():
    option_chosen = input("\nVocê confirma a operação?\n1. Sim\n2. Não\n\n")
    
    return option_chosen


# def count_transaction_limit(count_transaction, transaction_daily_limit):
#     if (count_transaction > transaction_daily_limit):
#         print("você atingiu o limite de transações diárias!")

def main():
    MENU = """
    \n0. Encerrar
    \n1. Saque
    \n2. Depósito
    \n3. Extrato
    \n"""


    bank_balance, count_withdrawal, count_transaction = 0, 0, 0
    bank_statement = []   # Array para armezenar valores para imprimir extrato
    WITHDRAWAL_LIMIT = 500   # Valor limite de saque.
    WITHDRAWAL_DAILY_LIMIT = 3    # quantidade limite de saque diário.
    TRANSACTION_DAILY_LIMIT = 10  # Limite de transações diárias.
        
    while(True):
        # Loop infinito para escolha das operações. O loop só irar para caso o usuário digite 0 ou um caractere ou número inválido.
        chosen_operation = input(f"""
                                \n_____________________________________________________
                                \nOlá!
                                \nEscolha qual operação você deseja reliazar:
                                \n{MENU}
                                \n""")
        
        if(chosen_operation == "1"):
            if (count_transaction >= TRANSACTION_DAILY_LIMIT):
                print("você atingiu o limite de transações diárias!")
                continue
            
            bank_balance, bank_statement, count_withdrawal, count_transaction = withdrawal_function(withdrawal_limit=WITHDRAWAL_LIMIT,
                                                                                withdrawal_daily_limit=WITHDRAWAL_DAILY_LIMIT,
                                                                                bank_balance=bank_balance,
                                                                                count_withdrawal=count_withdrawal,
                                                                                count_transaction=count_transaction,
                                                                                bank_statement=bank_statement)
            
            
        elif(chosen_operation == "2"):
            if (count_transaction >= TRANSACTION_DAILY_LIMIT):
                print("você atingiu o limite de transações diárias!")
                continue
            
            bank_balance, bank_statement, count_transaction = deposit_function(bank_balance, bank_statement, count_transaction)
            
            
        elif(chosen_operation == "3"):
            statement_function(bank_balance, bank_statement = bank_statement)
            
            
        elif(chosen_operation == "0"):
            print("Sessão finalizada! Até logo...")
            break
        
        
        else: 
            print("Não consegui identificar essa opção. Selecione novamente a opção correta.")
        
        

main()