armorentries = ""
def ArmorEntries(keyword):
    if keyword[-10:] == ".forcefire" and keyword != "versus.forcefire":
        parts = keyword.split(".",2)
        armorparts = parts[1]
        armorentries = "该弹头是否可以对"+armorparts+"护甲强行攻击"
    elif keyword[-10:] == ".retaliate" and keyword != "versus.retaliate":
        parts = keyword.split(".",2)
        armorparts = parts[1]
        armorentries = "该弹头是否可以对"+armorparts+"护甲反击"
    elif keyword[-15:] == ".passiveacquire" and keyword != "versus.passiveacquire":
        parts = keyword.split(".",2)
        armorparts = parts[1]
        armorentries = "该弹头是否可以对"+armorparts+"护甲主动攻击"
    elif keyword.count('.') == 1:
        parts = keyword.split(".",1)
        armorparts = parts[1]
        armorentries = "该弹头对"+armorparts+"护甲的伤害百分比"
    else:
        armorentries = "Keyword not found."
    return armorentries

turretindexentries = ""
def TurretIndexEntries(keyword):
    if keyword != "weaponturretindex":
        parts = keyword.split("index",1)
        numparts = parts[1]
        if numparts.isdigit():
            numparts = int(numparts)
            turretindexentries = f"(Ares3.0)在Weapon{numparts}和EliteWeapon{numparts}启用时将使用这个炮塔，通过乘客的IFVMode来定义。\n对应步兵的IFVMode{numparts-1}。"
        else:
            turretindexentries = "(Ares3.0)在Weapon“"+numparts+"”和EliteWeapon“"+numparts+"”启用时将使用这个炮塔，通过乘客的IFVMode来定义。\n对应步兵的IFVMode“"+numparts+"-1'。\n“"+numparts+"”为正整数，在原版中不得超过18，Ares将其扩展至127"
    else:
        turretindexentries = "Keyword not found."
    return turretindexentries

weaponnamentries = ""
def WeaponNameEntries(keyword):
    if keyword != "weaponuiname":
        parts = keyword.split("name",1)
        numparts = parts[1]
        if numparts.isdigit():
            numparts = int(numparts)
            weaponnamentries = f"(Ares3.0)Gunner=yes的单位可以让每一个武器有自己的提示文本，此即对应第{numparts}个武器"
        else:
            weaponnamentries = "(Ares3.0)Gunner=yes的单位可以让每一个武器有自己的提示文本，此即对应第“"+numparts+"”个武器\n“"+numparts+"”为正整数，在原版中不得超过18，Ares将其扩展至127"
    else:
        weaponnamentries = "Keyword not found."
    return weaponnamentries

prerequisitentries = ""
def PrerequisiteEntries(keyword):
    if keyword != "prerequisite.list":
        parts = keyword.split("list",1)
        numparts = parts[1]
        if numparts.isdigit():
            numparts = int(numparts)
            prerequisitentries = f"(Ares3.0)指定的第{numparts}个新建造前提，新建造前提的数量对应Prerequisite.Lists="
        else:
            if numparts == 's':
                prerequisitentries = "(Ares3.0)填数字，指定此单位有多少建造前提"
            else:
                prerequisitentries = "(Ares3.0)指定的第“"+numparts+"”个新建造前提，新建造前提的数量对应Prerequisite.Lists="
    else:
        prerequisitentries = "Keyword not found."
    return prerequisitentries

