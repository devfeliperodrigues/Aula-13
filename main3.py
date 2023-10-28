class Pessoa:
    def __init__(self, nome:str, rg:int, cpf:str, telefone:int, endereco:str):
        self.__nome = nome
        self.__rg = rg
        self.__cpf = cpf
        self.__telefone = telefone
        self.__endereco = endereco

    def informacoes(self):
        return f"""
            Nome: {self.__nome}
            RG: {self.__rg}
            CPF: {self.__cpf}
            Telefone: {self.__telefone}
            Endereço: {self.__endereco}
        """
    def getNome(self):
        return self.__nome
    
    def getRG(self):
        return self.__rg
    
    def getTelefone(self):
        return self.__telefone
    
    def getEndereco(self):
        return self.__endereco
    
    def getCPF(self):
        return self.__cpf
    
    def setNome(self,novo_nome):
        self.__nome = novo_nome
        return self.__nome
    
    def setCpf(self,novo_cpf):
        self.__cpf = novo_cpf
        return self.__cpf
    
    def setRg(self,novo_rg):
        self.__rg = novo_rg
        return self.__rg
    
    def setTelefone(self,novo_telefone):
        self.__telefone = novo_telefone
        return self.__telefone
    
    def setEndereco(self,novo_endereco):
        self.__endereco = novo_endereco
        return self.__endereco



abel = Pessoa(nome="Abelardo", rg=123, cpf=456, telefone=789, endereco="A")

abel.cpf = "Algodão Doce"

print(abel.informacoes())
