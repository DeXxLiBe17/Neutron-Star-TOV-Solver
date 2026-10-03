from eos import PolytropicEOS

K = 1.0e-2
Gamma = 2.000

eos = PolytropicEOS(K, Gamma)

rho = 100.0

P = eos.pressure_from_density(rho)
rho_back = eos.density_from_pressure(P)
epsilon = eos.energy_density_from_pressure(P)

print("Original density:", rho)
print("Pressure:", P)
print("Recovered density:", rho_back)
print("Energy density:", epsilon)

