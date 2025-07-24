# 🧠 YOLOv8l + RTAB-Map SLAM Integration on Raspberry Pi 5 AI Kit (64-bit)

This project demonstrates real-time object detection using the **YOLOv8l** model, integrated with **visual SLAM (RTAB-Map)** for spatial awareness on the **Raspberry Pi 5 AI Kit (64-bit OS)** using the **Raspberry Pi Camera Module**.

---

## 📁 Project Structure

```
yolo_slam_rpi_project/
│
├── camera/
│   └── cam_capture.py             # Captures frames using libcamera
│
├── detection/
│   └── yolo_detect.py            # YOLOv8l model inference
│
├── slam/
│   └── rtabmap_slam.launch.py    # Placeholder for ROS 2 launch
│
├── combined/
│   └── yolo_slam_main.py         # Integration script (YOLO + SLAM)
│
├── models/
│   └── yolov8l.pt                # YOLOv8l model (download manually)
│
├── utils/
│   └── helpers.py                # Optional utility functions
│
├── output/
│   └── sample_frame.jpg          # Example output (placeholder)
│
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

---

## 🔧 Setup Instructions

### ✅ 1. Prepare Raspberry Pi 5

- **OS**: Raspberry Pi OS 64-bit Lite (Bookworm or Bullseye)
- **Enable camera**:
  ```bash
  sudo raspi-config
  ```
  - Go to **Interface Options** > Enable **libcamera**.

---

### ✅ 2. Install Dependencies

```bash
sudo apt update && sudo apt upgrade
sudo apt install python3-pip python3-venv libopencv-dev libcamera-utils
```

---

### ✅ 3. Clone the Repository and Setup Virtual Environment

```bash
git clone https://github.com/yourusername/yolo_slam_rpi_project.git
cd yolo_slam_rpi_project
python3 -m venv yolo_slam_env
source yolo_slam_env/bin/activate
pip install -r requirements.txt
```

---

### ✅ 4. Download YOLOv8l Model

```bash
wget https://github.com/ultralytics/assets/releases/download/v8.0.0/yolov8l.pt -O models/yolov8l.pt
```

---

### ▶️ Run Object Detection + SLAM Integration

```bash
python combined/yolo_slam_main.py
```

This will:
- Capture a frame using `libcamera`
- Run YOLOv8l on the captured image
- (Optionally) Integrate it with RTAB-Map SLAM output
- Press `q` to quit the loop

---

## 🎯 What We Did

### ✅ Raspberry Pi Camera Capture
Used `libcamera-still` from shell inside Python to capture images reliably on Raspberry Pi OS.

### ✅ YOLOv8l Detection
Integrated Ultralytics YOLOv8 with OpenCV.
- Displayed real-time annotated bounding boxes.

### ✅ SLAM with RTAB-Map (Setup Placeholder)
- ROS 2 + RTAB-Map launch setup for future expansion.
- Visual SLAM module will be fully integrated using `rtabmap.launch.py` on ROS 2 Foxy/Humble.

---

## 🧠 Tech Stack

| Component         | Tool/Library               |
|------------------|----------------------------|
| Object Detection | YOLOv8l (ultralytics)      |
| SLAM             | RTAB-Map + ROS 2 (launch)  |
| Camera           | libcamera (CLI integration)|
| Hardware         | Raspberry Pi 5 AI Kit      |
| Language         | Python 3.9+                |
| Acceleration     | *(Future: Hailo-8 .hef)*   |

---

## 🔜 Future Improvements

- 🔁 Replace `.pt` model with compiled `.hef` for **Hailo acceleration**.
- 📦 Add **Docker + systemd** service to make it autostart.
- 🧭 Fuse **GPS/barometer/IMU** with SLAM map frame.
- 🧪 Add testing script with dummy image inputs.

---

## 📸 Sample Output

![Sample Output](output/sample_frame.jpg)

---

## 📬 Contributing

Feel free to fork this repo, open issues, or submit pull requests to improve the pipeline and expand features!

---

## 📄 License

MIT License
