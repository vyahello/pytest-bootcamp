Feature: A bucket of fruits
 
Scenario: Counting fruits in a bucket
    Given There are 9 fruits in a bucket
    When I have 2 friends
    And I give 3 fruits to my 1st friend
    And I give 3 fruits to my 2nd friend
    Then I should have 3 fruits for myself
