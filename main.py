from conta import Conta

conta1 = Conta(123, "Nico", 55.5, 1000.0)

print(conta1.get_titular())
print(conta1.get_saldo())
print(conta1.get_limite())
conta1.set_limite(10000.0)
print(conta1.get_limite())
