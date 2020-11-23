import calendar
from datetime import datetime


class FullRetirementAgeCalculator:

    def __init__(self, birth_year=1900, birth_month=1):
        if birth_month < 1 or birth_month > 12:
            raise ValueError('The month value must be an integer from 1 to 12.')

        if birth_year < 1900 or birth_year > datetime.now().year:
            raise ValueError('The year value must be an integer from 1900 to the current year.')

        self._birth_year = birth_year
        self._birth_month = birth_month

        self._retirement_age_year = 0
        self._retirement_age_month = 0
        self._retirement_year = 0
        self._retirement_month = 0

    def calculate_retirement_age(self):
        if 1900 <= self._birth_year <= 1937:
            self._retirement_age_year = 65
        elif self._birth_year == 1938:
            self._retirement_age_year = 65
            self._retirement_age_month = 2
        elif self._birth_year == 1939:
            self._retirement_age_year = 65
            self._retirement_age_month = 4
        elif self._birth_year == 1940:
            self._retirement_age_year = 65
            self._retirement_age_month = 6
        elif self._birth_year == 1941:
            self._retirement_age_year = 65
            self._retirement_age_month = 8
        elif self._birth_year == 1942:
            self._retirement_age_year = 65
            self._retirement_age_month = 10
        elif 1943 <= self._birth_year <= 1954:
            self._retirement_age_year = 66
        elif self._birth_year == 1955:
            self._retirement_age_year = 66
            self._retirement_age_month = 2
        elif self._birth_year == 1956:
            self._retirement_age_year = 66
            self._retirement_age_month = 4
        elif self._birth_year == 1957:
            self._retirement_age_year = 66
            self._retirement_age_month = 6
        elif self._birth_year == 1958:
            self._retirement_age_year = 66
            self._retirement_age_month = 8
        elif self._birth_year == 1959:
            self._retirement_age_year = 66
            self._retirement_age_month = 10
        elif self._birth_year >= 1960:
            self._retirement_age_year = 67

        # Calculate the year and month or retirement
        self._retirement_year = self._birth_year + self._retirement_age_year
        self._retirement_month = int(self._birth_month) + int(self._retirement_age_month)

        # Adjust year and month of the month value is greater than 12
        if self._retirement_month >= 12:
            self._retirement_year += self._retirement_month // 12
            self._retirement_month = self._retirement_month % 12

    def set_birth_year(self, birth_year):
        if birth_year < 1900 or birth_year > datetime.now().year:
            raise ValueError('The year value must be an integer from 1900 to the current year.')

        self._birth_year = birth_year

    def set_birth_month(self, birth_month):
        if birth_month < 1 or birth_month > 12:
            raise ValueError('The month value must be an integer from 1 to 12.')

        self._birth_month = birth_month

    def get_retirement_age_year(self):
        return self._retirement_age_year

    def get_retirement_age_month(self):
        return self._retirement_month

    def get_retirement_year(self):
        return self._retirement_year

    def get_retirement_month(self):
        return self._retirement_month


def main():
    # Display the program information
    print('Social Security Full Retirement Age Calculator')

    birth_year = input('Enter the year of birth or to exit ')

    while birth_year != "":
        birth_month = int(input('Enter the month of birth '))

        retirement = FullRetirementAgeCalculator(int(birth_year), birth_month)

        retirement.calculate_retirement_age()

        # Display the results to user
        print('your full retirement age is', retirement.get_retirement_age_year(), 'and',
              retirement.get_retirement_age_month(), 'months')
        print('this will be in', calendar.month_name[retirement.get_retirement_month()], 'of',
              retirement.get_retirement_year())

        birth_year = input('Enter the year of birth or to exit ')

