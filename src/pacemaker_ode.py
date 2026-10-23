"""
Biophysical Pacemaker Dynamical Model (Extended McSharry System)
Coupled with Vagal Acetylcholine Efferents, Acoustic Harmonic Stress, and Gravitational Hydrostatic Tilt.
"""

import numpy as np

class BiophysicalPacemaker:
    def __init__(self, intrinsic_hr=72.0, fs=250):
        self.fs = fs
        self.dt = 1.0 / fs
        self.omega_0 = 2.0 * np.pi * (intrinsic_hr / 60.0)
        
        # P-Q-R-S-T wave parameters (McSharry IEEE TBME standard)
        self.a_i = np.array([1.2, -5.0, 30.0, -7.5, 0.75])
        self.b_i = np.array([0.25, 0.1, 0.1, 0.1, 0.4])
        self.theta_i = np.array([-np.pi/3, -np.pi/12, 0.0, np.pi/12, np.pi/2])
        
    def step(self, state, vagal_input=0.0, acoustic_stress=0.0, gravity_angle_deg=0.0):
        """
        Integrates one time step of the 3D limit-cycle cardiac dynamical system.
        
        Args:
            state: np.array([x, y, z])
            vagal_input: Parasympathetic acetylcholine efferent discharge [0, 1]
            acoustic_stress: Dissonant acoustic pressure/stress factor >= 0
            gravity_angle_deg: Sagittal tilt angle (0=Standing, 90=Ruku, 180=Sujud)
            
        Returns:
            next_state: np.array([x+dx, y+dy, z+dz])
            instantaneous_hr: Current heart rate in beats per minute
        """
        x, y, z = state
        
        # 1. Baroreflex Hydrostatic Feedback
        baro_hydrostatic = 0.45 * np.sin(np.radians(gravity_angle_deg))
        
        # 2. Dynamic Angular Pacemaker Velocity omega(t)
        omega = self.omega_0 - (0.85 * vagal_input) + (0.95 * acoustic_stress) - (1.10 * baro_hydrostatic)
        omega = max(0.5 * np.pi, min(4.0 * np.pi, omega)) # Physiological bounds: 30 - 240 bpm
        
        # 3. Limit-Cycle Attractor Radius
        r = np.sqrt(x**2 + y**2)
        alpha = 1.0 - r
        
        # 4. Integrate Phase Space Trajectory
        dx = (alpha * x - omega * y) * self.dt
        dy = (alpha * y + omega * x) * self.dt
        
        # Current Phase Angle
        theta = np.arctan2(y, x)
        
        # 5. ECG Voltage Generator dz
        delta_theta = np.fmod(theta - self.theta_i + np.pi, 2 * np.pi) - np.pi
        z_mod = -np.sum(self.a_i * delta_theta * np.exp(-0.5 * (delta_theta / self.b_i)**2))
        dz = (z_mod - (z - 0.0)) * self.dt + np.random.normal(0, 0.005)
        
        next_state = np.array([x + dx, y + dy, z + dz])
        instantaneous_hr = (omega / (2.0 * np.pi)) * 60.0
        
        return next_state, instantaneous_hr

if __name__ == "__main__":
    pacemaker = BiophysicalPacemaker(intrinsic_hr=72.0)
    state = np.array([1.0, 0.0, 0.0])
    print("Testing 100 steps of Prostration (Sujud at 180 deg)...")
    for _ in range(100):
        state, hr = pacemaker.step(state, vagal_input=0.8, gravity_angle_deg=180.0)
    print(f"Final State: {state}, Stabilized Heart Rate: {hr:.1f} bpm")
