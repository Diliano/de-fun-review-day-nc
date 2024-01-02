import pytest
from src.part_2_vending_machine import VendingMachine

@pytest.mark.describe('All Vending Maching Methods')
class TestVendingMachine:

    @pytest.mark.it('has valid credit attribute')
    def test_credit(self):
        vm = VendingMachine()
        assert vm.credit == 0

    @pytest.mark.it('has expected stock attributes')
    def test_stock(self):
        vm = VendingMachine()
        assert vm.stock['A'] == {}
        assert vm.stock['B'] == {}
        assert vm.stock['C'] == {}

    @pytest.mark.it('adds credit to initial amount')
    def test_add_credit(self):
        vm = VendingMachine()
        vm.add_credit(75)
        assert vm.credit == 75
        new_vm = VendingMachine()
        new_vm.add_credit(62)
        assert new_vm.credit == 62

    @pytest.mark.it('accumulates credit')
    def test_accumulate_credit(self):
        vm = VendingMachine()
        vm.add_credit(19)
        assert vm.credit == 19
        vm.add_credit(33)
        assert vm.credit == 52

    @pytest.mark.it('validates when there is sufficient credit for an item')
    def test_sufficient_credit(self):
        vm = VendingMachine()
        vm.add_credit(36)
        assert vm.credit_checker(30)

    @pytest.mark.it('validates when there is insufficient credit for an item')
    def test_insufficient_credit(self):
        vm = VendingMachine()
        vm.add_credit(36)
        assert not vm.credit_checker(44)
