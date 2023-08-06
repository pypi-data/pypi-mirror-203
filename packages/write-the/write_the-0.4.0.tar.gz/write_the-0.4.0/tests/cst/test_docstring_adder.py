import pytest
import libcst as cst
from write_the.cst.docstring_adder import DocstringAdder
from write_the.cst.utils import has_docstring


@pytest.fixture
def docstring_adder():
    docstrings = {
        "function_1": "This is a docstring for function_1",
        "function_2": "This is a docstring for function_2",
        "ClassA.function_3": "This is a docstring for function_3",
        "ClassA.function_4": "This is a docstring for function_4",
    }
    return DocstringAdder(docstrings, False)


@pytest.fixture
def function_def_node():
    return cst.FunctionDef(
        name=cst.Name("function_1"),
        params=cst.Parameters(),
        body=cst.Suite([cst.Pass()]),
    )


@pytest.fixture
def class_def_node():
    return cst.ClassDef(name=cst.Name("ClassA"), body=cst.Suite([cst.Pass()]))


@pytest.fixture
def function_def_node_with_docstring():
    return cst.FunctionDef(
        name=cst.Name("function_1"),
        params=cst.Parameters(),
        body=cst.Suite(
            [
                cst.SimpleStatementLine(
                    [cst.Expr(cst.Constant('"""This is a docstring for function_1"""'))]
                )
            ]
        ),
    )


def test_leave_function_def_with_no_docstring(docstring_adder, function_def_node):
    updated_node = docstring_adder.leave_FunctionDef(
        function_def_node, function_def_node
    )
    assert has_docstring(updated_node)


def test_leave_function_def_with_docstring(
    docstring_adder, function_def_node_with_docstring
):
    updated_node = docstring_adder.leave_FunctionDef(
        function_def_node_with_docstring, function_def_node_with_docstring
    )
    assert has_docstring(updated_node)


def test_leave_class_def_with_no_docstring(docstring_adder, class_def_node):
    updated_node = docstring_adder.leave_ClassDef(class_def_node, class_def_node)
    assert has_docstring(updated_node)


def test_leave_class_def_with_docstring(docstring_adder, class_def_node):
    updated_node = docstring_adder.leave_ClassDef(class_def_node, class_def_node)
    assert has_docstring(updated_node)
