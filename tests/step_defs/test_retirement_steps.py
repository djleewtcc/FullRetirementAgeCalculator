import pytest
from pytest_bdd import scenarios, parsers, given, when, then, exceptions
from full_retirement_age_calculator import FullRetirementAgeCalculator
from datetime import datetime


CONVERTERS = {
    'birth_year': int,
    'birth_month': int,
    'retirement_year': int,
    'retirement_month': int,
    'retirement_age_year': int,
    'retirement_age_months': int
}

scenarios('../features/retirement.feature', example_converters=CONVERTERS)


@pytest.fixture()
@given('the birth month is "<birth_month>"')
def retirement_with_birth_month(birth_month):
    return FullRetirementAgeCalculator(birth_month=birth_month)


@when('the birth year is set to "<birth_year>"')
def set_birth_year(retirement_with_birth_month, birth_year):
    retirement_with_birth_month.set_birth_year(birth_year)


@then('the retirement age year is "<retirement_age_year>"')
def get_retirement_age_year(retirement_with_birth_month, retirement_age_year):
    retirement_with_birth_month.calculate_retirement_age()
    assert retirement_with_birth_month.get_retirement_age_year() == retirement_age_year


@then('the retirement age month is "<retirement_age_months>"')
def get_retirement_age_month(retirement_with_birth_month, retirement_age_months):
    assert retirement_with_birth_month.get_retirement_age_month() == retirement_age_months


@pytest.fixture()
@given('the birth year is "<birth_year>"')
def retirement_with_birth_year(birth_year):
    return FullRetirementAgeCalculator(birth_year=birth_year)


@when('the birth month is set to "<birth_month>"')
def set_birth_month(retirement_with_birth_year, birth_month):
    retirement_with_birth_year.set_birth_month(birth_month)


@then('the retirement year is "<retirement_year>"')
def get_retirement_year(retirement_with_birth_year, retirement_year):
    retirement_with_birth_year.calculate_retirement_age()
    assert retirement_with_birth_year.get_retirement_year() == retirement_year


@then('the retirement month is "<retirement_month>"')
def get_retirement_month(retirement_with_birth_year, retirement_month):
    assert retirement_with_birth_year.get_retirement_month() == retirement_month


@when('the invalid birth month is set to "<birth_month>"')
def set_invalid_birth_month(retirement_with_birth_year, birth_month):
    with pytest.raises(ValueError):
        retirement_with_birth_year.set_birth_month(birth_month)


@then("an error is generated")
def error_func():
    pass


@pytest.fixture()
@given("the birth day and month is the default value")
def retirement_default():
    return FullRetirementAgeCalculator()


@when("the birth year is one year greater than the current year")
def set_invalid_high_birth_year(retirement_default):
    with pytest.raises(ValueError):
        retirement_default.set_birth_year(datetime.now().year + 1)


@when("the birth year is 1899")
def set_invalid_low_birth_year(retirement_default):
    with pytest.raises(ValueError):
        retirement_default.set_birth_year(1899)


@given("start with the birth year is one year greater than the current year")
def retirement_with_invalid_high_birth_year():
    with pytest.raises(ValueError):
        return FullRetirementAgeCalculator(birth_year=datetime.now().year + 1)


@given("start with the birth year is 1899")
def retirement_with_invalid_low_birth_year():
    with pytest.raises(ValueError):
        return FullRetirementAgeCalculator(birth_year=1899)


@given('start with the invalid birth month is set to "<birth_month>"')
def retirement_with_invalid_birth_month(birth_month):
    with pytest.raises(ValueError):
        return FullRetirementAgeCalculator(birth_month=birth_month)
