from tov import tov_derivatives
from eos import PolytropicEOS

# Create our test EOS
K = 1.0e-2
Gamma = 2.0

eos = PolytropicEOS(K, Gamma)

# Choose a test point inside the star
r = 1000.0          # m
rho = 100.0         # kg/m^3

# Get pressure and energy density from EOS
P = eos.pressure_from_density(rho)
epsilon = eos.energy_density_from_density(rho)

# Assume some enclosed mass
m = 1.0e20          # kg

# Calculate TOV derivatives
dm_dr, dP_dr = tov_derivatives(r, m, P, epsilon)

print("Radius:", r, "m")
print("Mass:", m, "kg")
print("Density:", rho, "kg/m^3")
print("Pressure:", P, "Pa")
print("Energy density:", epsilon, "J/m^3")
print()
print("dm/dr:", dm_dr, "kg/m")
print("dP/dr:", dP_dr, "Pa/m")