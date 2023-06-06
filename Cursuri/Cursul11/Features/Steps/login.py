from behave import *

@Given('I am on the Sign in page')
def step_impl(context):
    context.Browser.go_to('sign-in')

@When('I input a valid email')
def step_impl(context):
    valid_email = 'vaman.mihai@yahoo.ro'
    context.Browser.input_email(valid_email)

@When('I input a valid password')
def step_impl(context):
    valid_password = 'Test12test!'
    context.Browser.input_password(valid_password)

@When('I click the Log in button')
def step_impl(context):
    context.Browser.click_login_button()

@Then('I receive the Succes message')
def step_impl(context):
    pass

@Then('I am on the main page')
def step_impl(context):
    pass