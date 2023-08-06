import os
import pytest
from pathlib import Path
from collections import defaultdict
from write_the.utils import list_python_files


@pytest.fixture
def code_dir():
    return Path("./tests/code_dir")


@pytest.fixture
def readme():
    return Path("./tests/README.md")


@pytest.fixture
def project_name():
    return "test_project"


def test_write_the_mkdocs_no_readme(code_dir, project_name):
    write_the_mkdocs(code_dir, readme=None, project_name=project_name)
    assert Path("./mkdocs.yml").exists()
    assert Path("./docs/reference/index.md").exists()
    assert Path("./docs/index.md").exists()
    assert Path(".github/workflows/mkdocs.yml").exists()


def test_write_the_mkdocs_with_readme(code_dir, readme, project_name):
    write_the_mkdocs(code_dir, readme=readme, project_name=project_name)
    assert Path("./mkdocs.yml").exists()
    assert Path("./docs/reference/index.md").exists()
    assert Path("./docs/index.md").exists()
    assert Path(".github/workflows/mkdocs.yml").exists()
    assert readme.read_text() in Path("./docs/index.md").read_text()


def test_write_the_mkdocs_no_project_name(code_dir, readme):
    write_the_mkdocs(code_dir, readme=readme)
    assert Path("./mkdocs.yml").exists()
    assert Path("./docs/reference/index.md").exists()
    assert Path("./docs/index.md").exists()
    assert Path(".github/workflows/mkdocs.yml").exists()
    assert code_dir.name in Path("./mkdocs.yml").read_text()
