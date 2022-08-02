def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor


def saca(conta, valor):
    conta["saldo"] -= valor


def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))


conta = cria_conta(123, "Wildson", 1200.00, 3600.00)
extrato(conta)
deposita(conta, 1500.00)
saca(conta, 300)
extrato(conta)

