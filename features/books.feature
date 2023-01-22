Feature: Books Menu

#  @single
  Scenario: Has 11 categories of the books on the menu
    Given I am on the books page
    When I found the books menu
    Then There are 11 categories of the books on the menu
#@single
  Scenario: Change number of books per page to 16 books per page
    Given I am on the books page
    When I click the drop and down button with number
    And I pick the number 16 from the list
    Then There are 16 books on the page