# YOLOv8l + SLAM Integration on Raspberry Pi 5

## 📌 Project Goal
Integrate YOLOv8l object detection and RTAB-Map SLAM to enable real-time scene understanding on Raspberry Pi 5 AI Kit using the Pi Camera and Hailo acceleration.

## 📂 Project Structure

- `camera/`: Camera capture using libcamera.
- `detection/`: YOLOv8l inference using Ultralytics.
- `slam/`: SLAM setup using RTAB-Map (ROS 2).
- `combined/`: YOLO + SLAM fusion logic.
- `models/`: YOLO model file.
- `output/`: Example output images.
- `requirements.txt`: Python dependencies.

## 🧪 Run the Project

```bash
git clone https://github.com/yourusername/yolo_slam_rpi_project.git
cd yolo_slam_rpi_project
python3 -m venv yolo_slam_env
source yolo_slam_env/bin/activate
pip install -r requirements.txt
python combined/yolo_slam_main.py
```

Press `q` to exit.

## ⚙️ Dependencies

- Python 3.9+
- OpenCV
- Ultralytics YOLOv8
- libcamera (for Raspberry Pi camera)
- ROS 2 + RTAB-Map (for full SLAM integration)

