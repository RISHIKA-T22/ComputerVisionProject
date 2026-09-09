# Smart Image Analysis & Object Detection using OpenCV

A Computer Vision project developed using Python, OpenCV, and NumPy. The project processes an input image, detects edges and contours, and identifies objects using contour area and bounding boxes.

## Features

- Load an input image
- Convert the image to grayscale
- Reduce image noise using Gaussian Blur
- Detect edges using Canny Edge Detection
- Detect contours
- Filter contours based on area
- Detect objects using contours
- Draw bounding boxes around detected objects
- Label detected objects
- Count the detected objects
- Save the processed result as `output.jpg`

## Technologies Used

- Python
- OpenCV
- NumPy

## Computer Vision Pipeline

Input Image
↓
Grayscale Conversion
↓
Gaussian Blur
↓
Canny Edge Detection
↓
Contour Detection
↓
Area Filtering
↓
Object Detection
↓
Bounding Boxes & Labels
↓
Output Image

## How It Works

### 1. Image Loading

The input image is loaded using OpenCV.

### 2. Grayscale Conversion

The color image is converted into a grayscale image to simplify image processing.

### 3. Gaussian Blur

Gaussian Blur is applied to reduce noise in the image before edge detection.

### 4. Canny Edge Detection

Canny Edge Detection is used to identify important edges and boundaries in the image.

### 5. Contour Detection

Contours are detected from the edges to identify object boundaries.

### 6. Area Filtering

Contours with an area greater than 500 pixels are considered for object detection. This helps ignore very small contours.

### 7. Object Detection

Bounding rectangles are created around the detected contours.

### 8. Object Labeling

Each detected object is assigned a label such as `Object 1`, `Object 2`, etc.

### 9. Output

The program displays:

- Original Image
- Grayscale Image
- Edge Detection
- Detected Objects

The detected-object result is also saved as:

`output.jpg`

## Project Structure

```text
ComputerVisionProject/
│
├── venv/
├── main.py
├── input.jpg
├── output.jpg
├── requirements.txt
└── README.md