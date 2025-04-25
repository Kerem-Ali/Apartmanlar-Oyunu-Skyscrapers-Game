# 🏙️ SKYSCRAPERS MIND GAME 🏙️
<div align="center">
  
  <img src="images/solver.png" width="300" alt="Game Logo">
  
  **A visual logic puzzle game that challenges your mental skills!**
  
  *Originally developed as a high school preparatory project in computer science - May 20, 2022*
  
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
  [![Pygame](https://img.shields.io/badge/pygame-2.0+-orange.svg)](https://www.pygame.org/)
</div>

## 🎮 About The Game
**Skyscrapers Mind Game** is a logic puzzle I created as my first programming project during my high school preparatory year in 2022. In this game, you fill a grid with skyscrapers of various heights by following clues placed along the edges. Each row and column must contain all numbers from 1 to N (grid size) exactly once, and the edge numbers indicate how many skyscrapers are visible when looking from that direction.

> *"Use your logic, understand perspective, and build the city skyline!"*

## 📋 How to Play
<div align="center">
  <img src="images/problem.png" width="300" alt="Problem Screen">
</div>

### Rules:
1. **Fill each cell** with a number representing a skyscraper's height (1 to grid size)
2. **Each row and column must contain each number exactly once** (similar to Sudoku)
3. **Edge numbers show** how many skyscrapers are visible when looking from that direction
4. **Taller skyscrapers block** the view of shorter ones behind them

<details>
<summary><b>🔍 Tip: How Skyscraper Visibility Works</b></summary>
<br>
For example, if you have skyscrapers arranged [2, 4, 1, 3] from left to right:
<ul>
<li>Looking from the left: You see 2 skyscrapers (2 and 4)</li>
<li>Looking from the right: You see 3 skyscrapers (3, 4 and 2)</li>
</ul>
<img src="images/starter.png" width="250" alt="Starter Screen">
</details>

## 📚 Project Background
This game was developed as my programming project during my high school preparatory year. I started working on it on May 20, 2022, as part of my curriculum requirements. The project helped me learn fundamentals of:
- Python programming
- Game development concepts
- GUI design with Pygame
- Logic puzzle algorithms

## ⚙️ Installation
```bash
# 1. Ensure Python is installed on your system
# 2. Install Pygame:
pip install pygame
# 3. Clone this repository:
git clone https://github.com/yourusername/skyscrapers-game.git
cd skyscrapers-game
# 4. Run the game
python main.py
```

## 🌟 Features
| Feature | Description |
|---------|-------------|
| 🔄 **Built-in Solver** | Assistance for challenging puzzles |
| 🖱️ **Interactive GUI** | User-friendly interface built with Pygame |
| 📊 **Multiple Difficulty Levels** | From beginner to expert |
| 💾 **Progress Saving** | Continue your game later |

## 🎯 Game Controls
- **Left click**: Select a cell
- **Number keys (1-N)**: Place a number
- **Reset Button**: Reset puzzle
- **Hint Button**: Get help on difficult puzzles

## 🤔 How It Works
<div align="center">
  <img src="images/solver.png" width="250" alt="Solver Screen">
</div>

The game uses complex constraint logic and visibility calculations. The solver algorithm employs advanced constraint propagation techniques that simulate human-like reasoning - a concept I was particularly interested in while developing this as my first major programming project.

## 🚀 Development Journey
Starting with minimal programming knowledge, I developed this game as part of my journey into computer science. What began as a high school assignment evolved into a passion project that taught me the fundamentals of software development and logical thinking.

## 📝 License
This project is licensed under the [MIT License](LICENSE).

---
<div align="center">
  
  **🏙️ Skyscrapers Mind Game - A Python implementation using Pygame 🏙️**
  
  **Originally developed as a high school preparatory project - May 20, 2022**
  
  [🐛 Report Bug](https://github.com/yourusername/skyscrapers-game/issues) | [🔄 Submit PR](https://github.com/yourusername/skyscrapers-game/pulls) | [⭐ Star](https://github.com/yourusername/skyscrapers-game)
  
</div>
