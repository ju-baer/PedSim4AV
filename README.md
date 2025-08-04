<p align="center">
  <img src="https://img.shields.io/badge/Version-1.0-blue.svg" alt="Version">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/Contributions-Welcome-orange.svg" alt="Contributions">
</p>

<h1 align="center"> PedSim4AV: Pedestrian Simulation Models for Autonomous Vehicles </h1>
<p align="center">
  <strong>A vibrant hub of pedestrian simulation models for researchers, urban planners, and tech enthusiasts .</strong>
</p>

---

## About This Repository
PedSim4AV is a comprehensive hub for pedestrian simulation models specifically designed for autonomous vehicle research and development. 

- **Comprehensive Coverage**: 34 models, including Social Force, Cellular Automata, RL-based, Vision-based, AI based and more.
- **Research-Ready Tools**: Benchmarks, comparisons, and integrations with existing simulators. 
- **Open & Modular**: MIT-licensed, designed for easy extensions and community contributions.


## Features That this repository will have after completing everything

- **34 Models**: From granular physics to generative AI, covering macroscopic, microscopic, mesoscopic, and hybrid approaches.
- **Performance Insights**: Compare models with `metrics_eval.ipynb` for runtime, accuracy, and scalability.
- **Real-World Integrations**: Plug into CARLA for AV testing, SUMO for traffic sims, or Unity. 
- **Data & Scenarios**: Synthetic datasets and example scenarios to jumpstart experiments.
- **Research Context**: Curated paper summaries in `docs/paper_summaries.md` to ground your work.


---


## Models at a Glance

Dive into the heart of pedestrian simulation with our **34 cutting-edge models**! From physics-inspired classics to AI-driven innovations, this table highlights each model’s type, key feature, and primary use case. Check `docs/paper_summaries.md` for the research behind each model!

### Microscopic Models
Fine-grained simulations tracking individual pedestrian movements with precision.

| Model | Type | Key Feature | Use Case |
|-------|------|-------------|----------|
| **Social Force** | Microscopic | Physics-based attractive/repulsive forces | Evacuation, crowd flow |
| **Cellular Automata** | Microscopic | Grid-based discrete movement | Large-scale crowds |
| **Granular** | Microscopic | Particle-based contact forces | Dense crowds |
| **Microscopic** | Microscopic | Individual-level detailed dynamics | High-precision simulations |
| **Agent-Based** | Microscopic | Mesa-driven individual agents | Flexible simulations |
| **Rule-Based** | Microscopic | Predefined movement rules | Simple crowd modeling |
| **Graph-Based** | Microscopic | Graph-based navigation (e.g., shortest paths) | Structured environments |
| **Path-Based** | Microscopic | A* pathfinding for movement | Optimal routing |
| **Optimal Steps** | Microscopic | Efficient A* with risk-based weights | Fast navigation |
| **Gradient Navigation** | Microscopic | Gradient field-guided movement | Structured navigation |
| **Behavioral Heuristics** | Microscopic | Heuristic rules for behavior | Simple realistic modeling |
| **Steering Behaviors** | Microscopic | Game-inspired steering (e.g., Reynolds) | Game-like simulations |
| **Collision-Free Speed** | Microscopic | Velocity-based collision avoidance | Safe navigation |
| **Anticipation Velocity** | Microscopic | Predictive collision avoidance | Dense environments |
| **Centrifugal Force** | Microscopic | Generalized force for crowd avoidance | High-density crowds |

---

### Flow-Based Models
Crowd dynamics modeled as continuous flows, ideal for large-scale scenarios.

| Model | Type | Key Feature | Use Case |
|-------|------|-------------|----------|
| **Macroscopic** | Flow-Based | Crowd treated as continuous flow | Urban planning |
| **Continuum** | Flow-Based | Continuous crowd flow dynamics | Large-scale urban planning |
| **Fluid Dynamics** | Flow-Based | Navier-Stokes-based crowd movement | High-density crowds |

---

### Group-Based Models
Balancing individual and group dynamics for realistic social interactions.

| Model | Type | Key Feature | Use Case |
|-------|------|-------------|----------|
| **Mesoscopic** | Group-Based | Group dynamics balancing micro/macro | Social group behavior |

---

### AI-Driven Models
Leveraging machine learning and AI for adaptive, data-driven simulations.

| Model | Type | Key Feature | Use Case |
|-------|------|-------------|----------|
| **Vision-Based** | AI-Driven | CNN for visual navigation | AV pedestrian detection |
| **RL-Based** | AI-Driven | Learned policies via reinforcement learning | Adaptive behaviors |
| **Prediction Models** | AI-Driven | Data-driven trajectory forecasting | AV safety, planning |
| **Social LSTM/GANs** | AI-Driven | Socially-aware trajectory prediction | Dense crowd forecasting |
| **Generative Models** | AI-Driven | VAEs and diffusion for synthetic trajectories | Data augmentation |
| **Vision Transformer (ViT) Models** | AI-Driven | Transformer-based visual trajectory prediction | AV perception, crowd forecasting |
| **Multi-Agent Reinforcement Learning Models** | AI-Driven | Multi-agent RL for interactive behaviors | Dynamic crowd interactions |
| **Bayesian Models** | AI-Driven | Uncertainty quantification in behavior | Probabilistic crowd modeling |
| **Attention-based Models** | AI-Driven | Attention mechanisms for pedestrian focus | Socially-aware navigation |
| **Imitation Learning Models** | AI-Driven | Learning from human demonstrations | Realistic pedestrian behavior |
| **Federated Learning Models** | AI-Driven | Privacy-preserving behavior learning | Decentralized crowd modeling |
| **Temporal Convolutional Networks (TCNs)** | AI-Driven | Sequence modeling for trajectories | Long-term trajectory forecasting |
| **Normalizing Flow Models** | AI-Driven | Generating realistic trajectory distributions | Synthetic crowd data generation |

---

### Hybrid Models
Combining physics and AI for versatile, robust simulations.

| Model | Type | Key Feature | Use Case |
|-------|------|-------------|----------|
| **Hybrid Models** | Hybrid | Combines physics and AI (e.g., Social Force + RL) | Complex scenarios |
| **SUMO Models** | Hybrid | Pedestrian simulation in SUMO | Traffic-pedestrian interactions |
| **Physics-Informed Neural Networks (PINNs)** | Hybrid | Neural networks with physics constraints | Physics-aware trajectory prediction |
| **Neuro-Symbolic Models** | Hybrid | Combines neural networks with symbolic reasoning | Interpretable crowd dynamics |

---

## Benchmarking
We want to test the pedestrina simulation models in this benchmarking way to see how they perform in robust scenarios and how pedestrian simulation models can be modeled for AV safety and more. 
### Evaluation Metrics
- **Safety**: Collision rates, minimum distances, reaction times
- **Realism**: Human behavior similarity, trajectory naturalness
- **Efficiency**: Computational performance, memory usage
- **Robustness**: Performance across diverse scenarios

### Benchmark Scenarios
1. **Urban Crosswalk**: Multi-directional pedestrian flow
2. **Intersection**: Complex vehicle-pedestrian interactions
3. **Emergency**: Sudden obstacle avoidance
4. **Crowded Areas**: High-density pedestrian dynamics

---
