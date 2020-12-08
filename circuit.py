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

