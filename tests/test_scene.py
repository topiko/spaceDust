from unittest import TestCase
import sys
sys.path.insert(1, '..')
from native.scene import Scene
import numpy as np

TOL = 1E-4


class TestScene(TestCase):
    def test_2_opposite_particles(self):
        """
        We put two particles with mass unity in opposite positions ([1,2], [-1,-2]) and compare with
        forces computed analytically
        :return:
        """
        n = 2
        scene = Scene(n)
        scene.position_array[:] = np.array([[1, 2], [-1, -2]])
        scene.masses[:] = 1
        scene.update_directions()
        scene.update_forces()
        forces = np.array([[-2, -4], [2, 4]]) / (20 * np.sqrt(20)) * scene.g
        error = np.linalg.norm(scene.force_array - forces)
        print(forces)
        print(scene.force_array)
        self.assertAlmostEqual(error, 0)

    def test_4_particles(self):
        """
        Because we are very dilligent and precise, we do the same thing with 4 particles of different masses,
        only calculating the force on the first one
        :return:
        """
        n = 4
        scene = Scene(n)
        scene.position_array[:] = np.array([[1, 0], [0, 1], [-1, 0], [0, -1]])
        scene.masses[:] = np.array([2, 3, 4, 5])
        scene.update_directions()
        scene.update_forces()
        first_force = -scene.masses[0] * scene.g * np.array([2 * np.sqrt(2) + 1,np.sqrt(2)/2])
        error = np.linalg.norm(first_force - scene.force_array[0,:])
        print(first_force)
        print(scene.force_array[0,:])
        self.assertAlmostEqual(error, 0)
