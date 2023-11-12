Feature: showing off behave

  Scenario: run a simple test
    Given we have behave installed
    When we implement a test
    Then behave will test it for us!

  @wip
  Scenario: should get all wines I am interested in
    Given I am interested in Purlieu
    # TODO: Specify the information in the email somehow
    When I get a new email from K&L Wine Merchants
    Then I should see 'Purlieu "Le Pich" Napa Valley Sauvignon Blanc (Elsewhere $30)'

  # TODO: should tell me the price elsewhere
  # TODO: should tell me the price they are selling it at
