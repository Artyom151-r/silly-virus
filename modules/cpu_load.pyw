#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import multiprocessing
import time
import os
import sys
import winreg
import ctypes

def cpu_bound_task():
    """Функция, которая создает нагрузку на CPU"""
    while True:
        # Выполняем математические операции для создания нагрузки
        _ = [i * i for i in range(1000000000000000)]

def create_cpu_load():
    """Создает максимальную нагрузку на все доступные ядра CPU"""
    # Получаем количество ядер процессора
    cpu_count = multiprocessing.cpu_count()
    
    # Создаем процессы для каждого ядра
    processes = []
    for _ in range(cpu_count):
        p = multiprocessing.Process(target=cpu_bound_task)
        p.daemon = True
        p.start()
        processes.append(p)
    
    try:
        # Держим процессы активными
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Завершаем все процессы
        for p in processes:
            p.terminate()
        print("Нагрузка остановлена")

if __name__ == "__main__":
    # Скрываем консоль
    if sys.platform == 'win32':
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    create_cpu_load() 