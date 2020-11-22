# Created by dlee at 11/22/2020
Feature: Retirement Age
  Calculate the retirement information based on the birth information.

  Scenario: Get the retirement age
    Given the birth month is 7
    When the birth year is set to 1979
    Then the retirement age year is 2046


