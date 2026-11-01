# AI Hand Gesture Virtual Mouse

A computer vision application built with Python that allows users to control system mouse operations (cursor movement, left click, right click, double click, and screenshots) using hand gestures detected via a webcam.

## 📁 Repository Structure
* `main.ipynb` (or `main.py`): Core application containing frame capture, hand landmarker detection, and gesture recognition logic.
* `util.py`: Helper module containing mathematical utilities for calculating joint angles and landmark distances.
* `hand_landmarker.task`: MediaPipe Tasks model file for 3D hand landmarker detection.

## 🚀 Features
* **Cursor Tracking:** Move system cursor using index finger coordinates.
* **Left Click:** Triggered via index finger flexion.
* **Right Click:** Triggered via middle finger flexion.
* **Double Click:** Simultaneous index and middle finger flexion.
* **Screenshot:** Automatic screenshot saved locally when screenshot gesture is performed.

## 🛠️ Built With
* [OpenCV](https://opencv.org/) - Real-time computer vision frame processing
* [MediaPipe Tasks API](https://developers.google.com/mediapipe) - Fast, high-accuracy hand landmark detection
* [PyAutoGUI](https://pyautogui.readthedocs.io/) & [PyNput](https://pynput.readthedocs.io/) - System mouse and keyboard control
