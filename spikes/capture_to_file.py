#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2

# Start capturing video from the webcam (device 0)
cap = cv2.VideoCapture(0)

# Set a frame rate for recording the video (adjust based on your webcam's
# capabilities)
FRAMES_PER_SECOND = 24.0
# Codec for saving the video
FOURCC = cv2.VideoWriter_fourcc(*"XVID")

out = None

try:
    while True:
        ret, frame = cap.read()  # Read a frame from the webcam

        if not ret:
            break  # Break the loop if no frame is captured

        if not out:
            out = cv2.VideoWriter(
                "capture_to_file.mp4",
                FOURCC,
                FRAMES_PER_SECOND,
                (frame.shape[1], frame.shape[0]),
            )

        # Write the frame to the output video file
        out.write(frame)

        # Display the frame in a window
        cv2.imshow("Webcam", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

except KeyboardInterrupt:
    print("Interrupted by user")

finally:
    cap.release()
    cv2.destroyAllWindows()
    if out:
        out.release()
