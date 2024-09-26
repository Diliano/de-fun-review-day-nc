from src.part_5_recursion import flatten


class TestFlatten:
    def test_returns_empty_list_when_given_empty_list(self):
        assert flatten([]) == []

    def test_returns_given_list_if_unnested(self):
        assert flatten([1, 2, 3]) == [1, 2, 3]

    def test_flattens_list_containing_one_nested_list_with_default_depth_1(self):
        assert flatten([1, 2, [3, 4]]) == [1, 2, 3, 4]

    def test_flattens_list_containing_multiple_nested_lists_with_default_depth_1(self):
        # Arrange
        test_input = [1, 2, [3, [4, [5, 6]]]]
        expected = [1, 2, 3, [4, [5, 6]]]
        # Act
        result = flatten(test_input)
        # Assert
        assert result == expected

    def test_flattens_list_containing_multiple_nested_lists_with_given_depth(self):
        # Arrange
        test_input = [1, 2, [3, [4, [5, 6]]]]
        test_depth = 2
        expected = [1, 2, 3, 4, [5, 6]]
        # Act
        result = flatten(test_input, test_depth)
        # Assert
        assert result == expected

        # Arrange
        test_input = [1, 2, [3, [4, [5, 6]]]]
        test_depth = 3
        expected = [1, 2, 3, 4, 5, 6]
        # Act
        result = flatten(test_input, test_depth)
        # Assert
        assert result == expected

        # Arrange
        test_input = [1, 2, [3, [4, [5, 6]]]]
        test_depth = 25
        expected = [1, 2, 3, 4, 5, 6]
        # Act
        result = flatten(test_input, test_depth)
        # Assert
        assert result == expected