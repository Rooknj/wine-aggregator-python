from behave.model import Scenario
from behave.runner import Context


def before_scenario(context: Context, scenario: Scenario):
    if "wip" in scenario.effective_tags:
        scenario.skip("Work in Progress")
    return
