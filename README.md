# 🧠 YOLOv8l Object Detection on Raspberry Pi with Hailo Integration

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Raspberry Pi](https://img.shields.io/badge/Platform-Raspberry%20Pi-red)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Object%20Detection-green)
![Hailo](https://img.shields.io/badge/Hailo-AI%20Accelerator-yellow)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A real-time object detection system using **YOLOv8l** on a **Raspberry Pi 5 (64-bit)** powered by the **Raspberry Pi Camera Module** and optionally accelerated using **Hailo AI SDK**. This project captures live video, processes it through YOLOv8, and displays the detection results in real-time.

---

## 📸 Project Highlights

- 🔍 Real-time object detection using YOLOv8l.
- 📷 Raspberry Pi Camera Module V3 used for capturing input.
- 🚀 Optional integration with Hailo AI SDK for inference acceleration.
- 🐍 Python-based implementation using `ultralytics`, `opencv-python`, and `picamera2`.
- 📦 Modular and expandable codebase for robotics/IoT applications.

---

## ⚙️ Setup Instructions

### ✅ Prerequisites

- Raspberry Pi 5 (64-bit OS)
- Python 3.9+
- Raspberry Pi Camera Module V3
- Optional: Hailo-8 AI accelerator + Hailo SDK

### 🔧 Installation

```bash
# Clone this repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

# (Optional) Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install required packages
pip install -r requirements.txt


