from constants import c


class PolytropicEOS:

    def __init__(self, K, Gamma):
        self.K = K
        self.Gamma = Gamma

    def pressure_from_density(self, rho):
        return self.K * rho**self.Gamma

    def density_from_pressure(self, P):
        return (P / self.K)**(1 / self.Gamma)

    def energy_density_from_density(self, rho):
        P = self.pressure_from_density(rho)
        return rho * c**2 + P / (self.Gamma - 1)

    def energy_density_from_pressure(self, P):
        rho = self.density_from_pressure(P)
        return self.energy_density_from_density(rho)