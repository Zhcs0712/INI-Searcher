import wx
import RA2_Entries
import XTypes
import Infor
import Wins

class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, style=wx.BORDER_SIMPLE)
        self.SetBackgroundColour("black")

class AboutWindow(wx.Frame):
    def __init__(self, MainFrame, title):
        wx.Frame.__init__(self, MainFrame, id=1, title='关于', size=(400,241))
        self.SetSizeHints(minSize=(400,241), maxSize=(400,241))
        self.SetBackgroundColour("white")
        self.Center()

        self.sash_window = MyPanel(self)
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

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.AddSpacer(200)
        sizer.Add(self.sash_window, 0, wx.EXPAND | wx.BOTTOM, 4)
        self.SetSizer(sizer)

    def OnUpdateLog(self, event):
        new_window = UpdateLogWindow(self, "")
        new_window.Show()

class UpdateLogWindow(wx.Frame):
    def __init__(self, AboutWindow, title):
        wx.Frame.__init__(self, AboutWindow, id=1, title='更新日志', size=(400,301))
        self.SetSizeHints(minSize=(400,301), maxSize=(400,301))
        self.SetBackgroundColour("white")
        self.Center()

        self.sash_window = MyPanel(self)
        self.scrolled_window = wx.ScrolledWindow(self, -1)
        self.logBox = wx.StaticText(self.scrolled_window, label=Infor.updatelog)
        self.scrolled_window.SetScrollbars(20, 20, 0, 50)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.scrolled_window,  0, wx.EXPAND)
        sizer.AddSpacer(200)
        sizer.Add(self.sash_window, 0, wx.EXPAND | wx.BOTTOM, 4)
        self.SetSizer(sizer)

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, id=0, title='INI查询', size=(500,405))
        self.SetSizeHints(minSize=(500, 405), maxSize=(500, 405))
        self.SetBackgroundColour("white")
        self.Center()

        self.sash_window = MyPanel(self)
        settingmenu = wx.Menu()
        settingItem = settingmenu.Append(wx.ID_SETUP, "设置", "")
        settingmenu.AppendSeparator()
        aboutItem = settingmenu.Append(wx.ID_ABOUT, "关于" , "")
        settingmenu.AppendSeparator()
        closeItem = settingmenu.Append(wx.ID_EXIT, "退出", "")
        self.Bind(wx.EVT_MENU, self.OnClose, closeItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
        settingItem.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_LIST_VIEW))
        aboutItem.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_HELP_PAGE))
        closeItem.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_CLOSE))

        helpmenu = wx.Menu()
        helpLabelItem = helpmenu.Append(wx.ID_HELP_INDEX, "标签说明", "")
        helpmenu.AppendSeparator()
        helpEngineItem = helpmenu.Append(wx.ID_HELP_CONTEXT, "平台说明", "")
        helpmenu.AppendSeparator()
        helpINIItem = helpmenu.Append(wx.ID_HELP_COMMANDS, "INI说明", "")
        self.Bind(wx.EVT_MENU, self.OnHelp_Label, helpLabelItem)
        self.Bind(wx.EVT_MENU, self.OnHelp_Engine, helpEngineItem)
        self.Bind(wx.EVT_MENU, self.OnHelp_INI, helpINIItem)
        helpLabelItem.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_TICK_MARK))
        helpEngineItem.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_TICK_MARK))
        helpINIItem.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_TICK_MARK))

        self.searchComboBox = wx.ComboBox(self, pos=(0, 0), size=(300, 25), style=wx.CB_DROPDOWN)
        self.filtrateComboBox = wx.ComboBox(self, pos=(0, 0), size=(300, 25), style=wx.CB_DROPDOWN)
        self.resultBox = wx.TextCtrl(self, pos=(0, 0), size=(450, 185), style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.filtrateCheckbox = wx.CheckBox(self, -1, "筛选")
        self.searchButton = wx.Button(self, label="查询")

        typechoices = ['[General]','[Side]','[AI]','[Other]','[TechnoType]','[SuperWeapon]','[BuildingType]','[InfantryType]','[VehicleType]','[AircraftType]','[WeaponType]','[Projectile]','[Warhead]','[Animation]']
        self.TypesChoice = wx.Choice(self, -1, choices=typechoices,size=(145,25))
        enginechoices = ['Original','Ares','Phobos']
        self.EnginesChoice = wx.Choice(self, -1, choices=enginechoices,size=(105,25))
        inifilechoices = ['rules','art','sound','ai','ui']
        self.INIFilesChoice = wx.Choice(self, -1, choices=inifilechoices,size=(105,25))

        self.TypesChoice.Disable()
        self.EnginesChoice.Disable()
        self.INIFilesChoice.Disable()
        self.filtrateComboBox.Disable()

        self.searchButton.Bind(wx.EVT_BUTTON, self.OnButtonClick)
        self.searchComboBox.Bind(wx.EVT_TEXT_ENTER, self.OnButtonClick)
        self.searchComboBox.Bind(wx.EVT_COMBOBOX, self.OnButtonClick)
        self.Bind(wx.EVT_CHECKBOX, self.OnCheckBox, self.filtrateCheckbox)
        sizer = wx.BoxSizer(wx.VERTICAL)
        inputsizer = wx.BoxSizer(wx.HORIZONTAL)
        choicesizer = wx.BoxSizer(wx.HORIZONTAL)
        inputFsizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.AddSpacer(10)
        sizer.Add(self.resultBox, flag=wx.ALIGN_CENTER)
        sizer.AddSpacer(20)
        sizer.Add(inputsizer, flag=wx.ALIGN_CENTER)
        sizer.AddSpacer(20)
        sizer.Add(choicesizer, flag=wx.ALIGN_CENTER)
        sizer.AddSpacer(20)
        sizer.Add(inputFsizer)
        sizer.AddSpacer(15)
        sizer.Add(self.sash_window, 0, wx.EXPAND | wx.BOTTOM, 4)
        inputsizer.Add(self.searchComboBox)
        inputsizer.AddSpacer(20)
        inputsizer.Add(self.filtrateCheckbox, flag=wx.ALIGN_CENTER)
        inputsizer.AddSpacer(10)
        inputsizer.Add(self.searchButton)
        choicesizer.Add(self.TypesChoice, flag=wx.ALIGN_CENTER)
        choicesizer.AddSpacer(50)
        choicesizer.Add(self.EnginesChoice, flag=wx.ALIGN_CENTER)
        choicesizer.AddSpacer(50)
        choicesizer.Add(self.INIFilesChoice, flag=wx.ALIGN_CENTER)
        inputFsizer.AddSpacer(15)
        inputFsizer.Add(self.filtrateComboBox, flag=wx.ALIGN_CENTER)
        self.SetSizer(sizer)

        menuBar = wx.MenuBar()
        menuBar.Append(settingmenu,"关于")
        menuBar.Append(helpmenu,"帮助")
        menuBar.Enable(wx.ID_SETUP, False)
        self.SetMenuBar(menuBar)

    def OnClose(self, event):
        self.Close()

    def OnAbout(self, event):
        new_window = AboutWindow(self, "")
        new_window.Show()

    def OnHelp_Label(self, event):
        new_window = Wins.LabelsWindow(self, "")
        new_window.Show()

    def OnHelp_Engine(self, event):
        new_window = Wins.EnginesWindow(self, "")
        new_window.Show()

    def OnHelp_INI(self, event):
        new_window = Wins.INIFilesWindow(self, "")
        new_window.Show()

    def OnCheckBox(self, event):
        if self.filtrateCheckbox.GetValue():
            self.searchButton.Bind(wx.EVT_BUTTON, self.OnButtonFiltrate)
            self.searchComboBox.Bind(wx.EVT_TEXT_ENTER, self.OnButtonFiltrate)
            self.TypesChoice.Enable()
            self.EnginesChoice.Enable()
            self.INIFilesChoice.Enable()
            self.filtrateComboBox.Enable()
        else:
            self.searchButton.Bind(wx.EVT_BUTTON, self.OnButtonClick)
            self.searchComboBox.Bind(wx.EVT_TEXT_ENTER, self.OnButtonClick)
            self.TypesChoice.Disable()
            self.EnginesChoice.Disable()
            self.INIFilesChoice.Disable()
            self.filtrateComboBox.Disable()

    def OnButtonClick(self, event):
        keyword = self.searchComboBox.GetValue().lower()
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
        for i in range(self.searchComboBox.GetCount()):
            if self.searchComboBox.GetString(i) == keyword:
                self.searchComboBox.Delete(i)
                break
        if self.searchComboBox.GetCount() >= MAX_HISTORY:
            self.searchComboBox.Delete(4)
        self.searchComboBox.Insert(keyword, 0)

    def OnButtonFiltrate(self, event):
        self.resultBox.SetValue("该功能暂不可用，请关闭筛选")

app = wx.App()
frame = MainFrame()
frame.Show()
app.MainLoop()
# pyinstaller --onefile --version-file version.txt --noconsole --icon=fishico.ico --add-data "XTypes.py;." --add-data "Wins.py;." --add-data "RA2_Entries.py;." --add-data "Infor.py;." __init__.py