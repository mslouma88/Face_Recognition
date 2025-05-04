
import face_recognition
import os
import pickle
import logging

KNOWN_FACES_DIR = "known_faces"
ENCODINGS_FILE = "face_encodings.pkl"
LOG_FILE = "encode_log.txt"

# Configuration du log
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(message)s")

print("🔐 Encodage des visages en cours...")

known_encodings = []
known_names = []

for filename in os.listdir(KNOWN_FACES_DIR):
    if filename.lower().endswith((".jpg", ".png", ".jpeg")):
        image_path = os.path.join(KNOWN_FACES_DIR, filename)
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)

        if encodings:
            name = os.path.splitext(filename)[0]
            if name not in known_names:
                known_encodings.append(encodings[0])
                known_names.append(name)
                logging.info(f"Encodé : {filename}")
                print(f"✅ Encodé : {filename}")
            else:
                logging.warning(f"Nom déjà existant ignoré : {filename}")
                print(f"⚠️ Ignoré (doublon) : {filename}")
        else:
            logging.warning(f"Aucun visage trouvé dans {filename}")
            print(f"❌ Aucun visage détecté dans {filename}")

with open(ENCODINGS_FILE, "wb") as f:
    pickle.dump((known_encodings, known_names), f)

print(f"✅ Encodage terminé. Données sauvegardées dans {ENCODINGS_FILE}")
print(f"📝 Journal disponible dans {LOG_FILE}")
