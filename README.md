A hand tracking system that detects and counts the number of open fingers using OpenCV and MediaPipe.

**Overview**:
This project utilizes OpenCV and MediaPipe to track a hand and determine the number of open fingers. The captured data can be used to control external devices, such as toggling sensors or even replicating hand movements in a robotic arm.

**Use Case Example**:
A robotic arm can be programmed to mimic real-time finger movements based on live tracking data.

**Installation**:
Ensure you have the following dependencies installed before running the project. 
pip install opencv-python mediapipe

**How to Run**:
> Clone the repository.
> Run FingerCounter.py to see track the hand and number of fingers.
> If you only need basic hand tracking, use HandTrackingMin.py, which contains the minimal required code for tracking. You can modify it based on your needs to perform further actions.
