# -*- coding: utf-8 -*-
"""Step implementations for tutorial example."""

from behavecrackle import *

@given('we have behavecrackle installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behavecrackle will test it for us!')
def step_impl(context):
    assert context.failed is False
