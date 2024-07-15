import cv2
from src.model.yolov10Model import modelYolo
import supervision as sv

path_video = "./deteksiMuka/src/data/WIN_20240715_15_12_59_Pro.mp4"
cap = cv2.VideoCapture(path_video)

# mendapatkan properti dari video input
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # mengambil lebar frame
frame_heigth = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # mengambil tinggi frame
fps = int(cap.get(cv2.CAP_PROP_FPS)) # mengambil fps

fourcc = cv2.VideoWriter_fourcc(*"mp4v") # format video
out = cv2.VideoWriter("./deteksiMuka/src/data/outputHasilDeteksi.mp4", fourcc, fps, (frame_width, frame_heigth))

i = 1
while True:
    ret, frame = cap.read()
    if not ret:
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
    out.write(annotated_image)
    # cv2.imshow("Video", annotated_image)
    # buat loading video lagi di proses untuk deteksi objek nya
    print("loading video ...")
    print("*" * i)
    if cv2.waitKey(1) == ord("q"):
        break
    i += 1
# menutup kamera
cap.release()
cv2.destroyAllWindows()
