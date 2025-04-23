# 🏙️ SKYSCRAPERS MIND GAME 🏙️

<div align="center">
  
  <img src="images/solver.png" width="300" alt="Game Logo">
  
  **A visual logic puzzle game that challenges your mental skills!**
  
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
  [![Pygame](https://img.shields.io/badge/pygame-2.0+-orange.svg)](https://www.pygame.org/)

</div>

## 🎮 About The Game

**Skyscrapers Mind Game** is a logic puzzle where you fill a grid with skyscrapers of varying heights following clues along the edges. Each row and column must contain all numbers from 1 to N (grid size) exactly once, while the edge numbers indicate how many skyscrapers are visible from that direction.

> _"Use your logic, understand perspective, and build the city skyline!"_

## 📋 How to Play

<div align="center">
  <img src="images/problem.png" width="300" alt="Problem Screen">
</div>

### Rules:
1. **Fill each cell** with a number representing a skyscraper's height (1 to grid size)
2. **Each row and column must contain each number exactly once** (like sudoku)
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

## 🎬 Video Tutorial

<div align="center">
  
  [![Video Tutorial](https://img.shields.io/badge/YouTube-Watch-red?style=for-the-badge&logo=youtube)](https://youtube.com/shorts/YoA0qptHH34)
  
  _Check out our quick video tutorial to get started_
</div>

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
| 🔄 **Built-in Solver** | Assistance for tough puzzles |
| 🖱️ **Interactive GUI** | User-friendly interface built with Pygame |

## 🎯 Game Controls

- **Left click**: Select a cell
- **Number keys (1-N)**: Place a number
- **Reset Button**: Reset puzzle



## 🤔 How It Works

<div align="center">
  <img src="images/solver.png" width="250" alt="Solver Screen">
</div>

The game uses complex constraint logic and visibility calculations. Our solver algorithm employs advanced constraint propagation techniques that simulate human-like reasoning.

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">
  
  **🏙️ Skyscrapers Mind Game - A Python implementation using Pygame 🏙️**
  
  [🐛 Report Bug](https://github.com/yourusername/skyscrapers-game/issues) | [🔄 Submit PR](https://github.com/yourusername/skyscrapers-game/pulls) | [⭐ Star](https://github.com/yourusername/skyscrapers-game)
  
</div>
