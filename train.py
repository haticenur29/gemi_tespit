from ultralytics import YOLO

# Hazır küçük model
model = YOLO("yolov8n.pt")

# Eğitim
model.train(
    data="dataset/data.yaml",
    epochs=10,
    imgsz=640
)