import pytest
from pathlib import Path
from black import FileMode
from write_the.tests.chain import run
from write_the.tests import write_the_tests


@pytest.fixture
def filename():
    return Path("test.py")


@pytest.fixture
def source_code():
    return "def test_function():\n    pass"


@pytest.fixture
def result():
    return "def test_function():\n    pass"


def test_write_the_tests_with_valid_filename(filename, source_code, result):
    with open(filename, "w") as file:
        file.write(source_code)
    assert write_the_tests(filename) == result


def test_write_the_tests_with_invalid_filename():
    with pytest.raises(FileNotFoundError):
        write_the_tests(Path("invalid.py"))


def test_write_the_tests_with_empty_file(filename):
    with open(filename, "w") as file:
        file.write("")
    assert write_the_tests(filename) == ""


def test_write_the_tests_with_invalid_code(filename):
    with open(filename, "w") as file:
        file.write("invalid code")
    with pytest.raises(SyntaxError):
        write_the_tests(filename)
