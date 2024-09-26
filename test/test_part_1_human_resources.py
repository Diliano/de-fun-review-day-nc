from src.part_1_human_resources import make_name_tags, create_poll
import pytest
from copy import deepcopy

@pytest.fixture
def guests():
    return [
        {
            'title': 'Mr',
            'forename': 'Sam',
            'surname': 'Caine',
            'age': 30,
            'company': 'Northcoders',
        },
        {
            'title': 'Mr',
            'forename': 'Kermit',
            'surname': 'The Frog',
            'age': 35,
            'company': 'Jim Henson Studios',
        }
    ]   

@pytest.fixture
def updated_guests():
    return [
        {
            'title': 'Mr',
            'forename': 'Sam',
            'surname': 'Caine',
            'age': 30,
            'company': 'Northcoders',
            'name_tag': 'Mr Sam Caine, Northcoders',
        },
        {
            'title': 'Mr',
            'forename': 'Kermit',
            'surname': 'The Frog',
            'age': 35,
            'company': 'Jim Henson Studios',
            'name_tag': 'Mr Kermit The Frog, Jim Henson Studios'
        }
    ]

class TestMakeNameTags:
    def test_returns_an_empty_list_when_given_an_empty_list(self):
        assert make_name_tags([]) == []

    def test_adds_formatted_name_tag_to_guest_dictionaries(self, guests, updated_guests):
        # Arrange
        test_input = guests
        # Act
        result = make_name_tags(test_input)
        # Assert
        assert result == updated_guests

    def test_original_list_is_unchanged(self, guests):
        # Arrange 
        test_input = guests
        copy_test_input = deepcopy(guests)
        # Act
        make_name_tags(test_input)
        # Assert
        assert test_input == copy_test_input