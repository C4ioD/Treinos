from datetime import datetime
import pytz

class ContaCorrente:

    def __init__(self, nome, conta, cpf , agencia):
        self.nome = nome
        self.cpf = cpf
        self.agencia = agencia
        self.conta = conta
        self.saldo = 0
        self.limite = None
        self.historico = [] 

    @staticmethod
    def _data_hora():
        data_hora = datetime.today()
        return data_hora.strftime("%d/%m/%Y %H:%M:%S")


    def _limite_conta(self):
        self.limite = -1000
        return self.limite

    def saldo_conta(self):
        print(f"Saldo atual: R$ {self.saldo}")

    def depositar(self, valor):
        self.saldo += valor
        self.historico.append((valor, self.saldo, ContaBanco._data_hora()))

    def sacar (self, valor):
        if self.saldo < self._limite_conta():
            print('Saldo insuficiênte em conta')
        else:
            self.saldo -= valor
            self.historico.append((-valor,self.saldo,ContaBanco._data_hora()))
    
    def extrato(self):
        for i in self.historico:
            print(i)

    def transferir(self,valor, conta_destino):
        if self.saldo < -1000:
            print('Você não possui saldo suficiente para realizar a trasnferência')
        else:
            self.saldo -= valor
            self.historico.append((-valor,self.saldo,ContaBanco._data_hora()))
            conta_destino.saldo += valor
            conta_destino.historico.append((valor,self.saldo,ContaBanco._data_hora()))


