# Monopoly Game

### Overview
This project is a digital implementation of the classic *Monopoly* board game developed in **Python**. The game features a graphical user interface (GUI) created using the **Turtle Graphics** library, showcasing interactive gameplay and object-oriented programming (OOP) design principles.

This project was developed as part of my high school computer science course, where I independently researched and applied core programming concepts to bring the game to life.

---

## Features
- **Graphical User Interface (GUI):** Utilizes Python's Turtle Graphics to display the game board and in-game events interactively.
- **Object-Oriented Design:** Encapsulates game functionality into classes such as:
  - `UserClass.py`: Manages player properties, turns, and in-game status.
  - `CardClass.py`: Implements game cards (e.g., Chance, Community Chest).
- **Gameplay Logic:** Supports basic Monopoly rules, including property buying, rent collection, and card events.
- **Turn-Based System:** Players take turns moving around the board, interacting with spaces and cards.

---

## Technologies Used
- **Programming Language:** Python
- **Libraries:**
  - Turtle Graphics (GUI rendering)
  - Standard Python modules for game logic

  ## Code Structure
The project is structured as follows:
```plaintext
Monopoly/
├── main.py          # Entry point for the game
├── CardClass.py     # Class to handle card-based events
├── UserClass.py     # Class to manage player attributes and actions
└── graphics.py      # Handles the Turtle GUI rendering

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/bella-cast/Monopoly.git
   cd Monopoly
   ```
2. Ensure you have Python installed (version 3.7 or later).
3. Run the main Python file:
   ```bash
   python main.py
   ```
## How to Play
1. Run the game using the installation instructions above.
2. The game displays a Monopoly board where players can:
   - Roll the dice to move around the board.
   - Purchase properties they land on.
   - Pay rent when landing on other players' properties.
   - Draw cards from *Chance* or *Community Chest* decks.
3. The game continues turn-by-turn until a winning condition is reached.
