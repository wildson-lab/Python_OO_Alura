def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta


print(cria_conta(123, "Wildson", 1200.00, 3600.00))
