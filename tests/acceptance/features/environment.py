from behave.model import Scenario  # type: ignore
from behave.runner import Context  # type: ignore


def before_scenario(context: Context, scenario: Scenario):
    if "wip" in scenario.effective_tags:
        scenario.skip("Work in Progress")
    return
