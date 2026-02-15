# 🎵 Spotify Console Manager: Data Structures in Harmony

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Pygame](https://img.shields.io/badge/Audio-Pygame-green)
![DataStructures](https://img.shields.io/badge/Logic-Linked_Lists-red)

A music playlist management system built to demonstrate the practical application of various linked list architectures. It allows users to manage and play local music files using different structural paradigms.

## 🧠 Data Structure Implementations

The core of this project is the custom implementation of four different linked list types:
1.  **Simple Linked List**: Basic sequential navigation.
2.  **Doubly Linked List**: Bidirectional navigation (Next/Previous).
3.  **Circular Linked List**: Continuous loop playback.
4.  **Doubly Circular Linked List**: Advanced bidirectional continuous playback (Standard in modern players).

## 🌟 Features

- **Dynamic Playback**: Integrated `pygame.mixer` for playing MP3/WAV files with pause/resume functionality.
- **Premium Model**: Logic for account tiers (Standard vs Premium) that unlocks advanced data structures and random 30-song playlist generation.
- **Persistence**: Save and load your customized playlists via JSON storage.
- **Autodetect**: Automatically scans the `data/audio-files` directory for new songs and calculates metadata.

## 🚀 Getting Started

1.  Place your music in `data/audio-files/`.
2.  Install requirements: `pip install pygame`.
3.  Run the application: `python main.py`.

## 📜 Structure
- `linked_lists/`: Custom Python implementations of list structures.
- `utils/`: Audio engine and storage wrappers.
- `data/`: Music files and saved playlist state.

---
*Exploring the intersection of algorithms and audio.*
