import wx
import wx.adv
import webbrowser
import Infor

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
        self.Github_pretext = wx.StaticText(self, label="更新:")
        self.Github_text = wx.StaticText(self, label="Github")
        udfont = self.update_text.GetFont()
        gtfont = self.Github_text.GetFont()
        udfont = udfont.Underlined()
        gtfont = gtfont.Underlined()
        self.update_text.SetFont(udfont)
        self.Github_text.SetFont(udfont)
        self.update_text.Bind(wx.EVT_LEFT_DOWN, self.OnUpdateLog)
        self.Github_text.Bind(wx.EVT_LEFT_DOWN, self.OnGithubLink)
        self.aboutText1.SetPosition((10, 5))
        self.aboutText2.SetPosition((10, 110))
        self.update_text.SetPosition((10, 80))
        self.Github_pretext.SetPosition((10, 160))
        self.Github_text.SetPosition((45, 160))

        handcursor = wx.Cursor(wx.CURSOR_HAND)
        self.update_text.SetCursor(handcursor)
        self.Github_text.SetCursor(handcursor)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.AddSpacer(200)
        sizer.Add(self.sash_window, 0, wx.EXPAND | wx.BOTTOM, 4)
        self.SetSizer(sizer)

    def OnUpdateLog(self, event):
        new_window = UpdateLogWindow(self, "")
        new_window.Show()

    def OnGithubLink(self, event):
        webbrowser.open("https://github.com/Zhcs0712/INI-Searcher")


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

class HelpWindow(wx.Frame):
    def __init__(self, AboutWindow, title):
        wx.Frame.__init__(self, AboutWindow, id=1, title='帮助', size=(400,301))
        self.SetSizeHints(minSize=(400,301), maxSize=(400,301))
        self.SetBackgroundColour("white")
        self.Center()

        self.sash_window = MyPanel(self)
        self.scrolled_window = wx.ScrolledWindow(self, -1)
        self.logBox = wx.StaticText(self.scrolled_window, label=Infor.helptext)
        self.scrolled_window.SetScrollbars(20, 20, 0, 20)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.scrolled_window,  0, wx.EXPAND)
        sizer.AddSpacer(200)
        sizer.Add(self.sash_window, 0, wx.EXPAND | wx.BOTTOM, 4)
        self.SetSizer(sizer)

