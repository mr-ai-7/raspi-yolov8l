import cv2
from camera.cam_capture import capture_image
from detection.yolo_detect import detect_objects

while True:
    print("🟢 Capturing frame...")
    frame = capture_image()
    if frame is None:
        print("❌ Failed to get image")
        continue

    print("🎯 Running detection...")
    result = detect_objects(frame)
    cv2.imshow("YOLOv8l Detection + SLAM Frame", result)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
