import numpy as np
from models.common.utils import distance, normalize_vector

class SocialForceModel:
    """Social Force Model for pedestrian simulation (Helbing et al., 1995)."""
    def __init__(self, n_pedestrians, dt=0.1, tau=0.5, A=2000, B=0.08, k=120000,kappa=240000):
        self.n_pedestrians = n_pedestrians
        self.dt = dt  # Time step (s)
        self.tau = tau  # Relaxation time (s)
        self.A = A  # Repulsion strength (N)
        self.B = B  # Repulsion range (m)
        self.k = k  # Body force coefficient (kg/s^2)
        self.kappa = kappa  # Friction coefficient (kg/s)
        self.positions = np.random.uniform(0, 10, (n_pedestrians, 2))  # Random initial positions
        self.velocities = np.zeros((n_pedestrians, 2))  # Initial velocities
        self.destinations = np.random.uniform(8, 10, (n_pedestrians, 2))  # Random destinations
        self.max_speed = 1.3  # Max walking speed (m/s)
        self.mass = 80  # Average pedestrian mass (kg)
        self.radius = 0.2  # Pedestrian radius (m)

    def desired_direction(self, i):
        """Calculate desired direction toward destination."""
        delta = self.destinations[i] - self.positions[i]
        return normalize_vector(delta)

    def desired_force(self, i):
        """Calculate force driving pedestrian to destination."""
        return self.mass * (self.max_speed * self.desired_direction(i) - self.velocities[i]) / self.tau

    def repulsive_force(self, i):
        """Calculate repulsive forces from other pedestrians."""
        force = np.zeros(2)
        for j in range(self.n_pedestrians):
            if i != j:
                r_ij = self.positions[i] - self.positions[j]
                dist = distance(self.positions[i], self.positions[j])
                if dist > 0:
                    n_ij = r_ij / dist
                    force += self.A * np.exp((2 * self.radius - dist) / self.B) * n_ij
                    # Body contact force
                    if dist < 2 * self.radius:
                        force += self.k * (2 * self.radius - dist) * n_ij
                        # Friction force
                        v_diff = self.velocities[j] - self.velocities[i]
                        force += self.kappa * (2 * self.radius - dist) * np.dot(v_diff, n_ij) * n_ij
        return force

    def step(self):
        """Update positions and velocities for one time step."""
        forces = np.zeros((self.n_pedestrians, 2))
        for i in range(self.n_pedestrians):
            forces[i] = self.desired_force(i) + self.repulsive_force(i)
        accelerations = forces / self.mass
        self.velocities += accelerations * self.dt
        # Cap velocity
        speeds = np.linalg.norm(self.velocities, axis=1)
        for i in range(self.n_pedestrians):
            if speeds[i] > self.max_speed:
                self.velocities[i] = self.velocities[i] * self.max_speed / speeds[i]
        self.positions += self.velocities * self.dt
