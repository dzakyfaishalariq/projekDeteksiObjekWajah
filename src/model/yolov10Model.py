from ultralytics import YOLO

def modelYolo(frame):
    load_model = YOLO("./deteksiMuka/src/model/best.pt")
    prediksi = load_model.predict(frame)
    return prediksi