import pytest
import libcst as cst
from write_the.cst.docstring_remover import DocstringRemover, remove_docstrings


@pytest.fixture
def function_def_node():
    return cst.FunctionDef(
        name=cst.Name("test_function"),
        params=cst.Parameters(),
        body=cst.Suite(
            [
                cst.SimpleStatementLine(
                    [cst.Expr(value=cst.SimpleString("This is a docstring"))]
                ),
                cst.SimpleStatementLine([cst.Expr(value=cst.Name("print"))]),
            ]
        ),
    )


@pytest.fixture
def class_def_node():
    return cst.ClassDef(
        name=cst.Name("TestClass"),
        body=cst.Suite(
            [
                cst.SimpleStatementLine(
                    [cst.Expr(value=cst.SimpleString("This is a docstring"))]
                ),
                cst.SimpleStatementLine([cst.Expr(value=cst.Name("print"))]),
            ]
        ),
    )


def test_leave_function_def_with_docstring(function_def_node):
    nodes = ["test_function"]
    remover = DocstringRemover(nodes)
    updated_node = remover.leave_FunctionDef(function_def_node, function_def_node)
    assert len(updated_node.body.body) == 1
    assert isinstance(updated_node.body.body[0], cst.SimpleStatementLine)
    assert isinstance(updated_node.body.body[0].body[0], cst.Expr)
    assert isinstance(updated_node.body.body[0].body[0].value, cst.Name)
    assert updated_node.body.body[0].body[0].value.value == "print"


def test_leave_function_def_without_docstring(function_def_node):
    nodes = ["other_function"]
    remover = DocstringRemover(nodes)
    updated_node = remover.leave_FunctionDef(function_def_node, function_def_node)
    assert len(updated_node.body.body) == 2
    assert isinstance(updated_node.body.body[0], cst.SimpleStatementLine)
    assert isinstance(updated_node.body.body[0].body[0], cst.Expr)
    assert isinstance(updated_node.body.body[0].body[0].value, cst.SimpleString)
    assert updated_node.body.body[0].body[0].value.value == "This is a docstring"


def test_leave_class_def_with_docstring(class_def_node):
    nodes = ["TestClass"]
    remover = DocstringRemover(nodes)
    updated_node = remover.leave_ClassDef(class_def_node, class_def_node)
    assert len(updated_node.body.body) == 1
    assert isinstance(updated_node.body.body[0], cst.SimpleStatementLine)
    assert isinstance(updated_node.body.body[0].body[0], cst.Expr)
    assert isinstance(updated_node.body.body[0].body[0].value, cst.Name)
    assert updated_node.body.body[0].body[0].value.value == "print"


def test_leave_class_def_without_docstring(class_def_node):
    nodes = ["OtherClass"]
    remover = DocstringRemover(nodes)
    updated_node = remover.leave_ClassDef(class_def_node, class_def_node)
    assert len(updated_node.body.body) == 2
    assert isinstance(updated_node.body.body[0], cst.SimpleStatementLine)
    assert isinstance(updated_node.body.body[0].body[0], cst.Expr)
    assert isinstance(updated_node.body.body[0].body[0].value, cst.SimpleString)
    assert updated_node.body.body[0].body[0].value.value == "This is a docstring"


def test_remove_docstrings(function_def_node, class_def_node):
    nodes = ["test_function", "TestClass"]
    tree = cst.Module([function_def_node, class_def_node])
    updated_tree = remove_docstrings(tree, nodes)
    assert len(updated_tree.body) == 2
    assert isinstance(updated_tree.body[0], cst.FunctionDef)
    assert len(updated_tree.body[0].body.body) == 1
    assert isinstance(updated_tree.body[1], cst.ClassDef)
    assert len(updated_tree.body[1].body.body) == 1
