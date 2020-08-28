class NegativeParameterError(ValueError):
    def __init__(self, message, value):
        self.message = message
        self.value = value

    def __str__(self):
        return f"{self.message}, value got: {self.value}"


class WheelDriveTypeError(TypeError):
    def __init__(self, mode):
        self.mode = mode

    def __str__(self):
        return f"SportCar wheel drive can be full, front or rear, value got: {self.mode}"
