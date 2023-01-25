# QA Automation Project - BDD Tests 

Project details

For this project I decide to make some tests on website of a bookstore named Librarius.

Librarius is a website of a bookstore where a logged-in or non-logged-in user can order books, games and school supplies.

The project contains 3 features, 14 scenarios and 64 steps. All of them passes successful.

The first feature 'Login LIBRARIUS' has 4 scenarios:
1. Login successful
2. Login fail with credentials: username: johndoe@gmail.com and password: python202
3. Login fail with credentials: username: johndo@gmail.com and password: librarius123
4. Logout successful

The second feature 'Main Page' has 6 scenarios:
1. Search product
2. Add product to cart
3. Go to Books Page
4. Delete product from cart
5. Has 47 locations of points of sales
6. Verify the sidebar functionality

The third feature 'Books Menu' has 4 scenarios:
1. Has 11 categories of the books on the menu
2. Change number of books per page to 16 books per page
3. Sort books by the ascending price
4. Check the logo button

To create this project I used the Python programming language with the PyCharm IDE.

Software Library from Python, I used:
1. selenium
2. behave (BDD library that interprets and runs tests written in gherkin)
3. behave-html-formatter (helps generate BDD reports)
4. webdriver-manager.

Steps to use the project:
1. Download or clone the project from GitHub with the command: git clone https://github.com/briceagm/FinalProject
2. Install the necessary libraries with the command: pip install -r .\requirements.txt
3. Run the tests with the command: behave
4. To create the HTML report of the tests, use the command: behave -f html -o report.html
5. To access the reports, look for the generated HTML file in the project folder and open it in a browser.