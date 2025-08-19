# Pedestrian Modeling Datasets for Autonomous Vehicle Testing

> **A comprehensive, curated catalog of datasets for PedSim4AV simulation and validation**

## Overview

High-quality datasets are the foundation of robust autonomous vehicle (AV) systems. This comprehensive guide catalogs the most important datasets for pedestrian modeling in AV testing, meticulously curated for **PedSim4AV**. Each dataset includes technical specifications, integration workflows, and direct relevance to AV safety and performance.

### Why These Datasets Matter

- **Diverse Scenarios**: From crowded intersections to adverse weather conditions
- **Multi-Modal Data**: RGB, LiDAR, radar, and event-based sensors  
- **Real-World Testing**: Validate AV behavior across complex pedestrian interactions
- **Simulation Enhancement**: Power realistic pedestrian dynamics in PedSim4AV

---


## Datasets

| Dataset | Source | Modalities | Key Scenarios | AV Testing Focus | License |
|---------|--------|------------|---------------|------------------|---------|
| **Waymo Open** | [Waymo Open](https://waymo.com/open/) | LiDAR, RGB | Urban, Suburban | Multi-sensor fusion | Custom |
| **NuScenes**| [Nuscenes](https://www.nuscenes.org/) | LiDAR, RGB, Radar | Night, Rain, Urban | Low-visibility conditions | CC BY-NC-SA 4.0 |
| **TrajImpute**  | [TrajImpute](https://arxiv.org/abs/2411.00174) | RGB, Trajectories | Occlusion scenarios | Missing data handling | Open-source |
| **PSI 2.0** | [PSI 2.0](https://pedestriandataset.situated-intent.net/) | RGB, Intent labels | Social interactions | Intent prediction | Custom |
| **JAAD 2.0** | [JAAD 2.0](https://github.com/ykotseruba/JAAD) | RGB, Behavior tags | Pedestrian crossings | Action prediction | CC BY-NC-SA 4.0 |
| **MSP60K**  | [MSP60K](https://github.com/Event-AHU/OpenPAR) | RGB, Event | Urban, Large-Scale | Attribute recognition | MIT |
| **Cchead**  | [Cchead](https://arxiv.org/abs/2408.05877) | RGB, Optical Flow | Crowded scenes | Occlusion handling | Open-source |
| **NU-AIR** | [NU-Air](https://drive.google.com/drive/folders/1N_k4zf5eCa3qAXfrSYPDJhiLfiL5betf) | Event-based | Aerial urban views | Neuromorphic vision | Open-source |
| **Cognata**  | [Cognata](https://www.cognata.com/) | Synthetic data | Work zones | Safety-critical testing | Proprietary |
| **KITTI**  | [KITTI](http://www.cvlibs.net/datasets/kitti/) | Stereo RGB, LiDAR, GPS/IMU | Urban, Rural, Highway | Detection, tracking | Free (Non-commercial) |
| **BDD100K**  | [BDD100K-Berkeley DeepDrive](https://bair.berkeley.edu/blog/2018/05/30/bdd/) | RGB, Annotations | Urban, Diverse | Multi-object detection | Custom (Non-commercial) |
| **Caltech Pedestrian** | [Caltech Vision](https://data.caltech.edu/records/f6rph-90m20) | RGB Video | Urban, Rural | Baseline detection | Free (Non-commercial) |

---

## Featured Datasets

### Waymo Open Dataset
**The Gold Standard for Multi-Sensor AV Data**

- **Scale**: 200,000+ scenes across major U.S. cities
- **Hardware**: 5 LiDAR sensors (200m range) + 5 RGB cameras (1920×1080)
- **Coverage**: San Francisco, Phoenix, urban intersections, suburban roads
- **Performance**: 95% detection accuracy with PointPillars

**Integration with PedSim4AV**:
```bash
# Convert TFRecord to CSV trajectories
pip install waymo-open-dataset-tf-2-11-0
python tools/waymo_converter.py --input waymo_segment.tfrecord --output ped_trajectories.csv
python run_simulation.py --input ped_trajectories.csv --scenario urban
```

**2024 Update**: Added 50,000 adverse weather scenes for enhanced robustness testing

---

### NuScenes
**Multi-Modal Excellence in Challenging Conditions**

- **Data Volume**: 1,000 scenes, 1.4M annotated objects across 23 classes
- **Geographic Diversity**: Boston and Singapore urban environments
- **Sensor Array**: 6 RGB cameras, 1 LiDAR (32 beams), 5 radars, GPS/IMU
- **Special Focus**: Night driving, rain conditions, crowded intersections

**Integration Workflow**:
```bash
pip install nuscenes-devkit
python tools/nuscenes_converter.py --input nuscenes_scene --output ped_data.json
python run_simulation.py --input ped_data.json --scenario rainy_intersection
```

**Performance Metrics**: 85% mAP for pedestrian detection with YOLOv9

---

### TrajImpute (2024)
**Handling Missing Data in Real-World Scenarios**

- **Focus**: Missing trajectory data due to occlusion or sensor failure
- **Base Data**: Enhanced ETH and UCY datasets with synthetic gaps
- **Applications**: Robust pedestrian tracking in partially observable environments
- **Innovation**: First dataset specifically designed for trajectory imputation

**Key Use Cases**:
- Testing AV behavior when pedestrians are temporarily occluded
- Validating sensor fusion under partial data loss
- Training robust tracking algorithms

```bash
python tools/trajimpute_converter.py --input trajimpute_data --output ped_trajectories.csv
python run_simulation.py --input ped_trajectories.csv --scenario occluded
```

**Research Impact**: 0.3m MSE post-imputation with LSTM models

---

## Advanced Behavioral Datasets

### PSI 2.0 - Pedestrian Situated Intent
**Understanding the "Why" Behind Pedestrian Movement**

- **Unique Feature**: Text-based driver explanations of pedestrian intent
- **Diversity**: 24 different drivers, enhanced cultural representation
- **Scale**: 10,000+ annotated frames with intent changes
- **Applications**: Social intelligence modeling, intent-driven simulations

**Intent Categories**:
- `crossing` - Pedestrian intends to cross
- `waiting` - Pedestrian is waiting/hesitating  
- `walking` - Pedestrian continues on sidewalk
- `stopping` - Pedestrian comes to a stop

---

### JAAD 2.0 - Joint Attention Dataset
**Crossing Behavior and Demographic Analysis**

- **Content**: 346 RGB video clips (720p) of urban crossings
- **Rich Annotations**: Actions, attributes (age, gender), behavioral patterns
- **Focus**: Intersection scenarios and crossing decisions
- **Performance**: 88% F1 score for action prediction

---

## Cutting-Edge 2024-2025 Releases

### NU-AIR - Neuromorphic Urban Aerial
**Next-Generation Event-Based Vision**

- **Ultra-Low Latency**: Microsecond-level response times
- **Aerial Perspective**: Quadrotor-mounted sensors
- **Rich Annotations**: 93,204 pedestrian and vehicle labels
- **All-Condition**: Day and night urban environments

**Why Event-Based Matters for AVs**:
- Zero motion blur at high speeds
- Exceptional performance in challenging lighting
- Minimal power consumption
- Real-time processing capabilities

---

## Specialized Application Datasets

### Cognata Synthetic - Work Zone Safety
**Safety-Critical Scenario Testing**

Perfect for stress-testing AV systems in high-risk environments:

- **Construction Workers**: High-visibility clothing, unpredictable movements
- **Emergency Responders**: First responders in active scenes
- **Traffic Controllers**: Human-directed traffic flow scenarios
- **Equipment Operators**: Heavy machinery interactions

**Synthetic Advantages**:
- Unlimited scenario generation
- Perfect ground truth annotations  
- Controllable environmental conditions
- No safety risks during data collection

---

### Cchead - Crowd Navigation
**Mastering Dense Urban Environments**

- **Urban Complexity**: 10 diverse cityscapes
- **Massive Scale**: 2,366,249 head annotations across 50,528 frames
- **Occlusion Focus**: Advanced crowd occlusion scenarios
- **Performance**: 85% tracking accuracy with MIFN

---
### MSP60K - Large-Scale Attribute Recognition
**Understanding Pedestrian Characteristics**

- **Scale**: 60,000 RGB and event-based samples
- **Attributes**: Clothing, age, gender, and behavioral annotations
- **Coverage**: Urban crowds, large-scale settings
- **Innovation**: First large-scale event-based attribute recognition dataset

**Integration**:
```bash
python tools/msp60k_converter.py --input msp60k_data --output ped_attributes.json
python run_simulation.py --input ped_attributes.json --model attribute_aware
```

**Attribute Categories**:
- Demographics: adult/child, gender
- Clothing: colors, types, visibility
- Behavior: walking, standing, crossing

---

## Foundational Datasets

### KITTI Vision Benchmark
**The Classic Multi-Sensor Benchmark**

- **Scale**: 7,481 training + 7,518 testing frames
- **Hardware**: Stereo RGB cameras (1242×375), LiDAR, GPS/IMU
- **Coverage**: Karlsruhe, Germany - urban streets, rural roads, highways
- **Annotations**: 3D bounding boxes for pedestrians and vehicles

**Integration with PedSim4AV**:
```bash
python tools/kitti_converter.py --input kitti_data --output ped_trajectories.csv
python run_simulation.py --input ped_trajectories.csv
```

**2024 Update**: Enhanced tracking annotations for improved temporal consistency

---

### BDD100K - Berkeley DeepDrive
**Large-Scale Diverse Driving Dataset**

- **Scale**: 100,000 RGB videos (720p) from diverse U.S. cities
- **Annotations**: Bounding boxes for pedestrians, vehicles, traffic signs
- **Coverage**: Urban environments, diverse weather, day/night conditions
- **Focus**: Multi-object detection and tracking in dynamic environments

**Integration Workflow**:
```bash
python tools/bdd100k_converter.py --input bdd100k_videos --output ped_data.json
python run_simulation.py --input ped_data.json --scenario urban
```

---

### Caltech Pedestrian Dataset
**The Baseline Standard**

- **Scale**: 10 hours of 30fps RGB video (640×480), 2,300 pedestrians
- **Annotations**: 350,000 bounding boxes
- **Coverage**: Urban sidewalks, rural roads, day conditions
- **Applications**: Benchmarking baseline detection and tracking algorithms

**Integration**:
```bash
python tools/caltech_converter.py --input caltech_videos --output ped_trajectories.csv
python run_simulation.py --input ped_trajectories.csv
```
---

## Dataset Performance Notes

**Important**: The original document contained specific performance metrics cited from research papers. These metrics are based on the referenced studies and should be verified against the original sources:

- **Waymo**: 95% detection accuracy with PointPillars (as cited in original document)
- **NuScenes**: 85% mAP for pedestrian detection with YOLOv9 (as cited in original document)  
- **TrajImpute**: 0.3m MSE post-imputation with LSTM models (from arXiv paper)
- **PSI 2.0**: 90% F1 score for intent prediction with Mediapipe (as cited)
- **JAAD 2.0**: 88% F1 score for action prediction (as cited)
- **MMPD**: 71.1 AP on COCO-Persons, 72.6 AP on LLVIP (from arXiv paper)
- **MSP60K**: 80% mAP for attribute recognition (from arXiv paper)
- **Cchead**: 85% tracking accuracy with MIFN (from arXiv paper)

---

## Factors Already Considered in Current Datasets
- **Scene Diversity**: urban, suburban, rural, highway, intersections, construction zones  
- **Sensor Modalities**: RGB, stereo, LiDAR, radar, GPS/IMU, event-based (neuromorphic)  
- **Environmental Conditions**: day/night, rain, fog, adverse weather, low visibility  
- **Pedestrian Attributes**: demographics (age/gender), clothing, pose, activity labels  
- **Crowd Dynamics**: dense crowds, occlusion, multi-pedestrian interactions  
- **Intent & Behavior**: crossing, waiting, stopping, walking, joint attention cues  
- **Trajectory & Motion Data**: bounding boxes, tracking, trajectory interpolation/imputation  
- **Synthetic vs. Real-World**: controllable synthetic datasets (Cognata) and real-world datasets (Waymo, NuScenes, KITTI, etc.)  

---

## Factors Yet to Be Considered (But Necessary for Robust Testing) [Contribution of pedestrian archetypes]
- **Psychological & Cognitive States**  
  - Distraction (phone usage, headphones)  
  - Attention & eye contact (driver–pedestrian negotiation)  
  - Emotional states (stress, urgency, calmness)  

- **Cultural & Regional Diversity**  
  - Crossing norms vary by country/region  
  - Different walking speeds and group behavior patterns  

- **Special Populations**  
  - Children, elderly, and people with mobility aids (wheelchairs, crutches, strollers)  
  - Pedestrians with disabilities (visual/hearing impairments)  

- **Contextual Interactions**  
  - Interaction with traffic signals and signage  
  - Group dynamics (families, friends walking together)  
  - Pedestrian–vehicle negotiation (hand gestures, hesitation, yielding)  

- **Edge Cases**  
  - Sudden running into streets  
  - Cyclists/pedestrians overlap in mixed zones  
  - Pedestrians interacting with delivery robots, e-scooters, or autonomous shuttles  

- **Sensor Challenges Beyond Weather**  
  - Shadows, reflections (glass buildings, puddles)  
  - Extreme lighting transitions (tunnels, headlights, sunset glare)  
  - Partial visibility (behind parked cars, bushes)  

- **Temporal & Longitudinal Behavior**  
  - Long-term pedestrian trajectories over extended time  
  - Repeated daily behaviors (commuting patterns)  

- **Ethical & Safety-Critical Scenarios**  
  - Emergency evacuations (panic crowds)  
  - Pedestrians during natural disasters (flood, earthquake zones)  
  - First responders directing traffic in chaotic conditions  

---

## Dataset Coverage

| Dataset              | Scene Diversity | Multi-Modal Sensors | Envir. Conditions | Attributes / Demographics | Crowd Dynamics | Behavior / Intent Labels | Trajectories / Tracking | Synthetic Data | Event-based / Aerial | Notes                         |
|---------------------|-----------------|----------------------|--------------------|---------------------------|----------------|---------------------------|--------------------------|-----------------|------------------------|------------------------------|
| Waymo Open          | Urban, suburban | LiDAR, RGB, Radar    | Yes (weather, light) | Limited                   | Medium         | No                        | Yes                      | No              | No                     | Large-scale, multi-modal     |
| NuScenes            | Urban           | LiDAR, RGB, Radar    | Yes                | Limited                   | Medium         | No                        | Yes                      | No              | No                     | Comprehensive multi-modal    |
| TrajImpute (2024)   | Urban           | RGB, trajectories    | Partial (occlusion) | No                        | No             | No                        | Yes                      | No              | No                     | Focused on missing data      |
| PSI 2.0             | Urban / crossings | RGB                | Yes (daylight)     | No (behavioral)           | Low            | Yes                       | Yes                      | No              | No                     | Intent labels included       |
| JAAD 2.0            | Urban crossings | RGB                  | Yes                | Yes (demographics)        | Low            | Yes                       | Yes                      | No              | No                     | Detailed crossing behavior   |
| MSP60K              | Urban crowds    | RGB, attribute data  | Yes                | Yes                       | High           | No                        | No                       | No              | No                     | Attributes rich               |
| Cchead (2024)       | Dense crowds    | RGB, optical flow    | Partial            | No                        | Very High      | No                        | Yes (head-level)         | No              | No                     | Crowd & occlusion focus      |
| NU-AIR              | Aerial urban    | Event-camera         | Yes (lighting)     | No                        | Medium         | No                        | Yes                      | No              | Yes                    | Event-based & aerial         |
| Cognata Synthetic   | Work zones      | Synthetic sensors    | Full control       | Customizable              | Medium         | Yes (configurable)        | Yes                      | Yes             | No                     | Synthetic flexibility        |
| KITTI               | Urban, rural    | Stereo RGB, LiDAR    | Yes                | No                        | Low            | No                        | Yes                      | No              | No                     | Classic baseline dataset     |
| BDD100K             | Urban, weather  | RGB, annotations     | Yes                | No                        | Medium         | No                        | Yes                      | No              | No                     | Broad annotated video        |
| Caltech Pedestrian  | Urban, rural    | RGB video            | Yes (daylight)     | No                        | Low            | No                        | Yes                      | No              | No                     | Baseline detection dataset   |

---

## Future Directions

### Research Opportunities
- Cross-dataset generalization studies
- Multi-modal fusion architectures  
- Intent prediction in complex scenarios
- Adversarial robustness testing

---
