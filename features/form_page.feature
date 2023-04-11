Feature: Add a content to the form
  As a user
  I want to be welcome
  So that I know I am on the right spot

  Background:
    When Logo is displayed

  @regression
  Scenario Outline: Populate multiple fields
    Given Go to Form Page
    When I enter first name "<first_name>"
    And I enter first name "<last_name>"
    And click submit
    Then A success message should be displayed.
    Examples:
      | first_name | last_name  |
      | Ana        | Banana     |
      | Ileana     | Cosanzeana |
      | Ion        | Creanga    |




