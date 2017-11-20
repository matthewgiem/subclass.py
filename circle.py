class Circle:
    def __init__(self, diameter):
        self.diameter = diameter

    @property
    def radius(self):
        return self.diameter / 2

    @radius.setter
    def radius(self, new_radius):
        print("new setter")
        self.diameter = new_radius * 2

small = Circle(10)
print("the diamter of the circle is {}".format(small.diameter))
print("the radius of the circle is {}".format(small.radius))
# change the radius of the Circle
small.radius = 20
print("we changed the radius to be 20")
print("the diameter of the circle is {}".format(small.diameter))
print("the radius of the circle is {}".format(small.radius))
