# To allow pytest to autodetect this test file, its name must start with 'test_'
# Use a similar similar naming convention for test functions within the file.
from app.calculations import add, subtract, multiply, divide, BankAccount
import pytest

@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("a, b, expected", [
    (3, 2, 5),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_add(a, b, expected):
    assert add(a, b) == expected

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 5) == 0

def test_divide():
    assert divide(6, 3) == 2.0
    assert divide(-4, 2) == -2.0
    try:
        divide(5, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero."

def test_bank_ser_initial_amount(bank_account):
    assert bank_account.balance == 50

def test_bank_default_amount(zero_bank_account):
    assert zero_bank_account.balance == 0.0

def test_withdraw():
    bankaccount = BankAccount(100)
    bankaccount.withdraw(40)
    assert bankaccount.balance == 60

def test_deposit():
    bankaccount = BankAccount(100)
    bankaccount.deposit(50)
    assert bankaccount.balance == 150

def test_collect_interest():
    bankaccount = BankAccount(100)
    bankaccount.collect_interest()
    assert bankaccount.balance == 210.0

@pytest.mark.parametrize("deposited, withdrew, expected", [
    (200, 100, 100),
    (50, 10, 40),
    (1200, 200, 1000),
])
def test_bank_transactions(zero_bank_account, deposited, withdrew, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected

def test_insufficient_funds(bank_account):
    with pytest.raises(ValueError) as excinfo:
        bank_account.withdraw(1000)
    assert str(excinfo.value) == "Insufficient funds."