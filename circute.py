#!/usr/bin/python3
# Developer: Otumian-empire
# email: popecan1000@gmail.com
# GitHub: https://www.github.com/Otumian-empire
# Program: A simple program the demonstrate basic circuitory/electricity
# concept involving ohms law, V=IR
# Run: ./circuit.py or python3 circuit.py

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


class Circuit:
    """ Circuit board takes electronics components such as the resistor,
     current and voltage instance """

    def __init__(self, *components):
        self.board = list(components)

    def add(self, *components):
        """ Add an extra component to the board """
        self.board.extend(components)

    def remove(self, *components):
        """ Remove a component from the board """
        for component in components:
            self.board.remove(component)

    def display_circuit_board(self):
        """ Print a description of the components on the circuit board """
        print("Circuit board is made of:")
        for component in self.board:
            print(component)


class CircuitAlgebra:

    def __init__(self, circuit):
        self.circuit = circuit

    def component_detail(self, component_type=None):
        """ Returns the number of components of type `component_type` and their sum """
        num_components = 0
        sum_components = 0

        if component_type != None:

            for component in self.circuit.board:
                if type(component) == component_type:
                    num_components += 1
                    sum_components += component.magnitude

        return [num_components, sum_components]

    # Rewrite `circuit_details` in a generalized version so that the
    # function itself can tell what components it is made up of
    def circuit_details(self):
        """ Returns the details of the components on the board, for the Voltages, 
        the Currents and Resistors """
        res = self.component_detail(Resistor)
        volt = self.component_detail(Voltage)
        cur = self.component_detail(Current)

        return f"Res({res[0]}: {res[1]}), Cur({cur[0]}: {cur[1]}), Volt({volt[0]}: {volt[1]})"

    def evaluate_board(self):
        """ Evaluates and then calls the `self.circuit_detail` to prints
         details of the components on the board  """
        res = self.component_detail(Resistor)
        volt = self.component_detail(Voltage)
        cur = self.component_detail(Current)

        if not volt[0]:
            # v=ir
            volt[0] = 1
            volt[1] = cur[1] * res[1]
            self.circuit.add(Voltage(volt[1]))

        elif not cur[0]:
            # i=v/r
            cur[0] = 1
            cur[1] = volt[1] / res[1]
            self.circuit.add(Current(cur[1]))

        elif not res[0]:
            # r=v/i
            res[0] = 1
            res[1] = volt[1] / cur[1]
            self.circuit.add(Resistor(res[1]))

        else:
            if volt[1] != cur[1] * res[1]:
                print(
                    "Board inaccurate - voltage does not \
                        correspond to the current and resistance.")

        print(self.circuit_details())


# The components to use
v = Voltage(4.5)
r1 = Resistor(4.0)
r2 = Resistor(4.5)
# i = Current(2.5)

# A circuit instance to mount the components
cir = Circuit(r1, r2, v)
cir.display_circuit_board()

# An Algebraic instance of the circuit to evaluate the
alg = CircuitAlgebra(cir)
print(alg.circuit_details())
alg.evaluate_board()