survivorentries = ""
def SurvivoreEntries(keyword):
    if keyword != "survivor.side":
        parts = keyword.split("side",1)
        numparts = parts[1]
        if numparts.isdigit():
            numparts = int(numparts)
            if numparts == 0:
                survivorentries = f"(Ares3.0)第{numparts+1}阵营，一般为盟军阵营(GDI)，单位建筑被摧毁时产生什么步兵。默认值为阵营设置的基础步兵"
            elif numparts == 1:
                survivorentries = f"(Ares3.0)第{numparts+1}阵营，一般为苏军阵营(Nod)，单位建筑被摧毁时产生什么步兵。默认值为阵营设置的基础步兵"
            elif numparts == 2:
                survivorentries = f"(Ares3.0)第{numparts+1}阵营，一般为尤里阵营(ThirdSide)，单位建筑被摧毁时产生什么步兵。默认值为阵营设置的基础步兵"
            elif numparts == 3:
                survivorentries = f"(Ares3.0)第{numparts+1}阵营，一般为焚风阵营(FourthSide)，单位建筑被摧毁时产生什么步兵。默认值为阵营设置的基础步兵"
            else:
                survivorentries = f"(Ares3.0)第{numparts+1}阵营，单位建筑被摧毁时产生什么步兵。默认值为阵营设置的基础步兵。"
        else:
            survivorentries = "(Ares3.0)第“"+numparts+"+1”阵营，单位建筑被摧毁时产生什么步兵。默认值为阵营设置的基础步兵。"
    else:
        survivorentries = "Keyword not found."
    return survivorentries

campaignentries = ""
def CampaignEntries(keyword):
    if keyword[-6:] == ".image":
        num = keyword[8]
        campaignentries = "(Ares3.0)第"+num+"个任务入口按钮的样子，大小260x136，可参考fsalg.shp。默认fsalg.shp或fsslg.shp"
    elif keyword[-8:] == ".palette":
        num = keyword[8]
        campaignentries = "(Ares3.0)第"+num+"个任务入口按钮使用的色盘。默认fsalg.pal，fsslg.pal或fsbclg.pal"
    elif keyword[-8:] == ".subline":
        num = keyword[8]
        campaignentries = "(Ares3.0)第"+num+"个任务入口按钮下方的CSF。默认为STT:AlliedCampaignIcon，STT:SovietCampaignIcon或STT:CampaignAnimTutorial"
    elif keyword[-8:] == ".tooltip":
        num = keyword[8]
        campaignentries = "(Ares3.0)把鼠标放在第"+num+"个任务入口按钮上底部工具条显示的CSF。默认为Campaign"+num+".Subline"
    elif "." not in keyword:
        num = keyword.replace("campaign", "")
        campaignentries = "(Ares3.0)任务入口按按钮从第"+num+"关开始，必须在battle.ini里有，如果要隐藏按钮就写Campaign"+num+"=no。默认ALL1，SOV1，TUT1或norespectively"
    else:
        campaignentries = "Keyword not found."
    return campaignentries

slotentries = ""
def SlotEntries(keyword):
    if keyword[-13:] == ".displaycolor" and keyword != "slot.displaycolor":
        parts = keyword.split(".",1)
        numparts = parts[0]
        num = numparts.replace("slot", "")
        slotentries = "(Ares3.0)定制的玩家颜色，第"+num+"个颜色显示的颜色，填写格式为R,G,B"
    elif keyword[-12:] == ".colorscheme" and keyword != "slot.colorscheme":
        parts = keyword.split(".",1)
        numparts = parts[0]
        num = numparts.replace("slot", "")
        slotentries = "(Ares3.0)定制的玩家颜色，第"+num+"个颜色在rulesmd的[Colors]定义配色方案的名称"
    elif keyword[-8:] == ".tooltip" and keyword != "slot.tooltip":
        parts = keyword.split(".",1)
        numparts = parts[0]
        num = numparts.replace("slot", "")
        slotentries = "(Ares3.0)定制的玩家颜色，第"+num+"个颜色在底部工具条显示的CSF"
    else:
        slotentries = "Keyword not found."
    return slotentries

