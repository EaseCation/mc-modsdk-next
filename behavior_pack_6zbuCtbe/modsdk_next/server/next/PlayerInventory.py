# -*- coding: utf-8 -*-
import mod.server.extraServerApi as serverApi

class PlayerInventory(object):
    def __init__(self, playerId):
        self.playerId = playerId

    def addItemEnchant(self, slotPos, enchantType, level):
        # type: (int, int, int) -> bool
        """
        给物品栏的物品添加附魔信息
        :param slotPos: int 物品栏槽位
        :param enchantType: int 附魔类型，可通过 serverApi.GetMinecraftEnum().EnchantType 获取
        :param level: int 附魔等级
        :return: bool 设置结果
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
            comp.AddEnchantToInvItem(0, serverApi.GetMinecraftEnum().EnchantType.BowDamage, 2)
        """
        comp = serverApi.GetEngineCompFactory().CreateItem(self.playerId)
        return comp.AddEnchantToInvItem(slotPos, enchantType, level)

    def addItemModEnchant(self, slotPos, modEnchantId, level):
        # type: (int, str, int) -> bool
        """
        给物品栏中物品添加自定义附魔信息
        :param slotPos: int 物品栏槽位
        :param modEnchantId: str 自定义附魔identifier
        :param level: int 自定义附魔等级
        :return: bool 设置结果
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
            comp.AddModEnchantToInvItem(0, "customenchant", 2)
        """
        comp = serverApi.GetEngineCompFactory().CreateItem(self.playerId)
        return comp.AddModEnchantToInvItem(slotPos, modEnchantId, level)

    def setItemTipsAndExtraId(self, posType, slotPos, customTips, extraId):
        # type: (int, int, str, str) -> bool
        """
        修改玩家物品的自定义tips和自定义标识符（不支持盔甲栏）
        :param posType: int ItemPosType枚举
        :param slotPos: int 物品栏槽位
        :param customTips: str 物品的自定义tips
        :param extraId: str 物品的自定义标识符
        :return: bool 设置结果
        备注：
          * 不支持盔甲栏
          * 若需要更灵活的修改，建议使用 GetEntityItem & SetEntityItem
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
            comp.ChangePlayerItemTipsAndExtraId(
                serverApi.GetMinecraftEnum().ItemPosType.INVENTORY,
                0,
                "自定义tips",
                "自定义标识符"
            )
        """
        comp = serverApi.GetEngineCompFactory().CreateItem(self.playerId)
        return comp.ChangePlayerItemTipsAndExtraId(posType, slotPos, customTips, extraId)

    def setHeldItemIndex(self, slot):
        # type: (int) -> bool
        """
        设置玩家当前选中快捷栏物品的index
        :param slot: int 快捷栏物品的index, 范围0~8
        :return: bool 是否设置成功
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
            success = comp.ChangeSelectSlot(0)
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.ChangeSelectSlot(slot)

    def getItemEnchantData(self, slotPos):
        # type: (int) -> list
        """
        获取物品栏物品的附魔信息
        :param slotPos: int 物品栏槽位
        :return: list(tuple(int,int)) 每个tuple为(附魔类型, 附魔等级)，无附魔则返回空列表
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
            comp.GetInvItemEnchantData(0)
        """
        comp = serverApi.GetEngineCompFactory().CreateItem(self.playerId)
        return comp.GetInvItemEnchantData(slotPos)

    def getItemModEnchantData(self, slotPos):
        # type: (int) -> list
        """
        获取物品栏物品的自定义附魔信息
        :param slotPos: int 物品栏槽位
        :return: list(tuple(str,int)) 每个tuple为(自定义附魔id, 附魔等级)，无附魔则空列表
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
            comp.GetInvItemModEnchantData(0)
        """
        comp = serverApi.GetEngineCompFactory().CreateItem(self.playerId)
        return comp.GetInvItemModEnchantData(slotPos)

    def getAllItems(self, posType, getUserData=False):
        # type: (int, bool) -> list
        """
        获取玩家指定槽位的批量物品信息（服务端接口）
        :param posType: int ItemPosType枚举
        :param getUserData: bool 是否获取userData，默认为False
        :return: list(dict) 物品信息字典的数组，对应每个槽位；没有物品的位置为None
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
            comp.GetPlayerAllItems(serverApi.GetMinecraftEnum().ItemPosType.INVENTORY)
        """
        comp = serverApi.GetEngineCompFactory().CreateItem(self.playerId)
        return comp.GetPlayerAllItems(posType, getUserData)

    def getItem(self, posType, slotPos, getUserData=False):
        # type: (int, int, bool) -> dict
        """
        获取玩家物品（服务端接口）
        :param posType: int ItemPosType枚举
        :param slotPos: int 槽位；若获取INVENTORY或ARMOR需要该参数，其他情况0即可
        :param getUserData: bool 是否获取userData，默认为False
        :return: dict 物品信息字典，没有物品则返回None
        备注：
          * 可获取背包、盔甲栏、副手、主手物品
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
            comp.GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.INVENTORY, 0)
        """
        comp = serverApi.GetEngineCompFactory().CreateItem(self.playerId)
        return comp.GetPlayerItem(posType, slotPos, getUserData)

    def getHeldItemIndex(self):
        # type: () -> int
        """
        获取玩家当前选中的快捷栏槽位
        :return: int 当前槽位，错误时返回-1
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
            comp.GetSelectSlotId()
        """
        comp = serverApi.GetEngineCompFactory().CreateItem(self.playerId)
        return comp.GetSelectSlotId()

    def removeItemEnchant(self, slotPos, enchantType):
        # type: (int, int) -> bool
        """
        给物品栏的物品移除指定附魔信息
        :param slotPos: int 物品栏槽位
        :param enchantType: int 附魔类型
        :return: bool 移除结果
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
            comp.RemoveEnchantToInvItem(0, serverApi.GetMinecraftEnum().EnchantType.BowDamage)
        """
        comp = serverApi.GetEngineCompFactory().CreateItem(self.playerId)
        return comp.RemoveEnchantToInvItem(slotPos, enchantType)

    def removeItemModEnchant(self, slotPos, modEnchantId):
        # type: (int, str) -> bool
        """
        给物品栏的物品移除自定义附魔信息
        :param slotPos: int 物品栏槽位
        :param modEnchantId: str 自定义附魔identifier
        :return: bool 移除结果
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
            comp.RemoveModEnchantToInvItem(0, "customenchant")
        """
        comp = serverApi.GetEngineCompFactory().CreateItem(self.playerId)
        return comp.RemoveModEnchantToInvItem(slotPos, modEnchantId)

    def swapItems(self, slotIndex1, slotIndex2):
        # type: (int, int) -> bool
        """
        交换玩家背包物品（背包内两个槽位的物品对调）
        :param slotIndex1: int 物品位置
        :param slotIndex2: int 物品位置
        :return: bool 设置结果
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
            comp.SetInvItemExchange(0, 2)
        """
        comp = serverApi.GetEngineCompFactory().CreateItem(self.playerId)
        return comp.SetInvItemExchange(slotIndex1, slotIndex2)

    def setItemCount(self, slotPos, num):
        # type: (int, int) -> bool
        """
        设置玩家背包物品数目
        :param slotPos: int 物品栏槽位
        :param num: int 物品数量，设置为0可清除该槽位物品
        :return: bool 设置结果
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
            comp.SetInvItemNum(0, 10)
        """
        comp = serverApi.GetEngineCompFactory().CreateItem(self.playerId)
        return comp.SetInvItemNum(slotPos, num)

    def setAllItems(self, itemsDictMap):
        # type: (dict) -> dict
        """
        添加批量物品信息到指定槽位
        :param itemsDictMap: dict 需要添加的物品映射表
                             key是tuple(ItemPosType, slotPos)
                             value是物品信息字典
        :return: dict 设置结果, key同itemsDictMap, value为bool表示是否设置成功
        示例:
            import mod.server.extraServerApi as serverApi
            itemsDict = {
                'itemName': 'minecraft:bow',
                'count': 1,
                'enchantData': [(serverApi.GetMinecraftEnum().EnchantType.BowDamage, 1)],
                'auxValue': 0,
                'customTips': '§c new item §r',
                'extraId': 'abc',
                'userData': {}
            }
            comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
            itemsDictMap = {}
            itemsDictMap[(minecraftEnum.ItemPosType.INVENTORY, 0)] = itemsDict
            comp.SetPlayerAllItems(itemsDictMap)
        """
        comp = serverApi.GetEngineCompFactory().CreateItem(self.playerId)
        return comp.SetPlayerAllItems(itemsDictMap)

    def setItemInHand(self, itemDict, playerId):
        # type: (dict, str) -> bool
        """
        生成物品到玩家右手
        :param itemDict: dict 物品信息字典
        :param playerId: str 玩家id
        :return: bool 设置结果
        示例:
            import mod.server.extraServerApi as serverApi
            itemDict = {
                'itemName': 'minecraft:bow',
                'count': 1,
                'enchantData': [(serverApi.GetMinecraftEnum().EnchantType.BowDamage, 1)],
                'auxValue': 0,
                'customTips': '§c new item §r',
                'extraId': 'abc',
                'userData': {}
            }
            comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
            comp.SpawnItemToPlayerCarried(itemDict, playerId)
        """
        comp = serverApi.GetEngineCompFactory().CreateItem(self.playerId)
        return comp.SpawnItemToPlayerCarried(itemDict, playerId)

    def addItem(self, itemDict, playerId, slotPos=None):
        # type: (dict, str, int) -> bool
        """
        生成物品到玩家背包
        :param itemDict: dict 物品信息字典
        :param playerId: str 玩家id
        :param slotPos: int 背包槽位(可选)。若不指定则系统会自动寻找空槽或可叠加槽
        :return: bool 设置结果
        备注：
          * 若背包中物品数量超出64，则会生成至64，但接口会返回失败
        示例:
            import mod.server.extraServerApi as serverApi
            itemDict = {
                'itemName': 'minecraft:bow',
                'count': 1,
                'enchantData': [(serverApi.GetMinecraftEnum().EnchantType.BowDamage, 1)],
                'auxValue': 0,
                'customTips': '§c new item §r',
                'extraId': 'abc',
                'userData': {}
            }
            comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
            comp.SpawnItemToPlayerInv(itemDict, playerId, 0)
        """
        comp = serverApi.GetEngineCompFactory().CreateItem(self.playerId)
        if slotPos is not None:
            return comp.SpawnItemToPlayerInv(itemDict, playerId, slotPos)
        else:
            return comp.SpawnItemToPlayerInv(itemDict, playerId)

