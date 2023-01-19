import wx
import re
import wx.adv
import webbrowser
import Infor
import Database.RA2_Entries as RA2_Entries
import Database.EIP_Debug as EIP_Debug
import Database.XTypes as XTypes
import Win.Wins as Wins
import Win.Wins_Tool as Wins_Tool

class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, style=wx.BORDER_SIMPLE)
        self.SetBackgroundColour("black")

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
        closeItem = settingmenu.Append(wx.ID_EXIT, "&退出\tCtrl+Q", "")
        self.Bind(wx.EVT_MENU, self.OnClose, closeItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
        settingItem.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_LIST_VIEW))
        aboutItem.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_HELP_PAGE))
        closeItem.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_CLOSE))

        labelmenu = wx.Menu()
        rulesItem = labelmenu.Append(101, "rules标签")
        artItem = labelmenu.Append(102, "art标签")
        soundItem = labelmenu.Append(103, "sound标签")
        uiItem = labelmenu.Append(104, "ui标签")
        aiItem = labelmenu.Append(105, "ai标签")
        labelmenu.AppendSeparator()
        mapItem = labelmenu.Append(106, "map标签")
        snowItem = labelmenu.Append(107, "snow标签")
        movieItem = labelmenu.Append(108, "movie标签")
        battleItem = labelmenu.Append(109, "battle标签")
        missionItem = labelmenu.Append(110, "mission标签")
        ra2Item = labelmenu.Append(111, "ra2标签")
        rgbItem = labelmenu.Append(112, "rgb标签")
        self.Bind(wx.EVT_MENU, self.OnHelp_RulesLs, rulesItem)
        self.Bind(wx.EVT_MENU, self.OnHelp_ArtLs, artItem)
        self.Bind(wx.EVT_MENU, self.OnHelp_SoundLs, soundItem)
        self.Bind(wx.EVT_MENU, self.OnHelp_UiLs, uiItem)
        self.Bind(wx.EVT_MENU, self.OnHelp_AiLs, aiItem)
        self.Bind(wx.EVT_MENU, self.OnHelp_MapLs, mapItem)
        self.Bind(wx.EVT_MENU, self.OnHelp_SnowLs, snowItem)
        self.Bind(wx.EVT_MENU, self.OnHelp_MovieLs, movieItem)
        self.Bind(wx.EVT_MENU, self.OnHelp_BattleLs, battleItem)
        self.Bind(wx.EVT_MENU, self.OnHelp_MissionLs, missionItem)
        self.Bind(wx.EVT_MENU, self.OnHelp_Ra2Ls, ra2Item)
        self.Bind(wx.EVT_MENU, self.OnHelp_RgbLs, rgbItem)
        soundItem.Enable(False)
        aiItem.Enable(False)
        snowItem.Enable(False)

        helpmenu = wx.Menu()
        helpLabelItem = helpmenu.AppendSubMenu(labelmenu, "标签说明")
        helpmenu.AppendSeparator()
        helpEngineItem = helpmenu.Append(wx.ID_HELP_CONTEXT, "平台说明", "")
        helpmenu.AppendSeparator()
        helpINIItem = helpmenu.Append(wx.ID_HELP_COMMANDS, "INI说明", "")
        self.Bind(wx.EVT_MENU, self.OnHelp_Engine, helpEngineItem)
        self.Bind(wx.EVT_MENU, self.OnHelp_INI, helpINIItem)
        helpLabelItem.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_TICK_MARK))
        helpEngineItem.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_TICK_MARK))
        helpINIItem.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_TICK_MARK))

        toolmenu = wx.Menu()
        IEtoolItem = toolmenu.Append(200, "IE查错", "")
        self.Bind(wx.EVT_MENU, self.OnTool_IE, IEtoolItem)
        IEtoolItem.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_HELP_SIDE_PANEL))

        self.searchComboBox = wx.ComboBox(self, pos=(0, 0), size=(300, 25), style=wx.CB_DROPDOWN)
        self.filtrateChoice = wx.Choice(self, -1, size=(300, 25))
        self.resultBox = wx.TextCtrl(self, pos=(0, 0), size=(450, 185), style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.filtrateCheckbox = wx.CheckBox(self, -1, "筛选")
        self.searchButton = wx.Button(self, label="查询")
        self.helpButton = wx.Button(self, label="?", size=(25, 25))
        Hfont = wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD)
        self.helpButton.SetFont(Hfont)

        typechoices = ['','[General]','[Side]','[AI]','[Other]','[TechnoType]','[SuperWeapon]','[BuildingType]','[InfantryType]','[VehicleType]','[AircraftType]','[WeaponType]','[Projectile]','[Warhead]','[Animation]']
        self.TypesChoice = wx.Choice(self, -1, choices=typechoices,size=(145,25))
        enginechoices = ['','Original','Ares','Phobos']
        self.EnginesChoice = wx.Choice(self, -1, choices=enginechoices,size=(105,25))
        inifilechoices = ['','rules','art','sound','ai','ui']
        self.INIFilesChoice = wx.Choice(self, -1, choices=inifilechoices,size=(105,25))

        self.TypesChoice.Disable()
        self.EnginesChoice.Disable()
        self.INIFilesChoice.Disable()
        self.filtrateChoice.Disable()

        self.searchButton.Bind(wx.EVT_BUTTON, self.OnButtonClick)
        self.helpButton.Bind(wx.EVT_BUTTON, self.OnHelpButton)
        self.searchComboBox.Bind(wx.EVT_TEXT_ENTER, self.OnButtonClick)
        self.searchComboBox.Bind(wx.EVT_COMBOBOX, self.OnButtonClick)
        self.Bind(wx.EVT_CHECKBOX, self.OnCheckBox, self.filtrateCheckbox)
        self.filtrateChoice.Bind(wx.EVT_CHOICE, self.OnFiltrateChoice)
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
        inputFsizer.Add(self.filtrateChoice, flag=wx.ALIGN_CENTER)
        inputFsizer.AddSpacer(130)
        inputFsizer.Add(self.helpButton, flag=wx.ALIGN_CENTER)
        self.SetSizer(sizer)

        menuBar = wx.MenuBar()
        menuBar.Append(settingmenu,"关于")
        menuBar.Append(helpmenu,"帮助")
        menuBar.Append(toolmenu,"工具")
        menuBar.Enable(wx.ID_SETUP, False)
        self.SetMenuBar(menuBar)

    def OnClose(self, event):
        self.Close()

    def OnAbout(self, event):
        new_window = Wins.AboutWindow(self, "")
        new_window.Show()

    def OnHelpButton(self, event):
        new_window = Wins.HelpWindow(self, "")
        new_window.Show()

    def OnHelp_RulesLs(self, event):
        new_window = Wins.RulesLsWindow(self, "")
        new_window.Show()

    def OnHelp_ArtLs(self, event):
        new_window = Wins.ArtLsWindow(self, "")
        new_window.Show()

    def OnHelp_SoundLs(self, event):
        new_window = Wins.SoundLsWindow(self, "")
        new_window.Show()

    def OnHelp_UiLs(self, event):
        new_window = Wins.UiLsWindow(self, "")
        new_window.Show()

    def OnHelp_AiLs(self, event):
        new_window = Wins.AiLsWindow(self, "")
        new_window.Show()

    def OnHelp_MapLs(self, event):
        new_window = Wins.MapLsWindow(self, "")
        new_window.Show()

    def OnHelp_SnowLs(self, event):
        new_window = Wins.SnowLsWindow(self, "")
        new_window.Show()

    def OnHelp_MovieLs(self, event):
        new_window = Wins.MovieLsWindow(self, "")
        new_window.Show()

    def OnHelp_BattleLs(self, event):
        new_window = Wins.BattleLsWindow(self, "")
        new_window.Show()

    def OnHelp_MissionLs(self, event):
        new_window = Wins.MissionLsWindow(self, "")
        new_window.Show()

    def OnHelp_Ra2Ls(self, event):
        new_window = Wins.Ra2LsWindow(self, "")
        new_window.Show()

    def OnHelp_RgbLs(self, event):
        new_window = Wins.RgbLsWindow(self, "")
        new_window.Show()

    def OnHelp_Engine(self, event):
        new_window = Wins.EnginesWindow(self, "")
        new_window.Show()

    def OnHelp_INI(self, event):
        new_window = Wins.INIFilesWindow(self, "")
        new_window.Show()

    def OnTool_IE(self, event):
        new_window = Wins_Tool.IEToolWindow(self, "")
        new_window.Show()

    def OnCheckBox(self, event):
        if self.filtrateCheckbox.GetValue():
            self.searchButton.Bind(wx.EVT_BUTTON, self.OnButtonFiltrate)
            self.searchComboBox.Bind(wx.EVT_TEXT_ENTER, self.OnButtonFiltrate)
            # self.TypesChoice.Enable()
            # self.EnginesChoice.Enable()
            # self.INIFilesChoice.Enable()
            self.filtrateChoice.Enable()
        else:
            self.searchButton.Bind(wx.EVT_BUTTON, self.OnButtonClick)
            self.searchComboBox.Bind(wx.EVT_TEXT_ENTER, self.OnButtonClick)
            self.TypesChoice.Disable()
            self.EnginesChoice.Disable()
            self.INIFilesChoice.Disable()
            self.filtrateChoice.Disable()

    def OnButtonClick(self, event):
        keyword = self.searchComboBox.GetValue().lower()
        if "=" in keyword:
            equal_sign_index = keyword.find("=")
            keyword = keyword[:equal_sign_index]
        if keyword[:7] == "versus.":
            self.resultBox.SetValue(XTypes.ArmorEntries(keyword))
        elif keyword[:17] == "weaponturretindex":
            self.resultBox.SetValue(XTypes.TurretIndexEntries(keyword))
        elif keyword[:12] == "weaponuiname":
            self.resultBox.SetValue(XTypes.WeaponNameEntries(keyword))
        elif keyword[:17] == "prerequisite.list":
            self.resultBox.SetValue(XTypes.PrerequisiteEntries(keyword))
        elif keyword[:13] == "survivor.side":
            self.resultBox.SetValue(XTypes.SurvivoreEntries(keyword))
        elif keyword[:8] == "campaign":
            if len(keyword) >= 10:
                if keyword[9] == '.':
                    self.resultBox.SetValue(XTypes.CampaignEntries(keyword))
                else:
                    self.resultBox.SetValue("Keyword not found.")
            elif len(keyword) == 9:
                self.resultBox.SetValue(XTypes.CampaignEntries(keyword))
            else:
                self.resultBox.SetValue("Keyword not found.")
        elif keyword[:4] == "slot":
            self.resultBox.SetValue(XTypes.SlotEntries(keyword))
        elif keyword[:6] == "color." and keyword.count('.') == 2:
            self.resultBox.SetValue(XTypes.ColorEntries(keyword))
        elif keyword[:20] == "engineerdamagecursor":
            self.resultBox.SetValue(XTypes.MECursorEntries(keyword))
        elif keyword[:10] == "lasertrail" and keyword[11] == '.':
            self.resultBox.SetValue(XTypes.LasertrailEntries(keyword))
        elif "flh.burst" in keyword and keyword.count('.') == 1:
            self.resultBox.SetValue(XTypes.BurstFLHEntries(keyword))
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
        self.filtrateChoice.Clear()
        search_value = self.searchComboBox.GetValue()
        search_value = search_value.strip()
        search_value = re.sub(r"\s+", " ", search_value)
        space_count = len(re.findall(r'\s+', search_value))
        filtrate_result = []
        if search_value == "":
            self.resultBox.SetValue("")
        else:
            if space_count == 0:
                for key, values in RA2_Entries.entries.items():
                    if search_value in values[1]:
                        filtrate_result.append(RA2_Entries.entries[key][0])
                if len(filtrate_result) > 10:
                    self.resultBox.SetValue("符合筛选的词条超过了10个，请重新输入关键词\n你可以尝试输入多个关键词，关键词之间以空格隔开")
                else:
                    self.filtrateChoice.AppendItems(filtrate_result)
                    if len(filtrate_result) > 0:
                        self.filtrateChoice.SetSelection(0)
                        initialkeyword = filtrate_result[0].lower()
                        if initialkeyword in RA2_Entries.entries:
                            self.resultBox.SetValue(RA2_Entries.entries[initialkeyword][1])
                        else:
                            self.resultBox.SetValue("出错！可能是因为词条库未整合完成\n请关闭筛选手动搜索该词条")
                    else:
                        self.resultBox.SetValue("未搜索到符合筛选条件的词条")
            else:
                keywordNums = space_count + 1
                keywords = re.split(r'\s+', search_value)
                fresult = [[] for _ in range(keywordNums)]
                num = -1
                for fkeyword in keywords:
                    num = num + 1
                    for key, values in RA2_Entries.entries.items():
                        if fkeyword in values[1]:
                            fresult[num].append(RA2_Entries.entries[key][0])
                filtrate_result = list(set.intersection(*map(set, fresult)))
                if len(filtrate_result) > 10:
                    self.resultBox.SetValue("符合筛选的词条超过了10个，请重新输入关键词")
                else:
                    self.filtrateChoice.AppendItems(filtrate_result)
                    if len(filtrate_result) > 0:
                        self.filtrateChoice.SetSelection(0)
                        initialkeyword = filtrate_result[0].lower()
                        if initialkeyword in RA2_Entries.entries:
                            self.resultBox.SetValue(RA2_Entries.entries[initialkeyword][1])
                        else:
                            self.resultBox.SetValue("出错！可能是因为词条库未整合完成\n请关闭筛选手动搜索该词条")
                    else:
                        self.resultBox.SetValue("未搜索到符合筛选条件的词条\n你可以尝试减少关键词数量")

    def OnFiltrateChoice(self, event):
        filtratekeyword = event.GetString().lower()
        if filtratekeyword in RA2_Entries.entries:
            self.resultBox.SetValue(RA2_Entries.entries[filtratekeyword][1])
        else:
            self.resultBox.SetValue("出错！可能是因为词条库未整合完成\n请关闭筛选手动搜索该词条")

app = wx.App()
frame = MainFrame()
frame.Show()
app.MainLoop()
# pyInstaller 安装命令
# pyinstaller --onefile --version-file version.txt --noconsole --icon=fishico.ico --add-binary "Win/*;Win" --add-binary "Database/*;Database" --add-data "Infor.py;." __init__.py