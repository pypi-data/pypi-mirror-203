import pytest
import libcst as cst
from write_the.cst.function_and_class_collector import (
    FunctionAndClassCollector,
    get_node_names,
)


@pytest.fixture
def tree():
    return cst.parse_module(
        """
def foo():
    pass

class Bar:
    pass

def baz():
    pass

class Qux:
    pass
"""
    )


@pytest.fixture
def force():
    return False


def test_visit_FunctionDef_with_no_docstring(tree):
    collector = FunctionAndClassCollector(force=False)
    tree.visit(collector)
    assert collector.functions == ["foo", "baz"]


def test_visit_FunctionDef_with_docstring(tree):
    collector = FunctionAndClassCollector(force=True)
    tree.visit(collector)
    assert collector.functions == ["foo", "baz"]


def test_visit_ClassDef_with_no_docstring(tree):
    collector = FunctionAndClassCollector(force=False)
    tree.visit(collector)
    assert collector.classes == ["Bar", "Qux"]


def test_visit_ClassDef_with_docstring(tree):
    collector = FunctionAndClassCollector(force=True)
    tree.visit(collector)
    assert collector.classes == ["Bar", "Qux"]


def test_get_node_names_with_no_docstring(tree, force):
    assert get_node_names(tree, force) == ["foo", "Bar", "baz", "Qux"]


def test_get_node_names_with_docstring(tree, force):
    assert get_node_names(tree, force) == ["foo", "Bar", "baz", "Qux"]
