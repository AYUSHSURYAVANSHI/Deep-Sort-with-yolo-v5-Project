# Object Tracking with PyTorch, YOLOv5, and DeepSort

This repository contains the implementation of an object-tracking system using PyTorch, YOLOv5 for object detection, and DeepSort for tracking. The system is capable of detecting and tracking multiple objects in real-time from video streams.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project combines the power of YOLOv5, a state-of-the-art object detection model, with DeepSort, a robust object tracking algorithm. The goal is to detect and track objects across video frames efficiently.

**YOLOv5** is used to detect objects in each frame, and **DeepSort** is employed to assign unique IDs to each detected object and track them across the video. This combination allows for real-time object tracking in various applications like surveillance, autonomous vehicles, and more.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/Object-Tracking-PyTorch-YOLOv5-DeepSort.git
    cd Object-Tracking-PyTorch-YOLOv5-DeepSort
    ```

2. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Download YOLOv5 pretrained weights:**

    You can download the YOLOv5 weights from the official YOLOv5 repository or use the following command:

    ```bash
    wget https://github.com/ultralytics/yolov5/releases/download/v6.0/yolov5s.pt
    ```

4. **Set up DeepSort:**

    Ensure that the DeepSort module is correctly set up by downloading the necessary model weights:

    ```bash
    cd deep_sort/deep
    wget https://github.com/nwojke/deep_sort/releases/download/v1.0/model_weights.pb
    cd ../..
    ```

## Usage

To run the object tracking system, use the following command:

```bash
python track.py --source <input_video> --weights yolov5s.pt --output <output_directory>
