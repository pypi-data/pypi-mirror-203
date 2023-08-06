import pytest
import libcst as cst
from write_the.cst.node_extractor import extract_nodes_from_tree


@pytest.fixture
def tree():
    return cst.Module(
        [
            cst.FunctionDef(
                "foo", cst.Parameters(), cst.SimpleStatementSuite([cst.Pass()])
            ),
            cst.ClassDef(
                "Bar", cst.BaseSpecifier(), cst.SimpleStatementSuite([cst.Pass()])
            ),
        ]
    )


@pytest.fixture
def nodes():
    return ["foo", "Bar"]


def test_extract_nodes_from_tree(tree, nodes):
    extracted_nodes = extract_nodes_from_tree(tree, nodes)
    assert len(extracted_nodes) == 2
    assert isinstance(extracted_nodes[0], cst.FunctionDef)
    assert isinstance(extracted_nodes[1], cst.ClassDef)


def test_extract_nodes_from_tree_empty_nodes(tree):
    extracted_nodes = extract_nodes_from_tree(tree, [])
    assert len(extracted_nodes) == 0


def test_extract_nodes_from_tree_invalid_node(tree, nodes):
    nodes.append("invalid")
    extracted_nodes = extract_nodes_from_tree(tree, nodes)
    assert len(extracted_nodes) == 2
    assert isinstance(extracted_nodes[0], cst.FunctionDef)
    assert isinstance(extracted_nodes[1], cst.ClassDef)
