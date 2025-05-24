#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import webbrowser
import time
import random
import sys
import ctypes

def hide_console():
    if sys.platform == 'win32':
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def open_random_sites():
    sites = [
        'https://www.youtube.com',
        'https://www.google.com',
        'https://www.facebook.com',
        'https://www.twitter.com',
        'https://www.instagram.com',
        'https://www.reddit.com',
        'https://www.github.com',
        'https://www.stackoverflow.com'
    ]
    
    while True:
        try:
            # Открываем случайный сайт
            site = random.choice(sites)
            webbrowser.open(site)
            time.sleep(random.randint(10, 30))
        except:
            pass

if __name__ == "__main__":
    hide_console()
    open_random_sites() 