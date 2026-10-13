from ultralytics import YOLO
import cv2

model = YOLO('runs/detect/train/weights/best.pt')

cap = cv2.VideoCapture(0)
print("摄像头已打开，按 'q' 键退出...")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    results = model(frame, device='cpu')
    annotated_frame = results[0].plot()
    
    cv2.imshow('YOLO Real-Time Inference', annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()