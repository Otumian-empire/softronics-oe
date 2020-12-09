#!/usr/bin/python3
# Developer: Otumian-empire
# email: popecan1000@gmail.com
# GitHub: https://github.com/Otumian-empire/softronics-oe
# Program: A simple program the demonstrate basic circuitory/electricity
# concept involving ohms law, V=IR
# Run: ./app.py or python3 app.py

from circuit import Circuit
from circuit_algebra import CircuitAlgebra
from components import Current, Resistor, Voltage

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
