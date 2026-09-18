# AI Object Detection and Tracking

An AI-powered Computer Vision project for detecting, tracking, and counting objects in video using **YOLO11** and **OpenCV**.

This project was developed as **Task 3** of the **CodeAlpha Artificial Intelligence Internship – September 2026 Batch**.

---

## 📌 Project Overview

The system processes a video frame by frame and uses **YOLO11** to detect objects and **object tracking** to maintain a unique ID for each detected object across consecutive frames.

The project also includes object counting, center-point calculation, FPS monitoring, and line-crossing detection for counting people moving **IN** and **OUT**.

---

## ✨ Features

* 🎯 Object Detection using YOLO11
* 🔄 Real-Time Object Tracking
* 🆔 Unique Tracking IDs
* 📦 Bounding Boxes
* 📊 Confidence Scores
* 📍 Object Center Points
* 👥 Current Object Counting
* 🔢 Unique Object Counting
* 📏 Horizontal Line Crossing Detection
* ⬇️ IN Counting
* ⬆️ OUT Counting
* ⚡ FPS Monitoring
* 🎥 Processed Video Output

---

## 🧠 Technologies Used

* **Python**
* **YOLO11**
* **Ultralytics**
* **OpenCV**
* **Lap** for tracking support

---

## 🔄 Project Workflow

```text
Input Video
     ↓
YOLO11 Object Detection
     ↓
Object Tracking
     ↓
Tracking IDs
     ↓
Bounding Boxes + Center Points
     ↓
Object Counting
     ↓
Line Crossing Detection
     ↓
IN / OUT Counting
     ↓
Processed Output Video
```

---

## 🔍 How It Works

### 1. Object Detection

YOLO11 analyzes each video frame and detects objects by providing:

* Object class
* Confidence score
* Bounding box coordinates

### 2. Object Tracking

The tracking system associates detected objects between consecutive frames and assigns a unique **Tracking ID**.

For example:

```text
Person ID: 1
Person ID: 2
Backpack ID: 3
```

The IDs allow the system to follow the same object while it moves through the video.

### 3. Bounding Boxes

Each detected object is surrounded by a bounding box showing its location in the frame.

The displayed information includes:

```text
Object Class
Tracking ID
Confidence Score
```

### 4. Center Points

The center point of each bounding box is calculated and displayed.

These coordinates are useful for analyzing object movement and implementing line-crossing logic.

### 5. Object Counting

The system maintains two types of counts:

**Current Objects**

The number of objects detected in the current frame.

**Unique Objects**

The number of different tracking IDs observed during the video processing.

### 6. IN / OUT Counting

A horizontal line is placed in the middle of the video frame.

For detected people:

```text
Top → Bottom = IN

Bottom → Top = OUT
```

The system stores the previous position of each tracked person and compares it with the current position to determine whether the person crossed the line.

---

## 📊 Information Displayed

The processed video displays:

```text
Current Objects: ...
Unique Objects: ...
IN: ...
OUT: ...
FPS: ...
```

Each detected object also displays:

```text
person ID:1 0.91
```

where:

* `person` = detected object class
* `ID:1` = tracking ID
* `0.91` = confidence score

---

## 📁 Project Structure

```text
Task3-AI-Object-Detection-and-Tracking/
│
├── yolo_detection.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── video.mp4              # Local input video
├── yolo11n.pt             # YOLO model
└── output_tracking.mp4    # Generated output
```

> **Note:** Large local files such as the input video, YOLO model, and generated output video are excluded from the GitHub repository using `.gitignore`.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yomnaelameer/codealpha_tasks.git
```

Navigate to the Task 3 folder:

```bash
cd codealpha_tasks/Task3-AI-Object-Detection-and-Tracking
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

Place your input video inside the project folder and name it:

```text
video.mp4
```

Then run:

```bash
python yolo_detection.py
```

The system will process the video and generate:

```text
output_tracking.mp4
```

---

## 🛠️ Requirements

The project requires:

```text
ultralytics
opencv-python
lap>=0.5.12
```

---

## 🎓 Learning Outcomes

Through this project, I gained practical experience with:

* Computer Vision
* YOLO Object Detection
* Multi-Object Tracking
* Tracking IDs
* Bounding Box Coordinates
* Object Center Points
* Object Counting
* Line-Crossing Logic
* Video Processing
* FPS Calculation
* OpenCV
* Ultralytics YOLO

The project also helped me understand the difference between **object detection** and **object tracking**, and how tracking information can be used to build higher-level computer vision applications.

---

## 🚀 Future Improvements

Possible future improvements include:

* More advanced tracking algorithms
* Improved ID consistency
* Custom-trained YOLO models
* Region-based counting
* Multiple counting lines
* Entry/exit statistics
* Object trajectory visualization
* Web-based interface using Streamlit
* Real-time camera support

---

## 💼 Internship

This project was developed as part of:

**CodeAlpha Artificial Intelligence Internship**
**September 2026 Batch**

### Task 3: AI Object Detection and Tracking

---

## 👩‍💻 Author

**Yomna Mohamed Elameer**

GitHub:
https://github.com/yomnaelameer
