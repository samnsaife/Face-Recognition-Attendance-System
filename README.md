# Face Recognition Attendance System

## Overview
A secure and automated attendance system that uses facial recognition, video recording, and geolocation to ensure authentic attendance logging. Built using Python (Flask, OpenCV), React.js, and modern UI/UX principles.

## Features
- Real-time face detection and recognition
- Video recorded for each attendance entry
- Logs date, time, and location metadata
- Interactive and modern React dashboard

## Requirements
- Python 3.10+
- Node.js (for frontend)
- VS Code (recommended)
- Webcam access

## Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd face_attendance_system/backend
   ```
2. Create virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r ../requirements.txt
   ```
4. Run the Flask server:
   ```bash
   python app.py
   ```

## Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd face_attendance_system/frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the React app:
   ```bash
   npm start
   ```

## Folder Structure Tips
- Place known faces inside `dataset/known_faces/NAME/image.jpg`
- Videos will be saved to `attendance_data/videos/`
- Logs are saved in `attendance_data/attendance.json`

## Run Both in VS Code
- Open project folder in VS Code
- Use two terminal tabs: one for backend, one for frontend
- Allow webcam permissions when prompted

## License
MIT — For educational use by B.Tech students.