class RulesLsWindow(wx.Frame):
    def __init__(self, AboutWindow, title):
        wx.Frame.__init__(self, AboutWindow, id=1, title='rules标签说明', size=(400,301))
        self.SetSizeHints(minSize=(400,301), maxSize=(400,301))
        self.SetBackgroundColour("white")
        self.Center()

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetBackgroundColour(wx.WHITE)

        self.sash_window = MyPanel(self)
        self.tree = wx.TreeCtrl(self, style=wx.TR_HIDE_ROOT|wx.TR_NO_LINES, size=(400,240))
        root = self.tree.AddRoot("Label")
        General = self.tree.AppendItem(root, "[General] ✚")
        self.tree.AppendItem(General, "[General]")
        self.tree.AppendItem(General, "[JumpjetControls]")
        self.tree.AppendItem(General, "[SpecialWeapons]")
        self.tree.AppendItem(General, "[AudioVisual]")
        self.tree.AppendItem(General, "[CrateRules]")
        self.tree.AppendItem(General, "[Powerups]")
        self.tree.AppendItem(General, "[CombatDamage]")
        self.tree.AppendItem(General, "[Radiation]")
        self.tree.AppendItem(General, "[ElevationModel]")
        self.tree.AppendItem(General, "[WallModel]")
        self.tree.AppendItem(General, "[Colors]")
        self.tree.AppendItem(General, "[MultiplayerDialogSettings]")
        Side = self.tree.AppendItem(root, "[Side] ✚")
        self.tree.AppendItem(Side, "[Sides]")
        self.tree.AppendItem(Side, "[Countries]")
        AI = self.tree.AppendItem(root, "[AI] ✚")
        self.tree.AppendItem(AI, "[AI]")
        self.tree.AppendItem(AI, "[IQ]")
        self.tree.AppendItem(AI, "[Easy]")
        self.tree.AppendItem(AI, "[Normal]")
        self.tree.AppendItem(AI, "[Difficult]")
        Other = self.tree.AppendItem(root, "[Other] ✚")
        self.tree.AppendItem(Other, "[Particles]")
        self.tree.AppendItem(Other, "[VoxelAnims]")
        self.tree.AppendItem(Other, "[VariableNames]")
        self.tree.AppendItem(Other, "[ParticleSystems]")
        self.tree.AppendItem(Other, "[TerrainTypes]")
        self.tree.AppendItem(Other, "[Tiberium]")
        self.tree.AppendItem(Other, "[SmudgeTypes]")
        self.tree.AppendItem(Other, "[OverlayTypes]")
        self.tree.AppendItem(Other, "[ShieldTypes]")
        TechnoType = self.tree.AppendItem(root, "[TechnoType]")
        SuperWeapon = self.tree.AppendItem(root, "[SuperWeapon] ✚")
        self.tree.AppendItem(SuperWeapon, "[SuperWeapons]")
        BuildingType = self.tree.AppendItem(root, "[BuildingType] ✚")
        self.tree.AppendItem(BuildingType, "[BuildingTypes]")
        InfantryType = self.tree.AppendItem(root, "[InfantryType] ✚")
        self.tree.AppendItem(InfantryType, "[InfantryTypes]")
        VehicleType = self.tree.AppendItem(root, "[VehicleType] ✚")
        self.tree.AppendItem(VehicleType, "[VehicleTypes]")
        AircraftType = self.tree.AppendItem(root, "[AircraftType] ✚")
        self.tree.AppendItem(AircraftType, "[AircraftTypes]")
        WeaponType = self.tree.AppendItem(root, "[WeaponType] ✚")
        self.tree.AppendItem(WeaponType, "[WeaponTypes]")
        Projectile = self.tree.AppendItem(root, "[Projectile] ✚")
        self.tree.AppendItem(Projectile, "[Projectiles]")
        Warhead = self.tree.AppendItem(root, "[Warhead] ✚")
        self.tree.AppendItem(Warhead, "[Warheads]")
        self.tree.Bind(wx.EVT_TREE_ITEM_EXPANDED, self.on_item_expanded)
        self.tree.Bind(wx.EVT_TREE_ITEM_COLLAPSED, self.on_item_collapsed)
        self.tree.Bind(wx.EVT_TREE_SEL_CHANGED, self.on_item_selected)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.tree, 0, wx.EXPAND)
        sizer.AddSpacer(20)
        sizer.Add(self.sash_window, 0, wx.EXPAND | wx.BOTTOM, 4)
        self.SetSizer(sizer)

        self.Bind(wx.EVT_CLOSE, self.CloseWin)
        self.is_closed = False

    def CloseWin(self, event):
        self.is_closed = True
        self.Destroy()

    def on_item_expanded(self, event):
        item = event.GetItem()
        itemtext = self.tree.GetItemText(item)
        itemtext = itemtext.replace("✚", "")
        self.tree.SetItemText(item, itemtext+"━")

    def on_item_collapsed(self, event):
        item = event.GetItem()
        itemtext = self.tree.GetItemText(item)
        itemtext = itemtext.replace("━", "")
        self.tree.SetItemText(item, itemtext+"✚")

    def on_item_selected(self, event):
        if self.is_closed:
            return
        item = event.GetItem()
        itemtext = self.tree.GetItemText(item)
        itemtext = itemtext.replace("✚", "")
        itemtext = itemtext.replace("━", "")
        if itemtext == "[General] ":
            self.SetStatusText(" [General]，包含[General]在内的大多全局设定")
        elif itemtext == "[Side] ":
            self.SetStatusText(" [Side]，阵营和国家的相关初始设定")
        elif itemtext == "[AI] ":
            self.SetStatusText(" [AI]，包含AI的基础设定和难度分级设定")
        elif itemtext == "[Other] ":
            self.SetStatusText(" [Other]，包含覆盖物、地形、粒子系统，以及新增注册项目")
        elif itemtext == "[TechnoType]":
            self.SetStatusText(" [TechnoType]，科技")
        elif itemtext == "[SuperWeapon] ":
            self.SetStatusText(" [SuperWeapon]，超级武器设定")
        elif itemtext == "[BuildingType] ":
            self.SetStatusText(" [BuildingType]，建筑物设定")
        elif itemtext == "[InfantryType] ":
            self.SetStatusText(" [InfantryType]，步兵设定")
        elif itemtext == "[VehicleType] ":
            self.SetStatusText(" [VehicleType]，载具设定")
        elif itemtext == "[AircraftType] ":
            self.SetStatusText(" [AircraftType]，飞行器设定")
        elif itemtext == "[WeaponType] ":
            self.SetStatusText(" [WeaponType]，武器设定")
        elif itemtext == "[Projectile] ":
            self.SetStatusText(" [Projectile]，抛射体设定")
        elif itemtext == "[Warhead] ":
            self.SetStatusText(" [Warhead]，弹头设定")
        else:
            self.SetStatusText("")

        childitem = self.tree.GetSelection()
        childitemtext = self.tree.GetItemText(childitem)
        if childitemtext == "[General]":
            self.SetStatusText(" [General]，全局设定")
        elif childitemtext == "[JumpjetControls]":
            self.SetStatusText(" [JumpjetControls]，JUMPJET的行动方式控制")
        elif childitemtext == "[SpecialWeapons]":
            self.SetStatusText(" [SpecialWeapons]，超武设定")
        elif childitemtext == "[AudioVisual]":
            self.SetStatusText(" [AudioVisual]，音频或外观的控制。")
        elif childitemtext == "[CrateRules]":
            self.SetStatusText(" [CrateRules]，箱子个数和生成控制")
        elif childitemtext == "[Powerups]":
            self.SetStatusText(" [Powerups]，箱子内容的相关参数控制")
        elif childitemtext == "[CombatDamage]":
            self.SetStatusText(" [CombatDamage]，全局武器伤害控制")
        elif childitemtext == "[Radiation]":
            self.SetStatusText(" [Radiation]，辐射控制")
        elif childitemtext == "[ElevationModel]":
            self.SetStatusText(" [ElevationModel]，悬崖增加射程设定")
        elif childitemtext == "[WallModel]":
            self.SetStatusText(" [WallModel]，城墙设定")
        elif childitemtext == "[Colors]":
            self.SetStatusText(" [Colors]，颜色设定")
        elif childitemtext == "[MultiplayerDialogSettings]":
            self.SetStatusText(" [MultiplayerDialogSettings]，多人游戏(遭遇战)设定")
        elif childitemtext == "[Sides]":
            self.SetStatusText(" [Sides]，阵营设定")
        elif childitemtext == "[Countries]":
            self.SetStatusText(" [Countries]，国家设定")
        elif childitemtext == "[AI]":
            self.SetStatusText(" [AI]，AI相关注册和设定")
        elif childitemtext == "[IQ]":
            self.SetStatusText(" [IQ]，IQ设定")
        elif childitemtext == "[Easy]":
            self.SetStatusText(" [Easy]，简单难度设定")
        elif childitemtext == "[Normal]":
            self.SetStatusText(" [Normal]，普通难度设定")
        elif childitemtext == "[Difficult]":
            self.SetStatusText(" [Difficult]，困难难度设定")
        elif childitemtext == "[Particles]":
            self.SetStatusText(" [Particles]，粒子设定")
        elif childitemtext == "[VoxelAnims]":
            self.SetStatusText(" [VoxelAnims]，VXL设定")
        elif childitemtext == "[VariableNames]":
            self.SetStatusText(" [VariableNames]，全局变量控制")
        elif childitemtext == "[ParticleSystems]":
            self.SetStatusText(" [ParticleSystems]，粒子系统设定")
        elif childitemtext == "[TerrainTypes]":
            self.SetStatusText(" [TerrainTypes]，地形设定")
        elif childitemtext == "[Tiberium]":
            self.SetStatusText(" [Tiberium]，矿石设定")
        elif childitemtext == "[SmudgeTypes]":
            self.SetStatusText(" [SmudgeTypes]，污迹设定")
        elif childitemtext == "[OverlayTypes]":
            self.SetStatusText(" [OverlayTypes]，覆盖物设定")
        elif childitemtext == "[ShieldTypes]":
            self.SetStatusText(" [ShieldTypes]，护盾设定(Phobos)")
        elif childitemtext == "[SuperWeapons]":
            self.SetStatusText(" [SuperWeapons]，超级武器设定")
        elif childitemtext == "[BuildingTypes]":
            self.SetStatusText(" [BuildingTypes]，建筑物设定")
        elif childitemtext == "[InfantryTypes]":
            self.SetStatusText(" [InfantryTypes]，步兵设定")
        elif childitemtext == "[VehicleTypes]":
            self.SetStatusText(" [VehicleTypes]，载具设定")
        elif childitemtext == "[AircraftTypes]":
            self.SetStatusText(" [AircraftTypes]，飞行器设定")
        elif childitemtext == "[WeaponTypes]":
            self.SetStatusText(" [WeaponTypes]，武器设定")
        elif childitemtext == "[Projectiles]":
            self.SetStatusText(" [Projectiles]，抛射体设定")
        elif childitemtext == "[Warheads]":
            self.SetStatusText(" [Warheads]，弹头设定")

