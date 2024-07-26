import arvore

def test_node_leaf_must_have_no_children():
    actual_value = 50
    node = arvore.No(dado=actual_value)
    assert node is not None
    assert node.dado == actual_value
    assert node.filho_esquerdo == None
    assert node.filho_direito == None

def test_node_with_children():
    left_child, right_child = arvore.No(25), arvore.No(75)
    node = arvore.No(50, left_child, right_child)
    assert node.dado == 50
    assert node.filho_esquerdo is not None and node.filho_esquerdo == left_child
    assert node.filho_direito is not None and node.filho_direito == right_child
    