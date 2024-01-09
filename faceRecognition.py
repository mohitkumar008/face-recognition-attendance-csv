import face_recognition
import cv2
import os
import csv
from datetime import datetime

path = "/home/mohit/Desktop/python-projects/AttandanceByFace/studentImages"
student_images_list = os.listdir(path)
known_encodings = {}
written_names = set()

# Load known face encodings
for student_image in student_images_list:
    known_image = face_recognition.load_image_file(os.path.join(path, student_image))
    known_encoding = face_recognition.face_encodings(known_image)[0]
    name, _ = os.path.splitext(os.path.basename(student_image))
    known_encodings[name] = known_encoding

# Get current date for CSV file name
current_date = datetime.now().strftime("%d-%m-%Y")
csv_file_path = f"verification_log_{current_date}.csv"

# Open or create CSV file for writing
with open(csv_file_path, mode='a', newline='') as csv_file:
    fieldnames = ['Name', 'Verification Time']
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Check if the file is empty, write header if it is
    if os.stat(csv_file_path).st_size == 0:
        csv_writer.writeheader()

    # Open a video capture object
    video_capture = cv2.VideoCapture(0)  # Use 0 for the default camera

    while True:
        # Capture each frame from the camera
        ret, frame = video_capture.read()

        # Find all face locations in the current frame
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Check if the face matches any known face
            matches = face_recognition.compare_faces(list(known_encodings.values()), face_encoding)

            if any(matches):
                # Get the name corresponding to the matching encoding
                name = list(known_encodings.keys())[matches.index(True)]
            else:
                name = "Unknown"

            # Record the verification time
            verification_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Draw a rectangle around the face and display the name
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

            # Write data to CSV file if entry does not exist for the person
            if name != "Unknown" and name not in written_names:
                csv_writer.writerow({'Name': name, 'Verification Time': verification_time})
                written_names.add(name)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close all windows
    video_capture.release()
    cv2.destroyAllWindows()
