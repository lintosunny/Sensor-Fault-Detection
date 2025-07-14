# Sensor Fault Detection

## Problem Statement
The Air Pressure System (APS) is a critical component of a heavy-duty vehicle that uses compressed air to force a piston to provide pressure to the brake pads, slowing the vehicle down. The benefits of using an APS instead of a hydraulic system are the easy availability and long-term sustainability of natural air.
<br>
This is a Binary Classification problem, in which the affirmative class indicates that the failure was caused by a certain component of the APS, while the negative class indicates that the failure was caused by something else.

## Solution Proposed
In this project, the system in focus is the Air Pressure system (APS) which generates pressurized air that are utilized in various functions in a truck, such as braking and gear changes. The datasets positive class corresponds to component failures for a specific component of the APS system. The negative class corresponds to trucks with failures for components not related to the APS system.
<br>
The problem is to reduce the cost due to unnecessary repairs. So it is required to minimize the false predictions.

## Tech Stack Used
1. Python
2. FastAPI
3. Machine learning algorithms
4. Docker
5. MongoDB
# 🔧 Sensor Fault Detection – Flowchart Overview

This section illustrates the major components involved in the sensor fault detection pipeline using flowcharts.

---

## 1️⃣ Sensor Data Ingestion Component

![Sensor Data Ingestion](flowcharts/1_Sensor_Data_Ingestion_Component.png)

---

## 2️⃣ Sensor Data Validation Component

![Sensor Data Validation](flowcharts/2_Sensor_Data_Validation_Component.png)

---

## 3️⃣ Sensor Data Transformation Component

![Sensor Data Transformation](flowcharts/3_Sensor_Data_Transformation_Component.png)

---

## 4️⃣ Sensor Model Trainer Component

![Sensor Model Trainer](flowcharts/4_Sensor_Model_Trainer_Component.png)

---

## 5️⃣ Sensor Model Evaluation Component

![Sensor Model Evaluation](flowcharts/5_Sensor_Model_Evaluation_Component.png)

---

## 6️⃣ Sensor Model Pusher Component

![Sensor Model Pusher](flowcharts/6_Sensor_Model_Pusher_Component.png)

---

## 7️⃣ Sensor Prediction Pipeline

![Sensor Prediction Pipeline](flowcharts/7_Sensor_Prediction_Pipeline.png)