colorentries = ""
def ColorEntries(keyword):
    if keyword[-5:] == ".text":
        parts = keyword.split(".",2)
        buttonparts = parts[1]
        colorentries = "(Ares3.0)对于某些类型的控件的文本颜色，“"+buttonparts+"”可以是一个按钮，标签（描述），列表，复选框，组合框 （下拉列表），观察者（下拉列表中，选择与观察者），GroupBox（框架），滑块，或编辑 （文本框）。默认238,238,238（浅灰色）为观测器，即[UISettings]►Color，除了文本"
    elif keyword[-10:] == ".selection":
        parts = keyword.split(".",2)
        buttonparts = parts[1]
        colorentries = "对于某些类型的控件选定项的背景色，“"+buttonparts+"”可以是一个列表，ComboBox（下拉列表）或观察者（下拉列表中选择与观察者）。默认98,98,98（深黑）"
    elif keyword[-9:] == ".disabled":
        parts = keyword.split(".",2)
        buttonparts = parts[1]
        colorentries = "对某些类型的禁用控件的文本颜色，“"+buttonparts+"”可以是一个列表，ComboBox（下拉列表），观察者（下拉列表中选择与观察者）或滑块。默认167,0,0（深红) 按键，143,143,143（灰色）观察"
    else:
        colorentries = "Keyword not found."
    return colorentries

mecursorentries = ""
def MECursorEntries(keyword):
    if keyword.count('.') == 1:
        parts = keyword.split(".",1)
        cursorparts = parts[1]
        mecursorentries = "(Ares3.0)自定义鼠标动作"+cursorparts
    else:
        mecursorentries = "Keyword not found."
    return mecursorentries

lasertrailentries = ""
def LasertrailEntries(keyword):
    if keyword[-5:] == ".type":
        parts = keyword.split(".",1)
        numparts = parts[0]
        num = numparts.replace("lasertrail", "")
        mecursorentries = "(Phobos)在单位上附加激光尾迹，第"+num+"+1个激光尾迹的种类。"
    elif keyword[-4:] == ".flh":
        parts = keyword.split(".",1)
        numparts = parts[0]
        num = numparts.replace("lasertrail", "")
        mecursorentries = "(Phobos)在单位上附加激光尾迹，第"+num+"+1个激光尾迹的坐标。默认0，0，0。"
    elif keyword[-11:] == ".isonturret":
        parts = keyword.split(".",1)
        numparts = parts[0]
        num = numparts.replace("lasertrail", "")
        mecursorentries = "(Phobos)在单位上附加激光尾迹，第"+num+"+1个激光尾迹是否绘制在炮塔上。默认no。"
    else:
        mecursorentries = "Keyword not found."
    return mecursorentries

burstflhentries = ""
def BurstFLHEntries(keyword):
    if keyword[:6] == "primar":
        parts = keyword.split(".",1)
        numparts = parts[1]
        num = numparts.replace("burst", "")
        burstflhentries = "(Phobos)主武器Burst第"+num+"发的开火坐标。"
    elif keyword[:6] == "elitep":
        parts = keyword.split(".",1)
        numparts = parts[1]
        num = numparts.replace("burst", "")
        burstflhentries = "(Phobos)精英级主武器Burst第"+num+"发的开火坐标。"
    elif keyword[:6] == "second":
        parts = keyword.split(".",1)
        numparts = parts[1]
        num = numparts.replace("burst", "")
        burstflhentries = "(Phobos)副武器Burst第"+num+"发的开火坐标。"
    elif keyword[:6] == "'elites":
        parts = keyword.split(".",1)
        numparts = parts[1]
        num = numparts.replace("burst", "")
        burstflhentries = "(Phobos)精英级副武器Burst第"+num+"发的开火坐标。"
    elif keyword[:6] == "weapon":
        parts = keyword.split(".",1)
        numpart1 = parts[0]
        num1 = numpart1.replace("weapon", "")
        num1 = num1.replace("flh", "")
        numpart2 = parts[1]
        num2 = numpart2.replace("burst", "")
        burstflhentries = "(Phobos)第"+num1+"个武器Burst第"+num2+"发的开火坐标，用于盖特，IFV，充能炮塔等逻辑。"
    elif keyword[:11] == "eliteweapon":
        parts = keyword.split(".",1)
        numpart1 = parts[0]
        num1 = numpart1.replace("eliteweapon", "")
        num1 = num1.replace("flh", "")
        numpart2 = parts[1]
        num2 = numpart2.replace("burst", "")
        burstflhentries = "(Phobos)第"+num1+"个精英级武器Burst第"+num2+"发的开火坐标，用于盖特，IFV，充能炮塔等逻辑。"
    else:
        burstflhentries = "Keyword not found."
    return burstflhentries