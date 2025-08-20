from Antivilão import AntiVilao

class GerenciadorAntiViloes:
    def __init__(self):
        self.lista = []

    def adicionar(self, nome, armamento, fraqueza):
        antivilao = AntiVilao(nome, armamento, fraqueza)
        self.lista.append(antivilao)
        return antivilao

    def remover(self, nome):
        for av in self.lista:
            if av.nome == nome:
                self.lista.remove(av)
                return f"{nome} removido com sucesso."
        return f"AntiVilão {nome} não encontrado."

    def editar(self, nome, novo_armamento=None, nova_fraqueza=None):
        for av in self.lista:
            if av.nome == nome:
                av.atualizar(novo_armamento, nova_fraqueza)
                return f"{nome} atualizado com sucesso."
        return f"AntiVilão {nome} não encontrado."

    def buscar(self, nome):
        for av in self.lista:
            if av.nome == nome:
                return av
        return None

    def contar(self):
        return len(self.lista)

    def listar(self):
        return [av.descricao() for av in self.lista]
