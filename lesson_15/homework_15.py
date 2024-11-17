class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a
        self.angle_b = 180 - angle_a  # Automatically calculate angle_b

    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("Side length must be greater than 0.")
            object.__setattr__(self, name, value)
        elif name == "angle_a":
            if not (0 < value < 180):
                raise ValueError("Angle_a must be greater than 0 and less than 180 degrees.")
            object.__setattr__(self, name, value)
            object.__setattr__(self, "angle_b", 180 - value)
        elif name == "angle_b":
            if not (0 < value < 180):
                raise ValueError("Angle_b must be greater than 0 and less than 180 degrees.")
            object.__setattr__(self, name, value)
            object.__setattr__(self, "angle_a", 180 - value)
        else:
            object.__setattr__(self, name, value)

    def __repr__(self):
        return f"Rhombus: side_a = {self.side_a}, angle_a = {self.angle_a}, angle_b = {self.angle_b}"


# Example usage
rhombus = Rhombus(10, 60)
print(rhombus)  # Outputs: Rhombus: side_a = 10, angle_a = 60, angle_b = 120

rhombus.angle_b = 70
print(rhombus)  # Outputs: Rhombus: side_a = 10, angle_a = 110, angle_b = 70
