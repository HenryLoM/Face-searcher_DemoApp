# - - - - - - - - - - LIBRARIES - - - - - - - - - -

import cv2
import mediapipe as mp

# - - - - - - - - - - BASICS - - - - - - - - - -

# Initialize MediaPipe face detection and landmark model
mp_face_detection = mp.solutions.face_detection
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

# Initialize webcam
cap = cv2.VideoCapture(0)

# Set desired frame rate
desired_fps = 60
cap.set(cv2.CAP_PROP_FPS, desired_fps)

# - - - - - - - - - - RUN THE CAM - - - - - - - - - -

# Set up the context managers for the MediaPipe face detection and face mesh models
with mp_face_detection.FaceDetection(
        min_detection_confidence=0.5) as face_detection, \
        mp_face_mesh.FaceMesh(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as face_mesh:
    while cap.isOpened():
        # Read frame from webcam
        ret, frame = cap.read()
        if not ret:
            break

        # Frame settings
        frame = cv2.flip(src=frame, flipCode=1)  # flip the frame horizontally
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # convert the image to RGB
        results = face_detection.process(rgb_frame)  # detect faces in the image
        face_count = 0  # initialize face count

        # If faces are found
        if results.detections:
            for detection in results.detections:
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, _ = frame.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
                cv2.rectangle(frame, bbox, (255, 0, 255), 2)
                face_count += 1

                # Draw coordinates of the bounding box
                cv2.putText(frame, f'({bbox[0]}, {bbox[1]})', (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, (0, 255, 0), 2, cv2.LINE_AA)

            # Detect facial landmarks
            face_landmarks = face_mesh.process(rgb_frame)
            landmark_points = []
            if face_landmarks.multi_face_landmarks:
                for face_landmark in face_landmarks.multi_face_landmarks:
                    for i, landmark in enumerate(face_landmark.landmark):
                        ih, iw, _ = frame.shape
                        x, y = int(landmark.x * iw), int(landmark.y * ih)
                        landmark_points.append((x, y))
                # Draw landmarks
                for x, y in landmark_points:
                    cv2.putText(img=frame, text="*", org=(x, y), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                fontScale=0.5, color=(0, 255, 0), thickness=1, lineType=cv2.LINE_AA)

        # Display face count
        cv2.putText(img=frame, text=f"Faces Detected: {face_count}", org=(10, 20), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.5, color=(0, 255, 0), thickness=2)

        # Display face count
        cv2.putText(img=frame, text='Press "Q" to stop the program', org=(10, 80), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.5, color=(0, 255, 0), thickness=2)

        # Display the resulting frame
        cv2.imshow(winname="Frame", mat=frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

# - - - - - - - - - - ENDING - - - - - - - - - -

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
