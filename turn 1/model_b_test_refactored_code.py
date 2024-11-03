from hypothesis import given, strategies as st
import pytest
from refactored_code import ShapeCalculator


@given(st.one_of(st.text('square'), st.text('rectangle')), st.integers(min_value=1))
def test_calculate_area_valid_shapes(shape, length):
    calc = ShapeCalculator()
    assert calc.calculate_area(shape, length) >= 0


@given(st.text('rectangle'), st.integers(min_value=1), st.integers(min_value=1))
def test_calculate_area_rectangle(shape, length, width):
    calc = ShapeCalculator()
    assert calc.calculate_area(shape, length, width) == length * width


@given(st.text())
def test_calculate_area_invalid_shape(shape):
    calc = ShapeCalculator()
    with pytest.raises(ValueError):
        calc.calculate_area(shape, 1)


@given(st.integers(min_value=1))
def test_calculate_square_area(length):
    calc = ShapeCalculator()
    assert calc.calculate_area('square', length) == length * length


if __name__ == "__main__":
    pytest.main()
