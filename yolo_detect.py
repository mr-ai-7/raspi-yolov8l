from ultralytics import YOLO
import cv2

model = YOLO("models/yolov8l.pt")

def detect_objects(img):
    results = model(img)
    annotated = results[0].plot()
    return annotated