class ArtLsWindow(wx.Frame):
    def __init__(self, AboutWindow, title):
        wx.Frame.__init__(self, AboutWindow, id=1, title='art标签说明', size=(400,301))
        self.SetSizeHints(minSize=(400,301), maxSize=(400,301))
        self.SetBackgroundColour("white")
        self.Center()

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetBackgroundColour(wx.WHITE)

        self.sash_window = MyPanel(self)
        self.tree = wx.TreeCtrl(self, style=wx.TR_HIDE_ROOT|wx.TR_NO_LINES, size=(400,240))
        root = self.tree.AddRoot("Label")
        UnitArt = self.tree.AppendItem(root, "[UnitArt]")
        Animation = self.tree.AppendItem(root, "[Animation]")
        self.tree.Bind(wx.EVT_TREE_SEL_CHANGED, self.on_item_selected)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.tree, 0, wx.EXPAND)
        sizer.AddSpacer(20)
        sizer.Add(self.sash_window, 0, wx.EXPAND | wx.BOTTOM, 4)
        self.SetSizer(sizer)

        self.Bind(wx.EVT_CLOSE, self.CloseWin)
        self.is_closed = False

    def CloseWin(self, event):
        self.is_closed = True
        self.Destroy()

    def on_item_selected(self, event):
        if self.is_closed:
            return
        item = event.GetItem()
        itemtext = self.tree.GetItemText(item)
        if itemtext == "[UnitArt]":
            self.SetStatusText(" [UnitArt]，单位素材设定shp/vxl")
        elif itemtext == "[Animation]":
            self.SetStatusText(" [Animation]，动画素材设定shp")
        else:
            self.SetStatusText("")

