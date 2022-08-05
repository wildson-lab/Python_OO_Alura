from conta import Conta

conta1 = Conta(123, "Nico", 55.5, 1000.0)

print(conta1.titular)
print(conta1.saldo)
print(conta1.limite)
conta1.limite = 10000.0
print(conta1.limite)
