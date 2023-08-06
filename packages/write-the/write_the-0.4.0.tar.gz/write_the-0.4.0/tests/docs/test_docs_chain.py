import pytest
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from write_the.docs.chain import run


@pytest.fixture
def llm():
    return OpenAI(temperature=0, max_tokens=2000)


@pytest.fixture
def docs_template():
    return "\nWrite Google style docstrings for the following code, using the multi-line format with a description and examples. The first lines describe the code. Include parameter type definitions where possible, and specify any exceptions raised and side effects of the function. For functions with multiple return values or ambiguous behaviour, provide clear guidelines for documenting the behaviour. Please refer to the Google style guide for more information. Any notes should be include in the `Notes:` section of the docstring. Only return the docstring its self. Return each docstring on a single line with the name of the function/class as the key and the docstring as the value. Separate each result by a newline. If the function is a method return the name in the format Class.method. The Class docstrings should contain Description and Attributes. Each result should be separated by multiple newlines. \n---\nEXAMPLE\n---\n\ndef add(a, b): \n    return a + b \nHere are formatted docstrings for only add:\nadd:\n  Sums 2 numbers.\n  Args:\n    a (int): The first number to add.\n    b (int): The second number to add.\n  Returns:\n    int: The sum of `a` and `b`.\n  Examples:\n    >>> add(1, 2)\n    3\n\n\n---\nCODE\n---\n{code}\nHere are formatted docstrings for only {nodes}:\n"


@pytest.fixture
def docs_prompt(docs_template):
    return PromptTemplate(input_variables=["code", "nodes"], template=docs_template)


@pytest.fixture
def docs_chain(llm, docs_prompt):
    return LLMChain(llm=llm, prompt=docs_prompt)


def test_run_valid_input(docs_chain):
    code = "def add(a, b): \n    return a + b"
    nodes = ["add"]
    expected = "add:\n  Sums 2 numbers.\n  Args:\n    a (int): The first number to add.\n    b (int): The second number to add.\n  Returns:\n    int: The sum of `a` and `b`.\n  Examples:\n    >>> add(1, 2)\n    3"
    assert run(code, nodes) == expected


def test_run_invalid_input(docs_chain):
    code = "def add(a, b): \n    return a + b"
    nodes = ["add", "subtract"]
    expected = "add:\n  Sums 2 numbers.\n  Args:\n    a (int): The first number to add.\n    b (int): The second number to add.\n  Returns:\n    int: The sum of `a` and `b`.\n  Examples:\n    >>> add(1, 2)\n    3\nsubtract:\n  Subtracts 2 numbers.\n  Args:\n    a (int): The first number to subtract.\n    b (int): The second number to subtract.\n  Returns:\n    int: The difference of `a` and `b`.\n  Examples:\n    >>> subtract(1, 2)\n    -1"
    assert run(code, nodes) == expected


def test_run_empty_input(docs_chain):
    code = ""
    nodes = []
    expected = ""
    assert run(code, nodes) == expected