class SoundLsWindow(wx.Frame):
    def __init__(self, AboutWindow, title):
        wx.Frame.__init__(self, AboutWindow, id=1, title='sound标签说明', size=(400,301))
        self.SetSizeHints(minSize=(400,301), maxSize=(400,301))
        self.SetBackgroundColour("white")
        self.Center()

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetBackgroundColour(wx.WHITE)

        self.sash_window = MyPanel(self)
        self.tree = wx.TreeCtrl(self, style=wx.TR_HIDE_ROOT|wx.TR_NO_LINES, size=(400,240))
        root = self.tree.AddRoot("Label")
        Sound = self.tree.AppendItem(root, "[Sound]")
        self.tree.Bind(wx.EVT_TREE_SEL_CHANGED, self.on_item_selected)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.tree, 0, wx.EXPAND)
        sizer.AddSpacer(20)
        sizer.Add(self.sash_window, 0, wx.EXPAND | wx.BOTTOM, 4)
        self.SetSizer(sizer)

        self.Bind(wx.EVT_CLOSE, self.CloseWin)
        self.is_closed = False

    def CloseWin(self, event):
        self.is_closed = True
        self.Destroy()

    def on_item_selected(self, event):
        if self.is_closed:
            return
        item = event.GetItem()
        itemtext = self.tree.GetItemText(item)
        if itemtext == "[Sound]":
            self.SetStatusText(" [Sound]，语音音效设定")
        else:
            self.SetStatusText("")

class UiLsWindow(wx.Frame):
    def __init__(self, AboutWindow, title):
        wx.Frame.__init__(self, AboutWindow, id=1, title='ui标签说明', size=(400,301))
        self.SetSizeHints(minSize=(400,301), maxSize=(400,301))
        self.SetBackgroundColour("white")
        self.Center()

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetBackgroundColour(wx.WHITE)

        self.sash_window = MyPanel(self)
        self.tree = wx.TreeCtrl(self, style=wx.TR_HIDE_ROOT|wx.TR_NO_LINES, size=(400,240))
        root = self.tree.AddRoot("Label")
        UISettings = self.tree.AppendItem(root, "[UISettings]")
        Colors = self.tree.AppendItem(root, "[Colors]")
        LoadingScreen = self.tree.AppendItem(root, "[LoadingScreen]")
        Sidebar = self.tree.AppendItem(root, "[Sidebar]")
        ToolTips = self.tree.AppendItem(root, "[ToolTips]")
        VersionInfo = self.tree.AppendItem(root, "[VersionInfo]")
        self.tree.Bind(wx.EVT_TREE_SEL_CHANGED, self.on_item_selected)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.tree, 0, wx.EXPAND)
        sizer.AddSpacer(20)
        sizer.Add(self.sash_window, 0, wx.EXPAND | wx.BOTTOM, 4)
        self.SetSizer(sizer)

        self.Bind(wx.EVT_CLOSE, self.CloseWin)
        self.is_closed = False

    def CloseWin(self, event):
        self.is_closed = True
        self.Destroy()

    def on_item_selected(self, event):
        if self.is_closed:
            return
        item = event.GetItem()
        itemtext = self.tree.GetItemText(item)
        if itemtext == "[UISettings]":
            self.SetStatusText(" [UISettings]，游戏UI设定")
        elif itemtext == "[Colors]":
            self.SetStatusText(" [Colors]，阵营颜色设定")
        elif itemtext == "[LoadingScreen]":
            self.SetStatusText(" [LoadingScreen]，游戏载入界面设定")
        elif itemtext == "[Sidebar]":
            self.SetStatusText(" [Sidebar]，游戏侧边栏设定")
        elif itemtext == "[ToolTips]":
            self.SetStatusText(" [ToolTips]，工具提示设定")
        elif itemtext == "[VersionInfo]":
            self.SetStatusText(" [VersionInfo]，版本信息设定")
        else:
            self.SetStatusText("")

