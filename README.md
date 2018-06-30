# Pytest bootcamp
Describes basics of pytest python testing framework.

## Table of contents
All home works from every chapter will be located in it's `test_home.py` file.
- [Chapter one (master tests)](#chapter-one-(master-tests))
  - [Install pytest](#install-pytest)
  - [Structure and syntax](#structure-and-syntax)
  - [Basic test sample](#basic-test-run)
  - [Run tests](#run-test(s))
  - [Asserts](#asserts)
  - [Markers](#markers)
  - [Run every of marker](#run-every-marker)
- [Chapter two (use fixtures)](#chapter-two-(use-fixtures))
  - [Basic fixtures](#basic-fixtures)
  - [Run basic fixtures](#run-basic-fixtures)
  - [Scope of fixtures](#scope-of-fixtures)
  - [Run scope of fixtures](#run-scope-of-fixtures)
  - [Conftest fixture](#conftest-fixture)
  - [Run conftest fixture](#run-conftest-fixture)
- [Chapter three (write plugins)](#chapter-three-(write-plugins))
- [Contributing](#contributing)

## Chapter one (master tests)
This chapter consists basics of pytest usage.
### Install pytest
```bash
# Install latest pytest dependencies
~/pytest-bootcamp/chapter_one pip install -U pytest
  
# Check installed pytest version
~/pytest-bootcamp/chapter_one pytest --version
```
### Structure and syntax
```python
# every test module has to start with `test_` or end with '_test.py' prefix like `test_item.py` or `item_test.py`
  
def test_target():  # every test function has to start with `test_` prefix
    assert tested_target == expected_result

```
### Basic test run
```python
#  test_basic.py test module
 
def increment(number: int) -> int:
    """Increment a given number by `1`."""
    return number + 1
 
 
def test_increment() -> None:
    assert increment(2) == 3
```

### Run test(s)
```bash
# Basic test run
~/pytest-bootcamp/chapter_one pytest test_basic.py
  
# Run test in verbose mode
~/pytest-bootcamp/chapter_one pytest test_basic.py -v
  
# Run test in quite mode
~/pytest-bootcamp/chapter_one pytest test_basic.py -q
 
# Run specific test function in a test module
~/pytest-bootcamp/chapter_one pytest test_basic.py::test_increment
  
# Run all tests in current directory and it's subdirectories
~/pytest-bootcamp/chapter_one pytest
  
# More pytest options
~/pytest-bootcamp/chapter_one pytest --help
```
### Asserts
```python
#  test_asserts.py test module
  
import pytest
 
def to_int(element: Any) -> int:
    """Convert given element into `int` data type."""
    return int(element)
 
 
def test_to_int() -> None:
    assert to_int('5') == 5
 
 
def test_to_int_two_asserts() -> None:
    assert to_int('5') == 5
    assert to_int(10.0) == 10
 
 
def test_to_int_expected_exception() -> None:
    with pytest.raises(TypeError, message="Expecting TypeError"):
        to_int(None)
```
### Markers
```python
#  test_markers.py test module

import pytest
import sys
 
def length(itr: Iterable) -> int:
    """Count elements in iterable object."""
    return len(itr)
 
 
@pytest.mark.skip(reason="I just want to skip this test.")
def test_skip_length() -> None:
    assert length('12') == 2
 
 
@pytest.mark.skipif(sys.platform == 'win32', reason='Does not support 32bit Windows platform')
def test_skipif_length() -> None:
    assert length('12') == 2
 
 
@pytest.mark.xfail(reason="Expected failure.")
def test_exp_fail_length() -> None:
    assert length(None) == 1
 
 
@pytest.mark.parametrize("test_input, expected_output", [
    ('', 0),
    ('1', 1),
    ('123', 3)
])
def test_param_length(test_input: str, expected_output: int) -> None:
    assert length(test_input) == expected_output
 
 
@pytest.mark.own_marker
def test_own_marker_length() -> None:
    assert length([1, 2]) == 2
```
### Run every marker
```bash
# Run all markers
~/pytest-bootcamp/chapter_one pytest test_markers.py -v
  
# Run skip tests
~/pytest-bootcamp/chapter_one pytest test_markers.py -v -m skip
  
# Run skipif tests
~/pytest-bootcamp/chapter_one pytest test_markers.py -v -m skipif
  
# Run expected failure tests
~/pytest-bootcamp/chapter_one pytest test_markers.py -v -m xfail
  
# Run parametrize tests
~/pytest-bootcamp/chapter_one pytest test_markers.py -v -m parametrize
  
# Run test with my own marker
~/pytest-bootcamp/chapter_one pytest test_markers.py -v -m own_marker
```
## Chapter two (use fixtures)
This chapter consists basics of pytest fixtures usage.
### Basic fixtures
```python
from chapter_one.operation import increment


def setup() -> None:
    print("basic setup - executes before every test")


def teardown() -> None:
    print("basic teardown - executes after every test")


def setup_module() -> None:
    print("module setup - executes once for a module")


def teardown_module() -> None:
    print("module teardown - executes once for a module")


def test_increment() -> None:
    print("running test_increment test")
    assert increment(2) == 3


class TestFixtures:
    def setup_class(cls) -> None:
        print("basic class setup - executes once before all tests")

    def teardown_class(cls) -> None:
        print("basic class teardown - executes once after all tests")

    def setup(self) -> None:
        print("basic setup - executed once before every test")

    def teardown(self) -> None:
        print("basic teardown - executed once after every test")

    def test_increment_in_class(self) -> None:
        print("running test_increment_in_class test")
        assert increment(4) == 5

```
### Run basic fixtures
```bash
# Run all basic fixtures
~/pytest-bootcamp/chapter_two pytest test_basic_fixtures.py -s -v
```
### Scope of fixtures
```python
# test_extended_fixtures.py
import pytest


@pytest.fixture(scope="function")
def function_setup() -> str:
    print("executes for every test function")
    return "function_setup"


@pytest.fixture(scope="module")
def module_setup() -> str:
    print("executes once for module before all tests")
    return "module_setup"


@pytest.fixture(scope="class")
def class_setup() -> str:
    print("executes before every class")
    return "class_setup"


@pytest.fixture(scope="session")
def session_setup() -> str:
    print("executes once for a session")
    return "session_setup"


def test_module_one(module_setup: str) -> None:
    print('running test_module_one')
    assert module_setup == "module_setup"


def test_module_two(module_setup: str) -> None:
    print('running test_module_two')
    assert module_setup == "module_setup"


def test_function_one(function_setup: str) -> None:
    print('running test_function_one')
    assert function_setup == "function_setup"


def test_function_two(function_setup: str) -> None:
    print('running test_function_two')
    assert function_setup == "function_setup"


def test_session_one(session_setup: str) -> None:
    print('running test_session_one')
    assert session_setup == "session_setup"


def test_session_two(session_setup: str) -> None:
    print('running test_session_two')
    assert session_setup == "session_setup"


class TestOne:
    def test_class_one(self, class_setup: str) -> None:
        print('running test_class_one')
        assert class_setup == "class_setup"


class TestTwo:
    def test_class_two(self, class_setup: str) -> None:
        print('running test_class_two')
        assert class_setup == "class_setup"
```
### Run scope of fixtures
```bash
# Run all extended fixtures
~/pytest-bootcamp/chapter_two pytest test_extended_fixtures.py -s -v
  
# See all available fixtures for `test_extended_fixtures.py` module
~/pytest-bootcamp/chapter_two pytest --fixtures test_extended_fixtures.py

```
### Conftest fixture
```python
# conftest.py module
import pytest


@pytest.fixture(scope="module")
def num():
    return 3

# square.py module
from typing import List


def square_list(n: int) -> List[int]:
    return [i ** 2 for i in range(1, n)]

# test_square.py module
from chapter_two.square import square_list


def test_square_list(num: int) -> None:
    assert square_list(num) == [1, 4]


def test_len_square_list(num: int) -> None:
    assert len(square_list(num)) == 2
```
### Run conftest fixture
```bash
# Run `contest.py` fixture
~/pytest-bootcamp/chapter_two pytest test_square.py -s -v
  
# See `conftest.py` module as a fixture for `test_square.py` test module
~/pytest-bootcamp/chapter_two pytest --fixtures test_square.py
```
## Chapter three (write plugins)
## Contributing

### Setup
- clone the repository
- configure Git for the first time after cloning with your name and email
  ```bash
  git config --local user.name "Volodymyr Yahello"
  git config --local user.email "vjagello93@gmail.com"
  ```
- `python3.6` is required to run the code
- run `pip install -r requirements.txt` to install all required packages