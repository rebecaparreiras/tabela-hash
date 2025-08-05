from .tabela_hash import TabelaHash
from .dados_estados import estados

def main():
    tabela_hash = TabelaHash()

    print("Tabela Hash (antes das inserções):")
    tabela_hash.imprimir()

    for sigla, nome in estados:
        tabela_hash.inserir(sigla, nome)

    print("\nTabela Hash (após inserir os 27 estados):")
    tabela_hash.imprimir()

    tabela_hash.inserir("RP", "Rebeca Parreiras")

    print("\nTabela Hash (após inserir os 27 estados + RP):")
    tabela_hash.imprimir()

if __name__ == "__main__":
    main()