class AiLsWindow(wx.Frame):
    def __init__(self, AboutWindow, title):
        wx.Frame.__init__(self, AboutWindow, id=1, title='ai标签说明', size=(400,301))
        self.SetSizeHints(minSize=(400,301), maxSize=(400,301))
        self.SetBackgroundColour("white")
        self.Center()

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetBackgroundColour(wx.WHITE)

        self.sash_window = MyPanel(self)
        self.tree = wx.TreeCtrl(self, style=wx.TR_HIDE_ROOT|wx.TR_NO_LINES, size=(400,240))
        root = self.tree.AddRoot("Label")
        Sound = self.tree.AppendItem(root, "[AI]")
        self.tree.Bind(wx.EVT_TREE_SEL_CHANGED, self.on_item_selected)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.tree, 0, wx.EXPAND)
        sizer.AddSpacer(20)
        sizer.Add(self.sash_window, 0, wx.EXPAND | wx.BOTTOM, 4)
        self.SetSizer(sizer)

        self.Bind(wx.EVT_CLOSE, self.CloseWin)
        self.is_closed = False

    def CloseWin(self, event):
        self.is_closed = True
        self.Destroy()

    def on_item_selected(self, event):
        if self.is_closed:
            return
        item = event.GetItem()
        itemtext = self.tree.GetItemText(item)
        if itemtext == "[AI]":
            self.SetStatusText(" [AI]，AI触发等设定")
        else:
            self.SetStatusText("")

class MapLsWindow(wx.Frame):
    def __init__(self, AboutWindow, title):
        wx.Frame.__init__(self, AboutWindow, id=1, title='map标签说明', size=(400,301))
        self.SetSizeHints(minSize=(400,301), maxSize=(400,301))
        self.SetBackgroundColour("white")
        self.Center()

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetBackgroundColour(wx.WHITE)

        self.sash_window = MyPanel(self)
        self.tree = wx.TreeCtrl(self, style=wx.TR_HIDE_ROOT|wx.TR_NO_LINES, size=(400,240))
        root = self.tree.AddRoot("Label")
        Basic = self.tree.AppendItem(root, "[Basic]")
        Maximums = self.tree.AppendItem(root, "[Maximums]")
        self.tree.Bind(wx.EVT_TREE_SEL_CHANGED, self.on_item_selected)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.tree, 0, wx.EXPAND)
        sizer.AddSpacer(20)
        sizer.Add(self.sash_window, 0, wx.EXPAND | wx.BOTTOM, 4)
        self.SetSizer(sizer)

        self.Bind(wx.EVT_CLOSE, self.CloseWin)
        self.is_closed = False

    def CloseWin(self, event):
        self.is_closed = True
        self.Destroy()

    def on_item_selected(self, event):
        if self.is_closed:
            return
        item = event.GetItem()
        itemtext = self.tree.GetItemText(item)
        if itemtext == "[Basic]":
            self.SetStatusText(" [Basic]，Map内置INI，地图基础设定")
        elif itemtext == "[Maximums]":
            self.SetStatusText(" [Maximums]，Map内置INI，地图最大人数")
        else:
            self.SetStatusText("")

class SnowLsWindow(wx.Frame):
    def __init__(self, AboutWindow, title):
        wx.Frame.__init__(self, AboutWindow, id=1, title='snow标签说明', size=(400,301))
        self.SetSizeHints(minSize=(400,301), maxSize=(400,301))
        self.SetBackgroundColour("white")
        self.Center()

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetBackgroundColour(wx.WHITE)

        self.sash_window = MyPanel(self)
        self.tree = wx.TreeCtrl(self, style=wx.TR_HIDE_ROOT|wx.TR_NO_LINES, size=(400,240))
        root = self.tree.AddRoot("Label")
        Snow = self.tree.AppendItem(root, "[Snow]")
        self.tree.Bind(wx.EVT_TREE_SEL_CHANGED, self.on_item_selected)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.tree, 0, wx.EXPAND)
        sizer.AddSpacer(20)
        sizer.Add(self.sash_window, 0, wx.EXPAND | wx.BOTTOM, 4)
        self.SetSizer(sizer)

        self.Bind(wx.EVT_CLOSE, self.CloseWin)
        self.is_closed = False

    def CloseWin(self, event):
        self.is_closed = True
        self.Destroy()

    def on_item_selected(self, event):
        if self.is_closed:
            return
        item = event.GetItem()
        itemtext = self.tree.GetItemText(item)
        if itemtext == "[Snow]":
            self.SetStatusText(" [Snow]，雪地设定")
        else:
            self.SetStatusText("")

