Feature: Jules Sign in

  Scenario: Succes Log in with valid email and password
    Given I am on the Sign in page
    When I input a valid email
    And I input a valid password
    And I click the Log in button
    Then I receive the Succes message
    And I am on the main page

