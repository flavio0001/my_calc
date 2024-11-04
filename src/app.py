import wx
from src.gui.main_menu import MainMenu


def run_app():
    app = wx.App(False)
    frame = MainMenu(None, title="Write Calc", size=(400, 300))
    frame.Show(True)
    app.MainLoop()