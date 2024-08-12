import pytest
from src.part_2_vending_machine import VendingMachine


@pytest.fixture(scope="function")
def machine():
    return VendingMachine()


class TestVendingMachine:
    def test_initial_credit_set_to_0(self, machine):
        assert machine.credit == 0

    def test_initial_stock(self, machine):
        assert machine.stock["A"] == {}
        assert machine.stock["B"] == {}
        assert machine.stock["C"] == {}

    def test_add_credit_method_sets_credit_attribute(self, machine):
        machine.add_credit(75)
        assert machine.credit == 75
        new_machine = VendingMachine()
        new_machine.add_credit(62)
        assert new_machine.credit == 62

    def test_add_credit_increases_current_credit(self, machine):
        machine.add_credit(19)
        assert machine.credit == 19
        machine.add_credit(33)
        assert machine.credit == 52

    def test_credit_checker_returns_true_for_sufficient_credit(self, machine):
        machine.add_credit(36)
        assert machine.credit_checker(30) is True

    def test_credit_checker_returns_false_for_insufficient_credit(self, machine):
        machine.add_credit(36)
        assert machine.credit_checker(44) is False
