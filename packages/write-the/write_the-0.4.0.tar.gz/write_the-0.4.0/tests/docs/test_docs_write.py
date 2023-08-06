import pytest
import libcst as cst
from black import FileMode
from pathlib import Path

from write_the.cst.docstring_adder import DocstringAdder
from write_the.cst.docstring_remover import remove_docstrings
from write_the.cst.function_and_class_collector import get_node_names
from write_the.cst.node_extractor import extract_nodes_from_tree
from write_the.cst.node_remover import remove_nodes_from_tree
from write_the.cst import nodes_to_tree
from write_the.docs.write import write_the_docs


@pytest.fixture
def source_code():
    return """
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
"""


@pytest.fixture
def expected_code():
    return """
def add(a, b):
    \"\"\"Sums 2 numbers.
    Args:
        a (int): The first number to add.
        b (int): The second number to add.
    Returns:
        int: The sum of `a` and `b`.
    \"\"\"
    return a + b

def subtract(a, b):
    \"\"\"Subtracts 2 numbers.
    Args:
        a (int): The number to subtract from.
        b (int): The number to subtract.
    Returns:
        int: The difference of `a` and `b`.
    \"\"\"
    return a - b

def multiply(a, b):
    \"\"\"Multiplies 2 numbers.
    Args:
        a (int): The first number to multiply.
        b (int): The second number to multiply.
    Returns:
        int: The product of `a` and `b`.
    \"\"\"
    return a * b

def divide(a, b):
    \"\"\"Divides 2 numbers.
    Args:
        a (int): The number to divide.
        b (int): The number to divide by.
    Returns:
        int: The quotient of `a` and `b`.
    \"\"\"
    return a / b
"""


@pytest.fixture
def tree(source_code):
    return cst.parse_module(source_code)


@pytest.fixture
def nodes(tree):
    return get_node_names(tree, False)


def test_write_the_docs_no_args(source_code, expected_code):
    result = write_the_docs(Path("example.py"))
    assert result == expected_code


def test_write_the_docs_nodes_arg(source_code, tree, nodes):
    result = write_the_docs(Path("example.py"), nodes=nodes)
    assert result == expected_code


def test_write_the_docs_force_arg(source_code, tree, nodes):
    result = write_the_docs(Path("example.py"), nodes=nodes, force=True)
    assert result == expected_code


def test_write_the_docs_inplace_arg(source_code, tree, nodes):
    result = write_the_docs(Path("example.py"), nodes=nodes, inplace=True)
    assert result == expected_code


def test_write_the_docs_context_arg(source_code, tree, nodes):
    result = write_the_docs(Path("example.py"), nodes=nodes, context=False)
    assert result == expected_code


def test_write_the_docs_all_args(source_code, tree, nodes):
    result = write_the_docs(
        Path("example.py"), nodes=nodes, force=True, inplace=True, context=False
    )
    assert result == expected_code
