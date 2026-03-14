# Directory Structure (for your reference)
# face_attendance_system/
# ├── backend/
# │   ├── app.py
# │   ├── face_recognition_module.py
# │   ├── video_logger.py
# │   └── utils.py
# ├── frontend/
# │   ├── public/
# │   └── src/
# │       ├── App.js
# │       ├── Dashboard.js
# │       └── components/
# │           ├── Navbar.js
# │           └── AttendanceCard.js
# ├── attendance_data/
# │   ├── attendance.json
# │   └── videos/
# ├── dataset/
# │   └── known_faces/
# ├── README.md
# └── requirements.txt

# --------- BACKEND: app.py ---------
from flask import Flask, request, jsonify
from flask_cors import CORS
from face_recognition_module import recognize_face
from video_logger import record_video_with_metadata
import os

app = Flask(__name__)
CORS(app)

@app.route('/api/mark_attendance', methods=['POST'])
def mark_attendance():
    result = recognize_face()
    if result['status'] == 'success':
        record_video_with_metadata(result['name'], result['location'])
        return jsonify({"message": "Attendance marked", "name": result['name']}), 200
    return jsonify({"message": "Face not recognized"}), 404

if __name__ == '__main__':
    app.run(debug=True)
