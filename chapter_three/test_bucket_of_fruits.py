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
