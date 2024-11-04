# src/gui/main_menu.py
import wx


class MainMenu(wx.Frame):
    def __init__(self, *args, **kw):
        super(MainMenu, self).__init__(*args, **kw)

        panel = wx.Panel(self)
        panel.SetFocus()

        title = wx.StaticText(panel, label="Menu Principal", pos=(100, 10))

        button_calculator = wx.Button(panel, label="Iniciar Calculadora", pos=(50, 50), size=(200, 40))
        button_converter = wx.Button(panel, label="Conversor de Tempo", pos=(50, 100), size=(200, 40))
        button_exit = wx.Button(panel, label="Sair", pos=(50, 150), size=(200, 40))

        self.buttons = [button_calculator, button_converter, button_exit]
        self.selected_index = 0

        button_calculator.Bind(wx.EVT_BUTTON, self.on_calculator_click)
        button_converter.Bind(wx.EVT_BUTTON, self.on_converter_click)
        button_exit.Bind(wx.EVT_BUTTON, self.on_exit_click)

        panel.Bind(wx.EVT_KEY_DOWN, self.on_key_press)

        self.update_selection()

    def update_selection(self):
        for i, button in enumerate(self.buttons):
            if i == self.selected_index:
                button.SetBackgroundColour("light blue")
            else:
                button.SetBackgroundColour(wx.NullColour)

    def on_key_press(self, event):
        key_code = event.GetKeyCode()

        if key_code == wx.WXK_UP:
            self.selected_index = (self.selected_index - 1) % len(self.buttons)
            self.update_selection()
        elif key_code == wx.WXK_DOWN:
            self.selected_index = (self.selected_index + 1) % len(self.buttons)
            self.update_selection()
        elif key_code == wx.WXK_RETURN or key_code == wx.WXK_NUMPAD_ENTER:
            self.buttons[self.selected_index].Command(
                wx.CommandEvent(wx.wxEVT_COMMAND_BUTTON_CLICKED, self.buttons[self.selected_index].GetId()))

    def on_calculator_click(self, event):
        print("Calculadora iniciada")

    def on_converter_click(self, event):
        print("Conversor de Tempo iniciado")

    def on_exit_click(self, event):
        self.Close()
