@smoke @sanity
Feature: Automating OPS Portal

    Scenario: run a simple test

      Given login into the ops portal

      When Enter the valid user id and pwd

      Then user should be able to see home page




    Scenario Outline: Blenders
      Given I  <env> in a blender

      When I switch the blender on

      Then it should transform into <account>

    Examples: Amphibians
    | env | account | | dev | bsm |



   # Examples: Consumer Electronics
   # | thing | other thing | | iPhone | toxic waste | | Galaxy Nexus | toxic waste |