# -*- coding: utf-8 -*-
import mod.server.extraServerApi as serverApi

class PlayerAbility(object):
    def __init__(self, playerId):
        self.playerId = playerId

    def getAllAbilities(self):
        # type: () -> dict
        """
        获取玩家具体权限
        :return: dict 权限字段的布尔值集合，如：
            {
              'teleport': True,
              'opencontainers': True,
              'mine': True,
              'build': True,
              'op': True,
              'attackmobs': True,
              'doorsandswitches': True,
              'attackplayers': True
            }
        备注：
          * build -> 放置方块
          * mine -> 采集方块
          * doorsandswitches -> 使用门和开关
          * opencontainers -> 打开容器
          * attackplayers -> 攻击玩家
          * attackmobs -> 攻击生物
          * op -> 操作员命令
          * teleport -> 使用传送
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
            operation = comp.GetPlayerAbilities()
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.GetPlayerAbilities()

    def setAttackMobsAbility(self, canAttack):
        # type: (bool) -> bool
        """
        设置玩家能否攻击生物
        :param canAttack: bool True可攻击生物，False禁止攻击生物
        :return: bool 是否设置成功
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
            comp.SetAttackMobsAbility(False)
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.SetAttackMobsAbility(canAttack)

    def setAttackPlayersAbility(self, canAttack):
        # type: (bool) -> bool
        """
        设置玩家能否攻击其他玩家
        :param canAttack: bool True可攻击其他玩家，False禁止攻击其他玩家
        :return: bool 是否设置成功
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
            comp.SetAttackPlayersAbility(False)
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.SetAttackPlayersAbility(canAttack)

    def setBuildAbility(self, canBuild):
        # type: (bool) -> bool
        """
        设置玩家能否放置方块（生存模式下有效，会存档）
        :param canBuild: bool True可以放置，False禁止放置
        :return: bool 是否设置成功
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
            comp.SetBuildAbility(False)
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.SetBuildAbility(canBuild)

    def setMineAbility(self, canMine):
        # type: (bool) -> bool
        """
        设置玩家能否摧毁方块（生存模式下有效，会存档）
        :param canMine: bool True可以摧毁，False禁止摧毁
        :return: bool 是否设置成功
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
            comp.SetMineAbility(False)
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.SetMineAbility(canMine)

    def setOpenContainersAbility(self, canOpen):
        # type: (bool) -> bool
        """
        设置玩家能否打开容器
        :param canOpen: bool True可以打开，False禁止打开
        :return: bool 是否设置成功
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
            comp.SetOpenContainersAbility(False)
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.SetOpenContainersAbility(canOpen)

    def setOperateDoorsAndSwitchesAbility(self, canOperate):
        # type: (bool) -> bool
        """
        设置玩家能否与门和开关交互
        :param canOperate: bool True可以交互，False禁止交互
        :return: bool 是否设置成功
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
            comp.SetOperateDoorsAndSwitchesAbility(False)
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.SetOperateDoorsAndSwitchesAbility(canOperate)

    def setOperatorCommandAbility(self, canOperate):
        # type: (bool) -> bool
        """
        设置玩家是否具有操作员命令权限
        :param canOperate: bool True可执行操作员命令，False禁用
        :return: bool 是否设置成功
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
            comp.SetOperatorCommandAbility(False)
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.SetOperatorCommandAbility(canOperate)

    def setPermissionLevel(self, level):
        # type: (int) -> bool
        """
        设置玩家权限等级
        :param level: int 权限等级 0=访客,1=成员,2=操作员,3=自定义
        :return: bool 是否设置成功
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
            comp.SetPermissionLevel(3)
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.SetPermissionLevel(level)

    def setMute(self, isMute):
        # type: (bool) -> bool
        """
        设置玩家是否禁言（不存档）
        :param isMute: bool True禁言，False取消禁言
        :return: bool 是否设置成功
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
            comp.SetPlayerMute(True)
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.SetPlayerMute(isMute)

    def setTeleportAbility(self, canTeleport):
        # type: (bool) -> bool
        """
        设置玩家能否使用TP指令
        :param canTeleport: bool True可使用TP指令，False禁止
        :return: bool 是否设置成功
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
            comp.SetTeleportAbility(False)
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.SetTeleportAbility(canTeleport)

    def _get(self, key):
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.GetPlayerAbilities().get(key)

    teleport = property(
        lambda self: self._get("teleport"),
        lambda self, value: self.setTeleportAbility(value),
        None,
        "使用传送"
    )

    opencontainers = property(
        lambda self: self._get("opencontainers"),
        lambda self, value: self.setOpenContainersAbility(value),
        None,
        "打开容器"
    )

    mine = property(
        lambda self: self._get("mine"),
        lambda self, value: self.setMineAbility(value),
        None,
        "采集方块"
    )

    build = property(
        lambda self: self._get("build"),
        lambda self, value: self.setBuildAbility(value),
        None,
        "放置方块"
    )

    op = property(
        lambda self: self._get("op"),
        lambda self, value: self.setOperatorCommandAbility(value),
        None,
        "操作员命令"
    )

    attackmobs = property(
        lambda self: self._get("attackmobs"),
        lambda self, value: self.setAttackMobsAbility(value),
        None,
        "攻击生物"
    )

    doorsandswitches = property(
        lambda self: self._get("doorsandswitches"),
        lambda self, value: self.setOperateDoorsAndSwitchesAbility(value),
        None,
        "使用门和开关"
    )

    attackplayers = property(
        lambda self: self._get("attackplayers"),
        lambda self, value: self.setAttackPlayersAbility(value),
        None,
        "攻击玩家"
    )
