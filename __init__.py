import wx
import MO3

class AboutWindow(wx.Frame):
    def __init__(self, MainFrame, title):
        wx.Frame.__init__(self, MainFrame, id=1, title='关于', size=(400,250))
        self.SetSizeHints(minSize=(400,250), maxSize=(400,250))
        self.SetBackgroundColour("white")
        self.Center()

        self.aboutText = wx.StaticText(self, label="    兴趣使然用以练手写出来的，开源\n    完全没有任何技术含量，只是整合工作非常麻烦\n    在此对各大词典和说明书的编篡者和译者表示感谢\n    难免会有疏漏或错误，欢迎补充指正\n\n    V1.0\n    目前整合了大部分能用到的语句(1500条)\n    主要用来翻译词条语句\n    预计在后续版本中补全局变量和Phobos平台\n    以及加入新的可查询项     "+"\n\n    纠错补充或者有什么建议,欢迎联系我(溺水的鱼,QQ:1310623999)")

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
        # self.textCtrl = wx.TextCtrl(self, pos=(0, 0), size=(300, 25), style=wx.TE_PROCESS_ENTER)
        self.textCtrl2 = wx.TextCtrl(self, pos=(0, 0), size=(450, 185), style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.button = wx.Button(self, label="查询")
        self.button.Bind(wx.EVT_BUTTON, self.OnButtonClick)
        self.comboBox.Bind(wx.EVT_TEXT_ENTER, self.OnButtonClick)
        sizer = wx.BoxSizer(wx.VERTICAL)
        inputsizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.AddSpacer(10)
        sizer.Add(self.textCtrl2, flag=wx.ALIGN_CENTER)
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
            if keyword[-10:] == ".forcefire" and keyword != "versus.forcefire":
                parts = keyword.split(".",2)
                armorparts = parts[1]
                self.textCtrl2.SetValue("是否可以对"+armorparts+"护甲强行攻击")
            elif keyword[-10:] == ".retaliate" and keyword != "versus.retaliate":
                parts = keyword.split(".",2)
                armorparts = parts[1]
                self.textCtrl2.SetValue("是否可以对"+armorparts+"护甲反击")
            elif keyword[-15:] == ".passiveacquire" and keyword != "versus.passiveacquire":
                parts = keyword.split(".",2)
                armorparts = parts[1]
                self.textCtrl2.SetValue("是否可以对"+armorparts+"护甲主动攻击")
            elif keyword.count('.') == 1:
                parts = keyword.split(".",1)
                armorparts = parts[1]
                self.textCtrl2.SetValue("该弹头对"+armorparts+"护甲的伤害百分比")
            else:
                self.textCtrl2.SetValue("Keyword not found.")
        else:
            if keyword in MO3.data:
                self.textCtrl2.SetValue(MO3.data[keyword])
            else:
                self.textCtrl2.SetValue("Keyword not found.")
        MAX_HISTORY = 5
        # search_term = self.comboBox.GetValue()
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
# pyinstaller --onefile --version-file version.txt --noconsole --icon=fishico.ico --add-data "MO3.py;." __init__.py