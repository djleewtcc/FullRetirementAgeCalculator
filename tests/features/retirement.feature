# Created by dlee at 11/22/2020
Feature: Retirement Age
  Calculate the retirement information based on the birth information.

  Scenario Outline: Get retirement year and month
    Given the birth year is set to "<birth_year>"
    When the birth month is "<birth_month>"
    Then the retirement year is "<retirement_year>"

    Examples:
      | birth_year | birth_month | retirement_year |
      | 1900       | 1           | 1965            |
      | 1937       | 1           | 2002            |
      | 1938       | 1           | 2003            |
	  | 1938       | 12          | 2004            |
      | 1939       | 1           | 2004            |
	  | 1939       | 12          | 2005            |
      | 1940       | 1           | 2005            |
	  | 1940       | 12          | 2006            |
      | 1941       | 1           | 2006            |
	  | 1941       | 12          | 2007            |
      | 1942       | 1           | 2007            |
	  | 1942       | 12          | 2008            |
      | 1943       | 1           | 2009            |
      | 1954       | 1           | 2020            |
	  | 1955       | 1           | 2021            |
	  | 1955       | 12          | 2022            |
      | 1956       | 1           | 2022            |
	  | 1956       | 12          | 2023            |
      | 1957       | 1           | 2023            |
	  | 1957       | 12          | 2024            |
      | 1958       | 1           | 2024            |
	  | 1958       | 12          | 2025            |
      | 1959       | 1           | 2025            |
	  | 1959       | 12          | 2026            |
      | 1960       | 1           | 2027            |

  Scenario Outline: Get error when entering an invalid month
    Given the valid birth year is set to "<valid_birth_year>"
    When the invalid birth month is "<invalid_birth_month>"
    Then an error is raised
    Examples:
      | valid_birth_year | invalid_birth_month |
      | 1979             | 0                   |
      | 1979             | 13                  |

  Scenario Outline: Get error when entering an invalid month
    Given the valid birth month is set to "<valid_birth_month>"
    When the invalid birth year is "<invalid_birth_year>"
    Then an error is raised
    Examples:
      | valid_birth_month | invalid_birth_year |
      | 7                 | 1899               |
      | 7                 | 2021               |