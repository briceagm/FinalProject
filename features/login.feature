Feature: Login LIBRARIUS
#  @single
  Scenario: Login successful
    Given I am on the main page
    When I click the "Contul meu" button
    And I input a "johndoe@gmail.com" username
    And I input a "librarius123" password
    And I click the login button
    Then I find the username on the main page

#  @single
  Scenario Outline: Login fail
    Given I am on the main page
    When I click the "Contul meu" button
    And I input a "<username>" username
    And I input a "<password>" password
    And I click the login button
    Then I receive the error message
    Examples: Credentials
    | username          | password     |
    | johndoe@gmail.com | python202    |
    | johndo@gmail.com  | librarius123 |


#  @single
  Scenario: Logout successful
    Given I am on the main page
    When I am logged in successfully with "johndoe@gmail.com" username and "librarius123" password
    And I click the "Contul meu" button to go on the user menu page
    And On the user menu page I click the logout button
    Then I don't find the username on the main page
