Feature: Main Page

#  @single
  Scenario: Search product
    Given I am on the main page Librarius
    When I click on the search box
    And I input the name of the book "Alchimistul"
    And I click on the search button
    Then I am on the page with the results and I found the book "Alchimistul"

#  @single
  Scenario: Add product to cart
    Given I am on the main page Librarius
    When I click on the search box
    And I input the name of the book "Alchimistul"
    And I click on the search button
    And I click on the book "Alchimistul"
    And I click on the add to cart button
    Then The cart button is incremented by one

#  @single
   Scenario: Go to Books Page
     Given I am on the main page Librarius
     When I click books button
     Then I am on the books page