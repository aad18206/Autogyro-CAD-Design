import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")  

cap = cv2.VideoCapture(1)  

if not cap.isOpened():
    print("❌")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    results = model(frame, stream=True)

    for result in results:
        boxes = result.boxes
        names = result.names  
        for box in boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            label = names[cls_id]  
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            tag = f"{label} {conf:.2f}"
            cv2.putText(frame, tag, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow("YOLOv8 Detection with Tags", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
