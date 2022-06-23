import numpy as np

class Cosmology:

    def __init__(self, cosmo_dictionary):

        # Mandatory cosmological parameters
        self.h    = cosmo_dictionary['h']
        self.Ob = cosmo_dictionary['Ob']
        self.Oc = cosmo_dictionary['Oc']

        # Optional cosmological parameters, if not specified
        # use default values
        self.Ok   = cosmo_dictionary['Ok'] \
            if 'Ok' in cosmo_dictionary else 0.
        self.Mnu  = cosmo_dictionary['Mnu'] \
            if 'Mnu' in cosmo_dictionary else 0.
        self.w0    = cosmo_dictionary['w0'] \
            if 'w0' in cosmo_dictionary else -1.
        self.wa    = cosmo_dictionary['wa'] \
            if 'wa' in cosmo_dictionary else 0.

        # Derived parameters
        self.Om = self.Ob + self.Oc
        self.Omh2 = self.Om * self.h**2
        self.OLambda = 1. - self.Om - self.Ok

    def scale_factor_from_redshift(self, redshift):
        """Returns the scale factor a correspondent to redshift z
        """
        return 1./(1.+redshift)

    def compute_omega_m_evo(self, scalefactor):
        """Computes the time evolution of the matter density
        """
        return self.Om / scalefactor**3

    def dark_energy_evolution(self, scalefactor):
        """Dark energy density evolution as function of scalefactor.
        """
        return (1 / scalefactor)**(3.*(1. + self.w0 + self.wa)) * \
            np.exp(-3.*self.wa*(1. - scalefactor))

    def adimensional_hubble_factor(self, scalefactor):
        """Computes the adimensional Hubble factor
        """
        DE_evo = self.dark_energy_evolution(scalefactor) 
        return np.sqrt(self.OLambda * DE_evo + self.compute_omega_m_evo(scalefactor))

    def dhubble_da(self, scalefactor):
        """Computes the derivative of the adimensional Hubble factor
        with respect to the scale factor
        """
        factor = - 1.5 * self.Om / (scalefactor**3 *
                                    self.adimensional_hubble_factor(scalefactor))
        return factor / self.adimensional_hubble_factor(scalefactor)
