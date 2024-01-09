# Face Recognition Attendance System

## Overview

This Python project implements a face recognition attendance system. The system captures video from the camera, detects faces, matches them with known faces, and logs the attendance in a CSV file.

## Features

- **Real-time Face Recognition:** Utilizes the `face_recognition` and `OpenCV` libraries to perform real-time face recognition.
- **CSV Logging:** Records attendance information in a CSV file, including the name and verification time.
- **Easy Setup:** Straightforward setup using a `requirements.txt` file to install necessary dependencies.

## How it Works

1. **Known Faces:** Images of known faces are stored in the `studentImages` directory, and their face encodings are generated during initialization.

2. **Video Capture:** The system captures video from the default camera (you can change this by modifying `cv2.VideoCapture(0)`).

3. **Face Recognition:** For each frame, the system detects faces and compares them with known faces.

4. **CSV Logging:** Attendance information is logged in a CSV file (`verification_log_<date>.csv`).

## Setup

### Prerequisites

- Python 3.10
- Dependencies (Install using `pip install -r requirements.txt`)

### Running the Project

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mohitkumar008/face-recognition-attendance-csv.git

2. **Navigate to the project folder:**
   
   ```bash
   cd face-recognition-attendance-csv

3. **Install dependencies:**
   
   ```bash
   pip install -r requirements.txt

4. **Run the project:**
   
   ```bash
   python3 faceRecognition.py


# License

## This project is licensed under the MIT License.

You can copy and paste this Markdown content into your README.md file in your GitHub repository. Adjust the URLs, project structure, and other details as needed.


