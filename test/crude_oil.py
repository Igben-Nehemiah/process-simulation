"""
Created by ION
"""
from thermo.mixture import Mixture  # type: ignore

# Define main components or fractions of crude oil and their properties
components = {
    # Example properties for light ends fraction
    'C5H12': {'MW': 72.15, 'rho': 0.7},
    # Example properties for naphtha fraction
    'C8H18': {'MW': 114.23, 'rho': 0.8},
    # Example properties for diesel fraction
    'C12H26': {'MW': 170.34, 'rho': 0.85},
    # Example properties for gas oil fraction
    'C16H34': {'MW': 226.44, 'rho': 0.9}
}

# Define composition of crude oil (mole fractions)
fractions = {
    'C5H12': 0.1,
    'C8H18': 0.2,
    'C12H26': 0.3,
    'C16H34': 0.4
}

# Create a Mixture object representing the crude oil
crude_oil_mixture = Mixture(zs=fractions, IDs=components, T=300, P=101325)

# Calculate properties of the crude oil mixture
print("Density:", crude_oil_mixture.rho)  # Density
print("Enthalpy:", crude_oil_mixture.H)   # Enthalpy
print("Entropy:", crude_oil_mixture.S)    # Entropy
# Liquid-phase fractions
# print("Liquid-phase fractions:", crude_oil_mixture.)
# Vapor-phase fractions
# print("Vapor-phase fractions:", crude_oil_mixture.vapor_phase)
print("Molecular weight:", crude_oil_mixture.MW)  # Molecular weight

# Calculate and print properties of individual components
for component, properties in components.items():
    print(f"\nComponent: {component}")
    print("Molecular weight:", properties['MW'])
    print("Density:", properties['rho'])
    # Add more properties as needed

# Liquid-phase properties
# print("Liquid-phase enthalpy:", crude_oil_mixture.H_l)   # Liquid-phase enthalpy
# print("Liquid-phase entropy:", crude_oil_mixture.S)    # Liquid-phase entropy
# Liquid-phase heat capacity
print("Liquid-phase heat capacity:", crude_oil_mixture.Cpl)

# Vapor-phase properties
# print("Vapor-phase enthalpy:", crude_oil_mixture.H_g)   # Vapor-phase enthalpy
# print("Vapor-phase entropy:", crude_oil_mixture.S_g)    # Vapor-phase entropy
# Vapor-phase heat capacity
print("Vapor-phase heat capacity:", crude_oil_mixture.Cpg)
