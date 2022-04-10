# atividade_conta_AC2
# Email Impacta: roger.kechichian@aluno.faculdadeimpacta.com.br


class Conta:

    def __init__(self, titular, agencia, numero, saldo_inicial):
       
        self.__titular = titular
        self.__agencia = agencia
        self.__numero = numero
        self.__saldo = saldo_inicial
        self.__ativa = False
        self.__operacoes = [('saldo inicial', saldo_inicial)]

    @property
    def titular(self):
        
        return self.__titular

    @property
    def agencia(self):
       
        return self.__agencia

    @property
    def numero(self):
        
        return self.__numero

    @property
    def saldo(self):
       
        return self.__saldo

    @property
    def ativa(self):
        
        return self.__ativa

    @ativa.setter
    def ativa(self, situacao):
       
        if (isinstance(situacao, bool)):
            self.__ativa = situacao

    def depositar(self, valor):
        
        if (self.__ativa and valor > 0):
            self.__saldo += valor
            self.__operacoes.append(('deposito', valor))
            return 'Efetuado!'

        if (not self.__ativa):
            return 'Conta inativa.'
        else:
            return 'Valor negativo.'

    def sacar(self, valor):
        
        if (self.__ativa and 0 < valor <= self.__saldo):
            self.__saldo -= valor
            self.__operacoes.append(('saque', valor))
            return 'Efetuado sucesso!'

        if (not self.__ativa):
            return 'Conta inativa.'
        else:
            return 'Saldo insuficiente.'

    def transferir(self, conta_destino, valor):
        
        if (self.__ativa and conta_destino.ativa and 0 < valor <= self.__saldo):
            self.__saldo -= valor
            self.__operacoes.append(('transferencia', valor))
            conta_destino.depositar(valor)
            return 'Transferência confirmada!'

        if (not self.__ativa):
            return 'Conta inativa.'

        elif (not conta_destino.ativa):
            return 'Conta inativa'

        else:
            return 'Saldo insuficiente.'

    def tirar_extrato(self):
       
        return self.__operacoes
