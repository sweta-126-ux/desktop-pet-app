"""
Utility Constants - Global configuration values and enumerations

Defines all constant values used throughout the application.
"""

from enum import Enum
from pathlib import Path

# ============================================================================
# PATHS
# ============================================================================

APP_ROOT = Path(__file__).parent.parent.parent
DATA_DIR = APP_ROOT / 'data'
ASSETS_DIR = APP_ROOT / 'assets'
SPRITES_DIR = ASSETS_DIR / 'sprites'
SOUNDS_DIR = ASSETS_DIR / 'sounds'
SKINS_DIR = ASSETS_DIR / 'skins'
CONFIG_FILE = APP_ROOT / 'config.json'
PET_DATA_FILE = DATA_DIR / 'pet_data.json'
ACHIEVEMENTS_FILE = DATA_DIR / 'achievements.json'

# ============================================================================
# WINDOW PROPERTIES
# ============================================================================

WINDOW_WIDTH = 256
WINDOW_HEIGHT = 256
DEFAULT_PET_X = 100
DEFAULT_PET_Y = 100
WINDOW_OPACITY = 1.0
WINDOW_FLAGS = 0x00000008 | 0x00000002  # Frameless + stays on top (Windows)

# ============================================================================
# ANIMATION SETTINGS
# ============================================================================

ANIMATION_FRAME_RATE = 60
ANIMATION_WALK_SPEED = 50  # pixels per second
IDLE_ANIMATION_INTERVAL = 3000  # milliseconds
SLEEP_DURATION = 10000  # milliseconds

# ============================================================================
# PET STATS
# ============================================================================

INITIAL_HAPPINESS = 70
INITIAL_ENERGY = 80
INITIAL_AFFECTION = 60

MAX_STAT = 100
MIN_STAT = 0

# Stat changes per action
HAPPINESS_PER_PLAY = 15
HAPPINESS_PER_FEED = 10
AFFECTION_PER_PET = 5
AFFECTION_PER_PLAY = 8
ENERGY_LOSS_PER_WALK = 2
ENERGY_LOSS_PER_PLAY = 5
ENERGY_GAIN_PER_SLEEP = 20

# Decay rates (per second)
HAPPINESS_DECAY_RATE = 0.5
ENERGY_DECAY_RATE = 0.3
AFFECTION_DECAY_RATE = 0.2

# ============================================================================
# BEHAVIOR SETTINGS
# ============================================================================

AUTO_ACTION_INTERVAL = 5000  # milliseconds
FOLLOW_CURSOR_DISTANCE = 200  # pixels
FOLLOW_CURSOR_THRESHOLD = 50  # pixels
WALK_TIMEOUT = 8000  # milliseconds before stopping walk

# ============================================================================
# UI SETTINGS
# ============================================================================

STATUS_PANEL_WIDTH = 200
STATUS_PANEL_HEIGHT = 150
STATUS_PANEL_OPACITY = 0.9
SPEECH_BUBBLE_DURATION = 3000  # milliseconds
SPEECH_BUBBLE_MAX_WIDTH = 150

# ============================================================================
# SOUND SETTINGS
# ============================================================================

MASTER_VOLUME = 0.7
EFFECTS_VOLUME = 0.8
FX_VOLUME_PET = 0.6
FX_VOLUME_EAT = 0.5
FX_VOLUME_PLAY = 0.7

# ============================================================================
# FILE SETTINGS
# ============================================================================

AUTO_SAVE_INTERVAL = 60000  # milliseconds (1 minute)
CONFIG_VERSION = "1.0.0"

# ============================================================================
# ENUMERATIONS
# ============================================================================


class PetState(Enum):
    """Enumeration of possible pet states."""
    IDLE = "idle"
    WALKING = "walking"
    RUNNING = "running"
    JUMPING = "jumping"
    SITTING = "sitting"
    SLEEPING = "sleeping"
    EATING = "eating"
    PLAYING = "playing"
    FALLING = "falling"
    DEAD = "dead"


class AnimationType(Enum):
    """Types of animations available."""
    IDLE = "idle"
    WALK_LEFT = "walk_left"
    WALK_RIGHT = "walk_right"
    RUN_LEFT = "run_left"
    RUN_RIGHT = "run_right"
    JUMP = "jump"
    SIT = "sit"
    SLEEP = "sleep"
    EAT = "eat"
    PLAY = "play"
    FALL = "fall"
    REACTION_HAPPY = "reaction_happy"
    REACTION_SAD = "reaction_sad"
    REACTION_CONFUSED = "reaction_confused"


class SkinType(Enum):
    """Available cat skins."""
    ORANGE = "orange"
    BLACK = "black"
    WHITE = "white"
    GRAY = "gray"
    CALICO = "calico"
    TABBY = "tabby"
    SIAMESE = "siamese"


class InteractionType(Enum):
    """Types of user interactions."""
    PET = "pet"
    PLAY = "play"
    FEED = "feed"
    SLEEP = "sleep"
    PICK_UP = "pick_up"


class AchievementType(Enum):
    """Types of achievements."""
    FIRST_PET = "first_pet"
    HAPPINESS_100 = "happiness_100"
    AFFECTION_100 = "affection_100"
    PLAY_10_TIMES = "play_10_times"
    FEED_20_TIMES = "feed_20_times"
    SLEEP_1_HOUR = "sleep_1_hour"
    UNLOCK_ALL_SKINS = "unlock_all_skins"
    MINI_GAME_MASTER = "mini_game_master"
    LOYAL_FRIEND = "loyal_friend"
    ULTIMATE_COMPANION = "ultimate_companion"


class GameDifficulty(Enum):
    """Mini-game difficulty levels."""
    EASY = 1
    NORMAL = 2
    HARD = 3


# ============================================================================
# DEFAULT RESPONSES
# ============================================================================

PET_REACTIONS = {
    "happy": ["Meow! 😸", "Purr purr 😻", "So happy! 🐱"],
    "sad": ["Meow... 😿", "Sad meow 😿", "Lonely... 😾"],
    "hungry": ["Meowww! 🍖", "Feed me! 😺", "So hungry... 😾"],
    "sleepy": ["*yawn* 😴", "Zzzzz... 😴", "So sleepy... 😴"],
    "playful": ["Let's play! 🏾", "Play with me! 😸", "Meow meow! 😺"],
    "affection": ["*purrs* 😻", "I love you! 😻", "Thank you! 😸"],
}

SPEECH_BUBBLES = {
    "greeting": ["Hello there!", "Hi! 👋", "Nice to see you!"],
    "playing": ["This is fun!", "Weee! 🎉", "Again! Again!"],
    "eating": ["Nom nom nom 😋", "Delicious! 😺", "Thank you!"],
    "sleeping": ["Good night... 😴", "Zzzzz...", "Sweet dreams..."],
}

# ============================================================================
# PERFORMANCE SETTINGS
# ============================================================================

MAX_SPRITES_LOADED = 10
ENABLE_V_SYNC = True
REDUCED_ANIMATIONS_AT_LOW_PERFORMANCE = True
TARGET_FPS = 60
