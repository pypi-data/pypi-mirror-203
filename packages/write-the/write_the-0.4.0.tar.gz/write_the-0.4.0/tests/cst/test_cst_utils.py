import libcst as cst
from write_the.cst.utils import has_docstring, nodes_to_tree
import pytest

@pytest.fixture
def cst_node():
    return cst.CSTNode()


@pytest.fixture
def cst_function_def():
    return cst.FunctionDef(
        name="test_function",
        body=cst.Suite(
            [
                cst.SimpleStatementLine(
                    [cst.Expr(value=cst.SimpleString("test_docstring"))]
                )
            ]
        ),
    )


@pytest.fixture
def cst_class_def():
    return cst.ClassDef(
        name="TestClass",
        body=cst.Suite(
            [
                cst.SimpleStatementLine(
                    [cst.Expr(value=cst.SimpleString("test_docstring"))]
                )
            ]
        ),
    )


@pytest.fixture
def cst_module():
    return cst.Module(
        body=[
            cst.FunctionDef(
                name="test_function",
                body=cst.Suite(
                    [
                        cst.SimpleStatementLine(
                            [cst.Expr(value=cst.SimpleString("test_docstring"))]
                        )
                    ]
                ),
            )
        ]
    )


def test_has_docstring_with_function_def(cst_function_def):
    assert has_docstring(cst_function_def) == True


def test_has_docstring_with_class_def(cst_class_def):
    assert has_docstring(cst_class_def) == True


def test_has_docstring_with_cst_node(cst_node):
    assert has_docstring(cst_node) == False


def test_nodes_to_tree(cst_module):
    assert isinstance(nodes_to_tree([cst_module]), cst.Module) == True
