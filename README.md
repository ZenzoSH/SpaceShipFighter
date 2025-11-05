# Space Ship Fighter Game

A 2-player space combat game built with Pygame where two spaceships battle against each other.

## Game Preview
- Two-player local multiplayer game
- Each player has 10 lives
- Shoot bullets to defeat your opponent
- Features sound effects and space background

<img width="894" height="493" alt="image" src="https://github.com/user-attachments/assets/70e1bb35-4dc8-405d-9c11-6d625aa9e573" />

<img width="898" height="498" alt="image" src="https://github.com/user-attachments/assets/eb6e6686-9dff-4b50-b9b6-19dc28499245" />


## Prerequisites
- Python 3.x
- Pygame library

## Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/SpaceShipFighter.git
cd SpaceShipFighter
```

2. Create and activate a virtual environment:

For Windows:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

For macOS/Linux:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate
```

3. Install requirements:
```bash
# Using requirements.txt
pip install -r requirements.txt

# Or install Pygame directly
pip install pygame==2.5.2
```

4. Verify installation:
```bash
# Check if Pygame is installed correctly
python -c "import pygame; print(pygame.ver)"
```

## How to Play

Run the game:
```bash
python main.py
```

### Controls
- **Yellow Spaceship (Player 1)**
  - Move: WASD keys
  - Shoot: Left CTRL

- **Red Spaceship (Player 2)**
  - Move: Arrow keys
  - Shoot: Right SHIFT

- **General Controls**
  - Exit game: ESC
  - Play again after game over: SPACE

## Game Rules
1. Each player starts with 10 lives
2. Players can shoot up to 8 bullets at once
3. Hit your opponent to reduce their health
4. First player to reduce opponent's health to 0 wins

## Project Structure
```
SpaceShipFighter/
│
├── main.py           # Main game file
├── requirements.txt  # Python dependencies
└── Assets/          # Game assets (images and sounds)
    ├── spaceship_yellow.png
    ├── spaceship_red.png
    ├── space.png
    ├── Gun+Silencer.mp3
    └── Grenade+1.mp3
```
