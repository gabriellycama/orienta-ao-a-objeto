class Conta:
    def __init__(self, numero, titular, saldo, limite = 1000.0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite_especial = limite
        self.__codigo_banco = '001'

    def extrato(self):
        print(f"Saldo: {self.__saldo} do titular {self.__titular}")

    def depositar(self, valor):
        if(valor < 0):
            print("Valores negativos não podem ser depositados")
        else:
            self.__saldo += valor

    def __saque_permitido(self,valor_saque):
        valor_disponivel_saque = self.__saldo + self.__limite_especial 
        return valor_saque <= valor_disponivel_saque

    def sacar(self, valor):
        if (self.__saque_permitido(valor)):
            print("Saldo insuficiente")
            self.__saldo -= valor
        else:
            print(f"o valor {valor} passou do limite")


    

    def transferir(self, valor, destino):
        if(self.__saldo < valor) or (valor <= 0):
            print("Não é possível realizar a tranferência")
        else:
            self.sacar(valor)
            destino.depositar(valor)

    #Métodos apenas para retornar o valor das propriedades
    def get_saldo(self):
        return self.__saldo
    
    @property
    def get_titular(self):
        return self.__titular
    
    @property
    
    def get_limite(self):
        return self.__limite_especial
    
    @property
    def get_numero(self):
        return self.__numero
    

    @property
    def get_numero(self):
        return self.__codigo_banco

    #metudos para manipular os valores da  
    @staticmethod
    def codigo_banco():
        return '001'
    
    def set_limite(self,limite):
        self.__limite_especial = limite

    @staticmethod
    def codigos_bancos():
        return {'BB':'001','caixa':'104','bradesco':'237'}
    