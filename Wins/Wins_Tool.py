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

class MO_BHelpWindow(wx.Frame):
    def __init__(self, AboutWindow, title):
        wx.Frame.__init__(self, AboutWindow, id=1, title='战役对照帮助', size=(420,161))
        self.SetSizeHints(minSize=(420,161), maxSize=(420,161))
        self.SetBackgroundColour("white")
        self.Center()

        self.sash_window = MyPanel(self)
        self.scrolled_window = wx.ScrolledWindow(self, -1)
        self.logBox = wx.StaticText(self.scrolled_window, label=Infor.mo_bhelptext)
        self.scrolled_window.SetScrollbars(20, 5, 0, 20)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.scrolled_window,  0, wx.EXPAND)
        sizer.AddSpacer(60)
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

class MO_BToolWindow(wx.Frame):
    def __init__(self, AboutWindow, title):
        wx.Frame.__init__(self, AboutWindow, id=1, title='心灵终结(3.3.6)战役对照', size=(350,201))
        self.SetSizeHints(minSize=(350,201), maxSize=(350,201))
        self.SetBackgroundColour("white")
        self.Center()

        self.inputBox = wx.TextCtrl(self, size=(100, 25), style=wx.TE_PROCESS_ENTER|wx.TE_PROCESS_TAB)
        self.resultBox = wx.TextCtrl(self, size=(100, 25), style=wx.TE_PROCESS_ENTER|wx.TE_PROCESS_TAB)
        self.searchButton = wx.Button(self, label="查询", size=(50, 25))
        self.mapR_text = wx.StaticText(self, pos=(30, 15), label="")
        self.battleR_text = wx.StaticText(self, pos=(125, 15), label="")
        self.map_text = wx.StaticText(self, pos=(30, 85), label="map名称:")
        self.battle_text = wx.StaticText(self, pos=(150, 85), label="战役名称:")
        self.slash_text = wx.StaticText(self, pos=(135, 108), label="/")
        self.helpButton = wx.Button(self, label="?", size=(25, 25))
        Hfont = wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD)
        self.helpButton.SetFont(Hfont)

        sidechoices = ['','盟军','苏军','尤里','焚风']
        self.SideChoice = wx.Choice(self, -1, choices=sidechoices,size=(60,25))
        actchoices = ['','第一幕','第二幕','特殊行动','结局过场']
        self.ActChoice = wx.Choice(self, -1, choices=actchoices,size=(90,25))
        levelchoices = ['','1','2','3','4','5','6','7','8','9','10','11','12']
        self.LevelChoice = wx.Choice(self, -1, choices=levelchoices,size=(60,25))
        self.SideChoice.SetSelection(0)
        self.ActChoice.SetSelection(0)
        self.LevelChoice.SetSelection(0)

        self.helpButton.Bind(wx.EVT_BUTTON, self.OnHelpButton)
        self.searchButton.Bind(wx.EVT_BUTTON, self.OnSearchButton)
        self.inputBox.Bind(wx.EVT_TEXT_ENTER, self.OnSearchButton)
        self.resultBox.Bind(wx.EVT_TEXT_ENTER, self.OnSearchButton)

        sizer = wx.BoxSizer(wx.VERTICAL)
        inputsizer = wx.BoxSizer(wx.HORIZONTAL)
        choicesizer = wx.BoxSizer(wx.HORIZONTAL)
        buttonizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.AddSpacer(35)
        sizer.Add(choicesizer, flag=wx.ALIGN_CENTER)
        sizer.AddSpacer(45)
        sizer.Add(inputsizer, flag=wx.ALIGN_CENTER)
        sizer.AddSpacer(5)
        sizer.Add(buttonizer, flag=wx.ALIGN_CENTER)
        inputsizer.Add(self.inputBox)
        inputsizer.AddSpacer(20)
        inputsizer.Add(self.resultBox)
        inputsizer.AddSpacer(10)
        inputsizer.Add(self.searchButton)
        choicesizer.Add(self.SideChoice, flag=wx.ALIGN_CENTER)
        choicesizer.AddSpacer(33)
        choicesizer.Add(self.ActChoice, flag=wx.ALIGN_CENTER)
        choicesizer.AddSpacer(33)
        choicesizer.Add(self.LevelChoice, flag=wx.ALIGN_CENTER)
        buttonizer.AddSpacer(305)
        buttonizer.Add(self.helpButton, flag=wx.ALIGN_CENTER)
        self.SetSizer(sizer)

        self.SideChoice.Enable(False)
        self.ActChoice.Enable(False)
        self.LevelChoice.Enable(False)

    def SetLevelChoice(self):
        if self.ActChoice.GetStringSelection() == "第一幕":
            self.LevelChoice.Clear()
            self.LevelChoice.AppendItems(['','1','2','3','4','5','6','7','8','9','10','11','12'])
        elif self.ActChoice.GetStringSelection() == "第二幕":
            self.LevelChoice.Clear()
            self.LevelChoice.AppendItems(['','13','14','15','16','17','18','19','20','21','22','23','24'])
        elif self.ActChoice.GetStringSelection() == "特殊行动" and self.SideChoice.GetStringSelection() != "焚风":
            self.LevelChoice.Clear()
            self.LevelChoice.AppendItems(['','a1','a2','a3','a4','a5','a6'])
        elif self.ActChoice.GetStringSelection() == "特殊行动" and self.SideChoice.GetStringSelection() == "焚风":
            self.LevelChoice.Clear()
            self.LevelChoice.AppendItems(['','a1'])
        elif self.ActChoice.GetStringSelection() == "结局过场":
            self.LevelChoice.Clear()
            self.LevelChoice.AppendItems(['','END'])

    def OnHelpButton(self, event):
        new_window = MO_BHelpWindow(self, "")
        new_window.Show()

    def Emptymapname(self, mapname):
        if mapname in EIP_Debug.MO_Battle:
            self.mapR_text.SetLabel(mapname)
            self.battleR_text.SetLabel(EIP_Debug.MO_Battle[mapname][2])
            SideT = EIP_Debug.MO_Battle[mapname][0]
            LevelT = EIP_Debug.MO_Battle[mapname][1]
            if SideT == 'A':
                self.SideChoice.SetSelection(1)
            elif SideT == 'S':
                self.SideChoice.SetSelection(2)
            elif SideT == 'E':
                self.SideChoice.SetSelection(3)
            elif SideT == 'F':
                self.SideChoice.SetSelection(4)
            if 'a' in LevelT:
                self.ActChoice.SetSelection(3)
            elif 'end' in LevelT:
                self.ActChoice.SetSelection(4)
            elif int(LevelT) <= 12:
                self.ActChoice.SetSelection(1)
            elif int(LevelT) >= 13:
                self.ActChoice.SetSelection(2)
            self.SetLevelChoice()
            self.LevelChoice.SetSelection(self.LevelChoice.FindString(LevelT))
        else:
            self.mapR_text.SetLabel("?")
            self.battleR_text.SetLabel("?")
            self.SideChoice.SetSelection(0)
            self.ActChoice.SetSelection(0)
            self.LevelChoice.SetSelection(0)

    def OnSearchButton(self, event):
        mapname = self.inputBox.GetValue().lower()
        battlename = self.resultBox.GetValue().lower()
        if mapname != "":
            self.Emptymapname(mapname)
        elif mapname == "" and battlename != "":
            for key, values in EIP_Debug.MO_Battle.items():
                if battlename in values[2]:
                    mapname = key
                    self.mapR_text.SetLabel(mapname)
                    self.battleR_text.SetLabel(battlename)
                    if mapname != "":
                        self.Emptymapname(mapname)
        elif mapname == "" and battlename == "":
            self.mapR_text.SetLabel("")
            self.battleR_text.SetLabel("")
            self.SideChoice.SetSelection(0)
            self.ActChoice.SetSelection(0)
            self.LevelChoice.SetSelection(0)
        self.inputBox.SetValue("")
        self.resultBox.SetValue("")
