from .nodo import Nodo

class TabelaHash:
    def __init__(self):
        self.tabela = [None] * 10  # cria 10 posições iniciando com None

    def funcao_hash(self, sigla):
        if sigla == "DF":
            return 7
        else:
            char1 = ord(sigla[0])
            char2 = ord(sigla[1])
            return (char1 + char2) % 10

    def inserir(self, sigla, nome):
        posicao = self.funcao_hash(sigla)
        novo_nodo = Nodo(sigla, nome)
        novo_nodo.proximo = self.tabela[posicao]
        self.tabela[posicao] = novo_nodo

    def imprimir(self):
        for i in range(10):
            print(f"{i}:", end=" ")
            atual = self.tabela[i]
            if atual is None:
                print("None")
            else:
                while atual is not None:
                    print(f"{atual.sigla}->", end="")
                    atual = atual.proximo
                print("None")
