Feature: Login

  Scenario: Successful login
    Given I am on the login page
    When I enter valid credentials
    Then I should be redirected to the dashboard

  Scenario: Unsuccessful login
    Given I am on the login page
    When I enter invalid credentials
    Then I should see an error message