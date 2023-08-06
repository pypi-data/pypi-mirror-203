import pytest
from pathlib import Path
from write_the.utils import list_python_files


@pytest.fixture
def directory():
    return Path("/home/user/code")


def test_list_python_files(directory):
    python_files = list_python_files(directory)
    assert isinstance(python_files, list)
    assert len(python_files) == 2
    assert Path("/home/user/code/main.py") in python_files
    assert Path("/home/user/code/utils.py") in python_files


def test_list_python_files_empty_directory(directory):
    directory = Path("/home/user/empty_dir")
    python_files = list_python_files(directory)
    assert isinstance(python_files, list)
    assert len(python_files) == 0


def test_list_python_files_invalid_directory():
    with pytest.raises(TypeError):
        list_python_files("/home/user/code")
