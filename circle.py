class Circle:
    def __init__(slef, diameter):
        self.diameter = diameter

    @property
    def radius(self):
        return self.diameter / 2

small = circle(10)
