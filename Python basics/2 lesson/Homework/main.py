# heart_animation_project/main.py

import pygame
import logging
import sys
import random

# O'zimizning modullarimiz
import config
import setup
from entities import Yulduz, Zarracha, Yurakcha

def main():
    """Asosiy dastur funktsiyasi."""
    # --- Loglashni sozlash ---
    logging.basicConfig(
        level=logging.INFO,
        format=config.LOG_FORMAT,
        handlers=[
            logging.FileHandler(config.LOG_FILE),
            logging.StreamHandler(sys.stdout) # Konsolga ham chiqarish
        ]
    )
    logging.info("Dastur ishga tushirilmoqda...")

    # --- Muhitni tayyorlash ---
    setup.setup_environment()

    # --- Pygame ni ishga tushirish va xatoliklarni ushlash ---
    try:
        pygame.init()
        logging.info("Pygame muvaffaqiyatli ishga tushirildi.")
    except pygame.error as e:
        logging.critical(f"Pygame ni ishga tushirib bo'lmadi: {e}")
        sys.exit(1)

    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    pygame.display.set_caption(config.WINDOW_TITLE)
    clock = pygame.time.Clock()

    # --- Obyektlarni yaratish ---
    yulduzlar = [Yulduz() for _ in range(config.STAR_COUNT)]
    yurakcha = Yurakcha()
    zarrachalar: List[Zarracha] = []

    logging.info("Animatsiya sikli boshlandi.")
    running = True
    while running:
        # --- Tadbirlarni boshqarish ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                logging.info("Foydalanuvchi dasturni yopishni so'radi.")

        # --- Yangilash (Update) ---
        for yulduz in yulduzlar:
            yulduz.update()

        new_particles = yurakcha.update()
        zarrachalar.extend(new_particles)

        for zarracha in zarrachalar:
            zarracha.update()
        zarrachalar = [z for z in zarrachalar if z.life > 0]

        # --- Chizish (Draw) ---
        screen.fill(config.BACKGROUND_COLOR)
        for yulduz in yulduzlar:
            yulduz.draw(screen)
        for zarracha in zarrachalar:
            zarracha.draw(screen)
        yurakcha.draw(screen)

        pygame.display.flip()
        clock.tick(config.FPS)

    pygame.quit()
    logging.info("Dastur muvaffaqiyatli yakunlandi.")


if __name__ == '__main__':
    main()