Feature: Retirement Age
  Calculate the retirement information based on the birth information.

  Scenario Outline: Get the retirement age
    Given the birth month is "<birth_month>"
    When the birth year is set to "<birth_year>"
    Then the retirement age year is "<retirement_age_year>"
    And the retirement age month is "<retirement_age_months>"

    Examples:
      | birth_month | birth_year | retirement_age_year | retirement_age_months |
      | 1           | 1900       | 65                  | 0                     |
      | 1           | 1937       | 65                  | 0                     |
      | 1           | 1938       | 65                  | 2                     |
      | 1           | 1939       | 65                  | 4                     |
      | 1           | 1940       | 65                  | 6                     |
      | 1           | 1941       | 65                  | 8                     |
      | 1           | 1942       | 65                  | 10                    |
      | 1           | 1943       | 66                  | 0                     |
      | 1           | 1954       | 66                  | 0                     |
      | 1           | 1955       | 66                  | 2                     |
      | 1           | 1956       | 66                  | 4                     |
      | 1           | 1957       | 66                  | 6                     |
      | 1           | 1958       | 66                  | 8                     |
      | 1           | 1959       | 66                  | 10                    |
      | 1           | 1960       | 67                  | 0                     |


  Scenario Outline: Get retirement year and month
    Given the birth year is "<birth_year>"
    When the birth month is set to "<birth_month>"
    Then the retirement year is "<retirement_year>"
    And the retirement month is "<retirement_month>"

    Examples:
      | birth_year | birth_month | retirement_year | retirement_month |
      | 1900       | 1           | 1965            | 1                |
      | 1937       | 1           | 2002            | 1                |
      | 1938       | 1           | 2003            | 3                |
	  | 1938       | 12          | 2004            | 2                |
      | 1939       | 1           | 2004            | 5                |
	  | 1939       | 12          | 2005            | 4                |
      | 1940       | 1           | 2005            | 7                |
	  | 1940       | 12          | 2006            | 6                |
      | 1941       | 1           | 2006            | 9                |
	  | 1941       | 12          | 2007            | 8                |
      | 1942       | 1           | 2007            | 11               |
	  | 1942       | 12          | 2008            | 10               |
      | 1943       | 1           | 2009            | 1                |
      | 1954       | 1           | 2020            | 1                |
	  | 1955       | 1           | 2021            | 3                |
	  | 1955       | 12          | 2022            | 2                |
      | 1956       | 1           | 2022            | 5                |
	  | 1956       | 12          | 2023            | 4                |
      | 1957       | 1           | 2023            | 7                |
	  | 1957       | 12          | 2024            | 6                |
      | 1958       | 1           | 2024            | 9                |
	  | 1958       | 12          | 2025            | 8                |
      | 1959       | 1           | 2025            | 11               |
	  | 1959       | 12          | 2026            | 10               |
      | 1960       | 1           | 2027            | 1                |


  Scenario Outline: Set invalid value for birth month
    Given the birth year is "<birth_year>"
    When the invalid birth month is set to "<birth_month>"
    Then an error is generated

    Examples:
      | birth_year | birth_month |
      | 1900       | 0           |
      | 1900       | 13          |


  Scenario: Set invalid high year
    Given the birth day and month is the default value
    When the birth year is one year greater than the current year
    Then an error is generated


  Scenario: Set invalid low year
    Given the birth day and month is the default value
    When the birth year is 1899
    Then an error is generated


  Scenario: Start with invalid high year
    Given start with the birth year is one year greater than the current year
    Then an error is generated


  Scenario: Start with invalid low year
    Given start with the birth year is 1899
    Then an error is generated


  Scenario Outline: Start with invalid value for birth month
    Given start with the invalid birth month is set to "<birth_month>"
    Then an error is generated

    Examples:
      | birth_month |
      | 0           |
      | 13          |