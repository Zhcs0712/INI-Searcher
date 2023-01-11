import wx

class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, style=wx.BORDER_SIMPLE)
        self.SetBackgroundColour("black")

class LabelsWindow(wx.Frame):
    def __init__(self, AboutWindow, title):
        wx.Frame.__init__(self, AboutWindow, id=1, title='标签说明', size=(400,301))
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
        Animation = self.tree.AppendItem(root, "[Animation] ✚")
        self.tree.AppendItem(Animation, "[Animations]")
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
        elif itemtext == "[Animation] ":
            self.SetStatusText(" [Animation]，动画设定")
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
        else:
            self.SetStatusText("")