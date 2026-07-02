# 🎹 Virtual Piano

Play a virtual piano in the air — no physical keys, just your hands and a webcam.

This project uses real-time hand tracking to detect finger positions over an on-screen piano layout and triggers the corresponding note when a "press" is detected.

![Demo](image.png)

## How It Works

1. **Webcam feed** is captured frame-by-frame using OpenCV.
2. **MediaPipe Hands** detects landmarks for up to 2 hands and extracts the 5 fingertip positions per hand.
3. The frame is divided into 10 equal-width key regions (C4–E5), each tracked with a `pressed` / `prev_pressed` state.
4. On each frame, every fingertip is checked for collision with a key's bounding box. A note only plays on the *rising edge* — i.e. the first frame a fingertip enters a key — so holding a finger down doesn't re-trigger the sound.
5. **pygame** plays the corresponding `.mp3` note instantly, and the key is highlighted while pressed.

## Features

- 🎵 10 playable keys spanning **C4 to E5**
- ✋ Real-time, dual-hand fingertip tracking via MediaPipe (all 5 fingertips per hand)
- 🎼 Debounced key presses — a note plays once per press, not repeatedly while held
- 🖥️ Live visual overlay of the piano keys on the webcam feed, with pressed-key highlighting

## Project Structure

```bash
virtual-piano/
├── README.md
├── requirements.txt
├── main_piano.py           # entry point, captures webcam feed, ties tracker + piano together
├── piano_hand_tracker.py   # HandDetector class wrapping MediaPipe (landmarks, fingertip IDs)
├── virtual_piano.py        # key layout, drawing, collision-based press detection, sound playback
└── sounds/                  # C4.mp3, D4.mp3, ... E5.mp3
```

## Installation

```bash
git clone https://github.com/malakhishams/Virtual-Piano.git
cd Virtual-Piano
pip install -r requirements.txt
```

## Usage

```bash
python main_piano.py
```

Position your hand in front of the webcam so it's visible, then move your fingertips over the on-screen keys to play notes. Press `q` to quit.

## Requirements

- Python 3.8+
- opencv-python
- mediapipe
- pygame

## Tech Stack

`Python` · `OpenCV` · `MediaPipe` · `pygame`

Worked with [Wegdan Ashraf](https://github.com/wegdanashraf27-spe) and presented our project at **RoboTech Fair '26** at our faculty, proud of what we built!
