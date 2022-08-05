from conta import Conta

conta1 = Conta(123, "Nico", 55.5, 1000.0)
conta2 = Conta(321, "Marco", 100.0, 1000.0)

# Agora essa parte não está mais acessível, pois os atributos foram encapsulados.
# print(conta1.titular)
# print(conta1.saldo)

conta1.extrato()
conta2.extrato()
conta1.transfere(10.0,conta2)
conta1.extrato()
conta2.extrato()
