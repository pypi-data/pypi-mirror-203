import numpy as np
from gudhi.point_cloud.dtm import DTMDensity

class ManualDensity:
    """
    Class for handling density functions

    """

    def random_density(self, points):
        """
        Random density function for testing purposes

        :param points: set of landmarks in :math:`\mathbb{R}^d`.
        :type points: np.array size of *n_landmarks x 3*

        """
        return np.array(np.random.rand(1, len(points))[0])

    def dtm_density(self, points):
        """
        DTM density function

        :param points: set of landmarks in :math:`\mathbb{R}^d`.
        :type points: np.array size of *n_landmarks x 3*

        """
        dtm = DTMDensity(k=100)
        return dtm.fit_transform(points)

    # TODO
    # find out other useful density functions
    # implement them
