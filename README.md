# 🐾 Desktop Cat Companion

A cute virtual desktop pet for Windows that lives on your screen as a friendly feline companion. Watch your cat walk around, sleep, play, follow your mouse, react to interactions, and grow its friendship level over time.

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![PyQt6](https://img.shields.io/badge/PyQt6-GUI-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## ✨ Features

### 🐱 Interactive Cat Companion
- Walks around the desktop
- Follows the mouse cursor
- Sleeps when tired
- Random idle animations
- Drag-and-drop movement
- Stays above other windows

### ❤️ Pet Care System
- Feed your cat treats
- Play with your cat
- Increase friendship levels
- Happiness and energy stats
- Persistent progress saving

### 🎭 Animations & Reactions
- Idle animation
- Walking animation
- Sleeping animation
- Jump animation
- Click reactions
- Speech bubbles and messages

### 🎨 Customization
- Multiple cat skins
- Adjustable pet size
- Sound settings
- Behavior preferences

### 💾 Save System
- Auto-save progress
- Store friendship levels
- Save selected skins
- Local JSON storage

---

## 📸 Preview

```text
 /\_/\\
( o.o )
 > ^ <
```

*A tiny feline friend living on your desktop.*

---

## 🛠 Tech Stack

- Python 3.11+
- PyQt6
- Pygame
- Pillow
- JSON

---

##dekstop-pet-app/
├── main.py                 # Entry point
├── requirements.txt        # Dependencies
├── config.json            # Configuration file
├── README.md              # This file
├── src/
│   ├── pet.py            # Main Pet class
│   ├── animation.py       # Animation system
│   ├── sprite_manager.py  # Sprite handling
│   ├── sound_manager.py   # Audio management
│   ├── ui/
│   │   ├── main_window.py      # Main application window
│   │   ├── status_panel.py     # Pet stats display
│   │   ├── settings_dialog.py  # Settings window
│   │   └── speech_bubble.py    # Notification bubbles
│   ├── systems/
│   │   ├── save_system.py      # Save/load functionality
│   │   ├── interaction.py      # Pet interactions
│   │   ├── behavior.py         # Autonomous behaviors
│   │   ├── achievement.py      # Achievement tracking
│   │   └── mini_game.py        # Mini-games
│   ├── utils/
│   │   ├── constants.py        # Game constants
│   │   ├── config_manager.py   # Configuration management
│   │   └── helpers.py          # Utility functions
│   └── tray/
│       └── system_tray.py      # System tray integration
├── tests/
│   └── test_pet.py       # Unit tests
├── data/                 # Save files (auto-created)
└── assets/              # Game assets (auto-created)
    ├── sprites/
    ├── sounds/
    └── skins/
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/desktop-cat-companion.git
cd desktop-cat-companion
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python main.py
```

---

## 📦 Requirements

```txt
PyQt6
pygame
Pillow
```

---

## 🎮 Controls

| Action | Function |
|----------|----------|
| Left Click | Pet the cat |
| Double Click | Trigger animation |
| Right Click | Open settings |
| Drag | Move pet |
| Feed Button | Increase happiness |
| Play Button | Increase friendship |

---

## ⚙️ Settings

Customize your pet through the settings menu:

- Change cat skin
- Resize pet
- Enable/disable sounds
- Adjust activity frequency
- Reset saved data

---

## 💾 Save Data Example

```json
{
  "friendship": 52,
  "happiness": 88,
  "energy": 70,
  "skin": "orange_cat"
}
```

---

## 🌟 Planned Features

- Multiple pets
- Dog companion
- Weather reactions
- Daily rewards
- Achievement system
- Mini-games
- Voice interactions
- AI-powered conversations

---

## 🤝 Contributing

Contributions, suggestions, and bug reports are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## 🐛 Bug Reports

If you encounter issues:

- Open an Issue
- Include screenshots if possible
- Provide system information
- Describe steps to reproduce the problem

---

## 📜 License

This project is licensed under the MIT License.

---

## 💖 Acknowledgements

Inspired by cozy virtual pet companions and desktop pet applications that bring personality and fun to everyday computing.

---

### 🐾 Made with Python, PyQt6, and lots of cat energy. ✨
