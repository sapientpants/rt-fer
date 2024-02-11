#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time
import matplotlib
import matplotlib.pyplot as plt


matplotlib.use("MacOSX")

# Set up a matplotlib figure for displaying live emotion detection results
plt.ion()  # Turn on interactive mode for live updates

fig, ax = plt.subplots()

EMOTION_LABELS = ["angry", "disgust", "fear", "happy", "sad", "surprise", "neutral"]

bars = ax.bar(
    EMOTION_LABELS, [0] * 7, color="lightblue"
)  # Initialize bars for each emotion
plt.ylim(0, 1)
plt.ylabel("Confidence")
plt.title("Real-time Emotion Detection")
ax.set_xticklabels(EMOTION_LABELS, rotation=45)


def update_chart(detected_emotions, bars, ax, fig):
    print(detected_emotions)
    # Clear the current axes and set up the bar chart again
    # ax.clear()
    # ax.bar(
    #     EMOTION_LABELS,
    #     [detected_emotions.get(emotion, 0) for emotion in EMOTION_LABELS],
    #     color="lightblue",
    # )
    # plt.ylim(0, 1)
    # plt.ylabel("Confidence")
    # plt.title("Real-time Emotion Detection")
    # ax.set_xticklabels(EMOTION_LABELS, rotation=45)
    for bar, emotion in zip(bars, EMOTION_LABELS):
        bar.set_height(detected_emotions.get(emotion, 0))
    if fig.stale:
        fig.canvas.draw()
    fig.canvas.flush_events()


while True:
    current_emotions = {
        "angry": random.random(),
        "disgust": random.random(),
        "fear": random.random(),
        "happy": random.random(),
        "sad": random.random(),
        "surprise": random.random(),
        "neutral": random.random(),
    }
    update_chart(current_emotions, bars, ax, fig)

    time.sleep(1)
