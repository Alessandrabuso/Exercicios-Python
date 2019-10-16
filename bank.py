class Clientes():
    registro = None
    nome = None
    ctype = None

    def __init__(self, res, nam, type):
        self.registro = res
        self.nome = nam
        self.ctype = type

class Conta():
    saldo = None

    def __init__(self, sd):
        self.saldo = sd

class Transacao(Clientes, Conta):

    def __init__(self,  res, nam, type, sd):
        Clientes.__init__(self, res, nam, type)
        Conta.__init__(self, sd)

    def confirmid(self):
        print(self.registro)
        print(self.nome)
        print(self.ctype)

    def saque(self, value):
        self. saldo -=  value
        print("Você realizou um saque de", value)

    def deposito(self,value):
        self.saldo += value
        print("Você realizou um depósito de", value)
    def sald0 (self):
        print("Seu saldo atual é de:", self.saldo)


trs = Transacao(12345678, 'Alessandra', 'corrente', 0)
trs.confirmid()
trs.deposito(1234)
trs.sald0()
trs.saque(34)
trs.sald0()