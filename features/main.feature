Feature: Main Page

  Scenario: Search product
    Given I am on the main page Librarius
    When I click on the search box
    And I input the name of the book "Alchimistul"
    And I click on the search button
    Then I am on the page with the results and I found the book "Alchimistul"

  Scenario: Add product to cart
    Given I am on the main page Librarius
    When I click on the search box
    And I input the name of the book "Alchimistul"
    And I click on the search button
    And I click on the book "Alchimistul"
    And I click on the add to cart button
    Then The cart button is incremented by one

   Scenario: Go to Books Page
     Given I am on the main page Librarius
     When I click books button
     Then I am on the books page

   Scenario: Delete product from cart
     Given I am on the main page Librarius
     When I add an product "Alchimistul" to cart
     And I click the basket button
     And I click on the delete icon
     Then The cart counter becomes 0

   Scenario: Has 47 locations of points of sales
     Given I am on the main page Librarius
     When I click the 'Librarii' button
     Then There are 47 locations of point of sales