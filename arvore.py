from typing import Optional


class No:
    def __init__(self, dado: int, filho_esquerdo=None, filho_direito=None):
        self.dado = dado
        self.filho_esquerdo = filho_esquerdo
        self.filho_direito = filho_direito


def inserir(no: No, dado: int):
    # ir para esquerda
    if dado <= no.dado:
        if no.filho_esquerdo is None:
            no.filho_esquerdo = No(dado)
            return

        inserir(no.filho_esquerdo, dado)

    # ir para direita
    else:
        if no.filho_direito is None:
            no.filho_direito = No(dado)
            return

        inserir(no.filho_direito, dado)


def buscar(no: No, dado: int) -> Optional[No]:
    if no is None:
        return None

    if no.dado == dado:
        return no

    # ir para a esquerda
    if dado <= no.dado:
        return buscar(no.filho_esquerdo, dado)

    # ir para a direita
    return buscar(no.filho_direito, dado)


def contem(no: No, dado: int) -> bool:
    return buscar(no, dado) is not None


def imprimir_pre_ordem(no: No, nivel: int = 0):
    prefixo: str = ' ' * nivel

    if no is None:
        print(f'{prefixo}[]')
        return

    print(f'{prefixo}[{no.dado}]')
    imprimir_pre_ordem(no.filho_esquerdo, nivel + 4)
    imprimir_pre_ordem(no.filho_direito, nivel + 4)


# NOTA este metodo assume que o GC do intepretador consegue liberar ciclos inalcançáveis
def remover(no: No, dado: int) -> Optional[No]:
    if no is None or no.dado == dado:
        return None

    # ir para a esquerda
    if dado <= no.dado:
        no.filho_esquerdo = remover(no.filho_esquerdo, dado)
        return no

    # ir para a direita
    no.filho_direito = remover(no.filho_direito, dado)
    return no


