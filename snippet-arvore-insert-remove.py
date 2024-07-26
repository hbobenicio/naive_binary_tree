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
