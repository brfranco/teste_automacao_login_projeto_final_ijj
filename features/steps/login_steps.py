from behave import given, when, then
from login import login

@given('I am on the login page')
def step_given_i_am_on_the_login_page(context):
    context.url = "https://projetofinal.jogajuntoinstituto.org/"

@when('I enter valid credentials')
def step_when_i_enter_valid_credentials(context):
    context.result = login(context.url, "brfranco@gmail.com", "wonzuh-xutgoc-Pyfcy7")

@when('I enter invalid credentials')
def step_when_i_enter_invalid_credentials(context):
    context.result = login(context.url, "wronguser", "wrongpassword")

@then('I should be redirected to the dashboard')
def step_then_i_should_be_redirected_to_the_dashboard(context):
    assert context.result is True

@then('I should see an error message')
def step_then_i_should_see_an_error_message(context):
    assert context.result is False