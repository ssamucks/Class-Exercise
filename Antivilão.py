class AntiVilao:
    def __init__(self, nome, armamento, fraqueza):
        self.nome = nome
        self.armamento = armamento
        self.fraqueza = fraqueza

    def descricao(self):
        return f"AntiVilão: {self.nome}, Armamento: {self.armamento}, Fraqueza: {self.fraqueza}"

    def ataque(self):
        return f"{self.nome} ataca usando {self.armamento}!"

    def defesa(self):
        return f"{self.nome} se defende contra o ataque!"

    def atualizar(self, armamento=None, fraqueza=None):
        if armamento:
            self.armamento = armamento
        if fraqueza:
            self.fraqueza = fraqueza