#%%
import numpy as np
import matplotlib.pyplot as plt
from astropy.table import QTable
#from photutils.datasets import load_star_image
from photutils.datasets import make_gaussian_sources_image
from photutils.datasets import make_noise_image

class Image():
    def __init__(self, shape):
        self.shape=shape

    def load_image(self, n_sources):
        table = QTable()
        table['amplitude'] = np.random.rand(n_sources)*100
        table['x_mean'] = np.random.rand(n_sources)*self.shape[0]
        table['y_mean'] = np.random.rand(n_sources)*self.shape[1]
        table['x_stddev'] = np.random.rand(n_sources)
        table['y_stddev'] = np.random.rand(n_sources)
        table['theta'] = np.radians(np.random.rand(n_sources)*360)
        source= make_gaussian_sources_image(self.shape, table)
        image = source +  make_noise_image(self.shape, distribution='gaussian', mean=5., stddev=5.)
        image = image + make_noise_image(self.shape, distribution='poisson', mean=5.)
        return image

    def other_methods():
        return results

#%%
shape=(100,100)
array=Image(shape).load_image(n_sources=5)
plt.imshow(array, origin='lower')
#%%
