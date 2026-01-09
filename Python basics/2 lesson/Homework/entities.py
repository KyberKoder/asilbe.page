# heart_animation_project/entities.py

import pygame
import math
import random
from typing import List, Tuple
import config

class Yulduz:
    """Fondagi porlab turuvchi yulduz."""
    def __init__(self):
        self.x = random.randint(0, config.SCREEN_WIDTH)
        self.y = random.randint(0, config.SCREEN_HEIGHT)
        self.size = random.uniform(config.STAR_MIN_SIZE, config.STAR_MAX_SIZE)
        self.brightness = random.randint(100, 255)
        self.twinkle_speed = random.uniform(config.STAR_TWINKLE_SPEED_MIN, config.STAR_TWINKLE_SPEED_MAX)
        self.twinkle_phase = random.uniform(0, math.pi * 2)

    def update(self):
        self.twinkle_phase += self.twinkle_speed

    def draw(self, screen: pygame.Surface):
        current_brightness = int(self.brightness * (0.5 + 0.5 * math.sin(self.twinkle_phase)))
        color = (*config.STAR_COLOR_BASE, current_brightness) # Agar shaffoflik kerak bo'lsa
        pygame.draw.circle(screen, config.STAR_COLOR_BASE, (int(self.x), int(self.y)), int(self.size))

class Zarracha:
    """Yurakchadan sochiladigan, gravitatsiyaga ta'sirchan zarracha."""
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        angle = random.uniform(0, math.pi * 2)
        speed = random.uniform(config.PARTICLE_MIN_SPEED, config.PARTICLE_MAX_SPEED)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed - 1
        self.life = random.randint(config.PARTICLE_MIN_LIFE, config.PARTICLE_MAX_LIFE)
        self.initial_life = self.life
        self.size = random.uniform(config.PARTICLE_MIN_SIZE, config.PARTICLE_MAX_SIZE)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += config.PARTICLE_GRAVITY
        self.life -= 1

    def draw(self, screen: pygame.Surface):
        if self.life > 0:
            alpha_ratio = self.life / self.initial_life
            current_size = self.size * alpha_ratio
            pygame.draw.circle(screen, config.HEART_COLOR_GLOW, (int(self.x), int(self.y)), int(current_size))

class Yurakcha:
    """Pulsirlaydigan va zarrachalar sochadigan asosiy yurakcha ob'ekti."""
    def __init__(self):
        self.x = config.SCREEN_WIDTH // 2
        self.y = config.SCREEN_HEIGHT // 2
        self.pulse = 0

    def _get_points(self, scale: float) -> List[Tuple[float, float]]:
        """Matematik formula orqali yurakcha shaklini hisoblaydi."""
        points = []
        for t in range(0, 628, 5):
            t_rad = t / 100
            x = 16 * (math.sin(t_rad) ** 3)
            y = -(13 * math.cos(t_rad) - 5 * math.cos(2 * t_rad) - 2 * math.cos(3 * t_rad) - math.cos(4 * t_rad))
            points.append((self.x + x * scale, self.y + y * scale))
        return points

    def update(self) -> List[Zarracha]:
        self.pulse += config.HEART_PULSE_SPEED
        new_particles = []
        if random.random() < config.HEART_PARTICLE_SPAWN_RATE:
            points = self._get_points(self.get_current_scale())
            spawn_point = random.choice(points)
            new_particles.append(Zarracha(spawn_point[0], spawn_point[1]))
        return new_particles

    def get_current_scale(self) -> float:
        return self.base_size / 20 * (1 + config.HEART_PULSE_AMOUNT * math.sin(self.pulse))

    def draw(self, screen: pygame.Surface):
        scale = self.get_current_scale()
        points = self._get_points(scale)
        
        # Yorug'lik effekti (glow)
        glow_surface = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT), pygame.SRCALPHA)
        for i in range(5):
            glow_scale = scale * (1 + i * 0.15)
            glow_points = self._get_points(glow_scale)
            glow_alpha = 40 - i * 8
            pygame.draw.polygon(glow_surface, (*config.HEART_COLOR_GLOW, glow_alpha), glow_points)
        screen.blit(glow_surface, (0, 0))

        # Asosiy yurakcha
        pygame.draw.polygon(screen, config.HEART_COLOR_MAIN, points)

