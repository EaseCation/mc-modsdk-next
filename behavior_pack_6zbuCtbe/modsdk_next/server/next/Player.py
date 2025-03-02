# -*- coding: utf-8 -*-
import mod.server.extraServerApi as serverApi
from Entity import Entity
from modsdk_next.server.next.PlayerAbility import PlayerAbility
from modsdk_next.server.next.PlayerInventory import PlayerInventory


class Player(Entity):

    def __init__(self, playerId):
        super(Player, self).__init__(playerId)

    # 玩家游戏模式
    def getGameType(self):
        # type: () -> int
        """
        获取玩家的游戏模式
        :return: int 返回GameType枚举值（0: 生存模式, 1: 创造模式, 2: 冒险模式）<source_id data="1-ModAPI_接口_玩家_游戏模式.md" />
        """
        comp = serverApi.GetEngineCompFactory().CreateGame(self.playerId)
        return comp.GetPlayerGameType(self.playerId)

    def setGameType(self, gameType):
        # type: (int) -> bool
        """
        设置玩家的游戏模式
        :param gameType: 游戏模式的枚举值（0: 生存模式, 1: 创造模式, 2: 冒险模式）
        :return: bool 是否设置成功 <source_id data="1-ModAPI_接口_玩家_游戏模式.md" />
        注意：gameType 参数应使用 serverApi.GetMinecraftEnum().GameType.* 的值。
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.SetPlayerGameType(gameType)

    # 玩家属性

    def addExperience(self, exp):
        # type: (int) -> bool
        """
        增加玩家经验值
        :param exp: 玩家经验值，可设置负数
        :return: bool 是否成功
        备注：
          * 如果设置的exp值为负数，且超过当前等级已有的经验值，调用接口后，该玩家等级不会下降但是经验值会置为最小值
        """
        comp = serverApi.GetEngineCompFactory().CreateExp(self.playerId)
        return comp.AddPlayerExperience(exp)

    def addLevel(self, level):
        # type: (int) -> bool
        """
        修改玩家等级
        :param level: 玩家等级，可设置负数
        :return: bool 是否成功
        """
        comp = serverApi.GetEngineCompFactory().CreateLv(self.playerId)
        return comp.AddPlayerLevel(level)

    def collectOnlineClientData(self, collectTypes, callback, extraArgs=None):
        # type: (list, callable, dict) -> None
        """
        收集在线玩家客户端数据，用于判断玩家是否作弊
        :param collectTypes: list(str) 数据类型，不同类型收集到不同数据
        :param callback: function 回调函数，用于分析数据并判断玩家是否作弊
                         第一个参数为playerId(str)，第二个参数为收集到的数据(dict 或 None)
        :param extraArgs: dict 默认为None，根据collectTypes传入不同参数
        :return: None
        备注：
          * collectTypes 中的类型说明：
            - "game"：返回 { "gameType": int, "levelGravity": float }
            - "player"：返回 { "playerHealth": int }
            - "world"：返回 { "blockName": str, "blockAuxValue": int }，需在 extraArgs 中提供 "pos"
            - "entity"：返回 { "entityPos": tuple(float,float,float), "entityGravity": float }，需在 extraArgs 中提供 "entityId"
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.CollectOnlineClientData(collectTypes, callback, extraArgs)

    def getEnchantmentSeed(self):
        # type: () -> int
        """
        获取玩家的附魔种子
        :return: int 附魔种子
        备注：
          * 该属性会自动存档
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.GetEnchantmentSeed()

    def getExp(self, isPercent):
        # type: (bool) -> float
        """
        获取玩家当前等级下的经验值
        :param isPercent: bool 是否为百分比
        :return: float 玩家经验值
        备注：
          * 如果返回百分比为False，则返回玩家当前等级下经验的绝对值（非总经验值）
        """
        comp = serverApi.GetEngineCompFactory().CreateExp(self.playerId)
        return comp.GetPlayerExp(isPercent)

    def getHealthLevel(self):
        # type: () -> int
        """
        获取玩家健康临界值
        :return: int 健康临界值，-1表示获取失败
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.GetPlayerHealthLevel()

    def getHealthTick(self):
        # type: () -> int
        """
        获取玩家自然恢复速度
        :return: int 自然恢复速度，-1表示获取失败
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.GetPlayerHealthTick()

    def getHunger(self):
        # type: () -> float
        """
        获取玩家饥饿度
        :return: float 玩家饥饿度
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.GetPlayerHunger()

    def getLevel(self):
        # type: () -> int
        """
        获取玩家等级
        :return: int 玩家等级
        """
        comp = serverApi.GetEngineCompFactory().CreateLv(self.playerId)
        return comp.GetPlayerLevel()

    def getMaxExhaustionValue(self):
        # type: () -> float
        """
        获取玩家 foodExhaustionLevel 的归零值
        :return: float 归零值
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.GetPlayerMaxExhaustionValue()

    def getStarveLevel(self):
        # type: () -> int
        """
        获取玩家饥饿临界值
        :return: int 饥饿临界值，-1表示获取失败
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.GetPlayerStarveLevel()

    def getStarveTick(self):
        # type: () -> int
        """
        获取玩家饥饿掉血速度
        :return: int 饥饿掉血速度，-1表示获取失败
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.GetPlayerStarveTick()

    def getTotalExp(self):
        # type: () -> int
        """
        获取玩家的总经验值
        :return: int 总经验值，获取失败时返回-1
        """
        comp = serverApi.GetEngineCompFactory().CreateExp(self.playerId)
        return comp.GetPlayerTotalExp()

    def isNaturalRegen(self):
        # type: () -> bool
        """
        是否开启玩家自然恢复
        :return: bool True表示开启，False表示关闭，None表示获取失败
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.IsPlayerNaturalRegen()

    def isNaturalStarve(self):
        # type: () -> bool
        """
        是否开启玩家饥饿掉血
        :return: bool True表示开启，False表示关闭，None表示获取失败
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.IsPlayerNaturalStarve()

    def setEnchantmentSeed(self, enchantmentSeed):
        # type: (int) -> bool
        """
        设置玩家的附魔种子
        :param enchantmentSeed: int 随机种子
        :return: bool 是否设置成功
        备注：
          * 该属性会自动存档
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.SetEnchantmentSeed(enchantmentSeed)

    def setHealthLevel(self, healthLevel):
        # type: (int) -> bool
        """
        设置玩家健康临界值
        :param healthLevel: int 健康临界值
        :return: bool 是否设置成功
        备注：
          * 健康临界值始终大于等于饥饿临界值。如果设置的健康临界值小于饥饿临界值，饥饿临界值将被同步调整
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.SetPlayerHealthLevel(healthLevel)

    def setHealthTick(self, healthTick):
        # type: (int) -> bool
        """
        设置玩家自然恢复速度
        :param healthTick: int 自然恢复速度
        :return: bool 是否设置成功
        备注：
          * 最小值为1，即每秒恢复20点血量
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.SetPlayerHealthTick(healthTick)

    def setHunger(self, value):
        # type: (float) -> bool
        """
        设置玩家饥饿度
        :param value: float 饥饿度
        :return: bool 是否设置成功
        备注：
          * 该接口不会触发 PlayerHungerChangeServerEvent
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.SetPlayerHunger(value)

    def setMaxExhaustionValue(self, value):
        # type: (float) -> bool
        """
        设置玩家最大消耗度
        :param value: float 最大消耗度
        :return: bool 是否设置成功
        备注：
          * 例如：当 maxExhaustion=4 时，饥饿消耗速度是 maxExhaustion=8 时的两倍
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.SetPlayerMaxExhaustionValue(value)

    def setNaturalRegen(self, value):
        # type: (bool) -> bool
        """
        设置是否开启玩家自然恢复
        :param value: bool True开启，False关闭
        :return: bool 是否设置成功
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.SetPlayerNaturalRegen(value)

    def setNaturalStarve(self, value):
        # type: (bool) -> bool
        """
        设置是否开启玩家饥饿掉血
        :param value: bool True开启，False关闭
        :return: bool 是否设置成功
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.SetPlayerNaturalStarve(value)

    def setPrefixAndSuffixName(self, prefix, prefixColor, suffix, suffixColor, nameColor=""):
        # type: (str, str, str, str, str) -> bool
        """
        设置玩家前缀和后缀名字
        :param prefix: str 前缀内容
        :param prefixColor: str 前缀颜色描述
        :param suffix: str 后缀内容
        :param suffixColor: str 后缀颜色描述
        :param nameColor: str 名字颜色描述，可为空
        :return: bool 是否设置成功
        """
        comp = serverApi.GetEngineCompFactory().CreateName(self.playerId)
        return comp.SetPlayerPrefixAndSuffixName(prefix, prefixColor, suffix, suffixColor, nameColor)

    def setStarveLevel(self, starveLevel):
        # type: (int) -> bool
        """
        设置玩家饥饿临界值
        :param starveLevel: int 饥饿临界值
        :return: bool 是否设置成功
        备注：
          * 健康临界值始终大于等于饥饿临界值。如果设置的饥饿临界值大于健康临界值，将被同步调整
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.SetPlayerStarveLevel(starveLevel)

    def setStarveTick(self, starveTick):
        # type: (int) -> bool
        """
        设置玩家饥饿掉血速度
        :param starveTick: int 饥饿掉血速度
        :return: bool 是否设置成功
        备注：
          * 最小值为1，即每秒扣20点血量
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.SetPlayerStarveTick(starveTick)

    def setTotalExp(self, exp):
        # type: (int) -> bool
        """
        设置玩家的总经验值
        :param exp: int 总经验值，正整数
        :return: bool 是否设置成功
        备注：
          * 会根据总经验值重新计算等级，可能引起等级变化
          * 内部运算采用浮点数，数值较大时可能出现误差
        """
        comp = serverApi.GetEngineCompFactory().CreateExp(self.playerId)
        return comp.SetPlayerTotalExp(exp)

    # 玩家行为
    def addAroundEntityMotion(self, eID, angularVelocity, axis=(0, 1, 0), lockDir=False, stopRad=0, radius=-1):
        # type: (str, float, tuple, bool, float, float) -> int
        """
        给玩家添加对实体环绕运动器
        :param eID: str 要环绕的某个实体的ID
        :param angularVelocity: float 圆周运动的角速度（弧度/秒）
        :param axis: tuple(float,float,float) 圆周运动的轴，默认为(0, 1, 0)
        :param lockDir: bool 是否锁定实体朝向，默认为False
        :param stopRad: float 停止该运动器所需要的弧度，为0时会一直运行
        :param radius: float 环绕半径，为-1时使用当前与目标的距离作为半径
        :return: int 运动器ID，添加失败时返回-1
        备注：
          * 该接口会在客户端和服务端同步进行，使用前请确保环绕的对象在客户端和服务端都已创建
          * 该接口不屏蔽玩家控制的移动以及重力作用
          * 可叠加多个环绕运动器、可与速度运动器互相叠加
          * 建议将玩家与目标之间的环绕半径控制在30以内
        示例:
            import mod.server.extraServerApi as serverApi
            motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(playerId)
            axis=(-1, 1, 1)
            mID = motionComp.AddPlayerAroundEntityMotion(eID, 1.0, axis, lockDir=False, stopRad=0, radius=2.0)
            motionComp.StartPlayerMotion(mID)
        """
        comp = serverApi.GetEngineCompFactory().CreateActorMotion(self.playerId)
        return comp.AddPlayerAroundEntityMotion(eID, angularVelocity, axis, lockDir, stopRad, radius)

    def addAroundPointMotion(self, center, angularVelocity, axis=(0, 1, 0), lockDir=False, stopRad=0):
        # type: (tuple, float, tuple, bool, float) -> int
        """
        给玩家添加对点环绕运动器
        :param center: tuple(float,float,float) 要环绕的圆心点坐标
        :param angularVelocity: float 圆周运动的角速度（弧度/秒）
        :param axis: tuple(float,float,float) 圆周运动的轴，默认为(0, 1, 0)
        :param lockDir: bool 是否锁定玩家朝向，默认为False
        :param stopRad: float 停止该运动器所需要的弧度，为0时会一直运行
        :return: int 运动器ID，添加失败时返回-1
        备注：
          * 不屏蔽玩家控制的移动以及重力作用
          * 可叠加多个环绕运动器、可与速度运动器互相叠加
          * 建议将玩家运动范围控制在当前位置±100内
        示例:
            import mod.server.extraServerApi as serverApi
            motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(playerId)
            center = (0, 8, 0)
            axis=(-1, 1, 1)
            mID = motionComp.AddPlayerAroundPointMotion(center, 1.0, axis, lockDir=False, stopRad=0)
            motionComp.StartPlayerMotion(mID)
        """
        comp = serverApi.GetEngineCompFactory().CreateActorMotion(self.playerId)
        return comp.AddPlayerAroundPointMotion(center, angularVelocity, axis, lockDir, stopRad)

    def addTrackMotion(self, targetPos, duraTime, startPos=None, relativeCoord=False,
                       isLoop=False, targetRot=None, startRot=None, useVelocityDir=False,
                       ease=None):
        # type: (tuple, float, tuple, bool, bool, tuple, tuple, bool, object) -> int
        """
        给玩家添加轨迹运动器
        :param targetPos: tuple(float,float,float) 轨迹终点
        :param duraTime: float 到达终点所需要的时间
        :param startPos: tuple(float,float,float) 轨迹起点，默认None表示以StartPlayerMotion时的位置作为起点
        :param relativeCoord: bool 是否使用相对坐标，默认为False
        :param isLoop: bool 是否循环往复，默认为False
        :param targetRot: tuple(float,float) 终点朝向，受relativeCoord影响，默认None表示使用StartPlayerMotion时的朝向
        :param startRot: tuple(float,float) 起点朝向，受relativeCoord影响，默认None表示使用StartPlayerMotion时的朝向
        :param useVelocityDir: bool 是否使用速度方向作为朝向，默认为False
        :param ease: TimeEaseType 时间变化函数，默认为linear
        :return: int 运动器ID，添加失败时返回-1
        备注：
          * 不屏蔽玩家控制的移动
          * 轨迹运动器不可叠加，仅能添加一个
          * 设置朝向后会根据参数计算出顺时针或逆时针旋转
        示例:
            import mod.server.extraServerApi as serverApi
            motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(playerId)
            target = (5, 0, 0)
            rot1 = (0, 0)
            rot2 = (0, 360)
            mID = motionComp.AddPlayerTrackMotion(target, 3.0, startPos=None, relativeCoord=True, isLoop=False,
                                                  targetRot=rot1, startRot=rot2, useVelocityDir=True,
                                                  ease=serverApi.GetMinecraftEnum().TimeEaseType.linear)
            motionComp.StartPlayerMotion(mID)
        """
        comp = serverApi.GetEngineCompFactory().CreateActorMotion(self.playerId)
        minecraftEnum = serverApi.GetMinecraftEnum()
        if ease is None:
            ease = minecraftEnum.TimeEaseType.linear
        return comp.AddPlayerTrackMotion(targetPos, duraTime, startPos, relativeCoord, isLoop,
                                         targetRot, startRot, useVelocityDir, ease)

    def addVelocityMotion(self, velocity, accelerate=None, useVelocityDir=True):
        # type: (tuple, tuple, bool) -> int
        """
        给玩家添加速度运动器
        :param velocity: tuple(float,float,float) 速度向量
        :param accelerate: tuple(float,float,float) 加速度向量，默认为None
        :param useVelocityDir: bool 是否使用当前速度方向作为朝向，默认为True
        :return: int 运动器ID，添加失败时返回-1
        备注：
          * 不屏蔽玩家控制的移动以及重力作用
          * 速度运动器可叠加多个，可与环绕运动器互相叠加
          * 建议将玩家运动范围控制在当前位置±100内
        示例:
            import mod.server.extraServerApi as serverApi
            motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(playerId)
            velocity = (0, 0, 1)
            accelerate = (0, 0, -1)
            mID = motionComp.AddPlayerVelocityMotion(velocity, accelerate, useVelocityDir=True)
            motionComp.StartPlayerMotion(mID)
        """
        comp = serverApi.GetEngineCompFactory().CreateActorMotion(self.playerId)
        return comp.AddPlayerVelocityMotion(velocity, accelerate, useVelocityDir)

    def changeDimension(self, dimensionId, pos):
        # type: (int, tuple) -> bool
        """
        传送玩家
        :param dimensionId: int 维度 0-主世界; 1-地狱; 2-末地
        :param pos: tuple(int,int,int) 传送坐标
        :return: bool 是否设置成功
        备注：
          * 成功切换维度后，pos位置为玩家头的位置，比设定位置低1.62
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreateDimension(playerId)
            comp.ChangePlayerDimension(0, (0,4,0))
        """
        comp = serverApi.GetEngineCompFactory().CreateDimension(self.playerId)
        return comp.ChangePlayerDimension(dimensionId, pos)

    def changeFlyState(self, isFly, enterFly=True):
        # type: (bool, bool) -> bool
        """
        给予/取消飞行能力, 并根据enterFly参数确定是否进入飞行状态
        :param isFly: bool 给予/取消飞行能力
        :param enterFly: bool 是否进入飞行状态，只有当isFly为True时该参数才有效
        :return: bool 是否设置成功
        备注：
          * 不建议在OnGroundClientEvent事件回调中马上调用ChangePlayerFlyState
          * 拥有飞行能力时，不会受到摔落伤害
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreateFly(playerId)
            comp.ChangePlayerFlyState(True) # 给予并进入飞行
        """
        comp = serverApi.GetEngineCompFactory().CreateFly(self.playerId)
        return comp.ChangePlayerFlyState(isFly, enterFly) if isFly else comp.ChangePlayerFlyState(False)

    def enableKeepInventory(self, enable):
        # type: (bool) -> bool
        """
        设置玩家死亡不掉落物品
        :param enable: bool True-不掉落，False-掉落
        :return: bool 是否设置成功
        备注：
          * 只有全局的“保留物品栏”规则关闭时，才会使用此设置控制玩家是否掉落
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
            succ = comp.EnableKeepInventory(True)
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.EnableKeepInventory(enable)

    def getEntityRider(self):
        # type: () -> str
        """
        获取骑乘者正在骑乘的实体的id
        :return: str 骑乘者直接骑乘对象的实体id，若没有骑乘则返回"-1"
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreateRide(entityId)
            riderId = comp.GetEntityRider()
        """
        comp = serverApi.GetEngineCompFactory().CreateRide(self.playerId)
        return comp.GetEntityRider()

    def getInteracteCenterOffset(self):
        # type: () -> tuple
        """
        获取玩家服务端交互中心的偏移
        :return: tuple(float,float,float) 偏移量
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
            comp.GetInteracteCenterOffset()
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.GetInteracteCenterOffset()

    def getIsBlocking(self):
        # type: () -> bool
        """
        获取玩家激活盾牌状态
        :return: bool 玩家盾牌是否激活
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
            comp.GetIsBlocking()
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.GetIsBlocking()

    def getDestroyTotalTime(self, blockName):
        # type: (str) -> float
        """
        获取玩家破坏某方块需要的时间(服务端接口)
        :param blockName: str 方块标识符，格式[namespace:name:auxvalue]，auxvalue默认为0
        :return: float 需要消耗的时间
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
            comp.GetPlayerDestroyTotalTime("minecraft:diamond_block")
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.GetPlayerDestroyTotalTime(blockName)

    def getExhaustionRatioByType(self, ratioType):
        # type: (int) -> float
        """
        获取玩家某行为的饥饿度消耗倍率
        :param ratioType: int 行为枚举PlayerExhauseRatioType枚举
        :return: float 饥饿度消耗倍率值, -1获取失败(如创造模式)
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
            jumpType = serverApi.GetMinecraftEnum().PlayerExhauseRatioType.JUMP
            ratio = comp.GetPlayerExhaustionRatioByType(jumpType)
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.GetPlayerExhaustionRatioByType(ratioType)

    def getInteracteRange(self):
        # type: () -> float
        """
        获取玩家服务端的交互距离
        :return: float 交互半径
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
            comp.GetPlayerInteracteRange()
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.GetPlayerInteracteRange()

    def getMotions(self):
        # type: () -> dict
        """
        获取玩家身上的所有运动器
        :return: dict 运动器集合，key-运动器ID, value-运动器类型(0:轨迹,1:速度,2:环绕)
        备注：
          * 运动器非人为停止后会被移除
        示例:
            import mod.server.extraServerApi as serverApi
            motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(playerId)
            motions = motionComp.GetPlayerMotions()
        """
        comp = serverApi.GetEngineCompFactory().CreateActorMotion(self.playerId)
        return comp.GetPlayerMotions()

    def getRespawnPos(self):
        # type: () -> dict
        """
        获取玩家复活点
        :return: dict 复活点信息，包括维度和坐标
        备注：
          * 使用spawnpoint指令设置玩家出生点后，可通过此接口获取
          * 若未使用setworldspawn指令设置出生点，则y轴可能为32767
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
            print comp.GetPlayerRespawnPos()
            # 结果示例 {'dimensionId': 0, 'pos': (44, 32767, 4)}
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.GetPlayerRespawnPos()

    def getRelevantPlayer(self, exceptList=None):
        # type: (list) -> list
        """
        获取附近玩家id列表
        :param exceptList: list(str) 排除的玩家id列表,默认None表示不排除
        :return: list(str) 附近玩家id列表
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
            comp.GetRelevantPlayer(exceptId)
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.GetRelevantPlayer(exceptList)

    def isEntityRiding(self):
        # type: () -> bool
        """
        检查玩家是否骑乘
        :return: bool 是否骑乘
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreateRide(entityId)
            isRiding = comp.IsEntityRiding()
        """
        comp = serverApi.GetEngineCompFactory().CreateRide(self.playerId)
        return comp.IsEntityRiding()

    def isCanFly(self):
        # type: () -> bool
        """
        获取玩家能否飞行
        :return: bool True可飞行，False不可飞行
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreateFly(playerId)
            comp.IsPlayerCanFly()
        """
        comp = serverApi.GetEngineCompFactory().CreateFly(self.playerId)
        return comp.IsPlayerCanFly()

    def isFlying(self):
        # type: () -> bool
        """
        获取玩家是否处于飞行状态
        :return: bool True在飞行，False未在飞行
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreateFly(playerId)
            comp.IsPlayerFlying()
        """
        comp = serverApi.GetEngineCompFactory().CreateFly(self.playerId)
        return comp.IsPlayerFlying()

    def openWorkBench(self):
        # type: () -> bool
        """
        在玩家当前位置打开工作台UI，不依赖工作台方块
        :return: bool 是否打开成功
        备注：
          * 工作台有交互距离要求，过远会自动关闭
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreateBlockInfo(playerId)
            comp.OpenWorkBench()
        """
        comp = serverApi.GetEngineCompFactory().CreateBlockInfo(self.playerId)
        return comp.OpenWorkBench()

    def pickUpItemEntity(self, playerEntityId, itemEntityId):
        # type: (str, str) -> bool
        """
        某个Player拾取物品ItemEntity
        :param playerEntityId: str 拾取者的playerEntityId
        :param itemEntityId: str 要拾取的物品itemEntityId
        :return: bool 是否拾取成功
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
            comp.PickUpItemEntity(playerEntityId, itemEntityId)
        """
        comp = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
        return comp.PickUpItemEntity(playerEntityId, itemEntityId)

    def attackEntity(self, entityId):
        # type: (str) -> bool
        """
        玩家使用手持武器攻击某个生物
        :param entityId: str 生物entityId
        :return: bool 执行结果
        备注：
          * 1.会触发PlayerAttackEntityEvent，可被cancel
          * 2.此接口无视距离，但无法跨维度，且需目标区域已加载
          * 3.若要多次伤害同生物，可将目标受伤CD置0
          * 4.不会播放原版攻击动作，可使用Swing接口
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
            suc = comp.PlayerAttackEntity("-123456")
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.PlayerAttackEntity(entityId)

    def destroyBlock(self, pos, particle=1, sendInv=False):
        # type: (tuple, int, bool) -> bool
        """
        使用手上工具破坏方块
        :param pos: tuple(int,int,int) 方块位置
        :param particle: int 是否开启破坏粒子效果，默认1(开启)
        :param sendInv: bool 是否同步服务端背包信息，默认False
        :return: bool 设置结果
        备注：
          * 手上工具的附魔效果会生效，并扣除耐久度
          * 会触发ServerPlayerTryDestroyBlockEvent事件，可被cancel
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreateBlockInfo(playerId)
            comp.PlayerDestoryBlock((0,5,0),1,False)
            comp.PlayerDestoryBlock((0,6,0),1,True)
        """
        comp = serverApi.GetEngineCompFactory().CreateBlockInfo(self.playerId)
        return comp.PlayerDestoryBlock(pos, particle, sendInv)

    def useItemToEntity(self, entityId):
        # type: (str) -> bool
        """
        玩家使用手上物品对某个生物使用
        :param entityId: str 生物entityId
        :return: bool 设置结果
        备注：
          * 1.会触发PlayerInteractServerEvent，可被cancel
          * 2.可触发PlayerNamedEntityServerEvent、PlayerFeedEntityServerEvent等事件
          * 3.此接口无视距离，但需目标区域已加载，无法跨维度
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreateBlockInfo(playerId)
            suc = comp.PlayerUseItemToEntity("-123456")
        """
        comp = serverApi.GetEngineCompFactory().CreateBlockInfo(self.playerId)
        return comp.PlayerUseItemToEntity(entityId)

    def useItemToPos(self, pos, posType, slotPos, facing):
        # type: (tuple, int, int, int) -> bool
        """
        模拟玩家对某个坐标使用物品
        :param pos: tuple(int,int,int) 坐标
        :param posType: int 物品所在的地方ItemPosType枚举
        :param slotPos: int 槽位，仅INVENTORY或ARMOR时需要，其他情况0即可
        :param facing: int 朝向，详见Facing枚举
        :return: bool 设置结果
        备注：
          * 使用抛射物时，非创造模式才会返回True
          * 只能对玩家周边200格以内的坐标使用
          * 此接口可作为方块交互使用
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreateBlockInfo(playerId)
            comp.PlayerUseItemToPos((0,5,0),
                                    serverApi.GetMinecraftEnum().ItemPosType.INVENTORY,
                                    0,
                                    1)
        """
        comp = serverApi.GetEngineCompFactory().CreateBlockInfo(self.playerId)
        return comp.PlayerUseItemToPos(pos, posType, slotPos, facing)

    def removeMotion(self, motionId):
        # type: (int) -> bool
        """
        移除玩家身上的运动器
        :param motionId: int 要移除的运动器ID
        :return: bool 是否成功移除
        示例:
            import mod.server.extraServerApi as serverApi
            motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(playerId)
            motionComp.RemovePlayerMotion(mID)
        """
        comp = serverApi.GetEngineCompFactory().CreateActorMotion(self.playerId)
        return comp.RemovePlayerMotion(motionId)

    def setBanFishing(self, isBan):
        # type: (bool) -> bool
        """
        设置是否屏蔽玩家钓鱼功能（仅屏蔽钓起任何物品的效果）
        :param isBan: bool True屏蔽，False取消屏蔽
        :return: bool 是否设置成功
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
            comp.SetBanPlayerFishing(True)
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.SetBanPlayerFishing(isBan)

    def setInteracteCenterOffset(self, offset):
        # type: (tuple) -> bool
        """
        设置玩家服务端交互中心偏移
        :param offset: tuple(float,float,float) 偏移量
        :return: bool 是否设置成功
        备注：
          * 仅修改服务端交互中心，需配合客户端SetCameraAnchor或SetPickCenterOffset
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
            comp.SetInteracteCenterOffset(offset)
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.SetInteracteCenterOffset(offset)

    def setPickUpArea(self, area):
        # type: (tuple) -> bool
        """
        设置玩家的拾取物品范围
        :param area: tuple(float,float,float) 拾取范围，(0,0,0)表示取消设置
        :return: bool 是否设置成功
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
            succ = comp.SetPickUpArea((5,0,3))
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.SetPickUpArea(area)

    def setAttackSpeedAmplifier(self, amplifier):
        # type: (float) -> bool
        """
        设置玩家攻击速度倍数
        :param amplifier: float 攻击速度倍数，范围[0.5,2.0]，1.0表示正常
        :return: bool 是否设置成功
        备注：
          * 该接口影响SetHurtCD设置的全局受击间隔
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
            comp.SetPlayerAttackSpeedAmplifier(1.1)
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.SetPlayerAttackSpeedAmplifier(amplifier)

    def setExhaustionRatioByType(self, ratioType, ratio):
        # type: (int, float) -> bool
        """
        设置玩家某行为饥饿度消耗倍率
        :param ratioType: int 行为枚举PlayerExhauseRatioType枚举
        :param ratio: float 倍率
        :return: bool 是否设置成功
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
            jumpType = serverApi.GetMinecraftEnum().PlayerExhauseRatioType.JUMP
            comp.SetPlayerExhaustionRatioByType(jumpType, 20)
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.SetPlayerExhaustionRatioByType(ratioType, ratio)

    def setInteracteRange(self, interacteRange):
        # type: (float) -> bool
        """
        设置玩家服务端的交互距离
        :param interacteRange: float 交互半径
        :return: bool 是否设置成功
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
            comp.SetPlayerInteracteRange(interacteRange)
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.SetPlayerInteracteRange(interacteRange)

    def setJumpable(self, isJumpable):
        # type: (bool) -> bool
        """
        设置玩家是否可跳跃
        :param isJumpable: bool True允许跳跃，False禁止跳跃
        :return: bool 是否设置成功
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
            comp.SetPlayerJumpable(False)
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.SetPlayerJumpable(isJumpable)

    def setMotion(self, motion):
        # type: (tuple) -> bool
        """
        设置玩家瞬时移动方向向量(可解决SetMotion闪现问题)
        :param motion: tuple(float,float,float) 世界坐标系下的向量
        :return: bool 是否设置成功
        备注：
          * 在damageEvent中使用该接口，需要将damageEvent回调的knock参数设置为False
          * 相比SetMotion，此接口无需客户端调用，可避免网络延迟导致的闪现
        示例:
            import mod.server.extraServerApi as serverApi
            # 使生物向准星方向突进
            rotComp = serverApi.GetEngineCompFactory().CreateRot(entityId)
            rot = rotComp.GetRot()
            x, y, z = serverApi.GetDirFromRot(rot)
            motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(entityId)
            motionComp.SetPlayerMotion((x*5, y*5, z*5))
        """
        comp = serverApi.GetEngineCompFactory().CreateActorMotion(self.playerId)
        return comp.SetPlayerMotion(motion)

    def setMovable(self, isMovable):
        # type: (bool) -> bool
        """
        设置玩家是否可移动
        :param isMovable: bool True允许移动，False禁止移动
        :return: bool 是否设置成功
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
            comp.SetPlayerMovable(False)
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.SetPlayerMovable(isMovable)

    def setRespawnPos(self, pos, dimensionId=0):
        # type: (tuple, int) -> bool
        """
        设置玩家复活的位置与维度
        :param pos: tuple(int,int,int) 复活点位置
        :param dimensionId: int 复活点维度，默认0(主世界)
        :return: bool 是否设置成功
        备注：
          * 不能在PlayerDieEvent之后再设置
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
            suc = comp.SetPlayerRespawnPos((0,4,0), 0)
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.SetPlayerRespawnPos(pos, dimensionId)

    def startMotion(self, motionId):
        # type: (int) -> bool
        """
        启动玩家身上的某个运动器
        :param motionId: int 运动器ID
        :return: bool 是否成功启动
        备注：
          * 运动器控制的玩家会无视原生碰撞逻辑
          * 等待EntityMotionStartServerEvent事件触发再确认真正启动
        示例:
            import mod.server.extraServerApi as serverApi
            motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(playerId)
            motionComp.StartPlayerMotion(mID)
        """
        comp = serverApi.GetEngineCompFactory().CreateActorMotion(self.playerId)
        return comp.StartPlayerMotion(motionId)

    def stopMotion(self, motionId):
        # type: (int) -> bool
        """
        停止玩家身上的某个运动器
        :param motionId: int 运动器ID
        :return: bool 是否成功停止
        备注：
          * 调用该接口不会触发EntityMotionStopServerEvent
        示例:
            import mod.server.extraServerApi as serverApi
            motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(playerId)
            motionComp.StopPlayerMotion(mID)
        """
        comp = serverApi.GetEngineCompFactory().CreateActorMotion(self.playerId)
        return comp.StopPlayerMotion(motionId)

    def isSneaking(self):
        # type: () -> bool
        """
        获取玩家是否处于潜行状态(服务端)
        :return: bool 是否潜行
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
            is_sneaking = comp.isSneaking()
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.isSneaking()

    def isSwimming(self):
        # type: () -> bool
        """
        获取玩家是否处于游泳状态(服务端)
        :return: bool 是否游泳
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
            is_swimming = comp.isSwimming()
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.isSwimming()

    # 玩家背包
    def getInventory(self):
        # type: () -> PlayerInventory
        """
        获取玩家背包对象（面向对象操作）
        :return: PlayerInventory 玩家背包对象
        """
        return PlayerInventory(self.playerId)

    # 玩家权限

    def getOperation(self):
        # type: () -> int
        """
        获取玩家权限类型信息
        :return: int 权限类型，Visitor=0，Member=1，Operator=2，Custom=3
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
            operation = comp.GetPlayerOperation()
        """
        comp = serverApi.GetEngineCompFactory().CreatePlayer(self.playerId)
        return comp.GetPlayerOperation()

    def getAbility(self):
        # type: () -> PlayerAbility
        """
        获取玩家能力对象
        :return: PlayerAbility 玩家能力对象
        """
        return PlayerAbility(self.playerId)

    # 消息相关

    def getNameTag(self):
        # type: () -> str
        """
        获取玩家名字
        :return: str 玩家名字
        """
        comp = serverApi.GetEngineCompFactory().CreateName(self.playerId)
        return comp.GetName()

    def setNameTag(self, name):
        # type: (str) -> bool
        """
        设置玩家名字
        :param name: str 玩家名字
        :return: bool 是否设置成功
        """
        comp = serverApi.GetEngineCompFactory().CreateName(self.playerId)
        return comp.SetName(name)

    def sendMessage(self, msg, color = None):
        # type: (str, str) -> None
        """
        向玩家发送消息
        :param msg: str 消息内容
        :param color: str 消息颜色，默认白色
        示例:
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
            comp.SendMessage("Hello World!")
        """
        comp = serverApi.GetEngineCompFactory().CreateMsg(serverApi.GetLevelId())
        comp.NotifyOneMessage(self.playerId, msg, color)

    def chat(self, msg):
        # type: (str) -> None
        """
        模拟玩家给所有人发送聊天栏消息
        :param msg: str 消息内容
        """
        comp = serverApi.GetEngineCompFactory().CreateMsg(serverApi.GetLevelId())
        comp.SendMsg(self.getNameTag(), msg)

    def chatTo(self, target, msg):
        # type: (str, str) -> None
        """
        模拟玩家给指定玩家发送私聊消息
        :param target: str 目标玩家实体ID
        :param msg: str 消息内容
        """
        comp = serverApi.GetEngineCompFactory().CreateMsg(serverApi.GetLevelId())
        comp.SendMsgToPlayer(self.playerId, target, msg)

    def sendNotifyMessage(self, msg, color = None):
        # type: (str, str) -> None
        """
        向玩家发送通知消息
        :param msg: str 消息内容
        :param color: str 消息颜色，默认白色
        """
        comp = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
        comp.SetNotifyMsg(msg, color)

    def sendPopup(self, message, subTitle = ""):
        # type: (str, str) -> None
        """
        在具体某个玩家的物品栏上方弹出popup类型通知，位置位于tip类型消息下方，此功能更建议客户端使用game组件的对应接口SetPopupNotice
        :param message: str 消息内容,可以在消息前增加extraServerApi.GenerateColor("RED")字符来设置颜色，具体参考样例
        :param subTitle: str 消息子标题内容,效果同message，也可设置颜色，位置位于message上方
        """
        comp = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
        comp.SetOnePopupNotice(self.playerId, message, subTitle)

    def sendTip(self, message):
        # type: (str) -> None
        """
        在具体某个玩家的物品栏上方弹出tip类型通知，位置位于popup类型通知上方，此功能更建议在客户端使用game组件的对应接口SetTipMessage
        :param message: str 消息内容
        """
        comp = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
        comp.SetOneTipMessage(self.playerId, message)