class MovieLsWindow(wx.Frame):
    def __init__(self, AboutWindow, title):
        wx.Frame.__init__(self, AboutWindow, id=1, title='movie标签说明', size=(400,301))
        self.SetSizeHints(minSize=(400,301), maxSize=(400,301))
        self.SetBackgroundColour("white")
        self.Center()

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetBackgroundColour(wx.WHITE)

        self.sash_window = MyPanel(self)
        self.tree = wx.TreeCtrl(self, style=wx.TR_HIDE_ROOT|wx.TR_NO_LINES, size=(400,240))
        root = self.tree.AddRoot("Label")
        Movie = self.tree.AppendItem(root, "[Movie]")
        self.tree.Bind(wx.EVT_TREE_SEL_CHANGED, self.on_item_selected)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.tree, 0, wx.EXPAND)
        sizer.AddSpacer(20)
        sizer.Add(self.sash_window, 0, wx.EXPAND | wx.BOTTOM, 4)
        self.SetSizer(sizer)

        self.Bind(wx.EVT_CLOSE, self.CloseWin)
        self.is_closed = False

    def CloseWin(self, event):
        self.is_closed = True
        self.Destroy()

    def on_item_selected(self, event):
        if self.is_closed:
            return
        item = event.GetItem()
        itemtext = self.tree.GetItemText(item)
        if itemtext == "[Movie]":
            self.SetStatusText(" [Movie]，影片视频设定")
        else:
            self.SetStatusText("")

class BattleLsWindow(wx.Frame):
    def __init__(self, AboutWindow, title):
        wx.Frame.__init__(self, AboutWindow, id=1, title='battle标签说明', size=(400,301))
        self.SetSizeHints(minSize=(400,301), maxSize=(400,301))
        self.SetBackgroundColour("white")
        self.Center()

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetBackgroundColour(wx.WHITE)

        self.sash_window = MyPanel(self)
        self.tree = wx.TreeCtrl(self, style=wx.TR_HIDE_ROOT|wx.TR_NO_LINES, size=(400,240))
        root = self.tree.AddRoot("Label")
        Battle = self.tree.AppendItem(root, "[Battle]")
        self.tree.Bind(wx.EVT_TREE_SEL_CHANGED, self.on_item_selected)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.tree, 0, wx.EXPAND)
        sizer.AddSpacer(20)
        sizer.Add(self.sash_window, 0, wx.EXPAND | wx.BOTTOM, 4)
        self.SetSizer(sizer)

        self.Bind(wx.EVT_CLOSE, self.CloseWin)
        self.is_closed = False

    def CloseWin(self, event):
        self.is_closed = True
        self.Destroy()

    def on_item_selected(self, event):
        if self.is_closed:
            return
        item = event.GetItem()
        itemtext = self.tree.GetItemText(item)
        if itemtext == "[Battle]":
            self.SetStatusText(" [Battle]，战役、作战相关设定")
        else:
            self.SetStatusText("")

class MissionLsWindow(wx.Frame):
    def __init__(self, AboutWindow, title):
        wx.Frame.__init__(self, AboutWindow, id=1, title='mission标签说明', size=(400,301))
        self.SetSizeHints(minSize=(400,301), maxSize=(400,301))
        self.SetBackgroundColour("white")
        self.Center()

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetBackgroundColour(wx.WHITE)

        self.sash_window = MyPanel(self)
        self.tree = wx.TreeCtrl(self, style=wx.TR_HIDE_ROOT|wx.TR_NO_LINES, size=(400,240))
        root = self.tree.AddRoot("Label")
        Mission = self.tree.AppendItem(root, "[Mission]")
        self.tree.Bind(wx.EVT_TREE_SEL_CHANGED, self.on_item_selected)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.tree, 0, wx.EXPAND)
        sizer.AddSpacer(20)
        sizer.Add(self.sash_window, 0, wx.EXPAND | wx.BOTTOM, 4)
        self.SetSizer(sizer)

        self.Bind(wx.EVT_CLOSE, self.CloseWin)
        self.is_closed = False

    def CloseWin(self, event):
        self.is_closed = True
        self.Destroy()

    def on_item_selected(self, event):
        if self.is_closed:
            return
        item = event.GetItem()
        itemtext = self.tree.GetItemText(item)
        if itemtext == "[Mission]":
            self.SetStatusText(" [Mission]，战役设定")
        else:
            self.SetStatusText("")

class Ra2LsWindow(wx.Frame):
    def __init__(self, AboutWindow, title):
        wx.Frame.__init__(self, AboutWindow, id=1, title='ra2标签说明', size=(400,301))
        self.SetSizeHints(minSize=(400,301), maxSize=(400,301))
        self.SetBackgroundColour("white")
        self.Center()

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetBackgroundColour(wx.WHITE)

        self.sash_window = MyPanel(self)
        self.tree = wx.TreeCtrl(self, style=wx.TR_HIDE_ROOT|wx.TR_NO_LINES, size=(400,240))
        root = self.tree.AddRoot("Label")
        Phobos = self.tree.AppendItem(root, "[Phobos]")
        self.tree.Bind(wx.EVT_TREE_SEL_CHANGED, self.on_item_selected)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.tree, 0, wx.EXPAND)
        sizer.AddSpacer(20)
        sizer.Add(self.sash_window, 0, wx.EXPAND | wx.BOTTOM, 4)
        self.SetSizer(sizer)

        self.Bind(wx.EVT_CLOSE, self.CloseWin)
        self.is_closed = False

    def CloseWin(self, event):
        self.is_closed = True
        self.Destroy()

    def on_item_selected(self, event):
        if self.is_closed:
            return
        item = event.GetItem()
        itemtext = self.tree.GetItemText(item)
        if itemtext == "[Phobos]":
            self.SetStatusText(" [Phobos]，Phobos平台的拓展设定")
        else:
            self.SetStatusText("")

