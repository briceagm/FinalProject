Feature: Books Menu

  Scenario: Has 11 categories of the books on the menu
    Given I am on the books page
    When I found the books menu
    Then There are 11 categories of the books on the menu

  Scenario: Change number of books per page to 16 books per page
    Given I am on the books page
    When I click the drop and down button 'page filter'
    And I pick the number 16 from the list
    Then There are 16 books on the page

  Scenario: Sort books by the ascending price
    Given I am on the books page
    When I click the drop and down button 'by filter'
    And I pick the option with ascending price
    Then There are books ordered ascending on the page