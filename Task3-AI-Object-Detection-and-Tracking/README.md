# AI Object Detection and Tracking

An AI-powered computer vision project for detecting and tracking objects in video using YOLO and OpenCV.

## Project Overview

This project uses the YOLO11 object detection model to detect objects in video frames and track them across consecutive frames.

The system assigns a unique ID to each tracked object and provides additional analytics such as object counting, line crossing, IN/OUT counting, confidence scores, center points, and FPS.

## Features

- Object Detection using YOLO11
- Real-time Object Tracking
- Unique Tracking IDs
- Bounding Boxes
- Confidence Scores
- Object Center Points
- Current Object Counting
- Unique Object Counting
- Line Crossing Detection
- IN / OUT Counting
- FPS Monitoring
- Processed Video Output

## Technologies

- Python
- YOLO11
- Ultralytics
- OpenCV
- Computer Vision

## How It Works

The system processes the input video frame by frame.

### 1. Object Detection

YOLO detects objects in each frame and provides:

- Object class
- Confidence score
- Bounding box coordinates

### 2. Object Tracking

YOLO tracking associates detected objects between frames and assigns a unique tracking ID.

For example:

```text
Person ID: 1
Person ID: 2
Person ID: 3