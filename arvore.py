from typing import Optional

class No:
    def __init__(self, dado: int, filho_esquerdo=None, filho_direito=None):
        self.dado = dado
        self.filho_esquerdo = filho_esquerdo
        self.filho_direito = filho_direito


def inserir(no: No, dado: int) -> No:
    if no is None:
        return No(dado)

    # ir para esquerda
    if dado <= no.dado:
        if no.filho_esquerdo is None:
            no.filho_esquerdo = No(dado)
            return no

        return inserir(no.filho_esquerdo, dado)

    # ir para direita
    if no.filho_direito is None:
        no.filho_direito = No(dado)
        return no

    return inserir(no.filho_direito, dado)


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
def remover_subtree(no: No, dado: int) -> Optional[No]:
    """Remove toda a subarvore a partir do primeiro nó encontrado cujo valor é igual ao dado informado
    """
    if no is None or no.dado == dado:
        return None

    # ir para a esquerda
    if dado <= no.dado:
        no.filho_esquerdo = remover_subtree(no.filho_esquerdo, dado)
        return no

    # ir para a direita
    no.filho_direito = remover_subtree(no.filho_direito, dado)
    return no


def remover_node(no: No, dado: int) -> Optional[No]:
    """Remove apenas o primeiro nó encontrado cujo valor é igual ao dado informado.
    """
    if no is None:
        return None

    # No a ser removido foi encontrado recursivamente
    if no.dado == dado:
        if no.filho_direito is not None:
            no.filho_direito.filho_esquerdo = no.filho_esquerdo
            return no.filho_direito

        return no.filho_esquerdo

    # Busca recursiva à esquerda do nó corrente, atualizando a subarvore esquerda
    if dado <= no.dado:
        no.filho_esquerdo = remover_node(no.filho_esquerdo, dado)
        return no

    # Busca recursiva à direita do nó corrente, atualizando a direita direita
    no.filho_direito = remover_node(no.filho_direito, dado)
    return no

