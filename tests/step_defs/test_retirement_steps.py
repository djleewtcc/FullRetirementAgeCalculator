import pytest
from pytest_bdd import scenarios, parsers, given, when, then
from full_retirement_age_calculator import FullRetirementAgeCalculator


EXTRA_TYPES = {
    'Number': int
}

CONVERTERS = {
    'birth_year': int,
    'birth_month': int,
    'retirement_year': int
}

scenarios('../features/retirement.feature', example_converters=CONVERTERS)


@pytest.fixture()
@given('the birth year is set to "<birth_year>"')
def retire_age(birth_year):
    return FullRetirementAgeCalculator(birth_year=birth_year)


@when('the birth month is "<birth_month>"')
def set_year(retire_age, birth_month):
    retire_age.set_birth_month(birth_month)


@then('the retirement year is "<retirement_year>"')
def check_retirement_year(retire_age, retirement_year):
    retire_age.calculate_retirement_age()
    assert retire_age.get_retirement_year() == retirement_year

