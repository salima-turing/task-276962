import unittest
from hypothesis import given, strategies as st


# Code under test (CUT)
def calculate_area(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise ValueError("Length and width must be numeric")
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive")
    return length * width


# Redesigned function to handle more diverse cases
def revised_calculate_area(length, width):
    try:
        length = float(length)
        width = float(width)
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive")
        return length * width
    except ValueError as ve:
        raise ve


class TestCalculateArea(unittest.TestCase):

    @given(length=st.floats(min_value=0.1, max_value=100), width=st.floats(min_value=0.1, max_value=100))
    def test_positive_float_inputs(self, length, width):
        result = revised_calculate_area(length, width)
        self.assertAlmostEqual(result, length * width)

    @given(length=st.integers(min_value=1, max_value=100), width=st.integers(min_value=1, max_value=100))
    def test_positive_integer_inputs(self, length, width):
        result = revised_calculate_area(length, width)
        self.assertEqual(result, length * width)

    @given(length=st.one_of(st.text(), st.lists()))
    def test_invalid_input_types(self, length):
        with self.assertRaises(ValueError):
            revised_calculate_area(length, 1)

    @given(st.floats(allow_nan=False, allow_infinity=False))
    def test_non_positive_values(self, value):
        with self.assertRaises(ValueError):
            revised_calculate_area(value, 1)
            revised_calculate_area(1, value)


if __name__ == '__main__':
    unittest.main()
