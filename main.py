#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fer import FER
import cv2

# Initialize the detector
detector = FER(mtcnn=True)

# Start webcam
cap = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Detect emotions on the frame
        result = detector.detect_emotions(frame)
        for face in result:
            # Unpack the values
            box = face["box"]
            emotions = face["emotions"]

            x, y, w, h = box
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Find the emotion with the highest score
            emotion_type = max(emotions, key=emotions.get)
            emotion_score = emotions[emotion_type]

            # Display the emotion type and its confidence level
            emotion_text = f"{emotion_type}: {emotion_score:.2f}"
            cv2.putText(
                frame,
                emotion_text,
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (0, 255, 0),
                2,
            )

        # Display the resulting frame
        cv2.imshow("Emotion Detection", frame)

        # Break the loop
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
except KeyboardInterrupt:
    print("Interrupted by user")
finally:
    # When everything is done, release the capture
    cap.release()
    cv2.destroyAllWindows()
