from components import Current, Resistor, Voltage


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
    # Also there seems to be a dependency - No allowed
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
