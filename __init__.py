import wx
import RA2_Entries
import XTypes
import Infor

class AboutWindow(wx.Frame):
    def __init__(self, MainFrame, title):
        wx.Frame.__init__(self, MainFrame, id=1, title='关于', size=(400,250))
        self.SetSizeHints(minSize=(400,250), maxSize=(400,250))
        self.SetBackgroundColour("white")
        self.Center()

        self.aboutText1 = wx.StaticText(self, label=Infor.aboutinfor1)
        self.update_text = wx.StaticText(self, label="更新日志")
        self.aboutText2 = wx.StaticText(self, label=Infor.aboutinfor2)
        udfont = self.update_text.GetFont()
        udfont = udfont.Underlined()
        self.update_text.SetFont(udfont)
        self.update_text.Bind(wx.EVT_LEFT_DOWN, self.OnUpdateLog)
        self.aboutText1.SetPosition((10, 5))
        self.aboutText2.SetPosition((10, 110))
        self.update_text.SetPosition((10, 80))

        handcursor = wx.Cursor(wx.CURSOR_HAND)
        self.update_text.SetCursor(handcursor)

    def OnUpdateLog(self, event):
        new_window = UpdateLogWindow(self, "新窗口")
        new_window.Show()

class UpdateLogWindow(wx.Frame):
    def __init__(self, AboutWindow, title):
        wx.Frame.__init__(self, AboutWindow, id=1, title='更新日志', size=(400,300))
        self.SetSizeHints(minSize=(400,300), maxSize=(400,300))
        self.SetBackgroundColour("white")
        self.Center()

        self.scrolled_window = wx.ScrolledWindow(self, -1)
        self.logBox = wx.StaticText(self.scrolled_window, label=Infor.updatelog)

        self.scrolled_window.SetScrollbars(20, 20, 0, 50)



class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, id=0, title='INI查询', size=(500,310))
        self.SetSizeHints(minSize=(500, 310), maxSize=(500, 310))
        self.SetBackgroundColour("white")
        self.Center()

        settingmenu = wx.Menu()
        settingItem = settingmenu.Append(wx.ID_SETUP, "设置", "")
        settingmenu.AppendSeparator()
        aboutItem =settingmenu.Append(wx.ID_ABOUT, "关于" , "")
        settingmenu.AppendSeparator()
        closeItem = settingmenu.Append(wx.ID_EXIT, "退出", "")
        self.Bind(wx.EVT_MENU, self.OnClose, closeItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
        settingItem.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_LIST_VIEW))
        aboutItem.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_HELP_PAGE))
        closeItem.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_CLOSE))

        self.comboBox = wx.ComboBox(self, pos=(0, 0), size=(300, 25), style=wx.CB_DROPDOWN)
        self.resultBox = wx.TextCtrl(self, pos=(0, 0), size=(450, 185), style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.button = wx.Button(self, label="查询")
        self.button.Bind(wx.EVT_BUTTON, self.OnButtonClick)
        self.comboBox.Bind(wx.EVT_TEXT_ENTER, self.OnButtonClick)
        sizer = wx.BoxSizer(wx.VERTICAL)
        inputsizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.AddSpacer(10)
        sizer.Add(self.resultBox, flag=wx.ALIGN_CENTER)
        sizer.AddSpacer(20)
        sizer.Add(inputsizer, flag=wx.ALIGN_CENTER)
        inputsizer.Add(self.comboBox)
        inputsizer.AddSpacer(75)
        inputsizer.Add(self.button)
        self.SetSizer(sizer)

        menuBar = wx.MenuBar()
        menuBar.Append(settingmenu,"关于")
        menuBar.Enable(wx.ID_SETUP, False)
        self.SetMenuBar(menuBar)

        self.comboBox.Bind(wx.EVT_COMBOBOX, self.OnButtonClick)

    def OnClose(self, event):
        self.Close()

    def OnAbout(self, event):
        new_window = AboutWindow(self, "新窗口")
        new_window.Show()

    def OnButtonClick(self, event):
        keyword = self.comboBox.GetValue().lower()
        if "=" in keyword:
            equal_sign_index = keyword.find("=")
            keyword = keyword[:equal_sign_index]
        if keyword[:7] == "versus.":
            self.resultBox.SetValue(XTypes.ArmorEntries(keyword))
        else:
            if keyword in RA2_Entries.entries:
                self.resultBox.SetValue(RA2_Entries.entries[keyword][1])
            else:
                self.resultBox.SetValue("Keyword not found.")
        MAX_HISTORY = 5
        for i in range(self.comboBox.GetCount()):
            if self.comboBox.GetString(i) == keyword:
                self.comboBox.Delete(i)
                break
        if self.comboBox.GetCount() >= MAX_HISTORY:
            self.comboBox.Delete(4)
        self.comboBox.Insert(keyword, 0)

app = wx.App()
frame = MainFrame()
frame.Show()
app.MainLoop()
# pyinstaller --onefile --version-file version.txt --noconsole --icon=fishico.ico --add-data "XTypes.py;." --add-data "RA2_Entries.py;." --add-data "Infor.py;." __init__.py