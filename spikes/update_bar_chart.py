#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import threading
import queue

EMOTION_LABELS = ["angry", "disgust", "fear", "happy", "sad", "surprise", "neutral"]

emotions_queue = queue.Queue()

fig, ax = plt.subplots()
bars = ax.bar(
    EMOTION_LABELS, [0] * 7, color="lightblue"
)

def init_chart():
    plt.ylim(0, 1)
    plt.ylabel("Confidence")
    plt.title("Real-time Emotion Detection")
    ax.set_xticklabels(EMOTION_LABELS, rotation=45)
    return bars

def update_chart(_frame):
    if not emotions_queue.empty():
        detected_emotions = emotions_queue.get()

        for bar, emotion in zip(bars, EMOTION_LABELS):
            bar.set_height(detected_emotions.get(emotion, 0))
    return bars

def detect_emotions():
    while True:
        detected_emotions = {
            "angry": random.random(),
            "disgust": random.random(),
            "fear": random.random(),
            "happy": random.random(),
            "sad": random.random(),
            "surprise": random.random(),
            "neutral": random.random(),
        }

        emotions_queue.put(detected_emotions)

        time.sleep(0.01)

thread = threading.Thread(target=detect_emotions)
thread.start()

ani = FuncAnimation(fig, update_chart, init_func=init_chart, blit=True)

plt.show()
