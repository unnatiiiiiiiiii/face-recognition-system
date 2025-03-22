import cv2
import face_recognition
import pickle
import os
import csv
from datetime import datetime

# Load encodings
with open("face_encodings.pkl", "rb") as file:
    data = pickle.load(file)

known_encodings = data["encodings"]
known_names = data["names"]

# Initialize webcam
video_capture = cv2.VideoCapture(0)

# Check if attendance file exists, if not create it
ATTENDANCE_FILE = "attendance.csv"
if not os.path.exists(ATTENDANCE_FILE):
    with open(ATTENDANCE_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Time", "Date"])  # Header

# Function to mark attendance
def mark_attendance(name):
    with open(ATTENDANCE_FILE, "r") as file:
        reader = csv.reader(file)
        recorded_names = [row[0] for row in reader]  # Get all recorded names

    # Only mark attendance if person is NOT already recorded today
    if name not in recorded_names:
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        with open(ATTENDANCE_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, now.strftime("%H:%M:%S"), now.strftime("%Y-%m-%d")])
        print(f"✅ Attendance marked for {name} at {dt_string}")

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)  # Faster processing
    rgb_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_encodings, face_encoding, tolerance=0.6)
        name = "Unknown"

        if True in matches:
            match_index = matches.index(True)
            name = known_names[match_index]

        # Draw rectangle and name
        top, right, bottom, left = face_location
        top, right, bottom, left = top*4, right*4, bottom*4, left*4  # Scale back to original size
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        # Mark attendance
        if name != "Unknown":
            mark_attendance(name)

    cv2.imshow("Face Recognition Attendance", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
