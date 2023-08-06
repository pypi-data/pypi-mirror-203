import pytest
import libcst as cst
from write_the.cst.node_remover import NodeRemover, remove_nodes_from_tree


@pytest.fixture
def tree():
    return cst.parse_module("def foo(): pass")


@pytest.fixture
def nodes():
    return ["foo"]


def test_node_remover_init():
    remover = NodeRemover(nodes)
    assert remover.nodes == nodes


def test_leave_function_def_remove(tree, nodes):
    remover = NodeRemover(nodes)
    updated_tree = tree.visit(remover)
    assert updated_tree.body == []


def test_leave_function_def_no_remove(tree, nodes):
    remover = NodeRemover(["bar"])
    updated_tree = tree.visit(remover)
    assert updated_tree.body == [tree.body[0]]


def test_leave_class_def_remove(tree, nodes):
    class_def = cst.ClassDef("foo")
    tree.body.append(class_def)
    remover = NodeRemover(nodes)
    updated_tree = tree.visit(remover)
    assert updated_tree.body == []


def test_leave_class_def_no_remove(tree, nodes):
    class_def = cst.ClassDef("bar")
    tree.body.append(class_def)
    remover = NodeRemover(nodes)
    updated_tree = tree.visit(remover)
    assert updated_tree.body == [tree.body[0], tree.body[1]]


def test_remove_nodes_from_tree(tree, nodes):
    updated_tree = remove_nodes_from_tree(tree, nodes)
    assert updated_tree.body == []
