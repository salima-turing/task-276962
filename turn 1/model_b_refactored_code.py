# After refactoring
class ShapeCalculator:
    def calculate_area(self, shape, length, width=None):
        method = getattr(self, f'calculate_{shape}_area', None)
        if method is None:
            raise ValueError("Invalid shape")
        return method(length, width)

    def calculate_square_area(self, length, _):
        return length * length

    def calculate_rectangle_area(self, length, width):
        if width is None:
            raise ValueError("Width is required for a rectangle.")
        return length * width