class RgbLsWindow(wx.Frame):
    def __init__(self, AboutWindow, title):
        wx.Frame.__init__(self, AboutWindow, id=1, title='rgb标签说明', size=(400,301))
        self.SetSizeHints(minSize=(400,301), maxSize=(400,301))
        self.SetBackgroundColour("white")
        self.Center()

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetBackgroundColour(wx.WHITE)

        self.sash_window = MyPanel(self)
        self.tree = wx.TreeCtrl(self, style=wx.TR_HIDE_ROOT|wx.TR_NO_LINES, size=(400,240))
        root = self.tree.AddRoot("Label")
        URBAN = self.tree.AppendItem(root, "[URBAN]")
        self.tree.Bind(wx.EVT_TREE_SEL_CHANGED, self.on_item_selected)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.tree, 0, wx.EXPAND)
        sizer.AddSpacer(20)
        sizer.Add(self.sash_window, 0, wx.EXPAND | wx.BOTTOM, 4)
        self.SetSizer(sizer)

        self.Bind(wx.EVT_CLOSE, self.CloseWin)
        self.is_closed = False

    def CloseWin(self, event):
        self.is_closed = True
        self.Destroy()

    def on_item_selected(self, event):
        if self.is_closed:
            return
        item = event.GetItem()
        itemtext = self.tree.GetItemText(item)
        if itemtext == "[URBAN]":
            self.SetStatusText(" [URBAN]，城市地图相关设定")
        else:
            self.SetStatusText("")

class EnginesWindow(wx.Frame):
    def __init__(self, AboutWindow, title):
        wx.Frame.__init__(self, AboutWindow, id=1, title='平台说明', size=(400,301))
        self.SetSizeHints(minSize=(400,301), maxSize=(400,301))
        self.SetBackgroundColour("white")
        self.Center()

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetBackgroundColour(wx.WHITE)

        self.sash_window = MyPanel(self)
        self.tree = wx.TreeCtrl(self, style=wx.TR_HIDE_ROOT, size=(400,240))
        root = self.tree.AddRoot("Engine")
        Original = self.tree.AppendItem(root, "Original")
        Ares = self.tree.AppendItem(root, "Ares")
        Phobos = self.tree.AppendItem(root, "Phobos")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.tree, 0, wx.EXPAND)
        sizer.AddSpacer(20)
        sizer.Add(self.sash_window, 0, wx.EXPAND | wx.BOTTOM, 4)
        self.SetSizer(sizer)

        self.tree.Bind(wx.EVT_TREE_SEL_CHANGED, self.on_item_selected)
        self.Bind(wx.EVT_CLOSE, self.CloseWin)
        self.is_closed = False

    def CloseWin(self, event):
        self.is_closed = True
        self.Destroy()

    def on_item_selected(self, event):
        if self.is_closed:
            return
        item = event.GetItem()
        itemtext = self.tree.GetItemText(item)
        if itemtext == "Original":
            self.SetStatusText("Original，原平台,包含TS等")
        elif itemtext == "Ares":
            self.SetStatusText("Ares，阿瑞斯(战神)平台")
        elif itemtext == "Phobos":
            self.SetStatusText("Phobos，火卫一平台")
        else:
            self.SetStatusText("")

