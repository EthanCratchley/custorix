from ultralytics import YOLO

# Load a pretrained YOLO11n model
model = YOLO("yolo11n.pt")

# Perform object detection on an image
results = model("assets/test1.jpg")  # Predict on an image
results[0].show()  # Display results

for r in results:
    for box in r.boxes:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        coords = box.xyxy[0].tolist()
        print(f"Detected {r.names[cls_id]} with {conf:.2f} confidence at {coords}")
