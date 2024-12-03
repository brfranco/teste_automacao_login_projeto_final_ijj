from behave import given, when, then
from login import login

@given('que estou na página de login')
def step_given_i_am_on_the_login_page(context):
    context.url = "https://projetofinal.jogajuntoinstituto.org/"

@when('eu insiro credenciais válidas')
def step_when_i_enter_valid_credentials(context):
    context.result = login(context.url, "brfranco@gmail.com", "wonzuh-xutgoc-Pyfcy7")

@when('eu insiro credenciais inválidas')
def step_when_i_enter_invalid_credentials(context):
    context.result = login(context.url, "wronguser@example.com", "wrongpassword")

@then('eu devo ser redirecionado para o painel')
def step_then_i_should_be_redirected_to_the_dashboard(context):
    assert context.result is True

@then('eu devo ver uma mensagem de erro')
def step_then_i_should_see_an_error_message(context):
    assert context.result is False