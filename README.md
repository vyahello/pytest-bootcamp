# Pytest bootcamp
Describes basics of pytest python testing framework.

## Table of contents
- [Chapter one. Mastering test(s)](#chapter-one)
  - [Install pytest](#install-pytest)
  - [Structure and syntax](#structure-and-syntax)
  - [Basic test sample](#basic-test-run)
  - [Run tests](#run-test(s))
  - [Asserts](#asserts)
  - [Markers](#markers)
  - [Run every of marker](#run-every-marker)
- [Chapter two. Use fixtures](#)
- [Chapter three. Write plugins](#)
- [Contributing](#contributing)

## Chapter one
Consists basics of pytest usage.
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