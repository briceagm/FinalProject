Feature: LIBRARIUS Login

  Scenario: Login successful
    Given I am on the main page
    When I click the "Contul meu" button
    And I input a "johndoe@gmail.com" username
    And I input a "librarius123" password
    And I click the login button
    Then I find the username on the main page
