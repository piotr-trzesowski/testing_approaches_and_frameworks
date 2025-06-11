import pytest
from pytest_bdd import scenarios, given, when, then
from calculator import Calculator

scenarios('../calculator.feature')

@given("I have a calculator", target_fixture="calculator")
def calculator():
    return Calculator()

@when('I enter "<a>" and "<b>" into the calculator')
def enter_numbers(calculator, a, b):
    calculator.a = float(a)
    calculator.b = float(b)

@when("I press add")
def press_add(calculator):
    calculator.result = calculator.add(calculator.a, calculator.b)

@when("I press subtract")
def press_subtract(calculator):
    calculator.result = calculator.subtract(calculator.a, calculator.b)

@then('the result should be "<expected>" on the screen')
def verify_result(calculator, expected):
    assert calculator.result == float(expected)