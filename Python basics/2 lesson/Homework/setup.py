# heart_animation_project/setup.py

import sys
import subprocess
import logging

def check_and_install(package_name: str) -> bool:
    """
    Berilgan paket mavjudligini tekshiradi. Agar bo'lmasa, o'rnatadi.
    O'rnatish jarayoni logga yoziladi.

    Args:
        package_name (str): O'rnatiladigan paket nomi (masalan, 'pygame').

    Returns:
        bool: Paket muvaffaqiyatli o'rnatilganda yoki allaqachon mavjud bo'lganda True,
              aks holda False.
    """
    try:
        __import__(package_name)
        logging.info(f"'{package_name}' paketi allaqachon o'rnatilgan.")
        return True
    except ImportError:
        logging.warning(f"'{package_name}' paketi topilmadi. O'rnatish boshlanmoqda...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
            logging.info(f"'{package_name}' paketi muvaffaqiyatli o'rnatildi.")
            return True
        except subprocess.CalledProcessError as e:
            logging.error(f"'{package_name}' ni o'rnatishda xatolik yuz berdi: {e}")
            return False
        except Exception as e:
            logging.error(f"'{package_name}' ni o'rnatishda kutilmagan xatolik: {e}")
            return False

def setup_environment():
    """
    Dastur uchun zarur bo'lgan barcha muhit shartlarini tekshiradi va o'rnatadi.
    Python versiyasini ham tekshiradi.
    """
    # Python versiyasini tekshirish (masalan, 3.7 dan yuqori kerak)
    if sys.version_info < (3, 7):
        logging.critical("Bu dastur Python 3.7 yoki undan yuqori versiyasini talab qiladi.")
        sys.exit(1)
    
    # Kerakli paketlar ro'yxati
    required_packages = ['pygame']
    
    all_installed = True
    for package in required_packages:
        if not check_and_install(package):
            all_installed = False
    
    if not all_installed:
        logging.critical("Barcha kerakli paketlar o'rnatilmadi. Dastur ishga tushmaydi.")
        sys.exit(1)
    
    logging.info("Muvaffaqiyatli: Barcha shartlar qondirildi.")