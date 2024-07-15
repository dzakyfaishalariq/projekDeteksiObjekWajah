import cv2
from src.model.yolov10Model import modelYolo
import supervision as sv
cap = cv2.VideoCapture(0)  # '0' adalah default untuk webcam internal

# Periksa apakah kamera berhasil dibuka
if not cap.isOpened():
    print("Error: Kamera tidak dapat diakses")
    exit()

while True:
    # Membaca frame demi frame
    ret, frame = cap.read()
    
    # Jika frame dibaca dengan benar ret adalah True
    if not ret:
        print("Tidak dapat menerima frame (stream end?). Keluar ...")
        break
    
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    prediksi = modelYolo(frame_rgb)
    
    detections = sv.Detections.from_ultralytics(prediksi[0])

    bounding_box_annotator = sv.BoundingBoxAnnotator()
    label_annotator = sv.LabelAnnotator()

    annotated_image = bounding_box_annotator.annotate(
        scene=frame, detections=detections)
    annotated_image = label_annotator.annotate(
        scene=annotated_image, detections=detections)
    
    cv2.imshow('Video', annotated_image)
    
    # Tunggu untuk 'q' ditekan untuk keluar
    if cv2.waitKey(1) == ord('q'):
        break
# Melepaskan objek capture dan tutup semua jendela
cap.release()
cv2.destroyAllWindows()

    
    