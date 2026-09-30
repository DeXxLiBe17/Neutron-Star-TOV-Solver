"""Internal unit system:
    Length       -> metre (m)
    Mass         -> kilogram (kg)
    Time         -> second (s)
    Energy       -> joule (J)
    Pressure     -> pascal (Pa)
    Energy density -> J/m^3"""

# Fundamental physical constants

#Gravitational constant
G = 6.67430e-11          # m^3 kg^-1 s^-2

# Speed of light in vacuum
c = 299792458.0          # m s^-1

# Planck constant
h = 6.62607015e-34       # J s

# Reduced Planck constant
hbar = 1.054571817e-34   # J s

# Boltzmann constant
k_B = 1.380649e-23       # J K^-1


# Particle masses

#Neutron mass
m_n = 1.67492749804e-27   # kg

# Proton mass
m_p = 1.67262192369e-27   # kg

# Electron mass
m_e = 9.1093837139e-31    # kg

# Atomic mass unit
u = 1.66053906660e-27     # kg


# Astronomical constants

# Solar mass
M_sun = 1.98847e30        # kg


# Useful length scales

km = 1.0e3                # m
fm = 1.0e-15              # m


# Energy conversion

# 1 MeV in joules
MeV = 1.602176634e-13     # J


# Conversion functions

def kg_to_solar_mass(mass_kg):
    #Convert mass from kg to solar masses
    return mass_kg / M_sun


def solar_mass_to_kg(mass_solar):
    #Convert mass from solar masses to kg
    return mass_solar * M_sun


def m_to_km(length_m):
    #Convert length from metres to kilometres
    return length_m / km


def km_to_m(length_km):
    #Convert length from kilometres to metres
    return length_km * km


def mev_fm3_to_j_m3(value):
    
    #Convert energy density from MeV/fm^3 to J/m^3.
    
    return value * MeV / (fm ** 3)


def j_m3_to_mev_fm3(value):
    
    #Convert energy density from J/m^3 to MeV/fm^3.
    return value * (fm ** 3) / MeV