
# 🎭 Face Recognition Attendance System  

A real-time **AI-powered attendance system** using **Face Recognition** to automatically mark attendance based on detected faces.

## 📌 Overview  
This system uses **computer vision** and **machine learning** techniques to recognize faces from a live camera feed and log attendance. It is built using **OpenCV, Dlib, and the Face Recognition library** to ensure accuracy and efficiency.

### 🚀 Features  
✅ **Real-time Face Detection & Recognition**  
✅ **Automatic Attendance Logging** (CSV format)  
✅ **Multi-person Recognition** (Detects multiple faces at once)  
✅ **Prevents Duplicate Entries** (Attendance is marked only once per session)  
✅ **Performance Optimized** (Adjustable resolution & recognition tolerance)  

---

## 🛠 Technology Stack  
- **Programming Language**: Python  
- **Libraries Used**:  
  - OpenCV (Computer Vision)  
  - Face Recognition (Dlib-based face detection)  
  - NumPy (Data Processing)  
  - Pandas (Attendance Logging)  

---

## 🚀 Installation & Setup  

### 2️ Install Dependencies  
```bash
pip install opencv-python face-recognition numpy pandas
```
🔹 Download **CMake** 
🔹 Install `dlib`:  
```bash
pip install dlib
```

###  Train the System (Encode Faces)  
Place images of individuals in the **`train_images/`** folder. Then, run:  
```bash
python train_faces.py
```
✅ This will generate a file **`face_encodings.pkl`** containing encoded facial data.

###  Run the Recognition System  
```bash
python test_recognition.py
```
✅ The system will detect faces via the webcam and log attendance in **`attendance.csv`**.

---

## 📊 Attendance Output Format (CSV)  
| Name            | Time     | Date       |
|----------------|---------|------------|
|                |          |            |


---

## 📌 Future Enhancements  
🔹 **Liveness Detection** (Prevent Spoofing with Blink Detection)  
🔹 **Cloud Integration** (Store Attendance in a Database)  
🔹 **Performance Optimization** (Reduce Processing Overhead)  
🔹 **Web Dashboard** (Monitor Attendance in Real Time)  

---

## 👨‍💻 Author  
**Unnati Bornare**  
📧 unnatibornare1@gmail.com


---

## 📜 License  
This project is licensed under the **MIT License**.  

---

### 📢 Contributions Welcome!  
If you'd like to improve this project, feel free to submit a **Pull Request** or open an **Issue**. 🚀  

