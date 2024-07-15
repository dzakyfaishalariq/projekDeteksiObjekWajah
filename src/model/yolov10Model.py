<<<<<<< HEAD
from ultralytics import YOLO

def modelYolo(frame):
    load_model = YOLO("./deteksiMuka/src/model/best.pt")
    prediksi = load_model.predict(frame)
=======
from ultralytics import YOLO

def modelYolo(frame):
    load_model = YOLO("./deteksiMuka/src/model/best.pt")
    prediksi = load_model.predict(frame)
>>>>>>> 94a3114 (deteksi objek wajah)
    return prediksi