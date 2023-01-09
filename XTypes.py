armorentries = ""
def ArmorEntries(keyword):
    if keyword[-10:] == ".forcefire" and keyword != "versus.forcefire":
        parts = keyword.split(".",2)
        armorparts = parts[1]
        armorentries = "是否可以对"+armorparts+"护甲强行攻击"
    elif keyword[-10:] == ".retaliate" and keyword != "versus.retaliate":
        parts = keyword.split(".",2)
        armorparts = parts[1]
        armorentries = "是否可以对"+armorparts+"护甲反击"
    elif keyword[-15:] == ".passiveacquire" and keyword != "versus.passiveacquire":
        parts = keyword.split(".",2)
        armorparts = parts[1]
        armorentries = "是否可以对"+armorparts+"护甲主动攻击"
    elif keyword.count('.') == 1:
        parts = keyword.split(".",1)
        armorparts = parts[1]
        armorentries = "该弹头对"+armorparts+"护甲的伤害百分比"
    else:
        armorentries = "Keyword not found."
    return armorentries