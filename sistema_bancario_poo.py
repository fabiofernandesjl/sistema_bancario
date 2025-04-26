from abc import ABC, abstractmethod
from datetime import datetime, date

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor: float):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
        
    def registrar(self, conta):
        if conta.depositar(self._valor):
            conta._historico.adicionar_transacao(self)
            pass

class Saque(Transacao):
    def __init__(self, valor: float):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        if conta.sacar(self._valor):
            conta._historico.adicionar_transacao(self)
            pass

class Historico:
    def __init__(self):
        self._historico = []
        
    @property
    def historico(self):
        return self._historico
        
    def adicionar_transacao(self, transacao):
        self._historico.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y, %H-%M-%S"),
        })
        


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0.0  # O saldo inicial é igual a zero
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
        
        
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    
    def sacar(self, valor):
        
        if valor <= 0:
            print("Valor inválido! Tente novamente...")
            return False
        elif valor > self._saldo:
            print("Saldo insuficiente! Tente novamente...")
            return False
        else:
            self._saldo -= valor
            print("Saque efetuado com sucesso!")
            return True
        
    def depositar(self, valor):
        if valor <= 0:
            print("Valor informado Inválido!")
            return False     
        else:
            self._saldo += valor
            print("Valor depositado com sucesso!")
            return True    
    
    def exibir_historico(self):
        print(f"Extrato da conta {self._numero}")
        print("-" * 50)
        
        if not self._historico.historico:
            print("\nNenhuma transação foi efetuada ainda...")
        else:
            for transacao in self._historico.historico:
                print(f"tipo: {transacao["tipo"]}")
                print(f"valor: R$ {transacao["valor"]}")
                print(f"data: {transacao["data"]}")
                print("-" * 50)
        
        return
        
        
    @staticmethod
    def nova_conta(cliente, numero):
        return Conta(numero, cliente)
        

class ContaCorrente(Conta):
    def __init__(self, numero, cliente):
        super().__init__(numero, cliente)
        self.limite = 500.0
        self.limite_saques = 3
    
    
    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self._historico._historico if transacao["tipo"] == Saque.__name__])
        
        if numero_saques == self.limite_saques:
            print("Você já atingiu o limite de saque diário!")
            return False    
        elif valor > self.limite:
            print("Valor informado excedeu o limite permitido! Tente novamente...")
            return False
        else:
            return super().sacar(valor)



class Cliente:
    def __init__(self, endereco, contas=None):
        self.endereco = endereco
        self.contas = [] if contas is None else contas
        
        
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
        pass
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)
   

class PessoaFisica(Cliente): # Herda da classe cliente
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self._cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento




cliente = PessoaFisica("12345678900", "Clodenilson", date(1998, 3, 25), "Avenida Bandeira, 98")

conta = ContaCorrente.nova_conta(cliente, 1001)
cliente.adicionar_conta(conta)

print(conta.exibir_historico())

deposito = Deposito(500.0)
cliente.realizar_transacao(conta, deposito)

saque = Saque(200.00)
cliente.realizar_transacao(conta, saque)


print(f"Seu saldo é de {conta.saldo:.2f}")

saque2 = Saque(100.0)
cliente.realizar_transacao(conta, saque2)

deposito2 = Deposito(400.0)
cliente.realizar_transacao(conta, deposito2)

print(conta.exibir_historico())
print(f"Seu saldo é de {conta.saldo:.2f}")