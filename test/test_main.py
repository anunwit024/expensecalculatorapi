import pytest
from main import Summary, Income, Expense, Listpay

def test_initial_values():
    assert Summary == 0
    assert Income == 0
    assert Expense == 0
    assert Listpay == []

def test_add_income():
    amount = 1000
    Listpay.append({
        "Date": "2025-09-10",
        "Type": "Income",
        "Category": "Salary",
        "Amount": amount,
        "Description": "Test Income"
    })
    assert Listpay[-1]["Amount"] == 1000
    assert Listpay[-1]["Type"] == "Income"

def test_add_expense():
    amount = 500
    Listpay.append({
        "Date": "2025-09-10",
        "Type": "Expense",
        "Category": "Food",
        "Amount": amount,
        "Description": "Test Expense"
    })
    assert Listpay[-1]["Amount"] == 500
    assert Listpay[-1]["Type"] == "Expense"