class INIFilesWindow(wx.Frame):
    def __init__(self, AboutWindow, title):
        wx.Frame.__init__(self, AboutWindow, id=1, title='INI说明', size=(400,301))
        self.SetSizeHints(minSize=(400,301), maxSize=(400,301))
        self.SetBackgroundColour("white")
        self.Center()

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetBackgroundColour(wx.WHITE)

        self.sash_window = MyPanel(self)
        self.tree = wx.TreeCtrl(self, style=wx.TR_HIDE_ROOT, size=(400,240))
        root = self.tree.AddRoot("INIFiles")
        Rules = self.tree.AppendItem(root, "rules ✚")
        self.tree.AppendItem(Rules, "rules.ini")
        self.tree.AppendItem(Rules, "rulesmd.ini")
        self.tree.AppendItem(Rules, "rulesmo.ini")
        Art = self.tree.AppendItem(root, "art ✚")
        self.tree.AppendItem(Art, "art.ini")
        self.tree.AppendItem(Art, "artmd.ini")
        self.tree.AppendItem(Art, "artmo.ini")
        Sound = self.tree.AppendItem(root, "sound ✚")
        self.tree.AppendItem(Sound, "sound.ini")
        self.tree.AppendItem(Sound, "soundmd.ini")
        self.tree.AppendItem(Sound, "soundmo.ini")
        Ui = self.tree.AppendItem(root, "ui ✚")
        self.tree.AppendItem(Ui, "ui.ini")
        self.tree.AppendItem(Ui, "uimd.ini")
        self.tree.AppendItem(Ui, "uimo.ini")
        Ai = self.tree.AppendItem(root, "ai ✚")
        self.tree.AppendItem(Ai, "ai.ini")
        self.tree.AppendItem(Ai, "aimd.ini")
        self.tree.AppendItem(Ai, "aimo.ini")
        Map = self.tree.AppendItem(root, "map")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.tree, 0, wx.EXPAND)
        sizer.AddSpacer(20)
        sizer.Add(self.sash_window, 0, wx.EXPAND | wx.BOTTOM, 4)
        self.SetSizer(sizer)

        self.tree.Bind(wx.EVT_TREE_ITEM_EXPANDED, self.on_item_expanded)
        self.tree.Bind(wx.EVT_TREE_ITEM_COLLAPSED, self.on_item_collapsed)
        self.tree.Bind(wx.EVT_TREE_SEL_CHANGED, self.on_item_selected)

        self.Bind(wx.EVT_CLOSE, self.CloseWin)
        self.is_closed = False

    def CloseWin(self, event):
        self.is_closed = True
        self.Destroy()

    def on_item_expanded(self, event):
        item = event.GetItem()
        itemtext = self.tree.GetItemText(item)
        itemtext = itemtext.replace("✚", "")
        self.tree.SetItemText(item, itemtext+"━")

    def on_item_collapsed(self, event):
        item = event.GetItem()
        itemtext = self.tree.GetItemText(item)
        itemtext = itemtext.replace("━", "")
        self.tree.SetItemText(item, itemtext+"✚")

    def on_item_selected(self, event):
        if self.is_closed:
            return
        item = event.GetItem()
        itemtext = self.tree.GetItemText(item)
        itemtext = itemtext.replace("✚", "")
        itemtext = itemtext.replace("━", "")
        if itemtext == "rules ":
            self.SetStatusText(" rules，主要的规则文件")
        elif itemtext == "art ":
            self.SetStatusText(" art，动画、素材注册文件")
        elif itemtext == "sound ":
            self.SetStatusText(" sound，音效、语音注册文件")
        elif itemtext == "ui ":
            self.SetStatusText(" ui，用户界面设定文件")
        elif itemtext == "ai ":
            self.SetStatusText(" ai，AI行为控制文件")
        elif itemtext == "map":
            self.SetStatusText(" map，地图内置ini")
        else:
            self.SetStatusText("")

        childitem = self.tree.GetSelection()
        childitemtext = self.tree.GetItemText(childitem)
        if childitemtext == "rules.ini":
            self.SetStatusText(" rules.ini，原版规则文件")
        elif childitemtext == "rulesmd.ini":
            self.SetStatusText(" rulesmd.ini，尤里的复仇规则文件")
        elif childitemtext == "rulesmo.ini":
            self.SetStatusText(" rulesmo.ini，心灵终结规则文件")
        elif childitemtext == "art.ini":
            self.SetStatusText(" art.ini，原版动画、素材注册文件")
        elif childitemtext == "artmd.ini":
            self.SetStatusText(" artmd.ini，尤里的复仇动画、素材注册文件")
        elif childitemtext == "artmo.ini":
            self.SetStatusText(" artmo.ini，心灵终结动画、素材注册文件")
        elif childitemtext == "sound.ini":
            self.SetStatusText(" sound.ini，原版音效、语音注册文件")
        elif childitemtext == "soundmd.ini":
            self.SetStatusText(" soundmd.ini，尤里的复仇音效、语音注册文件")
        elif childitemtext == "soundmo.ini":
            self.SetStatusText(" soundmo.ini，心灵终结音效、语音注册文件")
        elif childitemtext == "ui.ini":
            self.SetStatusText(" ui.ini，原版用户界面设定文件")
        elif childitemtext == "uimd.ini":
            self.SetStatusText(" uimd.ini，尤里的复仇用户界面设定文件")
        elif childitemtext == "uimo.ini":
            self.SetStatusText(" uimo.ini，心灵终结用户界面设定文件")
        elif childitemtext == "ai.ini":
            self.SetStatusText(" ai.ini，原版AI行为控制文件")
        elif childitemtext == "aimd.ini":
            self.SetStatusText(" aimd.ini，尤里的复仇AI行为控制文件")
        elif childitemtext == "aimo.ini":
            self.SetStatusText(" aimo.ini，心灵终结AI行为控制文件")