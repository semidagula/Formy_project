import time

from Pages.checkbox_page import CheckboxPage
from Pages.home_page import HomePage
from behave import given, when, then


@given(u'Go to checkboxes')
def step_impl(context):
    print(u'Go to checkboxes')
    home = HomePage(context.driver)
    home.open_checkbox()
    time.sleep(3)


@given(u'I am on Checkbox page')
def step_impl(context):
    print(u'STEP: Given I am on Checkbox page')
    checkbox = CheckboxPage(context.driver)
    assert checkbox.text_checkbox()
    time.sleep(3)


@when(u'I click all checkboxes')
def step_impl(context):
    print(u'STEP: When I click all checkboxes')
    checkbox = CheckboxPage(context.driver)
    checkbox.click_checkbox1()
    checkbox.click_checkbox2()
    checkbox.click_checkbox3()
    time.sleep(3)

@then(u'I want all to be enabled')
def step_impl(context):
    print(u'STEP: Then I want all to be enabled')
    checkbox = CheckboxPage(context.driver)
    checkbox.enabled_checkbox1()
    checkbox.enabled_checkbox2()
    checkbox.enabled_checkbox3()
    time.sleep(3)

@when(u'I click the first checkbox')
def step_impl(context):
    print(u'STEP: When I click the first checkbox')
    checkbox = CheckboxPage(context.driver)
    checkbox.click_checkbox1()
    time.sleep(3)

@then(u'I want only the first checkbox to be enabled')
def step_impl(context):
    print(u'STEP: Then I want only the first checkbox to be enabled')
    checkbox = CheckboxPage(context.driver)
    checkbox.enabled_checkbox1()
    time.sleep(3)

@when(u'I click the second checkbox')
def step_impl(context):
    print(u'STEP: When I click the second checkbox')
    checkbox = CheckboxPage(context.driver)
    checkbox.click_checkbox2()
    time.sleep(3)

@then(u'I want only the second checkbox to be enabled')
def step_impl(context):
    print(u'STEP: Then I want only the second checkbox to be enabled')
    checkbox = CheckboxPage(context.driver)
    checkbox.enabled_checkbox2()
    time.sleep(3)