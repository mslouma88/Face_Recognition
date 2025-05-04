
import cv2
import face_recognition
import pickle
import datetime

ENCODINGS_FILE = "face_encodings.pkl"
ATTENDANCE_LOG = "recognition_log.csv"

with open(ENCODINGS_FILE, "rb") as f:
    known_encodings, known_names = pickle.load(f)

video_capture = cv2.VideoCapture(0)
print("🎥 Lancement de la reconnaissance faciale... Appuyez sur 'q' pour quitter.")

seen_names = set()

def log_recognition(name):
    if name not in seen_names:
        seen_names.add(name)
        with open(ATTENDANCE_LOG, "a") as log_file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(f"{timestamp},{name}\n")
        print(f"📝 {name} reconnu à {timestamp}")

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("❌ Impossible de lire la vidéo.")
        break

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_encodings, face_encoding, tolerance=0.45)
        name = "Inconnu"

        if True in matches:
            best_match_index = matches.index(True)
            name = known_names[best_match_index]

        log_recognition(name)

        top, right, bottom, left = [v * 4 for v in face_location]
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 255), 2)

    cv2.imshow("Reconnaissance Faciale", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
