from behave import *


@given("we have behave installed")
def step_impl(context):
    pass


@when("we implement a test")
def step_impl(context):
    assert True is not False


@then("behave will test it for us!")
def step_impl(context):
    assert context.failed is False


@given("I am interested in Purlieu")
def step_impl(context):
    pass


@when("I get a new email from K&L Wine Merchants")
def step_impl(context):
    pass


@then("I should see 'Purlieu \"Le Pich\" Napa Valley Sauvignon Blanc (Elsewhere $30)'")
def step_impl(context):
    pass
