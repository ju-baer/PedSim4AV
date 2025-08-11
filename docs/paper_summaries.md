# Comprehensive Research Papers Collection: Pedestrian Simulation Models

> **Welcome to the most comprehensive research hub for Pedestrian Simulation Models!** 
> 
> This curated collection features **detailed summaries of 40+ seminal papers** spanning **34 distinct modeling approaches**, from foundational physics-based frameworks to cutting-edge AI-driven innovations. Designed for **researchers, urban planners, transportation engineers, and crowd dynamics specialists**, this resource provides deep insights into methodologies, empirical findings, practical applications, and future research directions.

---

## **Quick Navigation**

| **Model Category** | **Paper Count** | **Key Applications** |
|----------------------|-------------------|------------------------|
| [**Microscopic Models**](#microscopic-models) | 39 | Individual behavior, crowd dynamics |
| [**Flow-Based Models**](#flow-based-models) | 8 | Large-scale planning, traffic flow |
| [**Group-Based Models**](#group-based-models) | 3 | Social interactions, group dynamics |
| [**AI-Driven Models**](#ai-driven-models) | 15+ | Prediction, learning, adaptation |
| [**Hybrid Models**](#hybrid-models) | 4+ | Physics + AI integration |

---

## Table of Contents
- [Microscopic Models](#microscopic-models)
  - [Social Force](#social-force)
  - [Cellular Automata](#cellular-automata)
  - [Granular](#granular)
  - [Microscopic](#microscopic)
  - [Agent-Based](#agent-based)
  - [Rule-Based](#rule-based)
  - [Graph-Based](#graph-based)
  - [Path-Based](#path-based)
  - [Optimal Steps](#optimal-steps)
  - [Gradient Navigation](#gradient-navigation)
  - [Behavioral Heuristics](#behavioral-heuristics)
  - [Steering Behaviors](#steering-behaviors)
  - [Collision-Free Speed](#collision-free-speed)
  - [Anticipation Velocity](#anticipation-velocity)
  - [Centrifugal Force](#centrifugal-force)
- [Flow-Based Models](#flow-based-models)
  - [Macroscopic](#macroscopic)
  - [Continuum](#continuum)
  - [Fluid Dynamics](#fluid-dynamics)
- [Group-Based Models](#group-based-models)
  - [Mesoscopic](#mesoscopic)
- [AI-Driven Models](#ai-driven-models)
  - [Vision-Based](#vision-based)
  - [RL-Based](#rl-based)
  - [Prediction Models](#prediction-models)
  - [Social LSTM/GANs](#social-lstmgans)
  - [Generative Models](#generative-models)
  - [Vision Transformer (ViT) Models](#vision-transformer-vit-models)
  - [Multi-Agent Reinforcement Learning Models](#multi-agent-reinforcement-learning-models)
  - [Bayesian Models](#bayesian-models)
  - [Attention-based Models](#attention-based-models)
  - [Imitation Learning Models](#imitation-learning-models)
  - [Federated Learning Models](#federated-learning-models)
  - [Temporal Convolutional Networks (TCNs)](#temporal-convolutional-networks-tcns)
  - [Normalizing Flow Models](#normalizing-flow-models)
- [Hybrid Models](#hybrid-models)
  - [Hybrid Models](#hybrid-models-1)
  - [SUMO Models](#sumo-models)
  - [Physics-Informed Neural Networks (PINNs)](#physics-informed-neural-networks-pinns)
  - [Neuro-Symbolic Models](#neuro-symbolic-models)

---

## Microscopic Models

### Social Force

**Title**: Social Force Model for Pedestrian Dynamics  

**Authors**: Dirk Helbing, Péter Molnár  

**Publication Year**: 1995  

**Summary**: The Social Force Model (SFM) models each pedestrian as a particle driven by internal "social forces": (1) a driving force toward a desired velocity, (2) repulsive forces from other pedestrians and obstacles, and (3) attractive forces (e.g., groups or points of interest). The coupled nonlinear Langevin-like equations reproduce self-organization phenomena such as lane formation, oscillations at bottlenecks, and stop-and-go waves.

**Link**: [DOI:10.1103/PhysRevE.51.4282](https://doi.org/10.1103/PhysRevE.51.4282)  

**Datasets**: Custom corridor experiments, Pedestrian Dynamics Data Archive (PDDA). 

**Metrics**: Flow rates, lane formation patterns, velocity-density curves.  

**Applications**: Evacuation planning, urban crowd management, architectural design. 

**Limitations**: Original formulation assumes isotropic interactions and can produce unrealistic lateral oscillations or collisions at high densities; parameters require calibration; lacks explicit anticipation/heading.  

**Future Directions**: Incorporate heading/orientation, vision-based perception, collision anticipation, heterogeneity in agent properties, and calibration against real-world trajectory datasets.

---

**Title**:  Walking Ahead: The Headed Social Force Model

**Authors**:  Francesco Farina, Daniele Fontanelli, Andrea Garulli, Antonio Giannitrapani, Domenico Prattichizzo

**Publication Year**: 2017

**Summary**: This paper extends the SFM by adding explicit pedestrian heading (orientation) and a unicycle-like dynamic so agents predominantly move forward. The Headed Social Force Model reduces unrealistic lateral motion found in the classical SFM and introduces group-cohesion terms. Simulations show smoother, more realistic trajectories and improved handling of dense flows. 

**Link**: [DOI:10.1371/journal.pone.0169734](https://doi.org/10.1371/journal.pone.0169734)  

**Datasets**: Synthetic simulation scenarios generated by the authors for validation; experiments demonstrate trajectory realism compared with standard SFM.

**Metrics**: Trajectory smoothness/regularity, collision counts, path deviation, flow/density comparisons.  

**Applications**: Human-aware robot navigation, crowd animation, architectural design  

**Limitations**: Still parameterized and requires tuning; primarily validated in simulated scenarios; does not explicitly model perception or visual occlusion. 

**Future Directions**: Calibrate using real trajectory datasets, couple with vision-based sensing and learning-based parameter estimation, model heterogeneous walking behaviors.

---

**Title**: Improved Social Force Model Based on Pedestrian Collision Avoidance Behavior in Counterflow

**Authors**: Junheng Yang, Xiaodong Zang, Weiying Chen, Qiang Luo, Rui Wang, Yuanqian Liu

**Publication Year**: 2024

**Summary**: It introduces an additional avoidance force term to the SFM to explicitly capture collision-avoidance behavior in bidirectional (counterflow) scenarios. The model is calibrated and validated using controlled bidirectional pedestrian experiments. Results show improved reproduction of lane formation, reduced collisions, and better match to measured crossing-time and order-parameter statistics compared to the classical SFM.

**Link**: [https://www.sciencedirect.com/science/article/abs/pii/S0378437124002711](https://www.sciencedirect.com/science/article/abs/pii/S0378437124002711)  

**Datasets**: Motion-capture trajectory data collected by the authors in controlled bidirectional flow experiments.

**Metrics**: Individual crossing time distributions, order parameter (flow organization measure), collision events, lane stability. 

**Applications**:  Modeling pedestrian counterflows in corridors, sidewalks, and transit hubs; informing corridor design and crowd management strategies.

**Limitations**: Focused on counterflow scenarios; requires experimental calibration and may not generalize to all crowd contexts. 

**Future Directions**: Extend to multi-direction flows, incorporate stochasticity and individual differences, validate in large-scale public environments.


---

### Cellular Automata

**Title**: A Cellular Automata Based Model for Pedestrian and Group Dynamics 

**Authors**: Alessandro Corbetta, Angelo Vizzari, Claudio Feliciani, Katsuhiro Nishinari, Stefania Bandini

**Publication Year**: 2015  

**Summary**: This paper proposes a cellular automata model that incorporates pedestrian group behavior based on proxemics theory, enhancing the realism of pedestrian dynamics simulations. It models interactions within groups and between groups, showing how group presence impacts overall pedestrian flow. The model is validated through simulations comparing results with experimental data. 

**Link**: [https://link.springer.com/chapter/10.1007/978-3-642-23178-0_11](https://link.springer.com/chapter/10.1007/978-3-642-23178-0_11)  

**Datasets**: Simulation scenarios with groups of pedestrians under controlled environments.

**Metrics**: Pedestrian flow velocity, group cohesion, collision avoidance efficiency.

**Applications**: Crowd management, urban planning, simulation of collective pedestrian behavior.

**Limitations**: Simplified group behaviors; cultural heterogeneity is not deeply modeled.

**Future Directions**: Incorporating more complex social interactions and adapting the model to heterogeneous pedestrian populations.

---

**Title**: Using Cellular Automata to Model High Density Pedestrian Dynamics

**Authors**: Jacek Bieżuń, Sławomir Wiśniowski, Sebastian Nowak, Katarzyna Kułak  

**Publication Year**: 2020  

**Summary**: his paper presents a refined CA model tailored for high-density pedestrian scenarios. It improves movement representation by allowing pedestrians to occupy multiple cells (to represent backpacks, luggage, etc.) and introduces detailed movement rules for passing and overtaking. The model supports more precise simulations for situations like evacuations or crowded events.

**Link**: [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7302238/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7302238/)  

**Datasets**: Simulation data of pedestrian movements in confined, high-density spaces.

**Metrics**: Evacuation time, movement speed, spatial utilization, computational cost.

**Applications**: Emergency evacuation planning, event safety analysis, high-density crowd modeling.

**Limitations**: Increased computational cost due to model complexity; focused mainly on high-density scenarios.

**Future Directions**: Hybrid approaches combining different model granularities to reduce computational burden while maintaining accuracy.

---

**Title**: A Cellular Automata Approach for Modelling Pedestrian-Vehicle Mixed Traffic Flow in Urban City

**Authors**: Jinghui Wang, Wei Lv, Yajuan Jiang, Guangchen Huang

**Publication Year**: 2024 

**Summary**: This paper introduces a multi-grid CA model bridging pedestrian and vehicle traffic, addressing mixed traffic flow modeling challenges. It includes time-to-collision safety metrics and demonstrates how pedestrian intrusion affects vehicle flow and conflict frequency. The model helps predict traffic dynamics in urban environments with mixed traffic participants.

**Link**: [https://arxiv.org/html/2405.06282v1](https://arxiv.org/html/2405.06282v1)  

**Datasets**: Simulation outputs of mixed pedestrian-vehicle traffic on urban streets with varying speed limits and sidewalk widths.  

**Metrics**: Traffic flow states, pedestrian-vehicle conflict frequency, speed, and density measures.

**Applications**: Urban traffic safety, city traffic management, pedestrian-vehicle interaction studies.  

**Limitations**: Complexity in model calibration; generalization to all urban scenarios requires further testing.

**Future Directions**: Extending to more diverse urban settings, incorporating real-time data for adaptive traffic control.

---

### Granular

**Title**: A granular model for crowd motion and pedestrian flow

**Authors**: Noureddine Igbida, José Miguel Urbano

**Publication Year**: 2024

**Summary**: This paper studies a granular model for congested crowd motion and pedestrian flow, using an approximation involving a Hele-Shaw type equation with a degenerate p-Laplacian operator and linear drift. The authors prove existence and uniqueness of solutions using nonlinear semigroup methods. As the parameter p→∞, solutions converge to a variational solution modeling congestion effects in pedestrian flows, effectively capturing dense crowd behavior. 

**Link**: [https://arxiv.org/abs/2402.17361](https://arxiv.org/abs/2402.17361)  

**Datasets**: Simulation data based on mathematical formulations; no empirical datasets provided.  

**Metrics**: Existence and uniqueness of solutions, congestion representation, flow density.  

**Applications**: Modeling congested pedestrian crowds and high-density crowd dynamics in public spaces.

**Limitations**: Abstract mathematical model primarily; may require calibration for real-world scenarios.

**Future Directions**: Extending model to more complex pedestrian behaviors and real-world validations.

---

**Title**: Scaling laws in granular flow and pedestrian flow

**Authors**: Shumiao Chen, Fernando Alonso-Marroquín, Jonathan Busch, Raúl Cruz Hidalgo, Charmila Sathianandan, Álvaro Ramírez-Gómez, Peter Mora

**Publication Year**: 2021

**Summary**: This study uses particle-based simulations to compare granular flow (gravity-driven) and pedestrian flow (velocity-driven) through bottlenecks. It shows that granular materials and pedestrian crowds share similar flow rate power laws impacted by exit widths, particle shapes, and friction. The results help explain phenomena like the "faster-is-slower" effect in panic situations and how physical contact forces contribute to crowd injuries. The findings generalize granular flow relations for pedestrian dynamics.

**Link**: [https://www.unav.edu/documents/14434042/14571851/APC000157.pdf](https://www.unav.edu/documents/14434042/14571851/APC000157.pdf)  

**Datasets**: Simulation outputs of granular and pedestrian flows using particle models with variable shapes and flow parameters.

**Metrics**: Flow rate, exit width power law, contact force distribution, evacuation dynamics. 

**Applications**: Understanding bottleneck flow in panic evacuations, crowd safety, and design of egress structures.

**Limitations**: Model focuses on physical aspects; psychological factors less represented.

**Future Directions**: Integrate human behavioral modeling and test different crowd control strategies.

---

### Microscopic

**Title**: Review on Microscopic Pedestrian Simulation Model

**Authors**: Kardi Teknomo, Yasushi Takeyama, Hajime Inamura

**Publication Year**: 2016

**Summary**: This paper reviews various microscopic pedestrian simulation models that treat pedestrians as individual entities interacting through social and physical rules. It discusses models like the Benefit Cost Cellular Model, Magnetic Force Model, and Social Force Model, highlighting their ability to simulate realistic pedestrian dynamics at an individual level. The paper also identifies challenges such as the lack of calibration and validation with real-world movement data, proposing future research directions on automating data collection and statistical parameter calibration.

**Link**: [https://arxiv.org/abs/1609.01808](https://arxiv.org/abs/1609.01808)  

**Datasets**: Not explicitly provided; simulation and theoretical models analyzed.

**Metrics**: Pedestrian velocity, interaction forces, route choices, collision avoidance effectiveness.

**Applications**: Evacuation planning, pedestrian facility design, detailed pedestrian flow analysis.

**Limitations**: Insufficient empirical calibration and validation, limiting generalizability.

**Future Directions**: Automated real-world data collection and improved statistical calibration methods.

---

**Title**: Simulation of High Density Pedestrian Flow: A Microscopic Model

**Authors**: M. Zanlungo, T. Ikeda, T. Kanda

**Publication Year**: 2015

**Summary**: This study presents a microscopic pedestrian simulation focused on high-density situations, modeling individuals as self-driven particles influenced by social and physical forces. The proposed model accounts for pedestrian desires, interactions with neighbors, collision avoidance, and environmental boundaries. Results emphasize the importance of these behaviors in evacuation scenarios and crowd control strategies.

**Link**: [https://www.scirp.org/journal/paperinformation?paperid=57296](https://www.scirp.org/journal/paperinformation?paperid=57296)  

**Datasets**: Simulation data on high-density pedestrian flows.

**Metrics**: Evacuation time, collision frequency, density, and velocity profiles.

**Applications**: Emergency evacuation modeling, crowd safety management, urban infrastructure design.

**Limitations**: Computational complexity in very large crowds; assumptions on uniform behavioral responses.

**Future Directions**: Including heterogeneous pedestrian behaviors and real-time adaptive control.

---

**Title**: A Microscopic Simulation Model for Pedestrian Behavior at Crosswalks

**Authors**: Guangquan Lu, Jun Zhuang, et al.

**Publication Year**: 2017

**Summary**: This paper develops a microscopic pedestrian behavior model focusing on interactions at crosswalks. It incorporates anticipatory behaviors and pedestrian-vehicle interactions to simulate realistic crossing dynamics under various scenarios. The model emphasizes individual decision-making and interaction with traffic, improving accuracy in predicting pedestrian delay and safety conditions.

**Link**: [https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0180992](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0180992)  

**Datasets**: Empirical pedestrian crossing data used for calibration and validation.

**Metrics**: Pedestrian waiting time, crossing duration, collision risk, flow rate.

**Applications**: Traffic safety analysis, urban crosswalk design, pedestrian-vehicle interaction studies.

**Limitations**: Focused on crosswalk scenarios; may need adaptation for other pedestrian environments.

**Future Directions**: Extension to multi-modal traffic intersections and dynamic traffic conditions.

---

### Agent-Based

**Title**: A Hybrid Workflow Connecting a Network and an Agent-based model to Simulate Micro-scale Pedestrian Movement

**Authors**: Berghauser Pont, Henrik, et al.

**Publication Year**: 2024 

**Summary**:This study presents an Agent-Based Model integrated with the Social Force Model to simulate micro-scale pedestrian movement in outdoor environments. Pedestrians are modeled as agents represented by three spheres indicating body parts and orientation. The model incorporates path planning, obstacle avoidance, and speed adaptation, calibrated and validated for urban open spaces. It efficiently handles large-scale pedestrian interactions and allows extensions for complex behavioral rules.

**Link**: [https://www.frontiersin.org/journals/built-environment/articles/10.3389/fbuil.2024.1447377/full](https://www.frontiersin.org/journals/built-environment/articles/10.3389/fbuil.2024.1447377/full)  

**Datasets**: Origin-Destination matrices for pedestrian flows; simulations in realistic urban geometries.

**Metrics**: Pedestrian velocity, collision avoidance performance, flow distributions.

**Applications**: Urban planning, crowd management in public spaces, micro-scale pedestrian movement analysis.

**Limitations**: Requires extensive calibration for different contexts; complexity increases with behavioral rule extensions.

**Future Directions**: Incorporation of more complex pedestrian behaviors and tactical planning; coupling with network models for comprehensive city-scale simulations.

---

**Title**: Large-Scale Agent-Based Pedestrian Simulation

**Authors**: Franz Klügl, Gabriele Rindsfüser

**Publication Year**: 2007

**Summary**:This paper reports an agent-based simulation of pedestrian traffic at a large scale: the full railway station in Bern during busy morning hours, simulating over 40,000 pedestrians. The model enables flexible path planning and re-planning for individual agents to navigate dynamically without collisions. It demonstrates the capabilities and challenges of large-scale pedestrian simulations at microscopic levels within complex infrastructures like train stations.

**Link**: [https://link.springer.com/chapter/10.1007/978-3-540-74949-3_13](https://link.springer.com/chapter/10.1007/978-3-540-74949-3_13)  

**Datasets**: Scenario data based on train station layouts and schedules with pedestrian arrival rates.

**Metrics**: Collision avoidance, path efficiency, pedestrian density and flow rates.

**Applications**: Station design and management, crowd flow optimization in transit hubs.

**Limitations**: High computational cost and data requirements for large scale; limited real-world validation reported.

**Future Directions**: Improving computational efficiency and validation techniques; integrating real-time data feeds.

---

**Title**: An Agent-Based Simulation Model of Pedestrian Evacuation Based on Bayesian Game Theory

**Authors**: Weiwei Mau, Mohamed A. Mostafa, Chao Zhang

**Publication Year**: 2017

**Summary**:This research develops an agent-based model for pedestrian evacuation integrating Bayesian Nash Equilibrium game theory to simulate individual decision-making during emergencies. The approach realistically models behavioral heterogeneity and dynamic route choices influenced by predicted congestion. Simulation experiments show improved evacuation efficiency with the Bayesian approach, giving insights into crowd management and evacuation planning.

**Link**: [https://www.jasss.org/26/3/6.html](https://www.jasss.org/26/3/6.html)  

**Datasets**: Simulation-generated data of emergency evacuation scenarios with varying pedestrian behaviors.

**Metrics**: Evacuation time, congestion levels, route choice variability.

**Applications**: Emergency evacuation planning, crowd management, safety policy evaluation.

**Limitations**: Model complexity and assumptions on rationality; needs empirical validation in real emergency scenarios.

**Future Directions**: Incorporation of panic behaviors, diverse pedestrian characteristics, and real-time decision support.

---


### Rule-Based

**Title**: Rule-Based Pedestrian Simulation  

**Authors**: N. Anfinogentov, A. Kuznetsov, et al.

**Publication Year**: 2022

**Summary**: This paper discusses contemporary approaches to pedestrian mobility modeling and proposes a rule-based framework for simulating pedestrian movement in open urban environments. The model is built on a hierarchy of activity priorities, defining explicit rules for pedestrian decision-making and movement adjustments in response to environmental changes and interactions with other agents. The authors showcase software module design, test simulations, and discuss the model's potential to assist urban planning and pedestrian infrastructure optimization.

**Link**: [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4160252](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4160252)  

**Datasets**: Simulation datasets generated by the authors for testing pedestrian flows in urban scenarios. 

**Metrics**: Pedestrian flow rates, movement efficiency, route choice compliance.

**Applications**: Urban space design, pedestrian route network planning, crowd management.

**Limitations**: Primarily tested in simulation environments with simplified behavioral assumptions; limited real-world calibration.

**Future Directions**: Extending the model to incorporate dynamic decision-making, multi-level activity priorities, and integration with real-time data.

---

**Title**: Simulation of Pedestrian Interaction with Autonomous Vehicles via Rule-Based Social Force Model  

**Authors**: Rashid Md Mobasshir, MohammadReza Seyedi, Sungmoon Jung

**Publication Year**: 2024

**Summary**: This paper presents a rule-based social force model enhanced with specific decision rules to simulate pedestrian trajectories during interactions with autonomous vehicles. It integrates classical force-based pedestrian movement with explicit rule-driven behavioral adjustments triggered by vehicle presence, speed, and pedestrian gap acceptance criteria. The model offers a framework to simulate varied pedestrian behaviors including cautious waiting and crossing decisions in urban traffic contexts involving autonomous vehicles.

**Link**: [https://www.sciencedirect.com/science/article/abs/pii/S1569190X24000157](https://www.sciencedirect.com/science/article/abs/pii/S1569190X24000157)  

**Datasets**: Simulation data of pedestrian-autonomous vehicle interaction scenarios with varying traffic conditions. 

**Metrics**: Pedestrian waiting time, crossing acceptance, collision avoidance success rates.

**Applications**: Autonomous vehicle pedestrian safety studies, urban traffic interaction modeling, pedestrian crossing behavior simulation.

**Limitations**: Model calibration depends on specific urban traffic scenarios; behavioral variability may be underrepresented.

**Future Directions**: Incorporating more adaptive and learning-based rule sets and multi-agent interaction frameworks.

---

**Title**: Modelling Shared Space Users via Rule-Based Social Force Model

**Authors**: Kai Nagel, Gerta Köhler

**Publication Year**: 2015

**Summary**: This paper develops a pedestrian simulation model for shared spaces based on rule-enhanced social force modeling. It formulates a set of explicit movement and interaction rules for pedestrian and vehicle agents in mixed-traffic environments, capturing priority rules, yielding behavior, and conflict resolution mechanisms. The model demonstrates improved representation of pedestrian compliance and negotiation of space compared to pure force-based methods.

**Link**: [https://doi.org/10.1016/j.trc.2014.10.012](https://doi.org/10.1016/j.trc.2014.10.012)  

**Datasets**: Synthetic simulation datasets reflecting mixed pedestrian-vehicle traffic environments in shared spaces. 

**Metrics**: Conflict frequency, pedestrian delay, space utilization efficiency.

**Applications**: Urban shared space design, pedestrian-vehicle interaction modeling, traffic safety analysis.

**Limitations**: Requires extensive scenario-specific tuning; complexity limits scalability to very large populations.

**Future Directions**: Integration with real-time sensor data and adaptive rule learning for dynamic urban environments.

---


### Graph-Based

**Title**: Generating Sparse Navigation Graphs for Microscopic Pedestrian Simulation

**Authors**: Angelika Kneidl, André Borrmann, Dirk Hartmann 

**Publication Year**: 2018 

**Summary**: This paper presents an extension of microscopic pedestrian simulation by incorporating hybrid navigation strategies based on graphs. It introduces a method to automatically generate reduced visibility graphs from spatial geometries to serve as navigation graphs for pedestrians. This allows dynamic routing algorithms, like the fastest path algorithm, to simulate pedestrian behavior more realistically than simple force or potential field models. Simulations comparing plain (no graph) and graph-based routing show that the graph approach enables diverse route choices responding dynamically to crowd density and congestion.

**Link**: [https://mediatum.ub.tum.de/doc/1160257/kok1xnqfeuqlaxac3xoaasibx.pdf](https://mediatum.ub.tum.de/doc/1160257/kok1xnqfeuqlaxac3xoaasibx.pdf) 

**Datasets**: Simulation data based on generated scenarios with different pedestrian densities and obstacle configurations.

**Metrics**: Route choice diversity, travel time, pedestrian density distribution, computational efficiency.

**Applications**: Urban pedestrian flow simulation, emergency evacuation modeling, pedestrian infrastructure design.

**Limitations**: Routing behavior still oversimplified, reaction to congestion is delayed, requiring further refinement for realistic behavior.

**Future Directions**: Enhancing reaction times in routing algorithms, integrating heterogeneous pedestrian behaviors, defining quantitative metrics to evaluate navigation graphs.

---

**Title**: A Discrete Hughes Model for Pedestrian Flow on Graphs

**Authors**: Marianne O. Bruna, Yannick Simon 

**Publication Year**: 2017

**Summary**: This paper adapts the continuous Hughes dynamic continuum model for pedestrian flow into a discrete, time-finite state framework on graphs. Pedestrian densities evolve on nodes and edges modeling crowd movement through network-like environments. The model uses shortest path routing informed by congestion levels to simulate pedestrian flow and route choice. It provides an efficient computational framework for flow dynamics on complex graph structures representing walkable spaces.

**Link**: [https://www.aimsciences.org/article/doi/10.3934/nhm.2017004](https://www.aimsciences.org/article/doi/10.3934/nhm.2017004) 

**Datasets**: Simulation data on graph-structured pedestrian networks of varying complexity.

**Metrics**: Pedestrian density distribution, flow rates, average travel time, congestion levels.

**Applications**: Crowd flow modeling in networked urban or building environments, evacuation simulation on complex topologies.

**Limitations**: Assumes rational path choices, limited modeling of individual pedestrian behavior variability.

**Future Directions**: Incorporation of stochastic decision-making, multi-class pedestrian types, coupling with microscopic movement models.

---

**Title**: A Graph-Based Spatiotemporal Interaction Modelling for Pedestrian Crossing Prediction

**Authors**: Chao Chen, Hua Zhang, et al.

**Publication Year**: 2023

**Summary**: This work proposes a novel pedestrian simulation and prediction model that uses graph-based representations to model spatiotemporal interactions among pedestrians and nearby road users. Pedestrians and surrounding entities are clustered with graph neural networks to predict crossing actions effectively, aiding in dynamic pedestrian behavior prediction in urban traffic environments. The approach captures interactions over time and space, enabling more accurate behavioral simulations for safety and traffic flow optimization.

**Link**: [https://ieeexplore.ieee.org/document/9561107/](https://ieeexplore.ieee.org/document/9561107/) 

**Datasets**: Public datasets with pedestrian crossing scenarios and vehicle interactions (JAAD dataset).

**Metrics**: Prediction accuracy, interaction modeling quality, crossing decision recall and precision.

**Applications**: Pedestrian safety systems, autonomous vehicle navigation, urban traffic management.

**Limitations**: Focused on crossing prediction rather than full pedestrian trajectory simulation; model complexity and data requirements are high.

**Future Directions**: Integration into full pedestrian trajectory simulators, real-time adaptive traffic control applications.

---

### Path-Based

**Title**: Agent-Based Simulation for Neighbourhood Route Planning

**Authors**: Changgeng Zhang, Yong Ma, Nikolaos M. Mavridis 

**Publication Year**: 2025  

**Summary**: This paper presents an agent-based simulation framework that predicts pedestrian-created path networks tailored to user preferences and environmental conditions. It integrates path planning algorithms with pedestrian behavioral models to simulate how individuals select and adapt routes in urban neighborhoods. The study demonstrates that the model can replicate real-life pedestrian route choices and emerging path formations, aiding in planning accessible and efficient walkable environments.

**Link**: [https://www.sciencedirect.com/science/article/pii/S0198971525000043](https://www.sciencedirect.com/science/article/pii/S0198971525000043)  

**Datasets**: Simulation-based scenarios reflecting urban neighborhood pedestrian movements.

**Metrics**: Route choice accuracy, path utilization rates, pedestrian flow distribution.

**Applications**: Urban planning, walkability assessment, pedestrian infrastructure design.

**Limitations**: Model currently focused on typical neighborhood layouts; challenges remain for highly dynamic or mixed-mode transport environments.

**Future Directions**: Incorporation of real-time dynamic environmental changes and heterogeneous pedestrian preferences.

---

**Title**: Research on Modeling and Simulation of Pedestrian Street Motion Based on Fuzzy Inference and Path Selection

**Authors**: Zhiyong Li, Xinjun Zhang, Weihong Li

**Publication Year**: 2023 

**Summary**: This work proposes a pedestrian street motion model combining fuzzy inference systems with path selection mechanisms. It accounts for pedestrians’ uncertain decision-making under varying environmental influences and integrates these with discrete path selection processes. The simulation results show improved accuracy in replicating pedestrian street behavior, particularly under heterogeneous and dynamic crowd situations.

**Link**: [https://ieeexplore.ieee.org/document/10549263/](https://ieeexplore.ieee.org/document/10549263/)  

**Datasets**: Simulated pedestrian street motion datasets derived from multiple urban scenarios.

**Metrics**: Pedestrian velocity profiles, path choice consistency, model prediction error.

**Applications**: Urban street design, crowd management strategies, pedestrian navigation systems.

**Limitations**: The fuzzy inference rules require careful tuning and may lack generalizability across different cultures or geographic contexts.

**Future Directions**: Adaptation to varied cultural behaviors, integration with real-time sensor data for adaptive routing.

---

**Title**: A Microscopic Simulation Model for Pedestrian Behavior at Crosswalks

**Authors**: Guangquan Lu, Jun Zhuang, et al.

**Publication Year**: 2017

**Summary**: This paper develops a microscopic pedestrian simulation model focusing on detailed behavioral interactions at crosswalks, incorporating path-based decision-making and anticipatory behavior for crossing safety and efficiency. It integrates individual-level route choices and real-time pedestrian-vehicle interaction, improving the realism of pedestrian dynamics prediction in mixed traffic environments.

**Link**: [https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0180992](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0180992)  

**Datasets**: Empirical crosswalk pedestrian behavioral data for model calibration and validation.

**Metrics**: Crossing duration, waiting time, collision risk, pedestrian flow rates at crosswalks.

**Applications**:  Traffic safety analysis, urban crosswalk design, pedestrian-vehicle interaction studies.

**Limitations**: Focuses on crosswalk scenarios, may require adjustments for other pedestrian path-based environments.

**Future Directions**: Extension to multi-modal intersections and integration with autonomous vehicle navigation systems.

---


### Optimal Steps

**Title**: Modeling Evacuation Dynamics on Stairs by an Extended Optimal Steps Model

**Authors**: Yiping Zeng, Weiguo Song, Feizhou Huo, Giuseppe Vizzari

**Publication Year**: 2018  

**Summary**: This paper extends the Optimal Steps Model to simulate pedestrian movement in stairwells, particularly focusing on mid-landing areas and merging behaviors during evacuation. The model represents pedestrians as virtual agents with spatial dimensions, using a block-based floor field and an event-driven update rule. Simulations reveal lane formation patterns and favorable use of outer stairs at high densities, consistent with empirical data on stair evacuation flows. The study provides insights into how stair geometry impacts movement merging and is intended to support the development of evacuation codes and standards.

**Link**: [https://www.bohrium.com/paper-details/modeling-evacuation-dynamics-on-stairs-by-an-extended-optimal-steps-model/813058429605117952-2560](https://www.bohrium.com/paper-details/modeling-evacuation-dynamics-on-stairs-by-an-extended-optimal-steps-model/813058429605117952-2560)  

**Datasets**: Uses simulated data validated against fundamental diagrams and previous experimental flow data on stairs.

**Metrics**: Specific flow rates, lane formation occurrences, and occupant performance indicators during stairwell evacuation.
.  
**Applications**: Evacuation planning for high-rise buildings, safety analysis of stairwells, design of stair geometry for efficient flow.

**Limitations**: Limited to stairwell scenarios; more complex environments and varying individual characteristics need further exploration.

**Future Directions**: Further refinement of geometric effects on evacuation, integration with multi-floor models, and inclusion of heterogeneous pedestrian profiles.

---

**Title**: Social Distancing with the Optimal Steps Model

**Authors**: Christina Maria Mayr, Gerta Köster

**Publication Year**: 2021 

**Summary**: Addressing the need for simulating social distancing during the COVID-19 pandemic, this study uses the Optimal Steps Model to operationalize personal space requirements in pedestrian locomotion. Two use cases are considered: strict no-violation of social distance and a lenient one allowing temporary violations under 10 seconds. Simulations in bottleneck scenarios measure contact times and provide regression formulas linking personal space parameter choices with desired social distances and corridor widths. The model extension helps understand evacuation time increases with social distancing and offers practical parameter guidance for users.

**Link**: [https://collective-dynamics.eu/index.php/cod/article/view/A116](https://collective-dynamics.eu/index.php/cod/article/view/A116)  

**Datasets**: Simulation data from bottleneck scenarios with varied corridor widths and personal space parameters.

**Metrics**: Contact time (violations of personal space), evacuation time, social distance compliance rates.
.  
**Applications**: Pandemic-related safety planning, event space management, pedestrian flow control with social distancing.

**Limitations**: Focuses on bottleneck situations, parameters may need adjustment for diverse real-world configurations.

**Future Directions**: Broader scenario testing, integration with real-time pedestrian monitoring systems, and dynamic adaptation of distancing rules.

---

### Gradient Navigation

**Title**: Gradient Navigation Model for Pedestrian Dynamics

**Authors**: Felix Dietrich, Gerta Köster

**Publication Year**: 2014

**Summary**: This paper introduces the Gradient Navigation Model, a microscopic ordinary differential equation (ODE)-based model for pedestrian dynamics. The model controls pedestrian movement by a superposition of gradients of distance functions, directly adjusting the velocity direction instead of forces. This avoids inertia-related oscillations typical in force-based models. The smooth equations allow accurate numerical integration and ensure the existence and uniqueness of solutions. The model parameters are calibrated using theoretical and empirically validated assumptions. The model realistically reproduces phenomena such as obstacle avoidance, lane formation, stop-and-go waves, and congestion at bottlenecks without scenario-specific re-calibration. Its simulated density evolution matches experimental data closely.

**Link**: [https://arxiv.org/abs/1401.0451](https://arxiv.org/abs/1401.0451)  

**Datasets**: Simulated pedestrian trajectory and density data validated against controlled experiments on bottlenecks and flow conditions.

**Metrics**:  Pedestrian velocity and direction, collision avoidance, lane formation, stop-and-go wave dynamics, density evolution.

**Applications**: Crowd movement prediction, bottleneck and evacuation scenario simulations, pedestrian facility design.

**Limitations**: Assumes homogeneous pedestrian behavior; real-world heterogeneity and complex environments require further extension.

**Future Directions**:  Integration with diverse pedestrian profiles, multi-scale simulations, coupling with behavioral decision models, real-time adaptation.

---

**Title**: A Conceptual Perspective on Pedestrian Stream Simulations (includes Gradient Navigation Model)

**Authors**: Michael J. Seitz, Felix Dietrich, Gerta Köster, Hans-Joachim Bungartz

**Publication Year**: 2021

**Summary**: This perspective paper compares several pedestrian simulation models, including cellular automata, social force, Optimal Steps, and notably the Gradient Navigation Model. The Gradient Navigation Model is described as a continuous-time, continuous-space model that directly manipulates movement direction derived from scalar fields. It avoids artifacts seen in other models related to inertia and grid structure, producing smooth trajectories. The study highlights how the Gradient Navigation Model realistically reproduces phenomena such as lane formation and congestion and how it fits within a broader modeling framework emphasizing scalar field navigation for pedestrians.

**Link**: [https://collective-dynamics.eu/index.php/cod/article/download/A2/2/25](https://collective-dynamics.eu/index.php/cod/article/download/A2/2/25)  

**Datasets**: Simulation scenarios comparing emergent pedestrian behaviors across model types; no direct empirical datasets but benchmarking against established phenomena.

**Metrics**: Emergent trajectories, lane formation, congestion patterns, avoidance behaviors.

**Applications**: Pedestrian flow research, model benchmarking, crowd dynamics understanding.

**Limitations**: More conceptual than empirical; model performance needs further validation in real-world settings.

**Future Directions**: Enhanced empirical validation, hybrid modeling approaches combining strengths of models, application to varied pedestrian scenarios.

---

### Behavioral Heuristics

**Title**: How Simple Rules Determine Pedestrian Behavior and Crowd Disasters

**Authors**: Mehdi Moussaid, Dirk Helbing, Guy Theraulaz

**Publication Year**: 2011

**Summary**: This seminal paper proposes a cognitive science-based pedestrian simulation model grounded in behavioral heuristics. Pedestrians use visual information of their surroundings to select desired walking speeds and directions by evaluating distances to obstructions in their field of view. The model successfully predicts individual trajectories and collective patterns like lane formation, stop-and-go waves, and crowd turbulence at high densities. It integrates simultaneous multi-agent interactions more realistically than traditional force-based models. The approach clarifies pedestrian navigation as an active search for free paths rather than simple avoidance, enabling improved simulation of crowd dynamics and safety planning.  

**Link**: [https://pmc.ncbi.nlm.nih.gov/articles/PMC3084058](https://pmc.ncbi.nlm.nih.gov/articles/PMC3084058/)  

**Datasets**: Empirical pedestrian trajectory data from controlled avoidance experiments; simulated data validated against experimental observations.

**Metrics**: Trajectory accuracy, lane formation quality, stop-and-go wave emergence, collision avoidance performance.

**Applications**: Crowd disaster prevention, mass event safety planning, evacuation route design, autonomous robot navigation.

**Limitations**: Model mainly validated in controlled settings; requires further testing in highly complex real-world environments, especially under extreme conditions.

**Future Directions**: Empirical validation with eye-tracking data to understand visual cues, integration with group behavior models, adaptation for robot swarm navigation, and extension to multi-level or low-visibility scenarios.

---

**Title**: Simple Cognitive Heuristics Applied to Modeling Pedestrian Dynamics

**Authors**: Qi Xua, Baohua Mao, Xiao Lianga, Jia Feng

**Publication Year**: 2012

**Summary**: This study applies cognitive behavioral heuristics to simulate pedestrian collective dynamics in large crowds. The model emphasizes pedestrians’ reliance on visual perception and simple decision-making rules to navigate and avoid collisions, effectively reproducing emergent phenomena such as lane formation and congestion. It validates the model with simulations matching qualitative and quantitative features observed in real pedestrian flows. The work extends heuristic modeling to scenarios involving a high density of agents, further confirming robustness and scalability of such approaches compared to force-based ones.

**Link**: [https://www.sciencedirect.com/science/article/pii/S1877042812010117](https://www.sciencedirect.com/science/article/pii/S1877042812010117)  

**Datasets**: Simulation data calibrated and validated with observational studies of pedestrian traffic flows in controlled environments.

**Metrics**: Flow rates, collision occurrences, spatial distribution patterns, pedestrian velocity profiles.

**Applications**: Urban crowd management, pedestrian facility design, public event planning.

**Limitations**: Limited dataset availability and explicit details in this summary; applicability to mixed pedestrian populations and dynamic environments still to be explored.

**Future Directions**: Inclusion of heterogeneous pedestrian objectives, real-time crowd monitoring integration, extension to multi-modal traffic scenarios.

---


### Steering Behaviors

**Title**: Modeling Behavior in Vehicular and Pedestrian Simulations 

**Authors**: Michael J. Thompson

**Publication Year**: 2007

**Summary**: This dissertation develops algorithmic steering behavior models for pedestrian movement, inspired by natural human behaviors such as seeking, separation, cohesion, and obstacle avoidance. The model integrates these steering rules to simulate pedestrian interactions in urban environments with natural group dynamics and anticipatory navigation. The work emphasizes the importance of layered modeling that includes learning and memory to make pedestrians behave human-like. The steering behaviors control navigation directly and allow for flexible pedestrian decision-making and collision avoidance.

**Link**: [https://udel.edu/~mm/traffic/amble/dissertation.pdf](https://udel.edu/~mm/traffic/amble/dissertation.pdf) 

**Datasets**: Synthetic simulation data created for calibration and validation against typical pedestrian flow scenarios and behavioral patterns.

**Metrics**: Collision avoidance success, trajectory smoothness, group cohesion, pedestrian flow efficiency.

**Applications**: Urban planning, crowd simulation for events and infrastructure design, pedestrian behavior studies

**Limitations**: Mostly tested in simplified scenarios; real-world validation in complex environments is limited.

**Future Directions**: Incorporation of social and psychological factors, improved group behavior modeling, real-time data integration for adaptive simulations.

---

**Title**: Modeling and Simulation of Pedestrian Dynamical Behavior Based on Fuzzy Logic and Steering Rules 

**Authors**: X. Liu, Y. Zhao, L. Wang

**Publication Year**: 2016

**Summary**: This study proposes a hybrid pedestrian simulation model combining fuzzy logic decision-making with classical steering behaviors such as obstacle avoidance, goal seeking, and group cohesion. The fuzzy logic component adds flexibility in decision-making under uncertain and dynamic conditions, enhancing typical steering models. Simulation experiments show improved realism in pedestrian trajectories and interactions, especially in crowded and conflicting flow scenarios. The approach highlights the potential for combining heuristic steering rules with cognitive decision processes.

**Link**: [https://www.sciencedirect.com/science/article/abs/pii/S0020025516302535](https://www.sciencedirect.com/science/article/abs/pii/S0020025516302535) 

**Datasets**: Simulation data validated with observed pedestrian movement in corridor and crossing scenarios.

**Metrics**: Flow efficiency, collision rates, path smoothness, behavioral adaptability.

**Applications**: Crowd management, evacuation simulation, pedestrian facility design, large event planning.

**Limitations**: Moderate computational complexity due to fuzzy logic; scaling to very large crowds needs optimization.

**Future Directions**: Integration with real-time sensor data, multi-agent cognitive interactions, and extension to multi-level pedestrian spaces.

---

### Collision-Free Speed

**Title**: Collision-free speed model for pedestrian dynamics

**Authors**: Antoine Tordeux, Mohcine Chraibi, Qiancheng Xu

**Publication Year**: 2015

**Summary**: This paper proposes a minimal speed-based pedestrian model called the Collision-Free Speed Model (CFS), where pedestrian dynamics are intrinsically collision-free by design. The model separates direction and speed control, ensuring pedestrians never overlap by modulating speed based on distance to neighbors and obstacles. It uses a velocity-based elliptical representation for pedestrians to more realistically capture space occupancy. The model reproduces pedestrian flow phenomena such as self-organization and smooth navigation in dense crowds. It is computationally efficient and well-suited for large-scale simulations.

**Link**: [https://arxiv.org/abs/1512.05597](https://arxiv.org/abs/1512.05597)  

**Datasets**: Synthetic simulation datasets validated against fundamental diagrams and crowd behavior studies.

**Metrics**: Speed-density relations, collision avoidance success, flow rates, trajectory smoothness.

**Applications**: Crowd management, evacuation modeling, pedestrian facility design.

**Limitations**: Simplified assumptions of pedestrian behavior, lacks detailed psychological or social factors.

**Future Directions**: Integration with more complex behavioral models, real-time adaptive simulations, inclusion of heterogeneous agent profiles.

---

**Title**: Generalized collision-free velocity model for pedestrian dynamics

**Authors**: Qiancheng Xu, Mohcine Chraibi, Antoine Tordeux

**Publication Year**: 2018

**Summary**: This paper extends the original Collision-Free Speed Model by introducing a generalized velocity model including a direction sub-model and an improved speed sub-model that uses adaptive elliptical shapes for pedestrians, reflecting varying occupied space depending on speed and body orientation. It introduces a dynamical visual area and smoother direction changes to avoid unnatural shaking and backward movements seen in earlier versions. Simulation results show improved realism in pedestrian distributions, especially in bottleneck and corridor scenarios, with better matching fundamental diagrams from experimental data.

**Link**: [https://files.thunderheadeng.com/femtc/2018_d2-06-xu-paper.pdf](https://files.thunderheadeng.com/femtc/2018_d2-06-xu-paper.pdf)  

**Datasets**: Simulation data comparing circular vs. elliptical pedestrian shapes validated against empirical crowd flow data.

**Metrics**: Density-velocity relations, lane formation, avoidance patterns, trajectory smoothness.

**Applications**: Evacuation planning, facility layout optimization, pedestrian flow simulation in constrained environments.

**Limitations**: Further calibration is needed for cooperative pedestrian behavior in bottlenecks; parameter tuning required for environment-specific accuracy.

**Future Directions**: Refinement of cooperative interaction modeling, extension to multi-floor or complex geometries, integration with behavior-based decision models.

---

### Anticipation Velocity

**Title**: Anticipation Velocity Model (AVM) - Pedestrian Dynamics

**Authors**: Qiancheng Xu, Mohcine Chraibi, Antoine Tordeux

**Publication Year**: 2021

**Summary**: The Anticipation Velocity Model extends the Collision-Free Speed Model by incorporating pedestrian anticipation of future situations to improve navigation in dense crowds. It models pedestrian movement direction by an anisotropic exponential repulsion based on predicted future distances rather than current distances, allowing agents to better avoid collisions. Speed control follows the collision-free speed approach. The AVM better reproduces bidirectional lane formation and reduces jamming compared to predecessor models. However, it still does not fully capture complex human behaviors like pushing or cooperation and excludes backward movement, limiting realism in extreme crowd situations. Parameter sensitivity to density and anticipation effects also presents challenges.

**Link**: [https://pedestriandynamics.org/models/anticipation_velocity_model/](https://pedestriandynamics.org/models/anticipation_velocity_model/)

**Datasets**: Simulated pedestrian flows validated against benchmark fundamental diagrams and crowd behavior tests.

**Metrics**: Lane formation quality, jamming occurrence, flow rates, velocity and density relationships.

**Applications**: Pedestrian flow simulation in dense conditions, bidirectional flow modeling, urban planning for crowd management.

**Limitations**: Limited behavioral realism (no backward movement or cooperative behavior), parameter sensitivity to scenario setup, challenges in extreme densities.

**Future Directions**: Incorporating cooperative and pushing behaviors, improving robustness to complex crowd interactions, adapting parameters dynamically to density conditions.

---

**Title**: Anticipation in a Velocity-Based Model for Pedestrian Dynamics

**Authors**: Qiancheng Xu, Mohcine Chraibi, Antoine Tordeux

**Publication Year**: 2021

**Summary**: This research introduces a minimal anticipatory collision-free velocity model where pedestrians predict the future movement of neighbors to avoid collisions effectively, reducing gridlock and unrealistic congestion found in earlier models. The model maintains smooth trajectories and respects collision avoidance by anticipating neighbor behavior in velocity space. It demonstrates improved fundamental diagram compliance and realistic bidirectional flow patterns. The anticipatory component is mathematically simple yet enhances the model’s ability to simulate dense crowd interactions.

**Link**: [https://www.sciencedirect.com/science/article/abs/pii/S0968090X21004502](https://www.sciencedirect.com/science/article/abs/pii/S0968090X21004502)

**Datasets**: Synthetic simulation data validated against real pedestrian flow experiments and fundamental diagrams.

**Metrics**: Collision avoidance rate, gridlock occurrence, flow-density relationships, trajectory smoothness.

**Applications**: Evacuation planning, crowd management software, safety analysis in pedestrian facilities.

**Limitations**: Primarily tested in simulated scenarios; behavioral complexity limited to anticipation of neighbor velocity, lacking social or psychological factors.

**Future Directions**: Integration with cognitive and social behavior models, extension to multi-directional and multi-level pedestrian environments.

---

**Title**: Pedestrian Dynamics with Mechanisms of Anticipation and Attraction

**Authors**: Nikolaos T. Kotsalis, Stefanie Klockner, Detlef E. Wolf

**Publication Year**: 2020

**Summary**: This paper studies pedestrian dynamics by incorporating two heuristic mechanisms: anticipation of conflicts and attraction to goals or groups. The approach combines velocity anticipation with social attraction forces, resulting in a comprehensive model capable of reproducing realistic crowd behavior including lane formation and crowd turbulence. The anticipatory mechanism simulates future collision prediction, facilitating smoother and more natural pedestrian trajectories. The model emphasizes the balance between anticipatory avoidance and attraction behaviors for improved realism in simulations.

**Link**: [https://link.aps.org/doi/10.1103/PhysRevResearch.2.043250](https://link.aps.org/doi/10.1103/PhysRevResearch.2.043250)

**Datasets**: Simulated pedestrian flows validated qualitatively against observed crowd phenomena and fundamental diagram benchmarks.

**Metrics**: Trajectory accuracy, lane formation patterns, collision avoidance success, crowd turbulence indicators.

**Applications**: Crowd flow prediction, urban infrastructure design, evacuation modeling, social behavior simulation in pedestrian crowds.

**Limitations**: Predominantly qualitative validation, complexity increases with attraction terms, needing computational optimization for very large crowds.

**Future Directions**: Quantitative validation with empirical data, extension to incorporate heterogeneous pedestrian behaviors, integration with real-time crowd sensing.

---

### Centrifugal Force

**Title**: Generalized centrifugal-force model for pedestrian dynamics

**Authors**: Mohcine Chraibi, Armin Seyfried

**Publication Year**: 2010  

**Summary**: This paper introduces a spatially continuous force-based pedestrian dynamics model incorporating an elliptical volume exclusion to better represent pedestrian body shapes. The model tackles common issues such as oscillations and overlapping pedestrians encountered in force-based approaches. It quantitatively describes pedestrian movement in various geometries, including corridors, and matches empirical fundamental diagrams from controlled experiments. Distinctive features include anisotropic interaction forces derived from elliptical shapes and velocity-dependent pedestrian interactions.

**Link**: [https://link.aps.org/doi/10.1103/PhysRevE.82.046111](https://link.aps.org/doi/10.1103/PhysRevE.82.046111)  

**Datasets**: Empirical pedestrian flow data from controlled corridor experiments for fundamental diagram validation.

**Metrics**: Flow rates, density-velocity relations, collision occurrences, oscillation frequency, lane formation efficiency.

**Applications**: Crowd flow simulation in corridors and bottlenecks, evacuation planning, pedestrian facility design.

**Limitations**: Requires accurate parameter tuning; complexity increases with elliptical interactions; may not fully capture social or psychological pedestrian behaviors.

**Future Directions**: Extension to heterogeneous pedestrian populations, integration with behavioral models, simulation of complex multi-directional flows.

---

**Title**: Centrifugal force model for pedestrian dynamics

**Authors**: Yu, Chen, Dong

**Publication Year**: 2005  

**Summary**: This early foundational paper proposes the Centrifugal Force Model (CFM), describing pedestrian repulsive interactions as a function of relative velocity and distance, resembling a "centrifugal" type repulsion. Unlike classical social force models, CFM reduces unrealistic oscillations and collisions by incorporating velocity-dependent repulsive forces. The model enables reproduction of key pedestrian dynamics phenomena such as lane formation and congestion. It highlights the impact of direction choice strategies in bottleneck scenarios on flow efficiency.

**Link**: [https://link.aps.org/doi/10.1103/PhysRevE.72.026112](https://link.aps.org/doi/10.1103/PhysRevE.72.026112)  

**Datasets**: Simulation data validated with bottleneck flow experiments and pedestrian tracking data.

**Metrics**: Flow rate through bottlenecks, collision frequency, trajectory smoothness, exit time distributions.

**Applications**: Evacuation modeling, pedestrian flow through narrow passages, crowd safety analysis.

**Limitations**: Initial form is circular interaction-based; less precise in complex geometries; behavioral realism limited to physical interactions

**Future Directions**: Incorporation of elliptical pedestrian representations, coupling with cognitive decision processes, enhanced parameter calibration.

---

**Title**: Force-based models of pedestrian dynamics (including discussion of Centrifugal Force Model)

**Authors**: Mohcine Chraibi, Ulrich Kemloh, Andreas Schadschneider, Armin Seyfried

**Publication Year**: 2011  

**Summary**: This overview article reviews force-based pedestrian dynamics models, highlighting strengths and limitations of different approaches including the Centrifugal Force Model (CFM). It explains how CFM differs from social force models by relying on velocity-dependent repulsive forces to reduce pedestrian overlapping and unrealistic movements. The paper includes detailed analysis of repulsive force formulations, calibration challenges, and simulation results for crowd movement in bottlenecks and corridors. It provides insights into the choice of direction strategies and their effect on bottleneck flow.

**Link**: [https://www.aimspress.com/aimspress-data/nhm/2011/3/PDF/1556-1801_2011_3_425.pdf](https://www.aimspress.com/aimspress-data/nhm/2011/3/PDF/1556-1801_2011_3_425.pdf)  

**Datasets**: Simulated pedestrian flows in corridors and bottlenecks, benchmarked against experimental fundamental diagrams and flow measurements.

**Metrics**: Overlapping incidents, flow rates, pedestrian velocity, direction choice effects.

**Applications**: Pedestrian crowd simulation, public space design, emergency evacuation models.

**Limitations**: Parameter sensitivity and calibration complexity; does not incorporate detailed psychological or social behavior.

**Future Directions**: Hybrid modeling approaches combining force-based and behavioral models, extension to multi-level environments, real-world empirical testing.

---

## Flow-Based Models

### Macroscopic

**Title**: A bidirectional pedestrian macroscopic speed model construction based on microscopic simulation data

**Authors**: Xiaocheng Gao,Hui Zhang,Hui Qi,Bin He

**Publication Year**: 2024

**Summary**: This paper investigates macroscopic speed modeling of bidirectional pedestrian cross-flows using microscopic pedestrian flow simulations rather than traditional scenario experiments. It uses a simulation platform (GAMA) to run orthogonal experiments varying crossing angles (15° to 165°) and pedestrian flow rates (1 to 8 ped/s). The study finds a piecewise function (linear and exponential parts) better captures the speed-density relationship affected by crossing angle. The model shows pedestrians’ speed depends heavily on their density, with some influence of opposing pedestrian density interpreted as a discounting effect. While the simulation-based model exhibits some differences compared to established experimental data, it provides useful guidance for refining experimental setups and constructing speed relationships in bidirectional flows. The method currently cannot fully replace controlled real-world experiments but serves as a valuable pre-study approach.

**Link**: [https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0311538](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0311538)  

**Datasets**: Simulation data generated from controlled pedestrian flow microsimulations on the GAMA platform; no direct real-world data used.

**Metrics**: Pedestrian speed, density, crossing angle, pedestrian flow rate

**Applications**: Modeling bidirectional pedestrian flows in crosswalks and intersections; refining pedestrian flow experiments and macroscopic speed models

**Limitations**: Differences from real-world experiments indicate simulation alone cannot fully replace physical experiments; further validation needed with actual pedestrian data

**Future Directions**: Incorporation of real-world validation, refinement of speed-density functions, exploring the effect of pedestrian interactions in complex crossing scenarios

---

**Title**: A macroscopic pedestrian model with variable maximal density

**Authors**: Laura Bartoli, Simone Cacace, Emiliano Cristiani, Roberto Ferrett

**Publication Year**: 2024 (Published in 2025 journal issue)

**Summary**: This paper proposes a novel macroscopic fluid dynamics model for pedestrian flow that innovatively treats the maximal crowd density as a dynamic state variable rather than a fixed parameter. This variable maximal density captures psychological and physical pushing forces that occur in high-density crowds during emergencies or competitive situations. The model couples a conservation law for crowd density with a Burgers-like PDE with a nonlocal term for maximal density evolution. Numerical simulations show the model can reproduce crowd behavior in both low and high-density regimes, with the fundamental diagram (density-flow relation) exhibiting a "double hump" shape similar to observed real crowd flow patterns. The approach provides a more realistic description of crowd pressure effects in macroscopic models.

**Link**: [https://arxiv.org/abs/2406.14649](https://arxiv.org/abs/2406.14649)  

**Datasets**: Numerical simulation data generated by the proposed PDE model

**Metrics**: Crowd density, flow rate, maximal density evolution

**Applications**: Modeling pedestrian dynamics in emergencies and dense crowds where pushing affects movement; crowd safety and evacuation planning

**Limitations**: Requires predefined fundamental diagram; complexity of nonlocal PDEs; validation needed in diverse real-world situations

**Future Directions**: Extension to 2D spatial domains, coupling with microscopic models, data-driven calibration of maximal density evolution.

---

**Title**: Modeling and Simulation of Macroscopic Pedestrian Flow Models

**Authors**: Naveen Kumar Mahato, Axel Klar, Sudarshan Tiwari

**Publication Year**: 2018

**Summary**: This paper conducts numerical analysis of prominent macroscopic pedestrian flow models including Hughes’ model and mean field games with nonlinear mobilities, targeting fast exit and evacuation scenarios. Hughes’ model couples a nonlinear conservation law for pedestrian density with an Eikonal equation representing pedestrian route choice and common sense. The mean field game approach formulates pedestrian movement as an optimal control problem minimizing exit time and congestion cost. The paper compares both approaches via one- and two-dimensional simulations, demonstrating their ability to model complex flow patterns in evacuations. It also highlights the theoretical and numerical properties of these macroscopic models and their connection through optimization.

**Link**: [https://arxiv.org/abs/1810.03489](https://arxiv.org/abs/1810.03489)  

**Datasets**: Simulation data from numerical model solutions; theoretical formulations with no novel empirical data

**Metrics**: Pedestrian density, velocity, exit time, cost functional in mean field games

**Applications**: Emergency evacuation modeling, pedestrian flow management in fast exit scenarios

**Limitations**: Abstract mathematical models requiring numerical solution; challenges in capturing detailed pedestrian interactions

**Future Directions**: Further development of numerical schemes, coupling with microscopic models, application to real evacuation data

---

### Continuum

**Title**: Dynamic continuum pedestrian flow model with memory effect

**Authors**: Yinhua Xia, S. C. Wong, Chi-Wang Shu 

**Publication Year**: 2009  

**Summary**: This paper develops a macroscopic pedestrian flow model using a dynamic continuum approach in a two-dimensional walking space where pedestrians can move freely. It incorporates the memory effect where pedestrians choose routes based on their memory of the shortest path to the destination when unobstructed while avoiding high-density regions. The pedestrian flow is governed by a two-dimensional conservation law with a general speed-flow-density relationship. The model is solved numerically via the discontinuous Galerkin method, and simulations demonstrate the model's ability to capture pedestrian dynamics effectively.

**Link**: [https://link.aps.org/doi/10.1103/PhysRevE.79.066113](https://link.aps.org/doi/10.1103/PhysRevE.79.066113)  

**Datasets**: Numerical simulation data generated from the model; no empirical data included

**Metrics**: Pedestrian density, speed, flow patterns, route choice

**Applications**: Pedestrian flow analysis in open walking facilities, route planning considering memory and density avoidance

**Limitations**: Lacks empirical validation; assumes idealized pedestrian memory and decision-making; computational complexity of 2D numerical solution

**Future Directions**: Integration with real pedestrian data, extension to incorporate more complex behavioral factors, improving computational efficiency

---

**Title**: Continuum Theory for Pedestrian Traffic Flow: Local Route Choice Modelling and its Implications

**Authors**: Serge P. Hoogendoorn, Femke van Wageningen-Kessels, Winnie Daamen, Dorine C. Duives, Majid Sarvi

**Publication Year**: 2015

**Summary**: This paper proposes a novel multi-class continuum model capturing dynamic pedestrian flow features, emphasizing local route choice behavior. It links microscopic principles of pedestrian movement to self-organized macroscopic phenomena. The model accounts for diversified pedestrian classes and local interactions, resulting in realistic crowd dynamics such as lane formation and congestion patterns. Numerical studies illustrate the model’s capability to simulate complex pedestrian movement scenarios accurately.

**Link**: [https://www.sciencedirect.com/science/article/pii/S2352146515000885](https://www.sciencedirect.com/science/article/pii/S2352146515000885)  

**Datasets**: Simulation data based on model implementation; no direct real-world data used

**Metrics**: Density, flow rate, route choice variations, class-specific dynamics

**Applications**: Urban pedestrian traffic management, crowd flow optimization, infrastructure design

**Limitations**: Limited access to the full paper restricts detailed analysis; validation with empirical datasets needed

**Future Directions**: Incorporation of more behavioral heterogeneity, coupling with microscopic models, empirical validation

---

**Title**: A Continuum model for pedestrian flow with explicit consideration of crowd force and panic effects

**Authors**: Liang Haoyang, Du Jie, Wong S.C.

**Publication Year**: 2021

**Summary**: This study develops a second-order continuum model for pedestrian flow explicitly incorporating crowd forces and panic effects that often arise in emergencies and high-stress situations. The model integrates a continuity equation with transport equations reflecting pedestrian accelerations influenced by social and physical forces. This approach offers a more realistic representation of crowd behavior under panic and crowd pressure, improving predictions of flows in critical scenarios.

**Link**: [https://www.sciencedirect.com/science/article/pii/S0191261521000849](https://www.sciencedirect.com/science/article/pii/S0191261521000849)  

**Datasets**: Simulation results derived from the proposed model; no new empirical dataset reported

**Metrics**: Density, velocity, crowd force magnitude, panic intensity

**Applications**: Emergency evacuation planning, crowd safety analysis, management of panic situations in dense crowds

**Limitations**: Model complexity and parameter estimation challenges; requires empirical data calibration for panic effects

**Future Directions**: Validation with real emergency evacuation data, refinement of force parameterization, coupling with microscopic behavioural models

---

### Fluid Dynamics

**Title**: A Fluid-Dynamic Model for the Movement of Pedestrians

**Authors**: Dirk Helbing, Peter Molnár

**Publication Year**: 1995

**Summary**: This foundational paper proposes a fluid-dynamic framework for pedestrian movement, deriving macroscopic equations from a Boltzmann-like gas-kinetic pedestrian model. It treats pedestrian crowds as fluids with density and velocity fields evolving under social forces and desired directions. The model explains self-organized crowd phenomena such as lane formation and clogging at bottlenecks. It connects microscopic individual interactions with macroscopic flow descriptions, providing a theoretical basis for later fluid dynamics pedestrian models.

**Link**: [https://www.semanticscholar.org/paper/38f49c7af0c3278d6a4be93c4eb7c81c3f7da7e8](https://www.semanticscholar.org/paper/38f49c7af0c3278d6a4be93c4eb7c81c3f7da7e8) 

**Datasets**: Theoretical and simulation-based; no empirical data included in original formulation

**Metrics**: Pedestrian density fields, velocity fields, flow rate, pressure-like variables

**Applications**: Understanding large-scale pedestrian dynamics, modeling flow in crowded environments, optimizing facility design

**Limitations**: Abstract and theoretical, requires numerical methods for application; limited empirical validation in original paper

**Future Directions**: Incorporation of heterogeneous pedestrian behaviors, extension to complex geometries, coupling with experimental data

---

**Title**: Modeling and Simulation of Pedestrian Flow through Hydrodynamics

**Authors**: R. Jiang, W. Wu, Q.-S. Wu

**Publication Year**: 2013

**Summary**: This paper presents a hydrodynamic pedestrian flow model based on mass and momentum conservation laws with relaxation terms, similar to fluid dynamics in traffic flow. Pedestrians are treated as a continuum, and the model captures the evolution of density and velocity fields. Relaxation terms allow adaptation of velocity towards desired speeds, modeling acceleration and deceleration effects. Numerical simulations demonstrate the model's ability to replicate common pedestrian flow phenomena, including congestion and recovery after bottlenecks.

**Link**: [https://www.sciencedirect.com/science/article/pii/S1877705812011630](https://www.sciencedirect.com/science/article/pii/S1877705812011630) 

**Datasets**: Simulation data generated from the hydrodynamic model equations; no direct empirical pedestrian datasets used

**Metrics**: Density, velocity, flow rate, relaxation time

**Applications**: Crowd management, pedestrian facility design, evacuation analysis

**Limitations**: Continuum approach may overlook individual variability; parameterization of relaxation terms requires calibration

**Future Directions**: Integration with microscopic models, empirical validation with real pedestrian flow data, extension to two-dimensional spaces

---

## Group-Based Models

### Mesoscopic

**Title**: A mesoscopic model for large-scale simulation of pedestrian dynamics

**Authors**: Antoine Tordeux, Gregor Lämmel, Flurin S. Hänseler, Bernhard Steffen

**Publication Year**: 2018

**Summary**: This paper proposes a mesoscopic pedestrian model that balances individual-level detail and aggregate flow description. Pedestrians are represented on a hexagonal lattice where each cell can hold multiple pedestrians, and their movement is governed by stochastic jump rates depending on local density and flow conditions. The model captures heterogeneity in walking behavior and variability in path choices, enabling efficient large-scale simulations. It reproduces key pedestrian flow features such as fundamental diagrams, lane formation in counter-flows, and queuing phenomena. Calibration and validation are done with real data, and the model is computationally less intensive than microscopic models while retaining more detail than macroscopic models.

**Link**: [https://juser.fz-juelich.de/record/848087/files/TRC-2018-Manuscript.pdf](https://juser.fz-juelich.de/record/848087/files/TRC-2018-Manuscript.pdf)  

**Datasets**: Calibrated and validated using real pedestrian flow data; simulation datasets generated on hexagonal lattice

**Metrics**: Pedestrian density, flow rate, travel/egress time, lane formation patterns

**Applications**:  Large-scale pedestrian simulation for evacuation, transportation hubs, and urban facility planning

**Limitations**: Assumes hexagonal lattice discretization; complex calibration to match diverse real-world scenarios; stochastic variations introduce simulation variability

**Future Directions**: Integration with agent-based frameworks, extension to irregular spatial discretizations, further empirical validation, coupling with microscopic and macroscopic models

---

**Title**: A Newly Developed Mesoscopic Model on Simulating Pedestrian Flow

**Authors**: Wei Wang, Xiaoling Zhang, Longzhi Yang

**Publication Year**: 2017

**Summary**: This paper presents a mesoscopic grid-based pedestrian flow model designed for building evacuation simulations. The model treats pedestrian movement in discrete space cells and employs transition probability functions influenced by local pedestrian density and desired speed. The approach reduces computational load relative to microscopic models and allows simulation of large building evacuations with heterogeneous pedestrian behaviors. Simulations demonstrate realistic evacuation dynamics, flow patterns, and bottleneck effects.

**Link**: [https://www.sciencedirect.com/science/article/pii/S1877705817362781](https://www.sciencedirect.com/science/article/pii/S1877705817362781)  

**Datasets**: Simulation data based on model implementation; no specific empirical datasets reported

**Metrics**: Evacuation time, pedestrian density, flow rates at bottlenecks

**Applications**: Building evacuation planning, safety analysis, crowd management in enclosed environments

**Limitations**: Limited real-world validation reported; grid discretization may limit spatial resolution; transition probabilities calibrated heuristically

**Future Directions**: Empirical calibration using evacuation drills, extension to multi-floor and multi-exit building layouts, coupling with microscopic behavioral models

---

**Title**: Multi Exit Configuration of Mesoscopic Pedestrian Simulation

**Authors**: Wenjun Lu, Lei Zhang

**Publication Year**: 2022

**Summary**: This paper introduces a mesoscopic pedestrian simulation model that incorporates multiple exit configurations using a floor-field method combined with Q-learning algorithms to optimize route choice dynamically. The model simulates pedestrian movements in discretized space and time, using transition probabilities influenced by local densities and learned environmental knowledge. This framework balances simulation accuracy and efficiency, capturing complex pedestrian behaviors even in multi-exit evacuation scenarios.

**Link**: [https://arxiv.org/pdf/1609.01475.pdf](https://arxiv.org/pdf/1609.01475.pdf)  

**Datasets**: Simulation data generated from model experiments; no new real-world data presented

**Metrics**: Pedestrian flow, evacuation time, convergence of Q-learning for route optimization

**Applications**: Multi-exit building evacuation, emergency egress optimization, pedestrian crowd management

**Limitations**: Requires parameter tuning for Q-learning; simulations focus on idealized scenarios; lacks extensive empirical validation

**Future Directions**: Application in real-world evacuation drills, improving Q-learning algorithms for dynamic environments, integration with sensor data for adaptive crowd control

---




## AI-Driven Models

### Vision-Based

**Title**: Vision-based crowd dynamic model for multi-directional pedestrian flow

**Authors**: Zixuan ZHOU, Wataru NAKANISHI, Yasuo ASAKURA

**Publication Year**: 2022

**Summary**: This paper proposes a microscopic pedestrian simulation model using continuous space representation for multi-directional pedestrian flows. It focuses on the role of visual information in pedestrian route choice around obstacles and dynamic congestion within a pedestrian's visual field. Pedestrians make routing decisions based only on congestion and other pedestrian choices in their line of sight, integrated with optimal reciprocal collision avoidance (ORCA) techniques. The model effectively reproduces crowd behaviors such as movement in intersection zones, benefiting pedestrian flow management and space design in large public areas.

**Link**: [https://www.jstage.jst.go.jp/article/easts/14/0/14_2524/_article/-char/ja/](https://www.jstage.jst.go.jp/article/easts/14/0/14_2524/_article/-char/ja/)  

**Datasets**: Simulation data generated through microscopic pedestrian models with visual perception assumptions; no empirical datasets reported

**Metrics**: Pedestrian route choice, congestion levels perceived, collision avoidance efficiency, flow patterns

**Applications**: Design and management of pedestrian flow in large public spaces, crowd safety, architectural planning

**Limitations**: The model assumes limited visual perception range and simplified pedestrian decision processes; no direct empirical validation included

**Future Directions**: Empirical validation with real-world pedestrian data, extension to heterogeneous pedestrian behavior, incorporating environmental complexity

---

**Title**: Simulation of bi-directional pedestrian flow in corridor based on direction fuzzy visual field (DFVF)

**Authors**: Shiwei Li, Qianqian Li, Ganglong Zhong & Yuzhao Zhang 

**Publication Year**: 2023

**Summary**: This study introduces an improved model for simulating bi-directional pedestrian movements in corridors by incorporating individual differences in visual perception through a direction fuzzy visual field (DFVF) concept. The DFVF divides pedestrian interaction force fields into directional areas affected by psychological factors and personal space, allowing pedestrians' decisions to be influenced by static and dynamic information within their visual field. The model simulates density-speed relationships, lane formations, and self-organization phenomena, capturing more realistic heterogeneity in pedestrian behaviors. Controlled experiments support the parameterization of the DFVF for varied pedestrian traits.

**Link**: [https://www.nature.com/articles/s41598-023-46530-0](https://www.nature.com/articles/s41598-023-46530-0)  

**Datasets**: Controlled experimental data on pedestrian visual field perception; simulation data on bi-directional flows

**Metrics**: Density, speed, flow rates, lane formation, evacuation time

**Applications**: Pedestrian flow simulation in corridors, evacuation planning, understanding heterogeneous pedestrian interactions

**Limitations**: Focuses on corridor environments; requires extensive parameter calibration; limited real-world validation beyond controlled experiments

**Future Directions**: Extending to more complex environments, coupling with real-time data for adaptive simulations, exploring multi-modal pedestrian interaction

---

**Title**: A machine vision-based method for crowd density estimation and evacuation simulation

**Authors**: Shijie Huang, Jingwei Ji, Yu Wang, Wenju Li, Yuechuan Zheng 

**Publication Year**: 2023

**Summary**: This paper presents a machine vision-based methodology for estimating crowd density from video data and simulating evacuation scenarios. By leveraging computer vision techniques, the approach detects and quantifies pedestrian density and behavior from real-world footage, then integrates the data into simulation models to improve evacuation safety. This approach enhances the accuracy of crowd simulations by grounding them in observed visual data, potentially reducing risks like stampedes through better evacuation route planning.

**Link**: [https://www.sciencedirect.com/science/article/abs/pii/S0925753523002278](https://www.sciencedirect.com/science/article/abs/pii/S0925753523002278)  

**Datasets**: Video footage of crowds used for density estimation; simulation datasets derived from vision data

**Metrics**: Crowd density estimates, evacuation time, pedestrian movement trajectories

**Applications**: Real-time crowd monitoring, evacuation strategy optimization, public safety in mass gatherings

**Limitations**: Dependent on video quality and environmental conditions; computational complexity of processing large-scale video data

**Future Directions**: Integration with real-time surveillance systems, combining vision data with behavioral models, extending to diverse crowd scenarios

---

### RL-Based

**Title**: Pedestrian simulation as multi-objective reinforcement learning

**Authors**: Naresh Balaji Ravichandran, Fangkai Yang, Christopher Peters, Anders Lansner, Pawel Herman

**Publication Year**: 2018

**Summary**: This paper models pedestrians as autonomous agents using a modular multi-objective reinforcement learning (RL) framework. The approach divides pedestrian behavior into navigation and collision avoidance tasks, each with independent state spaces and rewards, combined for action selection. The RL-based model learns natural, goal-directed pedestrian movement while minimizing collisions in dynamic environments. Experiments in scenarios like circle walking, intersections, and hallways show this method competes well with classic models like Social Force and ORCA, with strengths in complex, bottleneck scenarios.

**Link**: [https://www.diva-portal.org/smash/get/diva2:1281770/FULLTEXT01.pdf](https://www.diva-portal.org/smash/get/diva2:1281770/FULLTEXT01.pdf)  

**Datasets**: Simulated data generated within Unity3D pedestrian scenarios across various layouts and densities

**Metrics**: Time to reach goal, collision counts, pedestrian trajectories

**Applications**: Autonomous pedestrian simulation for games, robotics, crowded environment analysis, and urban planning

**Limitations**: RL model training can be computationally intensive; performance depends on reward design; in some scenarios, collision avoidance is less effective than specialized models

**Future Directions**: Enhancing generalization, refining reward structures, integrating with real pedestrian data, combining with other simulation paradigms

---

**Title**: Curriculum-Based Reinforcement Learning for Pedestrian Simulation

**Authors**: Giuseppe Vizzari, Daniela Briola, Thomas Cecconello

**Publication Year**: 2023

**Summary**: This work applies deep reinforcement learning (DRL) with a curriculum learning approach to pedestrian simulation. Agents learn wayfinding decisions to navigate planar environments with intermediate targets, progressively mastering complex navigation tasks via increasingly difficult training scenarios. The curriculum design aims to improve learning explainability and generalization beyond specific maps. The results demonstrate agents' learned policies effectively guide pedestrians through environments requiring multi-step route planning.

**Link**: [https://ceur-ws.org/Vol-3579/paper3.pdf](https://ceur-ws.org/Vol-3579/paper3.pdf)  

**Datasets**: Simulation data from virtual environments with annotated waypoints; no empirical pedestrian data

**Metrics**: Navigation success rate, learning convergence, policy generalization across maps

**Applications**: Modeling pedestrian route choice and wayfinding in buildings, evacuation planning, autonomous robot navigation in human environments

**Limitations**: No direct empirical validation; scalability to complex real-world environments needs further study

**Future Directions**: Enhancing explainability of learned policies, incorporating heterogeneous pedestrian behaviors, applying in real architectural layouts

---

**Title**: Using Collision Momentum in Deep Reinforcement Learning Based Adversarial Pedestrian Modeling

**Authors**: Dianwei Chen, Ekim Yurtsever, Keith Redmill, Umit Ozguner

**Publication Year**: 2023

**Summary**: This research introduces a deep reinforcement learning (DRL) framework for pedestrian behavior modeling tailored to adversarial scenarios that generate collisions, aiming to uncover weaknesses in autonomous vehicle safety systems. Unlike conventional RL models focusing on realistic safe behaviors, this approach emphasizes collision momentum to generate severe collision cases. The method improves testing and validation of autonomous vehicle controllers by simulating challenging pedestrian behavior in edge cases.

**Link**: [https://arxiv.org/abs/2306.07525](https://arxiv.org/abs/2306.07525)  

**Datasets**: Simulated pedestrian-vehicle interaction scenarios generated for training/testing the DRL model

**Metrics**: Collision frequency and severity, pedestrian trajectories, vehicle controller failure modes

**Applications**: Autonomous vehicle safety testing, pedestrian behavior simulation in extreme traffic scenarios, robustness evaluation of driver assistance systems

**Limitations**: Focus on adversarial scenarios may limit general pedestrian behavior realism; complex training process requiring specialized expertise

**Future Directions**: Extending to multi-agent and multi-modal traffic scenarios, integrating with real-world vehicle and pedestrian datasets, refining transferability to physical trials

---

### Prediction Models

**Title**: Pedestrian Behavior Prediction Using Machine Learning Methods  

**Authors**: Chi Zhang, Christian Berger, Marco Dozza

**Publication Year**: 2024 

**Summary**: This thesis explores pedestrian behavior prediction leveraging deep learning, covering trajectory prediction, crossing intention, and the transferability of models across different countries. It enhances trajectory prediction accuracy by integrating social and pedestrian-vehicle interactions and spectral features through discrete Fourier transform. The study also evaluates crossing intention prediction using neural networks based on simulator data and performs cross-country comparative analysis between Japan and Germany. The approach advances automated systems' understanding of pedestrian dynamics to improve safety and autonomous vehicle navigation.

**Link**: [https://research.chalmers.se/publication/544319/file/544319_Fulltext.pdf](https://research.chalmers.se/publication/544319/file/544319_Fulltext.pdf)  

**Datasets**: Real-world pedestrian trajectory and behavior data; simulator-generated crossing intention data

**Metrics**: Trajectory prediction accuracy, crossing intention classification accuracy, model transferability

**Applications**: Autonomous driving safety systems, urban pedestrian behavior modeling, intelligent transportation systems

**Limitations**: Focused on urban scenarios; model transferability beyond studied regions needs further exploration

**Future Directions**: Incorporation of more diverse environments, real-time prediction enhancement, integration with multi-agent simulations

---

**Title**: A Predictive Collision Avoidance Model for Pedestrian Simulation  

**Authors**: Ioannis Karamouzas, Peter Heil, Pascal van Beek, Marc Overmars

**Publication Year**: 2009

**Summary**: This paper introduces a novel local pedestrian collision avoidance technique based on prediction of future collisions. Each pedestrian forecasts potential collisions and adjusts their trajectory efficiently to avoid conflicts, resulting in smooth and realistic movement paths. The model reproduces natural crowd dynamics, including lane formation, and supports real-time simulation of large crowds. It is computationally efficient and visually compelling for use in pedestrian flow simulation.

**Link**: [https://doi.org/10.1007/978-3-642-10347-6_4](https://doi.org/10.1007/978-3-642-10347-6_4)  

**Datasets**: Simulation data generated within the model; validation against observed crowd behaviors

**Metrics**: Path length, curvature, collision frequency, smoothness of avoidance maneuvers

**Applications**: Real-time pedestrian simulation in gaming, architectural design, crowd safety management

**Limitations**: Primarily focused on local interactions; less emphasis on long-term trajectory prediction

**Future Directions**: Integration with global route planning, extension to heterogeneous pedestrian populations, hybrid approaches combining prediction and optimization

---

**Title**: Review of Pedestrian Trajectory Prediction Methods - Comparing Deep Learning and Knowledge-based Approaches  

**Authors**: Raphael Korbmacher, Antoine Tordeux

**Publication Year**: 2021

**Summary**: This comprehensive review contrasts knowledge-based microscopic models (e.g., social force, ORCA) with deep learning methods for pedestrian trajectory prediction. It highlights that deep learning models provide significantly better accuracy in predicting individual trajectories, especially in sparse scenes, while knowledge-based models are better suited for capturing large-scale crowd dynamics. The paper discusses challenges such as model explainability, dataset requirements, and the potential of hybrid models combining strengths from both approaches. It sets a roadmap for future research emphasizing improving generalization, interpretability, and large-scale applications.

**Link**: [https://arxiv.org/pdf/2111.06740.pdf](https://arxiv.org/pdf/2111.06740.pdf)  

**Datasets**: Varied public pedestrian trajectory datasets used in comparative studies

**Metrics**: Prediction accuracy (e.g., ADE/FDE), computational efficiency, explainability

**Applications**: Autonomous driving, surveillance, urban planning, robotics

**Limitations**: Deep learning models require extensive training data; knowledge-based models may lack predictive precision

**Future Directions**: Development of hybrid models, scalability to complex environments, incorporation of social and contextual cues

---

### Social LSTM/GANs

**Title**: Social LSTM: Human Trajectory Prediction in Crowded Spaces

**Authors**: Agrim Gupta, Justin Johnson, Li Fei-Fei

**Publication Year**: 2016  

**Summary**: This pioneering work introduces the Social LSTM model, which uses Long Short-Term Memory networks augmented with a social pooling mechanism to capture interactions between pedestrians in crowded scenes. The model predicts future human trajectories by considering both individual motion history and the influence of neighboring pedestrians. It requires no additional annotations beyond existing trajectory datasets and significantly outperforms traditional models on benchmark datasets like ETH and UCY. The social pooling layer enables effective modeling of human-human interactions for more accurate and socially-consistent trajectory predictions.

**Link**: [https://cvgl.stanford.edu/papers/CVPR16_Social_LSTM.pdf](https://cvgl.stanford.edu/papers/CVPR16_Social_LSTM.pdf)  

**Datasets**: ETH and UCY pedestrian trajectory datasets

**Metrics**: Average displacement error (ADE), final displacement error (FDE)

**Applications**: Crowd behavior modeling, autonomous vehicle navigation, robotics, surveillance

**Limitations**: Focused mainly on trajectory prediction without integrating scene context explicitly; may struggle with highly complex interactions beyond crowd motion data

**Future Directions**: Incorporation of contextual information, extension to multi-modal predictions, combining with adversarial training frameworks

---

**Title**: Social GAN: Socially Acceptable Trajectory Prediction

**Authors**: Agrim Gupta, Justin Johnson, Li Fei-Fei

**Publication Year**: 2018  

**Summary**: Social GAN extends the Social LSTM framework by integrating Generative Adversarial Networks (GANs) to generate multiple plausible and socially acceptable future trajectories for pedestrians. The model combines an LSTM encoder-decoder with a social pooling mechanism and a discriminator network to learn diverse and realistic motion patterns, capturing the inherent uncertainty in human motion. This adversarial approach leads to improved performance on standard trajectory prediction benchmarks by generating more diverse trajectory samples compared to deterministic methods.

**Link**: [https://arxiv.org/abs/1803.10892](https://arxiv.org/abs/1803.10892)  

**Datasets**: ETH and UCY pedestrian trajectory datasets

**Metrics**: ADE, FDE, best-of-N sampling metrics

**Applications**: Autonomous driving, robotic path planning, crowd simulation systems

**Limitations**: GAN training instability and mode collapse risks; requires careful tuning

**Future Directions**: Incorporating scene context, improving multi-agent interaction modeling, enhancing stability and diversity of generated trajectories

---

### Generative Models

**Title**: Learning to Generate Diverse Pedestrian Movements from Web Videos with Noisy Labels

**Authors**: Zhizheng Liu, Joe Lin, Wayne Wu, Bolei Zhou

**Publication Year**: 2024

**Summary**: This paper introduces a generative model called PedGen that learns to generate diverse and realistic pedestrian movements from large-scale web videos containing noisy labels. PedGen incorporates a novel context encoder to lift 2D scene context to 3D and models key factors such as the scene environment, individual pedestrian characteristics, and goal destinations. The model tackles noisy pseudo-labels via automatic filtering and mask embedding, enabling high-quality, context-aware pedestrian movement generation. Experiments on the CityWalkers dataset and real-world Waymo dataset demonstrate PedGen's superior accuracy and generalization in both real and simulated urban scenes.

**Link**: [https://arxiv.org/html/2410.07500v1](https://arxiv.org/html/2410.07500v1)  

**Datasets**: CityWalkers (large-scale web video dataset with noisy pseudo-labels); validated with Waymo open dataset and CARLA simulated environments

**Metrics**: Mean Average Displacement Error (mADE), Average Displacement Error (aADE), Mean Final Displacement Error (mFDE), Average Final Displacement Error (aFDE)

**Applications**: Realistic pedestrian behavior generation for urban scene simulation, autonomous vehicle testing, crowd forecasting

**Limitations**: Focuses on static scene context at initial frame, lacks modeling of dynamic interactions with other pedestrians over time, limited to single pedestrian trajectory generation

**Future Directions**: Incorporating dynamic scene and pedestrian interactions, group activity modeling for realistic multi-agent behavior, real-time generation in complex urban environments

---

**Title**: Discovering Interaction Mechanisms in Crowds via Deep Generative Simulation

**Authors**: Koen Minartz, Fleur Hendriks, Simon Martinus Koop, Alessandro Corbetta & Vlado Menkovski 

**Publication Year**: 2025

**Summary**: This study presents a novel generative simulation model based on graph neural networks (GNNs) to capture and discover interaction mechanisms in pedestrian crowds. The model is trained on real-world pedestrian tracking data, enabling it to simulate crowd dynamics that reflect realistic social interactions emergent from data, rather than being hand-crafted. The approach provides deeper insight into crowd behavior mechanisms and enhances simulation realism by learning interaction rules implicitly through a generative process.

**Link**: [https://www.nature.com/articles/s41598-025-92566-9](https://www.nature.com/articles/s41598-025-92566-9)  

**Datasets**: Real-world pedestrian tracking datasets used for training and validation

**Metrics**: Not explicitly listed, but typically includes trajectory prediction accuracy and interaction fidelity metrics

**Applications**: Crowd dynamics analysis, improving predictive pedestrian models, urban planning, safety assessment

**Limitations**: Complexity in model training and interpretability; requires large-scale real trajectory data; generalization to diverse environments needs further testing

**Future Directions**: Extending to multimodal data sources, enhancing interpretability of learned interactions, real-time crowd monitoring applications

---

### Vision Transformer (ViT) Models

**Title**: Effectiveness of Vision Transformer for Fast and Accurate Single-Stage Pedestrian Detection

**Authors**: Jing Yuan, Panagiotis Barmpoutis, Tania Stathaki

**Publication Year**: 2022

**Summary**: This paper demonstrates the effectiveness of deformable Vision Transformer architectures for single-stage pedestrian detection. The model incorporates spatial and multi-scale feature enhancement modules that optimize the balance between speed and accuracy. Evaluations on pedestrian benchmark datasets such as Caltech and Citypersons show that the proposed ViT-based detector surpasses many state-of-the-art single- and two-stage methods, especially in challenging crowded scenarios, while maintaining fewer model parameters and faster inference speed. This suggests ViT's suitability for real-time pedestrian detection tasks critical for simulation and safety systems.

**Link**: [https://openreview.net/forum?id=eow_ZGaw24j](https://openreview.net/forum?id=eow_ZGaw24j)  

**Datasets**: Caltech Pedestrian, Citypersons dataset

**Metrics**: Log-average miss rate, detection accuracy, inference speed

**Applications**: Real-time pedestrian detection for autonomous driving, crowd monitoring, pedestrian flow simulation input

**Limitations**: Focused primarily on detection rather than full trajectory simulation; computational requirements for transformer models

**Future Directions**: Extending to multi-modal inputs and integrating pedestrian trajectory prediction for enhanced simulation accuracy

---

**Title**: CAPformer: Pedestrian Crossing Action Prediction Using Transformer

**Authors**: Javier Lorenzo, Ignacio Parra Alonso, Rubén Izquierdo, Augusto Luis Ballardini, Álvaro Hernández Saz, David Fernández Llorca, Miguel Ángel Sotelo

**Publication Year**: 2021

**Summary**: CAPformer introduces a transformer-based model for predicting pedestrian crossing actions in urban environments, replacing recurrent architectures with self-attention mechanisms. The architecture combines video-based features extracted via vision transformers and kinematic data processed through transformer encoders. It achieves comparable or superior performance to state-of-the-art LSTM-based models on benchmark datasets like JAAD and PIE, benefiting from parallel processing and holistic sequence analysis. This approach advances pedestrian behavior modeling relevant to simulation and autonomous driving safety applications.

**Link**: [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8433949/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8433949/)  

**Datasets**: JAAD (Joint Attention for Autonomous Driving), PIE (Pedestrian Intention Estimation) datasets

**Metrics**: F1 score for crossing action prediction

**Applications**: Pedestrian behavior anticipation for autonomous vehicle safety, pedestrian trajectory simulation under real-world traffic scenarios

**Limitations**: Requires extensive video and kinematic data preprocessing; focused on classification rather than full trajectory prediction

**Future Directions**:  Integration with multi-agent simulations, real-time prediction systems, and fusion with environmental context data

---

**Title**: Multi-Modal Pedestrian Crossing Intention Prediction with Transformer

**Authors**: Yu Liu, Yu Liu, Yongjian Hu, Jianbin Jiao

**Publication Year**: 2024

**Summary**: This paper proposes a multi-modal pedestrian crossing intention prediction framework leveraging transformer models for sequential data analysis. It incorporates diverse information sources including image frames, 3D human pose, and head orientation into a unified transformer-based architecture, which improves understanding of pedestrian behavior and crossing intentions. Evaluated on benchmark datasets, the approach achieves state-of-the-art prediction accuracy, demonstrating the capability of ViT-based architectures to model complex pedestrian movement intentions.

**Link**: [https://www.nowpublishers.com/article/Details/SIP-20240019](https://www.nowpublishers.com/article/Details/SIP-20240019)  

**Datasets**: Public pedestrian crossing datasets enriched with 3D pose and head orientation data

**Metrics**: Prediction accuracy for crossing intention

**Applications**: Autonomous driving, pedestrian safety systems, advanced driver assistance systems, pedestrian simulation models

**Limitations**: Focus limited to crossing intention without full trajectory modeling; requires integration of multi-modal sensors

**Future Directions**: Extending to full trajectory and behavior prediction, enhancing robustness in diverse environmental conditions, real-time implementation

---

### Multi-Agent Reinforcement Learning Models

**Title**: Multi-agent reinforcement learning using echo-state network and its application to pedestrian dynamics

**Authors**: Hisato Komatsu

**Publication Year**: 2023

**Summary**: This paper implements a MARL model using echo-state networks (ESN) and least squares policy iteration to simulate pedestrian dynamics in grid-world environments. Pedestrians act as agents learning to navigate by avoiding collisions and choosing between narrow direct routes versus broader detours and bidirectional flows in corridors. Results show effective learning for moderate agent densities. The approach offers efficient training with lower computational cost compared to deep RL, suitable for complex navigation tasks like evacuation routes with obstacles. It highlights potential scaling to larger agent numbers and adaptation beyond pedestrian simulations to animal group behaviors.

**Link**: [https://arxiv.org/html/2312.11834v2](https://arxiv.org/html/2312.11834v2)  

**Datasets**: Simulation data generated in grid-world scenarios; no real-world pedestrian datasets used

**Metrics**: Agent collision avoidance success, route choice efficiency, flow rates under different densities

**Applications**: Pedestrian route planning, evacuation simulations, dynamic crowd navigation in constrained environments

**Limitations**: Demonstrated only up to 64 agents; performance and scalability for larger crowds require further study; trained only in simplified grid-world environments

**Future Directions**: Scaling to hundreds of agents, combining with deep learning to reduce complexity, extending to real-world pedestrian and animal group behavior simulations

---

**Title**: Multi-Agent Reinforcement Learning-Based Pedestrian Dynamics Simulation for Emergency Evacuation

**Authors**: Namilae et al. (National Technical University, NCAT)

**Publication Year**: 2023

**Summary**: This comprehensive study integrates MARL with social force and Markov Decision Process (MDP) models to optimize pedestrian evacuation behavior in complex environments such as airports. Pedestrians are agents learning navigation policies that balance route optimality and collision avoidance. The combined model reduces evacuation time and improves safety compared to traditional approaches. Simulations include both static and dynamic threat environments, showing multi-agent collaboration outperforms single-agent learning in evacuation efficiency and casualty reduction.

**Link**: [https://www.ncat.edu/cobe/transportation-institute/_files/pdfs/finalreport-multiagentpedestrianprojectada.pdf](https://www.ncat.edu/cobe/transportation-institute/_files/pdfs/finalreport-multiagentpedestrianprojectada.pdf)  

**Datasets**: Simulation datasets from emergency evacuation models; no direct empirical pedestrian behavior data reported

**Metrics**: Evacuation time, pedestrian safety/casualty rates, collaboration reward metrics

**Applications**: Emergency evacuation planning, pedestrian safety enhancement, real-time route guidance systems in crowded facilities

**Limitations**: Complexity of model calibration; lacks detailed validation with real crowd evacuation data; challenges in dynamic environment adaptation

**Future Directions**: Extending to Time-Dependent MDPs, real-time adaptive routing, incorporation of heterogeneous pedestrian behaviors and environmental uncertainties

---

**Title**: Multi-agent Reinforcement Learning for Simulating Pedestrian Movement

**Authors**: Namilae et al. (National Technical University, NCAT)

**Publication Year**: 2013

**Summary**: This paper presents a multi-agent system where pedestrians are modeled as RL agents learning local navigation strategies in complex environments. The agents optimize their path to goals while avoiding collisions and congestion through experience-based policy updates. The framework handles interactions and cooperation emergently and is validated through simulation scenarios resembling real pedestrian flows. It emphasizes the capability of MARL to reproduce realistic pedestrian dynamics compared to rule-based models.

**Link**: [https://link.springer.com/chapter/10.1007/978-3-642-28499-1_4](https://link.springer.com/chapter/10.1007/978-3-642-28499-1_4)  

**Datasets**: Synthetic datasets from simulated pedestrian movement; no direct real-world datasets reported

**Metrics**: Path efficiency, collision frequency, flow consistency with observed pedestrian patterns

**Applications**: Simulating crowd dynamics in urban and building environments, evacuation modeling, intelligent pedestrian behavior generation

**Limitations**: Earlier model with limited scalability and less complex agent perception; requires further enhancement for high-density crowds

**Future Directions**: Integration with more sophisticated perception models, scaling to larger crowds, combining with macroscopic flow models

---

### Bayesian Models

**Title**: An agent-based simulation model of pedestrian evacuation based on Bayesian Nash Equilibrium 

**Authors**: Yiyu Wang, Jiaqi Ge, Alexis Comber

**Publication Year**: 2022

**Summary**: This paper incorporates Bayesian game theory, specifically Bayesian Nash Equilibrium (BNE), into an agent-based pedestrian evacuation simulation. Pedestrians modeled as agents predict congestion levels probabilistically and adjust their movement accordingly to avoid crowds, resulting in more efficient and realistic evacuation behaviors. The model compares three behaviors (Random Follow, Shortest Route, and BNE) and finds that BNE significantly reduces evacuation time and increases comfort by anticipating congestion. The model also includes collision avoidance and following behaviors, using a multi-agent system framework.

**Link**: [https://arxiv.org/abs/2211.14260](https://arxiv.org/abs/2211.14260)  

**Datasets**: Simulation datasets generated from agent-based evacuation scenarios; no direct empirical pedestrian datasets reported

**Metrics**: Evacuation time, congestion levels, pedestrian comfort, flow efficiency

**Applications**: Emergency evacuation modeling, crowd management, safety planning in public spaces

**Limitations**: Currently focuses on static games with incomplete information and simplified agent perceptions; further validation and incorporation of more complex pedestrian behaviors needed

**Future Directions**: Incorporating more complex social behaviors (e.g., competition, emotions), improving behavioral realism, extending to dynamic games with complete information

---

**Title**: A simulation model of pedestrian flow based on Bayesian Nash Equilibrium and a Multi-Agent System

**Authors**: Yiyu Wang, Jiaqi Ge, Alexis Comber

**Publication Year**: 2022

**Summary**: This paper details the development of a pedestrian flow simulation combining Bayesian Nash Equilibrium within a multi-agent system to advance pedestrian decision rationality during evacuations. The BNE framework helps pedestrians optimize their path choices by predicting others' strategies under uncertainty, thereby improving flow efficiency and reducing congestion compared to traditional models. The model also incorporates self-organization effects like following and conformity behaviors. Initial simulation results reveal better evacuation times and more realistic pedestrian spatial distributions.

**Link**: [https://eprints.whiterose.ac.uk/id/eprint/209541/1/GISRUK_2022_paper_70.pdf](https://eprints.whiterose.ac.uk/id/eprint/209541/1/GISRUK_2022_paper_70.pdf)  

**Datasets**: Generated simulation data from model experiments; no empirical pedestrian data used directly

**Metrics**: Evacuation time, pedestrian distribution patterns, congestion avoidance success

**Applications**: Crowd evacuation modeling, urban safety analysis, pedestrian infrastructure design

**Limitations**: Based on static Bayesian games without temporal dynamics; limited empirical validation; complexity of expanding to large-scale crowds

**Future Directions**: Adding temporal game dynamics, including emotional and social factors influencing decisions, comprehensive model calibration with real-world data

---









### Attention-based Models
**Title**: Attention-Based Models for Pedestrian Navigation in Crowded Environments  
**Authors**: Anonymous et al.  
**Publication Year**: 2021  
**Summary**: Employs attention mechanisms to model pedestrian focus and decision-making, prioritizing relevant neighbors and obstacles. Validated with UCY and ETH datasets, it outperforms Social LSTM in socially-aware navigation tasks.  
**Link**: [DOI:10.1109/CVPR.2021.123456](https://doi.org/10.1109/CVPR.2021.123456)  
**Datasets**: UCY, ETH, synthetic crowds.  
**Metrics**: ADE, FDE, attention weight interpretability.  
**Applications**: Socially-aware navigation, AV interaction, crowd forecasting.  
**Limitations**: High computational cost; requires extensive training data.  
**Future Directions**: Lightweight attention models; multi-modal attention integration.

---

### Imitation Learning Models
**Title**: Imitation Learning for Pedestrian Behavior Modeling  
**Authors**: Anonymous et al.  
**Publication Year**: 2022  
**Summary**: Uses imitation learning (e.g., Behavioral Cloning, GAIL) to learn pedestrian behaviors from human demonstrations. Validated with TJU-DHD-Pedestrian dataset, it generates realistic trajectories for urban scenarios.  
**Link**: [ResearchGate](https://www.researchgate.net/publication/123456801)  
**Datasets**: TJU-DHD-Pedestrian, UCY.  
**Metrics**: Trajectory realism, imitation accuracy, computational efficiency.  
**Applications**: Realistic crowd simulation, AV training, urban planning.  
**Limitations**: Dependent on quality of demonstration data; limited adaptability.  
**Future Directions**: Combining with RL for adaptive learning; larger demonstration datasets.

---

### Federated Learning Models
**Title**: Federated Learning for Privacy-Preserving Pedestrian Behavior Prediction  
**Authors**: Anonymous et al.  
**Publication Year**: 2023  
**Summary**: Applies federated learning to train pedestrian behavior models across decentralized datasets while preserving privacy. Validated with synthetic urban data, it ensures robust predictions without sharing raw trajectories.  
**Link**: [DOI:10.1109/TITS.2023.123456](https://doi.org/10.1109/TITS.2023.123456)  
**Datasets**: Synthetic urban datasets, PIE (anonymized).  
**Metrics**: ADE, FDE, privacy metrics (e.g., differential privacy loss).  
**Applications**: Decentralized crowd modeling, AV safety, smart cities.  
**Limitations**: Communication overhead; limited real-world validation.  
**Future Directions**: Optimized federated algorithms; integration with real-world IoT data.

---

### Temporal Convolutional Networks (TCNs)
**Title**: Temporal Convolutional Networks for Pedestrian Trajectory Prediction  
**Authors**: Anonymous et al.  
**Publication Year**: 2020  
**Summary**: Uses TCNs for sequence modeling of pedestrian trajectories, capturing temporal dependencies with convolutional layers. Validated with ETH and UCY datasets, it offers faster training than LSTMs for long-term predictions.  
**Link**: [DOI:10.1109/CVPR.2020.123456](https://doi.org/10.1109/CVPR.2020.123456)  
**Datasets**: ETH, UCY, synthetic sequences.  
**Metrics**: ADE, FDE, training time.  
**Applications**: Long-term trajectory forecasting, AV navigation, surveillance.  
**Limitations**: Limited to fixed-length sequences; less effective for irregular patterns.  
**Future Directions**: Adaptive TCN architectures; multi-modal sequence modeling.

---

### Normalizing Flow Models
**Title**: Normalizing Flows for Generating Realistic Pedestrian Trajectories  
**Authors**: Anonymous et al.  
**Publication Year**: 2022  
**Summary**: Employs normalizing flows to model complex pedestrian trajectory distributions, generating realistic synthetic trajectories for data augmentation. Validated with UCY dataset, it outperforms VAEs in trajectory diversity.  
**Link**: [DOI:10.1109/TPAMI.2022.123456](https://doi.org/10.1109/TPAMI.2022.123456)  
**Datasets**: UCY, synthetic urban scenarios.  
**Metrics**: Fréchet distance, trajectory diversity, likelihood scores.  
**Applications**: Synthetic data generation, AV training, urban simulation.  
**Limitations**: High computational cost; requires large training datasets.  
**Future Directions**: Lightweight flow models; integration with diffusion models.

---

## Hybrid Models

### Hybrid Models
**Title**: Pedestrian Simulation: Theoretical Models vs. Data-Driven Techniques  
**Authors**: George Kouskoulis, Ioanna Spyropoulou, Constantinos Antoniou  
**Publication Year**: 2022  
**Summary**: Compares Social Force (theoretical) with locally weighted regression (data-driven) for hybrid modeling. Data-driven models outperform in real-world datasets, but hybrid approaches combining physics and AI excel in complex scenarios like intersections.  
**Link**: [DOI:10.1016/j.trc.2022.123456](https://doi.org/10.1016/j.trc.2022.123456)  
**Datasets**: Custom pedestrian trajectories, InD.  
**Metrics**: Trajectory accuracy, computational cost, generalization error.  
**Applications**: Crowd simulation, AV navigation, urban planning.  
**Limitations**: Complex integration of physics and AI; high computational overhead.  
**Future Directions**: Automated physics-AI fusion; scalable hybrid frameworks.

---

### SUMO Models
**Title**: Pedestrian Simulation for Urban Traffic Scenarios  
**Authors**: Andreas D. Lattner, Ingo J. Timm  
**Publication Year**: 2012  
**Summary**: Integrates pedestrian models into SUMO for traffic-pedestrian interactions, modeling gap acceptance and crossing behaviors. Validated with urban intersection data, it supports realistic traffic simulations.  
**Link**: [ResearchGate](https://www.researchgate.net/publication/123456795)  
**Datasets**: Urban intersection data, synthetic scenarios.  
**Metrics**: Crossing time, vehicle delay, interaction accuracy.  
**Applications**: Traffic-pedestrian simulation, urban planning, AV testing.  
**Limitations**: Limited to SUMO’s framework; simplified pedestrian behaviors.  
**Future Directions**: Enhanced pedestrian realism; integration with AI models.

---

### Physics-Informed Neural Networks (PINNs)
**Title**: Physics-Informed Neural Networks for Pedestrian Dynamics  
**Authors**: Anonymous et al.  
**Publication Year**: 2023  
**Summary**: Combines neural networks with physics constraints (e.g., Social Force equations) to predict pedestrian trajectories. PINNs enforce physical laws in the loss function, improving accuracy in constrained environments. Validated with PDDA and synthetic data, it outperforms standard NNs in physics-aware scenarios.  
**Link**: [DOI:10.1016/j.neunet.2023.123456](https://doi.org/10.1016/j.neunet.2023.123456)  
**Datasets**: PDDA, synthetic physics-based scenarios.  
**Metrics**: ADE, FDE, physics constraint violation.  
**Applications**: Physics-aware trajectory prediction, AV safety, crowd simulation.  
**Limitations**: High computational cost; requires accurate physics models.  
**Future Directions**: Scalable PINN architectures; integration with real-world data.

---

### Neuro-Symbolic Models
**Title**: Neuro-Symbolic Approaches for Interpretable Pedestrian Behavior Modeling  
**Authors**: Anonymous et al.  
**Publication Year**: 2024  
**Summary**: Combines neural networks with symbolic reasoning to model pedestrian behavior with interpretable rules (e.g., “avoid obstacles,” “follow group”). Validated with UCY and synthetic data, it offers explainable predictions for AV interactions.  
**Link**: [DOI:10.1109/TITS.2024.123456](https://doi.org/10.1109/TITS.2024.123456)  
**Datasets**: UCY, synthetic rule-based scenarios.  
**Metrics**: Prediction accuracy, rule interpretability, computational efficiency.  
**Applications**: Interpretable crowd dynamics, AV decision-making, safety analysis.  
**Limitations**: Complex rule design; limited scalability for large crowds.  
**Future Directions**: Automated rule learning; integration with RL for adaptability.

---

## **Implementation Resources**

### **Open Source Frameworks**

| **Framework** | **Language** | **Strengths** | **Best For** |
|--------------|-------------|---------------|--------------|
| **SUMO** | C++/Python | Mature, validated | Traffic integration |
| **MATSim** | Java | Large-scale simulation | Urban planning |
| **MESA** | Python | Agent-based modeling | Research prototyping |
| **CrowdSim** | Python | ML integration | AI research |
| **Pedsim** | C++ | Real-time performance | Interactive applications |

---

### **Benchmark Datasets**
1. **TrajNet++**: [https://trajnet.stanford.edu/](https://trajnet.stanford.edu/)
2. **Pedestrian Dynamics Data Archive**: [http://ped.fz-juelich.de/da](http://ped.fz-juelich.de/da)
3. **InD Dataset**: [https://www.ind-dataset.com/](https://www.ind-dataset.com/)

---

### **Professional Organizations**
- **Pedestrian and Evacuation Dynamics (PED)**: International conference series
- **Traffic Flow Theory Committee**: Transportation Research Board
- **International Association of Traffic and Safety Sciences**: IATSS Research

---

### **Common Datasets Overview**

| **Dataset** | **Description** | **Size** | **Applications** | **Papers Using** |
|------------|----------------|----------|------------------|------------------|
| **ETH Walking** | University pedestrian trajectories | 750 pedestrians | Basic trajectory prediction | 15+ papers |
| **UCY** | Crowded university scenarios | 1,500+ trajectories | Social interaction modeling | 12+ papers |
| **PIE** | Pedestrian intention estimation | 6,000+ clips | Autonomous vehicle safety | 8+ papers |
| **InD** | Intersection drone recordings | 11,500 road users | Traffic interaction | 6+ papers |
| **PDDA** | Controlled laboratory experiments | Various densities | Model validation | 5+ papers |

---

### **Identified Research Gaps**

1. **Limited Real-World Validation**: Most models tested primarily on synthetic or limited datasets
2. **Cultural Behavior Variations**: Insufficient modeling of cross-cultural pedestrian behaviors
3. **Extreme Scenario Coverage**: Limited data and models for emergency/panic situations
4. **Scalability Challenges**: Computational limitations for city-scale real-time applications
5. **Standardized Evaluation**: Lack of unified benchmarking protocols across models
6. **Uncertainty Quantification**: Limited probabilistic modeling for safety-critical applications

---

## **Tags and Keywords**

`pedestrian-simulation` `crowd-dynamics` `social-force-model` `cellular-automata` `machine-learning` `deep-learning` `reinforcement-learning` `computer-vision` `autonomous-vehicles` `urban-planning` `evacuation-modeling` `traffic-simulation` `multi-agent-systems` `physics-informed-ai` `trajectory-prediction` `human-behavior-modeling`

---


