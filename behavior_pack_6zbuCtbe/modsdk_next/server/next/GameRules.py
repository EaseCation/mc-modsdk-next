# -*- encoding: utf-8 -*-
import mod.server.extraServerApi as serverApi

class GameRules(object):

    def __init__(self):
        pass

    def getFullGameRulesInfo(self):
        # type: () -> dict
        """
        获取游戏规则
        :return: 游戏规则
        """
        comp = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
        return comp.GetGameRulesInfoServer()

    def setFullGameRulesInfo(self, gameRules):
        # type: (dict) -> None
        """
        设置游戏规则
        :param gameRules: 游戏规则
        """
        comp = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
        comp.SetGameRulesInfoServer(gameRules)

    def _get(self, rule_type, key):
        comp = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
        gameRules = comp.GetGameRulesInfoServer()
        return gameRules.get(rule_type, {}).get(key)

    def _set(self, rule_type, key, value):
        comp = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
        gameRules = comp.GetGameRulesInfoServer() or {}
        if rule_type not in gameRules:
            gameRules[rule_type] = {}
        gameRules[rule_type][key] = value
        comp.SetGameRulesInfoServer(gameRules)

    # 以下为 option_info 类型的属性定义

    pvp = property(
        lambda self: self._get("option_info", "pvp"),
        lambda self, value: self._set("option_info", "pvp", value),
        None,
        "玩家间伤害"
    )

    showCoordinates = property(
        lambda self: self._get("option_info", "show_coordinates"),
        lambda self, value: self._set("option_info", "show_coordinates", value),
        None,
        "显示坐标"
    )

    fireSpreads = property(
        lambda self: self._get("option_info", "fire_spreads"),
        lambda self, value: self._set("option_info", "fire_spreads", value),
        None,
        "火焰蔓延"
    )

    tntExplodes = property(
        lambda self: self._get("option_info", "tnt_explodes"),
        lambda self, value: self._set("option_info", "tnt_explodes", value),
        None,
        "TNT爆炸"
    )

    mobLoot = property(
        lambda self: self._get("option_info", "mob_loot"),
        lambda self, value: self._set("option_info", "mob_loot", value),
        None,
        "生物战利品"
    )

    naturalRegeneration = property(
        lambda self: self._get("option_info", "natural_regeneration"),
        lambda self, value: self._set("option_info", "natural_regeneration", value),
        None,
        "自然生命恢复"
    )

    respawnBlockExplosion = property(
        lambda self: self._get("option_info", "respawn_block_explosion"),
        lambda self, value: self._set("option_info", "respawn_block_explosion", value),
        None,
        "重生方块爆炸"
    )

    respawnRadius = property(
        lambda self: self._get("option_info", "respawn_radius"),
        lambda self, value: self._set("option_info", "respawn_radius", value),
        None,
        "重生半径（支持范围：[0,128]）"
    )

    tileDrops = property(
        lambda self: self._get("option_info", "tile_drops"),
        lambda self, value: self._set("option_info", "tile_drops", value),
        None,
        "方块掉落"
    )

    immediateRespawn = property(
        lambda self: self._get("option_info", "immediate_respawn"),
        lambda self, value: self._set("option_info", "immediate_respawn", value),
        None,
        "立即重生"
    )

    # 以下为 cheat_info 类型的属性定义

    enableCheat = property(
        lambda self: self._get("cheat_info", "enable"),
        lambda self, value: self._set("cheat_info", "enable", value),
        None,
        "激活作弊"
    )

    alwaysDay = property(
        lambda self: self._get("cheat_info", "always_day"),
        lambda self, value: self._set("cheat_info", "always_day", value),
        None,
        "终为白日"
    )

    mobGriefing = property(
        lambda self: self._get("cheat_info", "mob_griefing"),
        lambda self, value: self._set("cheat_info", "mob_griefing", value),
        None,
        "生物破坏"
    )

    keepInventory = property(
        lambda self: self._get("cheat_info", "keep_inventory"),
        lambda self, value: self._set("cheat_info", "keep_inventory", value),
        None,
        "保留物品栏"
    )

    weatherCycle = property(
        lambda self: self._get("cheat_info", "weather_cycle"),
        lambda self, value: self._set("cheat_info", "weather_cycle", value),
        None,
        "天气更替"
    )

    mobSpawn = property(
        lambda self: self._get("cheat_info", "mob_spawn"),
        lambda self, value: self._set("cheat_info", "mob_spawn", value),
        None,
        "生物生成"
    )

    entitiesDropLoot = property(
        lambda self: self._get("cheat_info", "entities_drop_loot"),
        lambda self, value: self._set("cheat_info", "entities_drop_loot", value),
        None,
        "实体掉落战利品"
    )

    daylightCycle = property(
        lambda self: self._get("cheat_info", "daylight_cycle"),
        lambda self, value: self._set("cheat_info", "daylight_cycle", value),
        None,
        "开启昼夜更替"
    )

    commandBlocksEnabled = property(
        lambda self: self._get("cheat_info", "command_blocks_enabled"),
        lambda self, value: self._set("cheat_info", "command_blocks_enabled", value),
        None,
        "启用命令方块"
    )

    randomTickSpeed = property(
        lambda self: self._get("cheat_info", "random_tick_speed"),
        lambda self, value: self._set("cheat_info", "random_tick_speed", value),
        None,
        "随机刻速度"
    )

    # 其他的网易API
    def addBannedItem(self, itemName):
        # type: (str) -> bool
        """
        添加禁用物品
        :param itemName: 物品标识符，格式[namespace:name:auxvalue]，auxvalue默认为0，auxvalue为*时候匹配任意auxvalue值。例如：minecraft:egg（也可以通过填写配置文件config/banned_items.json进行启动禁用）
        :return: 是否增加成功
        """
        comp = serverApi.GetEngineCompFactory().CreateItemBanned(serverApi.GetLevelId())
        return comp.AddBannedItem(itemName)