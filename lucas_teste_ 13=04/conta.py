class Conta:
    def __init__(self, numero, titular, saldo, limite = 1000.0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Saldo: {self.__saldo} do titular {self.__titular}")

    def depositar(self, valor):
        if(valor < 0):
            print("Valores negativos não podem ser depositados")
        else:
            self.__saldo += valor

    def sacar(self, valor):
        if(self.__saldo < valor):
            print("Saldo insuficiente")
        else:
            self.__saldo -= valor

    def transferir(self, valor, destino):
        if(self.__saldo < valor) or (valor < 0):
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
        return self.__limite
    
    @property
    def get_numero(self):
        return self.__numero
    

    #metudos para manipular os valores da  
    
    @limite.setter
    def set_limite(self,limite):
        self.__limite = limite


    