import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # 或 yolov8s.pt, yolov5s.pt

cap = cv2.VideoCapture(1)  # OBS 虚拟摄像头，可能是 0/1/2

if not cap.isOpened():
    print("❌ 摄像头打不开")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    results = model(frame, stream=True)

    for result in results:
        boxes = result.boxes
        names = result.names  # ✅ 正确使用 result.names
        for box in boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            label = names[cls_id]  # ✅ 正确获取标签名
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # 画框 + 标签
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            tag = f"{label} {conf:.2f}"
            cv2.putText(frame, tag, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow("YOLOv8 Detection with Tags", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
