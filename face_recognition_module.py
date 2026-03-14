# --------- BACKEND: face_recognition_module.py ---------
import face_recognition
import cv2
import os
import numpy as np
import json
from datetime import datetime
import geocoder

KNOWN_FACES_DIR = './dataset/known_faces'
ATTENDANCE_FILE = './attendance_data/attendance.json'

known_encodings = []
known_names = []

def load_known_faces():
    for name in os.listdir(KNOWN_FACES_DIR):
        person_dir = os.path.join(KNOWN_FACES_DIR, name)
        for img_name in os.listdir(person_dir):
            img_path = os.path.join(person_dir, img_name)
            image = face_recognition.load_image_file(img_path)
            encodings = face_recognition.face_encodings(image)
            if encodings:
                known_encodings.append(encodings[0])
                known_names.append(name)

load_known_faces()

def recognize_face():
    video = cv2.VideoCapture(0)
    recognized = False
    name = "Unknown"
    location = geocoder.ip('me').latlng

    while True:
        ret, frame = video.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for encoding in face_encodings:
            matches = face_recognition.compare_faces(known_encodings, encoding)
            face_distances = face_recognition.face_distance(known_encodings, encoding)
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                name = known_names[best_match_index]
                recognized = True

                # Save attendance
                with open(ATTENDANCE_FILE, 'r+') as file:
                    data = json.load(file)
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    entry = {
                        "name": name,
                        "time": timestamp,
                        "location": location
                    }
                    data.append(entry)
                    file.seek(0)
                    json.dump(data, file, indent=4)
                break

        if recognized:
            break

    video.release()
    cv2.destroyAllWindows()

    if recognized:
        return {"status": "success", "name": name, "location": location}
    else:
        return {"status": "fail"}
