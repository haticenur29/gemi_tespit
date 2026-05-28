from ultralytics import YOLO

# Eğitilmiş model
model = YOLO("runs/detect/train-3/weights/best.pt")

# Test görüntüsü
results = model("test.jpg", save=True)

print("Tahmin tamamlandı.")