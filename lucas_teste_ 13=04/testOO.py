numero = 123
titular = "gabrielly"
saldo = 105.5
limite = 1000.0

conta = {"numero":123, "titular":"gabrielly",
        "saldo":105.5, "limites":1000.0

}


def criar_conta(numero,titular,saldo,limite):
    conta = {"numero":numero, "titular":titular,
         "saldo":saldo, "limite":limite

    }

    return conta

conta = criar_conta(345,"camile",200.0,1000.0)
print(conta["limite"])

def depositar(conta, valor):
    conta["saldo"] += valor

def sacar(conta, valor):
    conta["saldo"] -=valor

def extrato(conta):
    print(f"seu saldo atual e {conta["saldo"]}")

depositar(conta, 250.0)
extrato(conta)
sacar(conta,200)
extrato(conta)