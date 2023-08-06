import threading
import time
from threading import Thread
from time import sleep

import win32api, win32con, win32gui, win32ui


# test is okc


def getCurrentTime():
    return int(time.time() * 1000)


class ToastUtil:
    """
    传递秒
    """

    def scheduleClosePostMsg(self, showTime: int, hWindow):
        # event = threading.Event()
        # toast.setEvent(event)
        print("name", threading.Thread.name)

        def closeFun(hWindow, showTime: int):
            currentStartTime = getCurrentTime()
            sleep(showTime)
            if currentStartTime >= self.lastUpdateToastTime:
                print("销毁window")
                try:
                    win32gui.PostMessage(hWindow, win32con.WM_CLOSE, 0, 0)
                except Exception as e:
                    print("无法定时关闭消息", e)
                # win32gui.DestroyWindow(self.hWindow)
                # win32api.PostQuitMessage()
            else:
                print("当前toast定时关闭已作废")

        t = Thread(target=closeFun, args=(hWindow, showTime,))
        t.start()
        return t

    def wndProc(self, hWnd, message, wParam, lParam):
        if message == win32con.WM_PAINT:
            hdc, paintStruct = win32gui.BeginPaint(hWnd)

            dpiScale = win32ui.GetDeviceCaps(hdc, win32con.LOGPIXELSX) / 60.0
            win32gui.SetTextColor(hdc, self.fontColor)
            # http://msdn.microsoft.com/en-us/library/windows/desktop/dd145037(v=vs.85).aspx
            lf = win32gui.LOGFONT()
            lf.lfFaceName = "Times New Roman"
            lf.lfHeight = int(round(dpiScale * self.fontsize))
            # lf.lfWeight = 150
            # Use nonantialiased to remove the white edges around the text.
            # lf.lfQuality = win32con.NONANTIALIASED_QUALITY
            hf = win32gui.CreateFontIndirect(lf)
            win32gui.SelectObject(hdc, hf)

            rect = win32gui.GetClientRect(hWnd)



            #------------
            flags = win32con.DT_WORDBREAK | win32con.DT_CENTER | win32con.DT_VCENTER

            # Set the rect to be the size of the window.
            # rect = win32gui.GetClientRect(hwnd)

            # Increase the rect's height to allow for multiple lines.
            # rect_bottom = rect[3] + ((len(text) // 10) * win32gui.GetTextExtentPoint32(hdc, " ")[1])
            # rect = (rect[0], rect[1], rect[2], rect_bottom)

            # Draw the text on the window.
            win32gui.DrawText(hdc,  self.toastText, -1, rect, flags)




            # http://msdn.microsoft.com/en-us/library/windows/desktop/dd162498(v=vs.85).aspx
            # win32gui.DrawText(
            #     hdc,
            #     self.toastText,
            #     -1,
            #     rect,
            #     win32con.DT_WORDBREAK |win32con.DT_CENTER | win32con.DT_NOCLIP | win32con.DT_SINGLELINE | win32con.DT_VCENTER
            # )





            win32gui.EndPaint(hWnd, paintStruct)

            # if message == win32con.WM_PAINT:
            #     hDC, paintStruct = win32gui.BeginPaint(hWnd)
            #
            #     rect = win32gui.GetClientRect(hWnd)
            #     win32gui.DrawText(
            #         hDC,
            #         windowText,
            #         -1,
            #         rect,
            #         win32con.DT_SINGLELINE | win32con.DT_CENTER | win32con.DT_VCENTER)
            #
            #     win32gui.EndPaint(hWnd, paintStruct)
            return 0

        elif message == win32con.WM_DESTROY:
            print('Closing the window.')
            win32gui.PostQuitMessage(0)
            return 0

        else:
            return win32gui.DefWindowProc(hWnd, message, wParam, lParam)

    def setFontSize(self, size: int):
        self.fontsize = size

    def showToastLoop(self, event: threading.Event):
        print("-------")
        # while True:

        #     print(event.)
        #     print("-0---")

    def setFontColor(self, color: int):
        self.fontColor = color

    # 获取所有显示器的大小和位置信息
    def get_display_info1(self):
        display_info = []
        for monitor in win32api.EnumDisplayMonitors():
            monitor_info = win32api.GetMonitorInfo(monitor[0])
            display_info.append(monitor_info["Monitor"])
        return display_info

    def get_display_info(self, display_index=0):
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

    def __init__(self, toastClass: str = "toast"):
        self.toastText = ""
        self.event = None
        self.hWindow = None
        self.fontColor = win32api.RGB(255, 0, 0)
        self.x = 0
        self.y = 0
        self.fontsize = 30
        self.lastUpdateToastTime = 0
        print(win32api.GetSystemMetrics(win32con.SM_CXSCREEN))
        self.width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        self.height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        self.hInstance = win32api.GetModuleHandle()
        # http://msdn.microsoft.com/en-us/library/windows/desktop/ms633576(v=vs.85).aspx
        # win32gui does not support WNDCLASSEX.
        self.wndClass = win32gui.WNDCLASS()
        # http://msdn.microsoft.com/en-us/library/windows/desktop/ff729176(v=vs.85).aspx
        self.wndClass.style = win32con.CS_HREDRAW | win32con.CS_VREDRAW
        self.wndClass.lpfnWndProc = self.wndProc
        self.wndClass.hInstance = self.hInstance
        self.wndClass.hCursor = win32gui.LoadCursor(None, win32con.IDC_ARROW)
        self.wndClass.hbrBackground = win32gui.GetStockObject(win32con.WHITE_BRUSH)
        self.wndClass.lpszClassName = toastClass
        # win32gui does not support RegisterClassEx
        self.wndClassAtom = win32gui.RegisterClass(self.wndClass)
        self.exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT

        self.style = win32con.WS_DISABLED | win32con.WS_POPUP | win32con.WS_VISIBLE

    def setLocationOffsize(self, x: int, y: int):
        self.x = x
        self.y = y

    def showToast(self, toastText: str, showTime: int):
        # print(toastText)
        self.toastText = toastText
        toastText = toastText.replace('\r\n', '\n')
        self.lastUpdateToastTime = getCurrentTime()
        # http://msdn.microsoft.com/en-us/library/windows/desktop/ff700543(v=vs.85).aspx
        # Consider using: WS_EX_COMPOSITED, WS_EX_LAYERED, WS_EX_NOACTIVATE, WS_EX_TOOLWINDOW, WS_EX_TOPMOST, WS_EX_TRANSPARENT
        # The WS_EX_TRANSPARENT flag makes events (like mouse clicks) fall through the window.

        # http://msdn.microsoft.com/en-us/library/windows/desktop/ms632600(v=vs.85).aspx
        # Consider using: WS_DISABLED, WS_POPUP, WS_VISIBLE

        # http://msdn.microsoft.com/en-us/library/windows/desktop/ms632680(v=vs.85).aspx
        if self.hWindow is not None:
            try:
                time.sleep(1.0)
                win32gui.RedrawWindow(self.hWindow, None, None, win32con.RDW_INVALIDATE | win32con.RDW_ERASE)
                # win32gui.PostMessage(tempWindow, win32con.WM_CLOSE, 0, 0)
            except Exception as e:
                print("close msg fail", e)
        else:
            self.hWindow = win32gui.CreateWindowEx(
                self.exStyle,
                self.wndClassAtom,
                None,  # WindowName
                self.style,
                self.x,  # x
                self.y,  # y

                self.width, self.height,
                None,  # hWndParent
                None,  # hMenu
                self.hInstance,
                None  # lpParam
            )

            # win32gui.DestroyWindow(self.hWindow)
            # self.hWindow=None
        # else:
        # win32gui.UpdateWindow(self.hWindow)
        # self.async_all_display()

        if showTime > 0:
            print("showTime:", showTime
                  )
            self.scheduleClosePostMsg(showTime, self.hWindow)  # 否则只有重新设置toast才会更新

        # http://msdn.microsoft.com/en-us/library/windows/desktop/ms633540(v=vs.85).aspx
        win32gui.SetLayeredWindowAttributes(self.hWindow, 0x00ffffff, 255,
                                            win32con.LWA_COLORKEY | win32con.LWA_ALPHA)

        # http://msdn.microsoft.com/en-us/library/windows/desktop/dd145167(v=vs.85).aspx
        # win32gui.UpdateWindow(hWindow)
        # 所有显示器显示
        # self.async_all_display()
        self.async_display()


        # http://msdn.microsoft.com/en-us/library/windows/desktop/ms633548(v=vs.85).aspx
        # win32gui.ShowWindow(hWindow, win32con.SW_SHOW)
        # print("显示" + self.toastText)
        win32gui.PumpMessages()
        # print("隐藏" + self.toastText)

    def setGravity(self, gravity):
        self.gravity=gravity
        if gravity == 1:
            self.width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
            self.height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
            self.x = 0
            self.y = 0
        pass

    def setWindowSize(self, width: int, height: int):
        self.width = width
        self.height = height

    def updateToast(self, toastText):
        print("start")
        # toast.showToast(toastText)
        sleep(2)
        self.showToast(toastText + "ffff")
        hWindow = win32gui.CreateWindowEx(
            self.exStyle,
            self.wndClassAtom,
            None,  # WindowName
            self.style,
            self.x,  # x
            self.y,  # y
            self.width, self.height,
            None,  # hWndParent
            None,  # hMenu
            self.hInstance,
            None  # lpParam
        )

        # http://msdn.microsoft.com/en-us/library/windows/desktop/ms633540(v=vs.85).aspx
        win32gui.SetLayeredWindowAttributes(hWindow, 0x00ffffff, 255, win32con.LWA_COLORKEY | win32con.LWA_ALPHA)
        # http://msdn.microsoft.com/en-us/library/windows/desktop/dd145167(v=vs.85).aspx
        win32gui.UpdateWindow(hWindow)
        print("end")

    def setEvent(self, event):
        self.event = event

    def showToastInMain(self, toastText: str, showTime: int):
        t = Thread(target=self.showToast, args=(toastText, showTime))
        t.start()

    def showToastSimple(self, text):
        self.showToastInMain(toastText=text, showTime=3)

    def showToastForever(self, text):
        self.showToastInMain(toastText=text, showTime=0)
        pass

    # 设置窗口位置和大小
    def set_window_pos(self, display_rect):
        x, y, width, height = display_rect
        win32gui.SetWindowPos(self.hWindow, win32con.HWND_TOPMOST, x, y, width, height, 0)

    def async_all_display(self):
        display_info = self.get_display_info(1)
        # 设置窗口位置和大小以适应所有显示器
        for display_rect in display_info:
            x, y, width, height = display_rect
            # win32gui.SetWindowPos(self.hWindow, win32con.HWND_TOPMOST, x, y, width, height,
            #                       win32con.SWP_NOACTIVATE | win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW)

            win32gui.SetWindowPos(self.hWindow, win32con.HWND_TOPMOST, x, y, width, height, 0)
            # win32gui.SetWindowPos(self.hWindow, win32con.HWND_TOPMOST, x, y, width, height,  None, None,None,None)
            # self.set_window_pos(display_rect)
            #                       win32con.SWP_NOACTIVATE | win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW
        pass

    def async_display(self):
        win32gui.SetWindowPos(self.hWindow, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                              win32con.SWP_NOACTIVATE | win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW)


def showToast(toastText):
    print(toastText)


if __name__ == '__main__':
    toast = ToastUtil()
    toast.setFontSize(30)
    toast.setGravity(1)
    toast.setWindowSize(200, 200)
    toast.setLocationOffsize(0, 0)
    toast.showToastForever("你好")
    # toast.showToastInMain("我好", 5)
    # toast.updateToast("----")
    # toast.showToastInMain("大家好", 5)
    sleep(3)
    toast.showToastForever("我好")
    sleep(3)
    toast.showToastForever("大家好")
    print("---end")
    sleep(3)
    toast.showToastInMain("才是真的好", 5)
    # toast.update
    # t.setName("")
    # e.set()  # 取消阻塞
