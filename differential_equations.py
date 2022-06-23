import numpy as np
from cosmology import Cosmology

class DifferentialEquation(Cosmology):

    def select_model(self, model):
        # This should select the function for the ode based on "model"
        return 0

    def lcdm_ode(self, scalefactor, vector):
        factor_D = -1.5 * self.compute_omega_m_evo(scalefactor) / \
            (scalefactor * self.adimensional_hubble_factor(scalefactor))**2
        factor_dD = 3 * (1 - 0.5 * self.compute_omega_m_evo(scalefactor) / \
                         self.adimensional_hubble_factor(scalefactor)**2) / scalefactor
        u, udot = vector[0], vector[1]
        udotdot = - factor_dD * udot - factor_D * u

        return np.r_[udot, udotdot]

    def model_ode(self, scalefactor, vector):
        # Differential equation for other models
        return 0.
