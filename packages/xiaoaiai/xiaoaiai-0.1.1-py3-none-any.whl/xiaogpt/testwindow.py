import win32api
import win32con
import win32gui


# 获取目标显示器的工作区大小和位置信息
def get_display_info(display_index):
    monitor_info = win32api.GetMonitorInfo(win32api.MonitorFromPoint((0, 0)))
    work_area = monitor_info["Work"]
    x, y, width, height = work_area
    if display_index > 0:
        monitor_handles = win32api.EnumDisplayMonitors()
        if len(monitor_handles) > display_index:
            monitor_info = win32api.GetMonitorInfo(monitor_handles[display_index][0])
            work_area = monitor_info["Work"]
            x, y, width, height = work_area
    return x, y, width, height


# 创建窗口
def create_window(display_index):
    x, y, width, height = get_display_info(display_index)
    hwnd = win32gui.CreateWindow("ClassName", "TitleName", win32con.WS_VISIBLE | win32con.WS_POPUP, x, y, width, height,
                                 None, None, None, None)
    return hwnd


# 消息循环
def message_loop():
    while True:
        try:
            win32gui.PumpWaitingMessages()
        except KeyboardInterrupt:
            break


# 在指定的显示器上显示窗口
def show_window_on_display(display_index):
    hwnd = create_window(display_index)
    message_loop()


# 在第一个显示器上显示窗口
show_window_on_display(1)
# Files/JetBrains/PyCharm Community Edition 2023.1/plugins/python-ce/helpers/pydev/pydevd.py" --multiprocess --qt-support=auto --client 127.0.0.1 --port 8016 --file C:\dev\xiaogpt\xiaogpt\testwindow.py
# Connected to pydev debugger (build 231.8109.197)
# Traceback (most recent call last):
#   File "C:\Program Files\JetBrains\PyCharm Community Edition 2023.1\plugins\python-ce\helpers\pydev\pydevd.py", line 1496, in _exec
#     pydev_imports.execfile(file, globals, locals)  # execute the script
#   File "C:\Program Files\JetBrains\PyCharm Community Edition 2023.1\plugins\python-ce\helpers\pydev\_pydev_imps\_pydev_execfile.py", line 18, in execfile
#     exec(compile(contents+"\n", file, 'exec'), glob, loc)
#   File "C:\dev\xiaogpt\xiaogpt\testwindow.py", line 44, in <module>
#     show_window_on_display(1)
#   File "C:\dev\xiaogpt\xiaogpt\testwindow.py", line 39, in show_window_on_display
#     hwnd = create_window(display_index)
#   File "C:\dev\xiaogpt\xiaogpt\testwindow.py", line 23, in create_window
#     hwnd = win32gui.CreateWindow("ClassName", "TitleName", win32con.WS_VISIBLE | win32con.WS_POPUP, x, y, width, height,
# pywintypes.error: (1407, 'CreateWindow', '找不到窗口类。')