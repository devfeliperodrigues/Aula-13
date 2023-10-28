"""Faça um programa que contenha 3 classes: Carro,
barco e avião, eles possuem 3 atributos:
Nome_do_veiculo, Quantidade_de_motores e
tem_rodas, e um método chamado buzinar, o
método buzinar da classe carro deve retornar
"Biiiii",

da classe barco:
"Foooom"
e avião:
"Tem buzina?"
Crie uma instância para cada classe e imprime na
tela todas as informações de cada um."""

class Veiculo:
    def __init__(self, nome_do_veiculo, quantidade_de_motores, tem_rodas):
        self.nome_do_veiculo = nome_do_veiculo
        self.quantidade_de_motores = quantidade_de_motores
        self.tem_rodas = tem_rodas
    
    def som(self):
        return "Som Indefinido"

class Carro(Veiculo):
    def __init__(self, quantidade_de_motores, tem_rodas):
        super().__init__(self, nome_do_veiculo="Carro", quantidade_de_motores=quantidade_de_motores, tem_rodas=tem_rodas)
    def som(self):
        return "Biiiiiiiii"
       
class Barco(Veiculo):
    def __init__(self, quantidade_de_motores, tem_rodas):
        super().__init__(self, nome_do_veiculo="Barco", quantidade_de_motores=quantidade_de_motores, tem_rodas=tem_rodas)
    def som(self):
        return "Fooooooommmmm"
    
class Aviao(Veiculo):
    def __init__(self, quantidade_de_motores, tem_rodas):
        super().__init__(self, nome_do_veiculo="Avião", quantidade_de_motores=quantidade_de_motores, tem_rodas=tem_rodas)
    def som(self):
        return "Tem buzina?"      


Carro1 = Carro(quantidade_de_motores=1, tem_rodas=True)

Barco1 = Barco(quantidade_de_motores=2, tem_rodas=False)

Aviao1 = Aviao(quantidade_de_motores=2, tem_rodas=True)

print(Carro1.som())
print(Barco1.som())
print(Aviao1.som())

