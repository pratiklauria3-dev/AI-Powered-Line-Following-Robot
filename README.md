
# AI-Powered-Line-Following-Robot
An AI-powered line following robot is an intelligent robotic system that autonomously follows a predefined path using computer vision and machine learning techniques. 
=======
# 🤖 AI-Based Line Follower Robot (Raspberry Pi)

## 📌 Overview

This project implements an **AI-powered Line Follower Robot** using a **Raspberry Pi 4B**, **IR sensor array**, and a **Machine Learning model (Random Forest)**.
The robot detects a path (black line on white surface) and autonomously follows it using real-time sensor data and intelligent decision-making.

---

## 🚀 Features

* 🧠 Machine Learning-based path decision (Forward / Left / Right)
* 📊 Custom dataset collection and training pipeline
* ⚡ Real-time IR sensor processing
* 🔄 Stable motion with noise filtering and turn-lock logic
* 🛑 Prevents false turning on white surface
* 🔋 Battery-powered autonomous operation

---

## 🛠️ Hardware Components

* Raspberry Pi 4 Model B
* IR Sensor Array (5-channel)
* L298N Motor Driver
* DC Gear Motors (4)
* Robot Chassis with Wheels
* 11.1V Li-ion/LiPo Battery
* Buck Converter (5V for Pi)
* Jumper Wires & Breadboard

---

## 💻 Software Requirements

* Python 3
* RPi.GPIO
* pandas
* scikit-learn
* joblib

Install dependencies:

```bash
pip install pandas scikit-learn joblib
```

---

## 🔌 GPIO Pin Configuration

| Function   | GPIO (BCM)       |
| ---------- | ---------------- |
| IR Sensors | 4, 17, 27, 22, 5 |
| IN1        | 6                |
| IN2        | 13               |
| ENA (PWM)  | 18               |
| IN3        | 19               |
| IN4        | 26               |
| ENB (PWM)  | 16               |

---

## 📂 Project Structure

```
.
├── collect_data_v3.py
├── train_model_v3.py
├── ml_line_follower_v3.py
├── ir_data_v3.csv
├── line_model_v3.pkl
└── README.md
```

---

## 📊 Workflow

### 1️⃣ Data Collection

Collect IR sensor readings and label actions:

```bash
python3 collect_data_v3.py
```

---

### 2️⃣ Train Model

Train Random Forest model:

```bash
python3 train_model_v3.py
```

---

### 3️⃣ Run Robot

Execute ML-based line follower:

```bash
python3 ml_line_follower_v3.py
```

---

## 🧠 Machine Learning Approach

* Input: IR sensor values (S1–S5)
* Output: Action (Forward, Left, Right)
* Model: Random Forest Classifier
* Technique:

  * Data augmentation
  * Noise filtering (action buffering)
  * Turn-lock mechanism

---

## ⚙️ Key Algorithms Used

* Decision smoothing (majority voting)
* Turn hold (to avoid mid-turn stopping)
* Line-loss detection (prevents random turning)

---

## 🧪 Challenges Faced

* Motor humming due to low PWM
* False turns on white surface
* Sensor noise and instability
* Dataset imbalance

---

## ✅ Solutions Implemented

* PWM boost for motor startup
* Action buffering (debouncing)
* Turn-lock timing
* Dataset augmentation

---

## 🎯 Results

* Smooth and stable line following
* Accurate turning at corners
* No random turns on white surface
* Improved reliability using ML

---

## 🔮 Future Enhancements

* Add camera-based line detection
* Obstacle avoidance (Ultrasonic sensor)
* Color-based path decisions
* Web dashboard for remote monitoring

---

## 📌 Conclusion

This project demonstrates the integration of **machine learning with embedded systems**, showcasing how intelligent decision-making can improve robotic navigation compared to traditional rule-based systems.

---

## 👨‍💻 Author

**Pratik Lauria**

---

!
>>>>>>> e2c9f59 (Initial commit - AI line following robot)
