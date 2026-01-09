# heart_animation_project/config.py

import os

# --- Ekran o'lchamlari va unvon ---
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
FPS = 60
WINDOW_TITLE = "Professional Yurakcha Animatsiyasi"

# --- Rang palitrasi ---
BACKGROUND_COLOR = (10, 10, 20) # Juda to'q ko'k, qora emas
STAR_COLOR_BASE = (255, 255, 255)
HEART_COLOR_MAIN = (220, 20, 60)
HEART_COLOR_GLOW = (255, 100, 150)

# --- Animatsiya parametrlari ---
# Yulduzlar
STAR_COUNT = 250
STAR_MIN_SIZE = 0.5
STAR_MAX_SIZE = 2.5
STAR_TWINKLE_SPEED_MIN = 0.01
STAR_TWINKLE_SPEED_MAX = 0.05

# Yurakcha
HEART_BASE_SIZE = 20
HEART_PULSE_SPEED = 0.05
HEART_PULSE_AMOUNT = 0.12
HEART_PARTICLE_SPAWN_RATE = 0.9 # Har kadrda zarracha paydo bo'lish ehtimoli

# Zarrachalar
PARTICLE_MIN_LIFE = 40
PARTICLE_MAX_LIFE = 80
PARTICLE_MIN_SPEED = 0.5
PARTICLE_MAX_SPEED = 2.5
PARTICLE_GRAVITY = 0.04
PARTICLE_MIN_SIZE = 1
PARTICLE_MAX_SIZE = 3

# --- Loglash sozlamalari ---
LOG_FILE = "app.log"
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'