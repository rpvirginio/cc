class Cliente:
    def __init__(self, nome, cpf, endereco, telefone):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone

    def __str__(self):
        return f"Cliente: {self.nome} | CPF: {self.cpf} | Endereço: {self.endereco} | Telefone: {self.telefone}"


class ContaBancaria:
    def __init__(self, numero, cliente, saldo=0):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de {valor} realizado com sucesso. Novo saldo: {self.saldo}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de {valor} realizado com sucesso. Novo saldo: {self.saldo}")
        else:
            print("Saldo insuficiente.")

    def transferir(self, destino, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            destino.saldo += valor
            print(f"Transferência de {valor} para conta {destino.numero} realizada com sucesso.")
        else:
            print("Saldo insuficiente.")

    def __str__(self):
        return f"Conta: {self.numero} | Cliente: {self.cliente.nome} | Saldo: {self.saldo}"
    
    
   
cliente1 = Cliente("Rodrigo Virginio", "123.456.789-00", "Rua R, 111", "(11) 90000-0000")
cliente2 = Cliente("Maria Santos", "987.654.321-00", "Rua Z, 222", "(11) 12345-6789")


conta1 = ContaBancaria("001", cliente1, 1000)
conta2 = ContaBancaria("002", cliente2, 500)


conta1.depositar(500)
conta2.sacar(200)
conta1.transferir(conta2, 300)


print(conta1)
print(conta2)