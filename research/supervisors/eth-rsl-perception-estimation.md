# ETH Robotic Systems Lab — perception, navigation and state estimation

**Current evidence:** [Perception & Navigation research page](https://rsl.ethz.ch/research/researchtopics/perception-navigation.html), [continuous PhD recruitment](https://rsl.ethz.ch/the-lab/open-positions.html).
**As-of:** 2026-11-11. **Class:** research lab recruitment lead, *no guaranteed funded PhD slot evidenced*.

## Technical trajectory
Official research page specifies:
1. **Multimodal SLAM / spatial mapping**: vision, IMU and LiDAR on legged robots in feature-sparse and mixed indoor/outdoor environments, observability loss mitigation, lighting changes and faulty measurements; neural radiance fields and Gaussian-splatting maps.
2. **State estimation**: continuous-time models, splines and Gaussian-process estimators for asynchronous sensors, odometry, calibration and SLAM.
3. **Dataset / sensor suite**: calibrated RGB/depth/LiDAR/IMU, strict sync/outlier modeling, lighting/fault stress tests; GrandTour and TartanGround datasets named.
4. **Navigation**: traversability, semantic scene graphs, visual-language navigation, model predictive control and RL.

The page lists **Turcan Tuna** as contact in multimodal SLAM, **William Talbot** in state-estimation research and other researchers; those labels are contact points, **not proof they can personally supervise or fund a PhD**. Actual qualified PI authority and current 2026 publications need confirmation.

## Candidate scientific match
- **Direct high overlap:** real inertial estimator generalization [*Measurement* 2023 DOI 10.1016/j.measurement.2023.113105](https://doi.org/10.1016/j.measurement.2023.113105), public [TG-DCM-PINN](https://github.com/GinkgoQ/TG-DCM-PINN) conditional IMU physics, candidate-CV ROS2/ORB-SLAM3 VIO work.
- **Gaps:** formal evidence of time-synchronized LiDAR/IMU field dataset, legged navigation performance and contribution to continuous-time splines. Do not claim familiarity from topic overlap.
- **Potential original research hypothesis:** adapt model-based estimator confidence to observability loss and asynchronous sensor reliability. Compare classical continuous-time and learned modules under feature scarcity/clock shift, using sequence/motion family uncertainty rather than only aggregate RMSE. Novelty unverified until reading current group papers.

## Recruitment path and constraints
The lab [continuously searches PhD applicants](https://rsl.ethz.ch/the-lab/open-positions.html) and requires a strong academic record, robotics experience, C++ and ROS, with CV/transcripts/motivation **through linked online form** (not email). The lab page does **not** quote a salary, specific PI hiring budget, international visa exception, deadline, final decision date or guaranteed 2026 offer. These must be verified before a **fully funded** portfolio A designation. The form is external to ETH webpages; verify official provenance and consent before submission.

## Evidence status
Research area = SUPPORTED_PRIMARY. Continuous recruitment channel = SUPPORTED_PRIMARY. Specific funded applicant position = UNVERIFIED. Candidate degree completion and methods evidence = source-confirmed article + unverified private documents. No outreach made.
