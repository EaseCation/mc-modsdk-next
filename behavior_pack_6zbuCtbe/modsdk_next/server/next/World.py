# -*- coding: utf-8 -*-
import mod.server.extraServerApi as serverApi

from .Dimension import Dimension
from .GameRules import GameRules
from .Player import Player
from .Entity import Entity
from .event.WorldEvents import WorldEvents

class World(object):

    def __init__(self):
        self.levelId = serverApi.GetLevelId()
        self.events = WorldEvents()
        self.gameRules = GameRules()

    def getAllPlayers(self):
        # type: () -> list[Player]
        """
        获取世界中的所有玩家
        :return: 玩家对象列表
        """
        players = []
        for playerId in serverApi.GetPlayerList():
            players.append(Player(playerId))
        return players

    def getEntity(self, entityId):
        # type: (str) -> Entity
        """
        获取实体对象
        :param entityId: 实体ID
        :return: 实体对象
        """
        return Entity(entityId)

    def getDimension(self, dimensionId):
        # type: (int) -> Dimension
        """
        获取维度对象
        :param dimensionId: 维度ID
        :return: 维度对象
        """
        return Dimension(dimensionId)

    def createDimension(self, dimensionId):
        # type: (int) -> Dimension | None
        """
        创建新的 Dimension (仅在dimensionId大于20时有意义；0/1/2不需要创建)
        :return: Dimension 创建后的Dimension对象，如果失败则返回None
        备注：
          * 维度21不可用
          * 建议在mod初始化时统一调用
          * 若想对主世界进行出生点设置等操作，需确保先CreateDimension(0)
        示例:
            comp = serverApi.GetEngineCompFactory().CreateDimension(levelId)
            comp.CreateDimension(3)
        """
        dimComp = serverApi.GetEngineCompFactory().CreateDimension(serverApi.GetLevelId())
        if dimComp.CreateDimension(dimensionId):
            return Dimension(dimensionId)
        return None

    def getCommandPermissionLevel(self):
        # type: () -> int
        """
        获取当玩家使用/op命令时的OP权限等级
        :return: int 权限等级
                 1 -> OP可以绕过重生点保护
                 2 -> OP可以使用所有单人游戏作弊命令
                 3 -> OP可以使用大多数多人游戏中独有的命令
                 4 -> OP可以使用所有命令
        示例:
            comp = serverApi.GetEngineCompFactory().CreateCommand(levelId)
            opLevel = comp.GetCommandPermissionLevel()
        """
        cmdComp = serverApi.GetEngineCompFactory().CreateCommand(self.levelId)
        return cmdComp.GetCommandPermissionLevel()

    def getDefaultPlayerPermissionLevel(self):
        # type: () -> int
        """
        返回新玩家加入时的权限身份
        :return: int 权限身份
                 0 -> Visitor
                 1 -> Member
                 2 -> Operator
                 3 -> 自定义
        示例:
            comp = serverApi.GetEngineCompFactory().CreateCommand(levelId)
            level = comp.GetDefaultPlayerPermissionLevel()
        """
        cmdComp = serverApi.GetEngineCompFactory().CreateCommand(self.levelId)
        return cmdComp.GetDefaultPlayerPermissionLevel()

    def runCommand(self, cmdStr, entityId=None, showOutput=False):
        # type: (str, str, bool) -> bool
        """
        使用游戏内指令
        :param cmdStr: str 指令
        :param entityId: str 指令执行者(可选，若不指定则随机选一个玩家)
        :param showOutput: bool 是否显示输出到聊天窗口，默认False
        :return: bool 命令是否执行成功
        备注：
          * 若entityId不是玩家，则即使showOutput=True也不会输出到聊天窗口
        示例:
            comp = serverApi.GetEngineCompFactory().CreateCommand(levelId)
            comp.SetCommand("/tp @p 100 5 100")
        """
        cmdComp = serverApi.GetEngineCompFactory().CreateCommand(self.levelId)
        return cmdComp.SetCommand(cmdStr, entityId, showOutput)

    def setDefaultOpPermissionLevel(self, opLevel):
        # type: (int) -> bool
        """
        设置当玩家使用/op命令时OP的权限等级
        :param opLevel: int 权限等级(1~4)
        :return: bool 是否设置成功
        备注：
          * 不会修改已经获取到op的玩家权限等级
          * 建议在游戏初始化时调用
        示例:
            comp = serverApi.GetEngineCompFactory().CreateCommand(levelId)
            opLevel = 4
            suc = comp.SetCommandPermissionLevel(opLevel)
        """
        cmdComp = serverApi.GetEngineCompFactory().CreateCommand(self.levelId)
        return cmdComp.SetCommandPermissionLevel(opLevel)

    def setDefaultPlayerPermissionLevel(self, opLevel):
        # type: (int) -> bool
        """
        设置新玩家加入时的权限身份
        :param opLevel: int 0=Visitor,1=Member,2=Operator,3=自定义
        :return: bool 是否设置成功
        备注：
          * 不会修改已加入过游戏的玩家权限身份
          * 建议在游戏初始化时调用
        示例:
            comp = serverApi.GetEngineCompFactory().CreateCommand(levelId)
            opLevel = 1
            suc = comp.SetDefaultPlayerPermissionLevel(opLevel)
        """
        cmdComp = serverApi.GetEngineCompFactory().CreateCommand(self.levelId)
        return cmdComp.SetDefaultPlayerPermissionLevel(opLevel)

    # 消息相关

    def broadcastMessage(self, message, color = None):
        # type: (str, str) -> None
        """
        广播消息
        :param message: str 消息
        :param color: str 颜色
        示例:
            world.broadcastMessage("消息", "§e")
        """
        comp = serverApi.GetEngineCompFactory().CreateGame(self.levelId)
        comp.SetNotifyMsg(message, color)

    def broadcastPopup(self, message, subTitle):
        # type: (str, str) -> None
        """
        以弹窗形式广播消息
        :param message: str 主消息
        :param subTitle: str 副消息
        示例:
            world.broadcastPopup("主消息", "副消息")
        """
        comp = serverApi.GetEngineCompFactory().CreateGame(self.levelId)
        comp.SetPopupNotice(message, subTitle)

    def broadcastTip(self, message):
        # type: (str) -> None
        """
        广播 Tip
        :param message: str Tip提示内容
        示例:
            world.broadcastTip("提示")
        """
        comp = serverApi.GetEngineCompFactory().CreateGame(self.levelId)
        comp.SetTipMessage(message)

    # 时间

    def getAbsoluteTime(self):
        # type: () -> int
        """
        当前时间，单位为帧数，表示该存档从新建起经过的时间，而非当前游戏天内的时间。
        mc中一个游戏天相当于现实的20分钟，即24000帧
        注意关闭昼夜更替后当前世界的时间会暂停
        :return: int 时间
        """
        comp = serverApi.GetEngineCompFactory().CreateTime(self.levelId)
        return comp.GetTime()

    def getDay(self):
        # type: () -> int
        """
        获取当前游戏天数
        :return: int 天数
        """
        comp = serverApi.GetEngineCompFactory().CreateTime(self.levelId)
        return int(comp.GetTime() / 24000)

    def getTimeOfDay(self):
        # type: () -> int
        """
        获取当前游戏时间
        :return: int 时间
        """
        comp = serverApi.GetEngineCompFactory().CreateTime(self.levelId)
        return comp.GetTime() % 24000

    def setTimeOfDay(self, time):
        # type: (int) -> bool
        """
        设置当前世界在一天内所在的时间
        :param time: int 时间，单位为帧数，表示游戏天内的时间，范围为0到24000。mc中一个游戏天相当于现实的20分钟，即24000帧
        """
        comp = serverApi.GetEngineCompFactory().CreateTime(self.levelId)
        return comp.SetTime(time)

    # 天气

    def isRaining(self):
        # type: () -> bool
        """
        是否下雨
        :return: bool 是否下雨
        """
        comp = serverApi.GetEngineCompFactory().CreateWeather(self.levelId)
        return comp.IsRaining()

    def setRaining(self, level, ticks):
        # type: (float, int) -> bool
        """
        设置是下雨
        :param level: float 下雨强度，范围为0-1
        :param ticks: int 天气的持续时间，单位为帧，一秒20帧。持续时间结束后会自动转换为相反的天气。注意，需要在游戏设置中开启天气更替后该参数才会生效。
        """
        comp = serverApi.GetEngineCompFactory().CreateWeather(self.levelId)
        return comp.SetRaining(level, ticks)

    def isThundering(self):
        # type: () -> bool
        """
        是否打雷
        :return: bool 是否打雷
        """
        comp = serverApi.GetEngineCompFactory().CreateWeather(self.levelId)
        return comp.IsThunder()

    def setThundering(self, level, ticks):
        # type: (float, int) -> bool
        """
        设置是否打雷
        :param level: float 打雷强度，范围为0-1
        :param ticks: int 天气的持续时间，单位为帧，一秒20帧。持续时间结束后会自动转换为相反的天气。注意，需要在游戏设置中开启天气更替后该参数才会生效。
        """
        comp = serverApi.GetEngineCompFactory().CreateWeather(self.levelId)
        return comp.SetThunder(level, ticks)