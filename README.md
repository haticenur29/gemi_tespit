# YOLOv8 ile Uydu/İHA Görüntülerinde Gemi Tespiti
Bu projede YOLOv8 kullanılarak uydu ve İHA görüntüleri üzerinden gemi tespiti gerçekleştirilmiştir. <br>
Model, görüntü üzerindeki gemileri tespit ederek bounding box ile göstermektedir.

## Kullanılan Teknolojiler
- Python
- YOLOv8
- Ultralytics
- OpenCV
- PyTorch
- Roboflow Dataset

## Projenin Hedefi
Uydu ve drone görüntülerinde bulunan gemileri yapay zeka yardımıyla tespit etmek.

## Kullanılan Dataset
Projede YOLO formatında hazırlanmış Ship Detection Dataset kullanılmıştır.

## Model Eğitimi
Model şu komut ile eğitilmiştir: python train.py

## Modeli Test Etme
Test işlemi için şu komut kullanılmıştır: python test.py

## Sonuç
Model görüntü üzerinde gemiyi başarıyla tespit etmiş ve bounding box ile göstermiştir.

## Örnek Girdi 1
<img width="1920" height="1017" alt="Ekran Görüntüsü (36)" src="https://github.com/user-attachments/assets/f81b25a0-c3bb-4100-8e08-c244644e033d" />

## Örnek Çıktı 1
<img width="1920" height="1019" alt="Ekran Görüntüsü (37)" src="https://github.com/user-attachments/assets/d5d29387-efba-467f-b094-d6768ddfcdff" />

## Örnek Girdi 2
<img width="1022" height="631" alt="Ekran Görüntüsü (38)" src="https://github.com/user-attachments/assets/870c1be6-caee-466d-9139-9cbec85d6f7f" />

## Örnek Çıktı 2
<img width="1125" height="624" alt="Ekran Görüntüsü (39)" src="https://github.com/user-attachments/assets/4769c96c-f7a1-4839-a804-7642e08c5357" />

<br>
Bu proje Bursa Uludağ Üniversitesi Bilgisayar Mühendisliği bölümünün Uygulamalı Sinir Ağları dersi için Hatice Nur İbiş tarafından hazırlanmıştır.

