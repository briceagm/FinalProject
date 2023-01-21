Feature: Login LIBRARIUS

  Scenario: Login successful
    Given I am on the main page
    When I click the "Contul meu" button
    And I input a "johndoe@gmail.com" username
    And I input a "librarius123" password
    And I click the login button
    Then I find the username on the main page



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
