class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a
        self.angle_b = 180 - angle_a

    def __setattr__(self, name, value):
        if name == "side_a" and value <= 0:
            raise ValueError("Side length must be greater than 0.")
        if name == "angle_a":
            if not (0 < value < 180):
                raise ValueError("Angle_a must be greater than 0 and less than 180 degrees.")
            object.__setattr__(self, "angle_b", 180 - value)
        object.__setattr__(self, name, value)

    def __repr__(self):
        return f"Rhombus: side_a = {self.side_a}, angle_a = {self.angle_a}, angle_b = {self.angle_b}"


# Example usage
rhombus = Rhombus(20, 50)
print(rhombus)

