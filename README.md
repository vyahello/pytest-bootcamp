# Pytest bootcamp
My own implementation of pytest bootcamp project is aimed on helping to comprehend a `pytest` framework by newcomers.
Describes basics of pytest python testing framework.

## Table of contents
All home works from every chapter will be located in it's `test_home.py` file.
- [First (master tests)](#first-(master-tests))
  - [Install pytest](#install-pytest)
  - [Structure and syntax](#structure-and-syntax)
  - [Basic test sample](#basic-test-run)
  - [Run tests](#run-test(s))
  - [Asserts](#asserts)
  - [Markers](#markers)
  - [Run every marker](#run-every-marker)
  - [Additional materials](#additional-materials-for-chapter-one)
- [Second (use fixtures)](#second-(use-fixtures))
  - [Basic fixtures](#basic-fixtures)
  - [Run basic fixtures](#run-basic-fixtures)
  - [Scope of fixtures](#scope-of-fixtures)
  - [Run scope of fixtures](#run-scope-of-fixtures)
  - [Conftest fixture](#conftest-fixture)
  - [Run conftest fixture](#run-conftest-fixture)
  - [Additional materials](#additional-metarials-from-chapter-two)
- [Third (write plugins)](#third-(write-plugins))
  - [Write plugin](#write-plugin)
  - [Use plugin](#use-plugin)
  - [Run test with plugin](#run-tests-with-plugin)
  - [Install external plugin](#install-external-plugin)
  - [Write test with pytest-bdd](#write-test-with-pytest-bdd)
  - [Run test with pytest-bdd plugin](#run-test-with-pytest-bdd-plugin)
  - [Add custom parameters](#add-custom-parameters)
  - [Run tests with custom parameters](#run-tests-with-custom-parameters)
  - [Write hooks](#write-hooks)
  - [Run tests with hooks](#run-tests-with-hooks)
  - [Additional materials](#additional-metarials-from-chapter-three)
- [Contributing](#contributing)

## First (master tests)
This chapter consists basics of pytest usage.
### Install pytest
```bash
# Install latest pytest dependencies
~/pytest-bootcamp/first pip install -U pytest
  
# Check installed pytest version
~/pytest-bootcamp/first pytest --version
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
~/pytest-bootcamp/first pytest test_basic.py
  
# Run test in verbose mode
~/pytest-bootcamp/first pytest test_basic.py -v
  
# Run test in quite mode
~/pytest-bootcamp/first pytest test_basic.py -q
 
# Run specific test function in a test module
~/pytest-bootcamp/first pytest test_basic.py::test_increment
  
# Run all tests in current directory and it's subdirectories
~/pytest-bootcamp/first pytest
  
# More pytest options
~/pytest-bootcamp/first pytest --help
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
~/pytest-bootcamp/first pytest test_markers.py -v
  
# Run skip tests
~/pytest-bootcamp/first pytest test_markers.py -v -m skip
  
# Run skipif tests
~/pytest-bootcamp/first pytest test_markers.py -v -m skipif
  
# Run expected failure tests
~/pytest-bootcamp/first pytest test_markers.py -v -m xfail
  
# Run parametrize tests
~/pytest-bootcamp/first pytest test_markers.py -v -m parametrize
  
# Run test with my own marker
~/pytest-bootcamp/first pytest test_markers.py -v -m own_marker
```
### Additional materials for chapter one
- [https://docs.pytest.org/en/latest/contents.html](https://docs.pytest.org/en/latest/contents.html)
- [https://docs.pytest.org/en/latest/getting-started.html](https://docs.pytest.org/en/latest/getting-started.html)
- [https://docs.pytest.org/en/latest/assert.html](https://docs.pytest.org/en/latest/assert.html)
- [https://docs.pytest.org/en/latest/mark.html#mark](https://docs.pytest.org/en/latest/mark.html#mark)

## Second (use fixtures)
This chapter consists basics of pytest fixtures usage.
### Basic fixtures
```python
from first.operation import increment


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
~/pytest-bootcamp/second pytest test_basic_fixtures.py -s -v
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
~/pytest-bootcamp/second pytest test_extended_fixtures.py -s -v
  
# See all available fixtures for `test_extended_fixtures.py` module
~/pytest-bootcamp/second pytest --fixtures test_extended_fixtures.py

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
from second.square import square_list


def test_square_list(num: int) -> None:
    assert square_list(num) == [1, 4]


def test_len_square_list(num: int) -> None:
    assert len(square_list(num)) == 2
```
### Run conftest fixture
```bash
# Run `contest.py` fixture
~/pytest-bootcamp/second pytest test_square.py -s -v
  
# See `conftest.py` module as a fixture for `test_square.py` test module
~/pytest-bootcamp/second pytest --fixtures test_square.py
```
### Additional metarials from chapter two
- [https://docs.pytest.org/en/3.5.0/fixture.html](https://docs.pytest.org/en/3.5.0/fixture.html)
- [https://docs.pytest.org/en/latest/example/simple.html](https://docs.pytest.org/en/latest/example/simple.html)

## Third (write plugins)
### Write plugin
```python
# plugin.py

import pytest
from typing import Iterable


@pytest.fixture(scope='module')
def rng() -> Iterable[int]:
    return range(5)
```
### Use plugin
```python
# load plugin in conftest.py
pytest_plugins = 'plugin'

# operations.py
from typing import Iterable


def total(rng: Iterable[int]) -> int:
    return sum(rng)


def count(rng: Iterable[int]) -> int:
    return len(rng)

# test_operations.py
  
from typing import Iterable
from third.operation import total, count

pytest_plugins = 'plugin'  # load plugin if conftest.py above is NOT configured


def test_total(rng: Iterable[int]) -> None:
    assert total(rng) == 10


def test_count(rng: Iterable[int]) -> None:
    assert count(rng) == 5
```
### Run tests with plugin
```bash
# Run test_operations.py test module
~/pytest-bootcamp/second pytest -v test_operations.py
```
### Install external plugin
```bash
# Install pytest-bdd plugin with pip
~/pytest-bootcamp/second pip install pytest-bdd
```
### Write test with pytest-bdd
```gherkin
# bucket_of_fruits.feature
  
Feature: A bucket of fruits
 
Scenario: Counting fruits in a bucket
    Given There are 9 fruits in a bucket
    When I have 2 friends
    And I give 3 fruits to my 1st friend
    And I give 3 fruits to my 2nd friend
    Then I should have 3 fruits for myself
```
```python
# test_bucket_of_fruits.py

from typing import Dict
from pytest_bdd import scenario, given, when, then, parsers


@scenario('bucket_of_fruits.feature', 'Counting fruits in a bucket')
def test_bucket_of_fruits():
    pass


@given(parsers.parse('There are {amount:d} fruits in a bucket'))
def initial_amount_of_fruits(amount: int) -> Dict[str, int]:
    return {'fruits': amount}


@when(parsers.parse('I have {amount:d} friends'))
def amount_of_friends(amount: int) -> None:
    assert amount == 2


@when(parsers.parse('I give {amount:d} fruits to my 1st friend'))
def give_fruits_to_1st_friend(initial_amount_of_fruits: Dict[str, int], amount: int) -> None:
    initial_amount_of_fruits['fruits'] -= amount


@when(parsers.parse('I give {amount:d} fruits to my 2nd friend'))
def give_fruits_to_2st_friend(initial_amount_of_fruits: Dict[str, int], amount: int) -> None:
    initial_amount_of_fruits['fruits'] -= amount


@then(parsers.parse('I should have {amount:d} fruits for myself'))
def amount_fruits_for_myself(initial_amount_of_fruits: Dict[str, int], amount: int) -> None:
    assert initial_amount_of_fruits['fruits'] == amount
```
### Run test with pytest-bdd plugin
```bash
# Run test_bucket_of_fruits.py test module
~/pytest-bootcamp/third pytest -vv --gherkin-terminal-reporter test_bucket_of_fruits.py
```
### Add custom parameters
```python
# checks.py
import os


def ping_host(host: str) -> int:
    return os.system(f"ping {host} -c 1")

# addoption_plugin.py
import pytest
from _pytest.config.argparsing import Parser
from _pytest.fixtures import SubRequest


def pytest_addoption(parser: Parser) -> None:
    parser.addoption("--host", "-H",
                     action="store",
                     default="localhost",
                     help="A host should be provided as a hostname (google.com) or ip address (172.217.13.238)")


@pytest.fixture(scope="module")
def host(request: SubRequest) -> str:
    return request.config.getoption("--host")

    
# conftest.py
pytest_plugins = 'third.basic_plugin', \
                 'third.addoption_plugin'

# test_checks.py
from third.checks import ping_host


def test_ping_host(host: str) -> None:
    assert ping_host(host) == 0
```
### Run tests with custom parameters
```bash
# Check just created custom parameter (--host/-H should be provided)
~/pytest-bootcamp/third pytest --help
  
# Run test_checks.py test module with custom parameter
~/pytest-bootcamp/third pytest test_ping.py --host pytest.org
```
### Write hooks
```python
# hooks_plugin

from typing import Callable, List
import pytest
from _pytest.fixtures import SubRequest
from _pytest.config import Config
from _pytest.config.argparsing import Parser
from _pytest.python import Function


@pytest.fixture
def hello() -> Callable[..., str]:
    def _hello(request: str = '') -> str:
        if not request:
            return "Hello !"
        return "Hello {}!".format(request)
    return _hello


@pytest.fixture(params=["Brianna", "Andreas", "Floris"])
def name(request: SubRequest) -> str:
    return request.param


def pytest_configure(config: Config) -> None:
    """Enable verbose output when running tests. Simulate ``-v`` option in a command line."""

    config.option.verbose = 1


def pytest_report_header(config: Config) -> List[str]:
    """Add information to test report header."""

    if config.option.verbose > 0:
        return ["Project: pytest-hooks", "Written by: Volodymyr Yahello"]


def pytest_addoption(parser: Parser) -> None:
    """Add custom parameters."""

    parser.addoption("--skip-marker",
                     "-S",
                     action="store",
                     default=None,
                     help="skip test(s) with certain marker.")


def pytest_runtest_setup(item: Function) -> None:
    """Skip tests that belong to specific marker with ``--skip-marker`` cmd option."""

    marker = item.config.getvalue("--skip-marker")
    if marker in item.keywords:
        pytest.skip(f"Skipping [@{marker}] pytest marker")

# conftest.py
pytest_plugins = 'third.basic_plugin', \
                 'third.addoption_plugin', \
                 'third.hooks_plugin'


# test_hello_hooks.py
from typing import Callable


def test_hello_default(hello: Callable[..., str]) -> None:
    assert hello() == "Hello !"


def test_hello_name(hello: Callable[..., str], name: str) -> None:
    assert hello(name) == "Hello {0}!".format(name)


# test_dir
import os
import pytest
from _pytest.fixtures import SubRequest


@pytest.fixture(scope='module', autouse=True)
def setup_dir(request: SubRequest) -> None:
    os.mkdir('test-dir', mode=0o777)

    def teardown_dir() -> None:
        os.rmdir('test-dir-1')

    request.addfinalizer(teardown_dir)


@pytest.mark.dir
def test_rename_dir() -> None:
    os.rename('test-dir', 'test-dir-1')
    assert os.path.basename('test-dir-1') == 'test-dir-1'


@pytest.mark.dir
def test_list_dir() -> None:
    assert os.listdir('test-dir-1') == []
    
# test_system
import sys
import pytest


@pytest.mark.system
def test_platform() -> None:
    assert sys.platform == 'darwin'


@pytest.mark.system
def test_python_version() -> None:
    assert sys.version_info[:3] == (3, 7, 0)
```
### Run tests with hooks
```bash
~/pytest-bootcamp/third pytest --skip-marker dir -rs
  
# Skip tests with `system` pytest marker
~/pytest-bootcamp/third pytest --skip-marker system -rs
```
### Additional metarials from chapter three
- [https://docs.pytest.org/en/latest/writing_plugins.html](https://docs.pytest.org/en/latest/writing_plugins.html)
- [https://docs.pytest.org/en/latest/plugins.html](https://docs.pytest.org/en/latest/plugins.html)
- [https://docs.pytest.org/en/latest/example/simple.html](https://docs.pytest.org/en/latest/example/simple.html)
- [https://docs.pytest.org/en/latest/writing_plugins.html#writing-hook-functions](https://docs.pytest.org/en/latest/writing_plugins.html#writing-hook-functions)
- [https://pytest.readthedocs.io/en/2.7.3/plugins_index/index.html](https://pytest.readthedocs.io/en/2.7.3/plugins_index/index.html)
- [http://pytest-bdd.readthedocs.io/en/latest/](http://pytest-bdd.readthedocs.io/en/latest/)

## Contributing

- clone the repository
- configure Git for the first time after cloning with your name and email
  ```bash
  git config --local user.name "Volodymyr Yahello"
  git config --local user.email "vyahello@gmail.com"
  ```
- `python3.6` is required to run the code
- run `pip install -r requirements.txt` to install all required packages