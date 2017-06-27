from atvdd import Aluno
class equipe:
    def __int__(self,projeto):
        self.projeto = projeto
        self.lista = []

    def getProjeto(self):
        return self.projeto

    def cadastrarA(self,nome,cpf):
        j = Aluno(nome,cpf)
        self.lista.append(j)

    def removerA(self,cpf):
        aluno = self.procuraA(cpf)
        if aluno == None:
            return

        else:
            self.lista.remove(aluno)
    def imprimir(self):
        for i in range (len(self.lista)):
            print "Aluno: %s \n CPF: %i" % (self.lista[i].getNome(), self.lista[i].getCpf())

    def procuraA(self,cpf):
        for i in range(len(self.lista)):
            if self.lista[i].getNome() == cpf:
                return self.lista[i]

        return None
    def informacao(self):

        print "Nome da equipe: %s " % (self.getProjeto())
        print "Lista de alunos: "
        for i in range(len(self.lista)):
            print "%s" % (self.lista[i].getNome())



