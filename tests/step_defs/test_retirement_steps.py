from pytest_bdd import scenario, given, when, then

from full_retirement_age_calculator import FullRetirementAgeCalculator


@scenario('../features/retirement.feature', 'Get the retirement age')
def test_add():
    pass


@given("the birth month is 7")
def retire_age():
    return FullRetirementAgeCalculator(birth_month=7)


@when("the birth year is set to 1979")
def set_year(retire_age):
    retire_age.set_birth_year(1979)


@then("the retirement age year is 2046")
def step_impl(retire):
    retire.calculate_retirement_age()
    assert retire.get_retirement_age_year() == 2046