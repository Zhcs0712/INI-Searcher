import wx
import Database.EIP_Debug as EIP_Debug
import Infor

class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, style=wx.BORDER_SIMPLE)
        self.SetBackgroundColour("black")

class IEHelpWindow(wx.Frame):
    def __init__(self, AboutWindow, title):
        wx.Frame.__init__(self, AboutWindow, id=1, title='IE查错帮助', size=(420,301))
        self.SetSizeHints(minSize=(420,301), maxSize=(420,301))
        self.SetBackgroundColour("white")
        self.Center()

        self.sash_window = MyPanel(self)
        self.scrolled_window = wx.ScrolledWindow(self, -1)
        self.logBox = wx.StaticText(self.scrolled_window, label=Infor.iehelptext)
        self.scrolled_window.SetScrollbars(20, 60, 0, 20)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.scrolled_window,  0, wx.EXPAND)
        sizer.AddSpacer(200)
        sizer.Add(self.sash_window, 0, wx.EXPAND | wx.BOTTOM, 4)
        self.SetSizer(sizer)

class IEToolWindow(wx.Frame):
    def __init__(self, AboutWindow, title):
        wx.Frame.__init__(self, AboutWindow, id=1, title='IE查错', size=(480,201))
        self.SetSizeHints(minSize=(480,201), maxSize=(480,201))
        self.SetBackgroundColour("white")
        self.Center()

        self.resultBox = wx.TextCtrl(self, pos=(0, 0), size=(430, 110), style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.searchButton = wx.Button(self, label="查询")
        self.inputBox = wx.TextCtrl(self, pos=(0, 0), size=(250, 25), style=wx.TE_PROCESS_ENTER|wx.TE_PROCESS_TAB)
        self.helpButton = wx.Button(self, label="?", size=(25, 25))
        Hfont = wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD)
        self.helpButton.SetFont(Hfont)

        self.inputBox.Bind(wx.EVT_CHAR, self.OnChar)
        self.searchButton.Bind(wx.EVT_BUTTON, self.OnButtonClick)
        self.helpButton.Bind(wx.EVT_BUTTON, self.OnHelpButton)

        sizer = wx.BoxSizer(wx.VERTICAL)
        inputsizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.resultBox, flag=wx.ALIGN_CENTER)
        sizer.AddSpacer(15)
        sizer.Add(inputsizer)
        inputsizer.AddSpacer(17)
        inputsizer.Add(self.inputBox)
        inputsizer.AddSpacer(25)
        inputsizer.Add(self.helpButton)
        inputsizer.AddSpacer(55)
        inputsizer.Add(self.searchButton)
        self.SetSizer(sizer)

    def OnChar(self,event):
        keycode = event.GetKeyCode()
        if keycode >= ord('a') and keycode <= ord('z'):
            self.inputBox.WriteText(chr(keycode-ord('a')+ord('A')))
        elif (keycode == 0 or (keycode >= 32) and (keycode <= 47) or (keycode >= 58) and (keycode <= 64) or (keycode >= 91) and (keycode <= 96) or (keycode >= 123) and (keycode <= 126)):
            event.StopPropagation()
        else:
            event.Skip()

    def OnButtonClick(self, event):
        keyword = self.inputBox.GetValue()
        if keyword in EIP_Debug.EIP:
            self.resultBox.SetValue(EIP_Debug.EIP[keyword])
        else:
                self.resultBox.SetValue("Keyword not found.")

    def OnHelpButton(self, event):
        new_window = IEHelpWindow(self, "")
        new_window.Show()