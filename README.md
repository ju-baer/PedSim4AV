# Pedestrian Simulation Models
A comprehensive repository for pedestrian simulation models, including social force, cellular automata, vision-based, RL-based, hybrid, and more. Designed for researchers, it offers modular implementations, Jupyter Notebook demos, comparisons, integrations with CARLA/SUMO/Unity, and example scenarios.

---
## Installation
```bash
git clone https://github.com/<your-username>/pedestrian-sim-models.git
cd pedestrian-sim-models
pip install -r models/social_force/requirements.txt
```
---
## Quickstart
Run the social force model demo:
```bash
jupyter notebook models/social_force/demo.ipynb
```
---
## Models
- Social Force: Physics-based model with attractive/repulsive forces (Helbing et al., 1995).
- Cellular Automata: Grid-based discrete movement (Burstedde et al., 2001).

Vision-Based: Uses visual input for navigation (e.g., CNN-based).

RL-Based: Reinforcement learning for pedestrian behavior (e.g., DQN).

Hybrid Models: Combines multiple approaches (e.g., social force + RL).

Granular: Models pedestrians as particles with contact forces.

Macroscopic: Treats crowds as flows (e.g., continuum models).

Microscopic: Individual-level dynamics.

Mesoscopic: Group-based dynamics.

Agent-Based: Individual behaviors with Mesa.

Rule-Based: Predefined movement rules.

Prediction Models: Data-driven trajectory prediction.

Social LSTM/GANs: LSTM and GAN-based trajectory prediction.

Generative Models: VAEs and diffusion models for trajectories.

Continuum: Flow-based crowd modeling.

Fluid Dynamics: Crowd as fluid flow.

Graph-Based: Navigation using graph structures.

Path-Based: Pathfinding-based movement.

SUMO Models: Pedestrian models in SUMO.

Optimal Steps: A* pathfinding for efficient movement.

Gradient Navigation: Gradient field-based navigation.

Behavioral Heuristics: Rule-based heuristics for behavior.

Steering Behaviors: Game-inspired steering (e.g., Reynolds).

Collision-Free Speed: Velocity-based collision avoidance.

Anticipation Velocity: Predicts and avoids collisions.

Centrifugal Force: Generalized force model for crowds.

---
## Usage
See models/*/demo.ipynb for demos and docs/paper_summaries.md for research context.


