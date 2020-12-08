class Resistor:
    """ A Resistor of 1 ohms by default """

    def __init__(self, mag=1):
        self.magnitude = mag

    def __str__(self):
        return f"{self.magnitude} ohms Resistor"


class Current:
    """ A current of 1 ampere by default """

    def __init__(self, mag=1):
        self.magnitude = mag

    def __str__(self):
        return f"Current of {self.magnitude} amperes"


class Voltage:
    """ A 1 volt Voltage supply """

    def __init__(self, mag=0):
        self.magnitude = mag

    def __str__(self):
        return f"{self.magnitude} volts Voltage supply"
