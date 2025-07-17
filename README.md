# 20-40-Ate

A hybrid Python game combining the mechanics of **2048** and **Snake**, built with Pygame.

Created by **Markandeya Yalamanchi**

## How to Play

- Move using arrow keys
- Eat number tiles to grow your snake
- Merge consecutive tiles (like 2048)
- Score points with every merge
- Avoid crashing into yourself or the walls
- Pause to access reset, music toggle, or return to main menu

## Controls

| Key        | Action              |
|------------|---------------------|
| Arrow Keys | Move snake          |
| `P` / ESC  | Pause / Resume      |
| `R`        | Restart             |
| Mouse      | Click menu buttons  |

## Music

- Title and Game music are different
- Toggle music from the title or pause menu

## How to Run

### 1. Install Requirements

Make sure Python 3.8+ is installed. Then:

```bash
pip install -r requirements.txt
```

### 2. Run the Game

```bash
python main.py
```

### 3. Check file structure

It should look like this, sorry if it is a little weird on Github:

20-40-Ate/
├── assets/
│   └── music/
│       ├── game_music.mp3
│       └── menu_music.mp3
├── main.py
├── requirements.txt
├── README.md
├── src/
│   ├── __init__.py
│   ├── audio.py              # Handles background music and toggling
│   ├── game.py               # Main gameplay logic (snake, merging, movement)
│   ├── menu.py               # Title screen logic and play/music buttons
│   ├── pause_menu.py         # Pause menu UI logic (optional modularization)
│   └── utils.py              # Button class, text rendering utilities

Enjoy!
