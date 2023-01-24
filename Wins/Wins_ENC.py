import wx
import os
from tkinter import Tk, filedialog
import Infor

class PseudoENCWindow(wx.Frame):
    def __init__(self, AboutWindow, title):
        wx.Frame.__init__(self, AboutWindow, id=1, title='伪加密工具', size=(480,371))
        self.SetSizeHints(minSize=(480,371), maxSize=(480,371))
        self.SetBackgroundColour("white")
        self.Center()

        self.searchBox = wx.TextCtrl(self, size=(350, 25))
        self.searchButton = wx.Button(self, label="选择文件")
        self.help_text = wx.StaticText(self, pos=(15, 55), label=Infor.PseudoENChelp)
        self.statusBox = wx.TextCtrl(self, size=(400, 25), style=wx.TE_CENTER)
        self.decryptionButton = wx.Button(self, label="解密")
        self.encryptionButton = wx.Button(self, label="加密")

        self.searchButton.Bind(wx.EVT_BUTTON, self.OnButtonClick)
        self.encryptionButton.Bind(wx.EVT_BUTTON, self.OnENCClick)
        self.statusBox.Enable(False)
        self.decryptionButton.Enable(False)

        sizer = wx.BoxSizer(wx.VERTICAL)
        inputsizer = wx.BoxSizer(wx.HORIZONTAL)
        buttonsizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.AddSpacer(20)
        sizer.Add(inputsizer, flag=wx.ALIGN_CENTER)
        sizer.AddSpacer(200)
        sizer.Add(self.statusBox, flag=wx.ALIGN_CENTER)
        sizer.AddSpacer(10)
        sizer.Add(buttonsizer, flag=wx.ALIGN_CENTER)
        inputsizer.Add(self.searchBox)
        inputsizer.AddSpacer(10)
        inputsizer.Add(self.searchButton)
        buttonsizer.Add(self.decryptionButton)
        buttonsizer.AddSpacer(40)
        buttonsizer.Add(self.encryptionButton)
        self.SetSizer(sizer)

    def OnButtonClick(self, event):
        root = Tk()
        root.withdraw()
        filepath = filedialog.askopenfilename(filetypes=[("INI Files", "*.ini"), ("MIX files", "*.mix")])
        self.searchBox.SetValue(filepath)

    def OnENCClick(self, event):
        filepath = self.searchBox.GetValue()
        if filepath == "":
            self.statusBox.SetValue("请选择文件或输入文件路径！")
        elif filepath.endswith(".ini"):
            if os.path.isfile(filepath):
                self.statusBox.SetValue("正在加密... ...")
                with open(filepath, 'rb') as f:
                    data = f.read()
                hex_data = 'fffe000a' + data.hex()
                file_path = filedialog.asksaveasfilename(defaultextension=".ini", filetypes=[("INI files", "*.ini")])
                data = bytes.fromhex(hex_data)
                if file_path != "":
                    with open(file_path, 'wb') as f:
                        f.write(data)
                else:
                    self.statusBox.SetValue("加密失败！未输入要保存的文件名！")
                if os.path.isfile(file_path):
                    self.statusBox.SetValue("加密成功！")
                else:
                    self.statusBox.SetValue("加密失败！")
            else:
                self.statusBox.SetValue("文件路径输入错误或文件不存在！")
        elif filepath.endswith(".mix"):
            if os.path.isfile(filepath):
                self.statusBox.SetValue("正在加密... ...")
                with open(filepath, 'rb') as f:
                    data = f.read()
                hex_data = data.hex() +'fffe'
                file_path = filedialog.asksaveasfilename(defaultextension=".mix", filetypes=[("MIX files", "*.mix")])
                data = bytes.fromhex(hex_data)
                if file_path != "":
                    with open(file_path, 'wb') as f:
                        f.write(data)
                else:
                    self.statusBox.SetValue("加密失败！未输入要保存的文件名！")
                if os.path.isfile(file_path):
                    self.statusBox.SetValue("加密成功！")
                else:
                    self.statusBox.SetValue("加密失败！")
            else:
                self.statusBox.SetValue("文件路径输入错误或文件不存在！")
        else:
            self.statusBox.SetValue("不支持此类文件或文件路径输入错误！")

