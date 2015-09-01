# -*- coding: utf-8 -*-

import sys
import os
import json
import ctypes
import win32con, win32gui, win32api

EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
IsWindowVisible = ctypes.windll.user32.IsWindowVisible

windows = {}
def getWindowPos(hwnd, lParam):
    if IsWindowVisible(hwnd) == False:
        return True
    
    rect = win32gui.GetWindowRect(hwnd)
    windows[str(int(hwnd))] = rect
    
    return True

def setWindowPos(hwnd, lParam):
    shwnd = str(int(hwnd))
    if not shwnd in windows.keys():
        return True

    if not shwnd in windows.keys():
        return True
    
    rect = windows[shwnd]
    w = rect[2] - rect[0]
    h = rect[3] - rect[1]
    if w == 0 or h == 0:
        return True
    
    try:
        win32gui.MoveWindow(hwnd, rect[0], rect[1], w, h, True)
    except:
        pass
        
    return True


if __name__ == '__main__':
    desktopSize = (win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN),
                   win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN))
    dat = os.path.join(os.path.dirname(__file__), '%dx%d.dat' % desktopSize)
    if len(sys.argv) == 1:
        win32gui.EnumWindows(getWindowPos, None)

        fp = open(dat, 'w')
        jsonData = json.dumps(windows, sort_keys=True, indent=4, ensure_ascii=False)
        fp.write(jsonData)
        fp.close()
    else:
        if os.path.exists(dat):
            fp = open(dat)
            jsonData = fp.read()
            fp.close()
            windows = json.loads(jsonData)
        
            win32gui.EnumWindows(setWindowPos, None)

    exit(0)
