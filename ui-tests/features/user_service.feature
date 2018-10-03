Feature: testing user service demo

  Scenario: AC 1: Live
      # Given an user opens his browser
      # When user hit "http://127.0.0.1:3000" in browser
      # Then website should open correctly.

      When we visit "http://127.0.0.1:3000"
      Then it should have a title "User Service Demo"

  Scenario: AC 2: Verify UI
      # Given user open the website
      # When user look at UI
      # Then UI count box is present
      # And which shows total available users in database

      Then user count is visible in UI
      And user count shows there are "0" users

  Scenario: AC 3: Add user Interface
      # Given user open the website
      # When user click on the "Add user button"
      # Then user can see UI showing fields to add a user

      When user click on the "Add user button"
      Then user can see UI showing fields "Name, Email, Birthday, Address" in this order


  Scenario Outline: AC 4: Adding a user
      # Given user open the website
      # And he clicks on add button
      # And he fills up data
      # When He clicks on the submit button
      # Then user is added

      When user feel <data> in form
      And click on "Add User" button

      Examples:
        | data  |
        | Samir Roy,samir.roy@gmail.com,1990-10-10,32 Brooklyn NY |


  Scenario: AC 5: Verify record count
      # Given user open the website
      # When he checks total users listed in UI
      # Then it matches with counnt shown in ui

      Then there are 1 records in UI
      And user count shows there are "0" users

  Scenario Outline: AC 6: Update user Interface
  Given user is in website
  When user click on any users

      When user click on user panel containing name "Samir Roy"
      Then user can see UI showing fields "Name, Email, Birthday, Address" in this order with data
      And user can see a button with text "Update"
      And user can see a button with text "Delete"
      And user can see a button with text "Go Back"

      Examples:
        | data  |
        | Samir Roy,samir.roy@gmail.com,1990-10-10,32 Brooklyn NY |
