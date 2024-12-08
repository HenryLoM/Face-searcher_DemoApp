# Face-Searcher

**Face-Searcher** is a real-time face detection and landmark recognition program using a webcam. Built with **MediaPipe**, it detects faces, marks key facial landmarks, and provides real-time feedback.

## Features

- **Face Detection**: Displays bounding boxes around detected faces.  
- **Face Counting**: Shows the number of faces detected in real-time.  
- **Landmark Recognition**: Highlights key facial features and their coordinates.  
- **Real-Time Processing**: Operates in real-time using a connected webcam.

## Prerequisites

- Python (version 3.7 or higher)  
- Libraries:  
  - `opencv-python`  
  - `mediapipe`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/HenryLoM/Face-Searcher_DemoApp.git
   cd MainDirectory_Face-Searcher
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the program:
   ```bash
   python main.py
   ```

## How to Use

1. Ensure your webcam is connected to your device.
2. Run the `main.py` script.
3. A video stream with overlaid bounding boxes and facial landmarks will appear.
4. Press **Q** to terminate the program.

## Contribution Guidelines

We welcome community contributions. To add features or make improvements, follow these steps:

1. Fork the repository.  
2. Create a new branch for your feature:  
   ```bash
   git checkout -b feature-name
   ```  
3. Implement your changes and commit them:  
   ```bash
   git commit -m "Description of changes."
   ```  
4. Push your changes to your fork:  
   ```bash
   git push origin feature-name
   ```  
5. Submit a pull request to the main repository.

## License

This project is licensed under the terms of the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.
