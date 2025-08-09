# Pedestrian Simulation Models Overview

This page provides a comprehensive overview of the 34 pedestrian simulation models supported by **PedSim4AV**, detailing their computational complexity, realism and accuracy, scalability, and application domains. These models, ranging from physics-based to AI-driven approaches, are designed to simulate realistic pedestrian behavior for autonomous vehicle (AV) testing, urban planning, and safety analysis. This table serves as a quick reference for researchers, developers, and students to select the right model for their AV simulation needs.

---

## Why This Table Matters
Understanding the strengths and limitations of each model is critical for selecting the appropriate simulation approach for your AV use case. Whether one is modeling dense crowds, predicting trajectories, or doing anything, **PedSim4AV** offers a diverse set of models to meet your needs. For research context, see [Paper Summaries](paper_summaries.md).

---

## Models Table

The table below summarizes the 34 pedestrian simulation models in **PedSim4AV**, categorized by their type, computational complexity, realism and accuracy, scalability, and primary application domains.

| Model | Type | Computational Complexity | Realism & Accuracy | Scalability | Application Domains |
|-------|------|--------------------------|--------------------|-------------|---------------------|
| **Social Force Models** | Microscopic | Moderate (depends on crowd size) | High: Realistic interactions | Moderate: Limited in large-scale | Evacuation, crowd behavior analysis |
| **Cellular Automata** | Microscopic | Low (grid-based, simple rules) | Moderate: Simplified dynamics | High: Scales well to large grids | Urban planning, **pedestrian flow optimization** |
| **Rule-Based Models** | Microscopic | Moderate (custom rules) | Moderate: Flexible behaviors | High: Adapts to various sizes | Scenario-specific studies |
| **Prediction Models** | AI-Driven | High (deep learning required) | Very High: Predictive accuracy | Low: Computationally expensive | **Trajectory prediction**, **AI-based simulations** |
| **Generative Models** | AI-Driven | High (probabilistic learning) | High: Captures diverse behaviors | Moderate: Depends on dataset size | Realistic behavior replication |
| **Path-Based Models** | Microscopic | Very Low (predefined pathways) | Moderate: Realistic movement along predefined pathways | High: Efficient for large scales | Navigation, urban infrastructure planning, crowd management |
| **Agent-Based Models** | Microscopic | Moderate to High (individual agents) | High: Individual and group behaviors | Moderate: Limited by agent count | Behavioral studies, emergency planning |
| **Macroscopic Models** | Flow-Based | Low (flow-based equations) | Low to Moderate: Aggregated movement patterns | Very High: Scales for large systems | Traffic analysis, urban-scale crowd dynamics |
| **Mesoscopic Models** | Group-Based | Moderate (group-level dynamics) | Moderate: Balances micro and macro | High: Efficient for medium scales | Large event simulations, mixed-density spaces |
| **Microscopic Models** | Microscopic | High (individual interactions) | Very High: Detailed behaviors | Moderate: Limited by agent count | **Individual trajectory prediction**, evacuation |
| **Granular Models** | Microscopic | High (physics-based interactions) | High: Detailed particle dynamics | Low: Computationally intensive | **Crowd dynamics**, granular material behavior |
| **Hybrid Models** | Hybrid | High (integration complexity) | High: Combines model strengths | Moderate: Limited by hybrid demands | Complex environments, mixed-scenario simulations |
| **Social LSTM and GANs** | AI-Driven | Very High (deep learning required) | Very High: Predictive and realistic | Low: Data-intensive | **Trajectory prediction**, **AI-driven applications** |
| **Continuum Models** | Flow-Based | Moderate (continuum equations) | High: Smooth representation of flow | High: Efficient for large crowds | Large-scale evacuation, continuous flow scenarios |
| **Fluid Dynamics Models** | Flow-Based | Moderate to High (Navier-Stokes equations) | High: Captures fluid-like behaviors | Moderate: Requires high computational resources | Dense crowd movement, bottleneck analysis |
| **Graph-Based Models** | Microscopic | Low to Moderate (pathfinding) | Moderate: Focused on route optimization | High: Efficient for large networks | Navigation, wayfinding, urban planning |
| **Simulation of Urban Mobility (SUMO)** | Hybrid | Moderate (network-level simulation) | High: Integrates real-world data | Very High: Optimized for city-scale simulations | Urban infrastructure planning, multimodal transit |
| **Optimal Steps Model (OSM)** | Microscopic | Moderate to High (environment complexity) | High: Finds near-optimal paths dynamically | Moderate: Handles multiple agents but may slow down with increasing complexity | Robotics, AI navigation, game AI |
| **Gradient Navigation Model (GNM)** | Microscopic | Low to Moderate (efficient but may require smoothing techniques) | Moderate: Requires potential field adjustments | High: Applicable to large groups of agents | Swarm robotics, **AI pathfinding**, multi-agent systems |
| **Behavioral Heuristics Model (BHM)** | Microscopic | Low (simple rule-based decision-making) | Moderate: Realistic behavior but may lack optimality | Very High: Scales well due to low computational cost | Game AI, **Crowd simulation**, **Human behavior modeling** |
| **Steering Behaviors Model** | Microscopic | Moderate (vector calculations increase with agent interactions) | High: Produces smooth, realistic movement | Moderate to High: Can scale but requires tuning | Game AI, **Autonomous vehicles**, Animation |
| **Collision-Free Speed Model (CFS)** | Microscopic | Low to Moderate (relies on simple speed adjustments) | Moderate: Ensures collision-free movement but may be too conservative | High: Efficient for large-scale crowd and traffic simulations | **Pedestrian dynamics**, traffic flow, **autonomous vehicle navigation** |
| **Anticipation Velocity Model (AVM)** | Microscopic | High (requires future state prediction for multiple agents) | High: Anticipates future collisions, leading to smoother and more natural movement | Moderate: Limited due to predictive computations | **Crowd simulation**, **Pedestrian dynamics**, AI-controlled movement |
| **Generalized Centrifugal Force Model (GCF)** | Microscopic | Moderate to High (computes centrifugal forces dynamically) | Very High: Realistic curved trajectories, fluid navigation in dense areas | Moderate: Handles multiple agents but requires fine-tuning | **Human behavior modeling**, **Crowd simulation**, emergency evacuation planning |
| **Vision-Based Models** | AI-Driven | High (CNN-based processing) | High: Accurate visual detection | Low: Computationally intensive | **AV pedestrian detection**, visual navigation |
| **RL-Based Models** | AI-Driven | High (reinforcement learning training) | High: Adaptive and learned behaviors | Low: Training and inference complexity | Adaptive pedestrian behavior, **AV safety** |
| **Vision Transformer (ViT) Models** | AI-Driven | Very High (transformer-based processing) | Very High: Precise visual and trajectory prediction | Low: Data and compute-intensive | AV perception, crowd forecasting |
| **Multi-Agent Reinforcement Learning Models** | AI-Driven | Very High (multi-agent RL training) | High: Dynamic multi-agent interactions | Low: Limited by computational demands | Dynamic crowd interactions, **multi-agent AV scenarios** |
| **Bayesian Models** | AI-Driven | Moderate to High (probabilistic inference) | High: Uncertainty-aware behavior modeling | Moderate: Scales with optimized inference | Probabilistic crowd modeling, risk assessment |
| **Attention-Based Models** | AI-Driven | High (attention mechanisms) | Very High: Socially-aware navigation focus | Low: Computationally expensive | Socially-aware navigation, **AV interaction modeling** |
| **Imitation Learning Models** | AI-Driven | High (learning from demonstrations) | High: Mimics realistic human behaviors | Moderate: Depends on demonstration dataset | **Realistic pedestrian behavior**, **AV training** |
| **Federated Learning Models** | AI-Driven | High (distributed learning) | High: Privacy-preserving behavior modeling | Moderate: Limited by network and data coordination | Decentralized crowd modeling, privacy-focused AVs |
| **Temporal Convolutional Networks (TCNs)** | AI-Driven | High (sequential deep learning) | High: Long-term trajectory forecasting | Low: Requires significant compute resources | **Long-term trajectory prediction**, AV planning |
| **Physics-Informed Neural Networks (PINNs)** | Hybrid | High (physics and neural network integration) | High: Physics-constrained trajectory prediction | Moderate: Limited by computational complexity | Physics-aware simulations, **complex AV scenarios** |

---
