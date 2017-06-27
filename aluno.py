class Aluno:
    def __int__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf

    def getNome(self):
        return self.nome

    def getCpf (self):
        return self.cpf
    def setNome(self,novoNome):
        self.nome = novoNome

    def setCpf(self,novoCpf):
        self.cpf = novoCpf