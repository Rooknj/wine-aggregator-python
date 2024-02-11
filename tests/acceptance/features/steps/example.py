from behave import given, when, then  # type: ignore
from behave.runner import Context  # type: ignore


@given("we have behave installed")  # type: ignore
def example_given_step_impl(context: Context) -> None:
    pass


@when("we implement a test")  # type: ignore
def example_when_step_impl(context: Context) -> None:
    assert True is not False


@then("behave will test it for us!")  # type: ignore
def example_then_step_impl(context: Context) -> None:
    assert context.failed is False


@given("I am interested in Purlieu")  # type: ignore
def interested_step_impl(context: Context) -> None:
    pass


@when("I get a new email from K&L Wine Merchants")  # type: ignore
def email_step_impl(context: Context) -> None:
    pass


@then("I should see 'Purlieu \"Le Pich\" Napa Valley Sauvignon Blanc (Elsewhere $30)'")  # type: ignore
def should_step_impl(context: Context) -> None:
    pass
