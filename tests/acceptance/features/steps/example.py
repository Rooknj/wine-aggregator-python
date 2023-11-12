from behave import given, when, then


@given("we have behave installed")
def example_given_step_impl(context):
    pass


@when("we implement a test")
def example_when_step_impl(context):
    assert True is not False


@then("behave will test it for us!")
def example_then_step_impl(context):
    assert context.failed is False


@given("I am interested in Purlieu")
def interested_step_impl(context):
    pass


@when("I get a new email from K&L Wine Merchants")
def email_step_impl(context):
    pass


@then("I should see 'Purlieu \"Le Pich\" Napa Valley Sauvignon Blanc (Elsewhere $30)'")
def should_step_impl(context):
    pass
