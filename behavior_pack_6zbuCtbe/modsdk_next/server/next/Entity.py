# -*- coding: utf-8 -*-
import mod.server.extraServerApi as serverApi


class Entity(object):
    __slots__ = ['entityId']

    def __init__(self, entityId):
        # type: (str) -> None
        """
        初始化实体代理对象

        :param entityId: str 实体的唯一标识符
        """
        self.entityId = entityId

    # Entity Component Methods
    def addComponent(self, componentName, componentValue):
        # type: (str, str) -> bool
        """
        给指定实体自定义添加实体Component

        :param componentName: str 实体行为包中定义的component的键名
        :param componentValue: str 实体行为包中定义的component的值的json
        :return: bool 指令是否成功发出
        """
        comp = serverApi.GetEngineCompFactory().CreateEntityEvent(self.entityId)
        return comp.AddActorComponent(componentName, componentValue)

    def removeComponent(self, componentName):
        # type: (str) -> bool
        """
        删除指定实体的指定Component

        :param componentName: str 实体行为包中定义的component的键名
        :return: bool 指令是否成功发出
        """
        comp = serverApi.GetEngineCompFactory().CreateEntityEvent(self.entityId)
        return comp.RemoveActorComponent(componentName)

    def addComponentGroup(self, groupName):
        # type: (str) -> bool
        """
        给指定实体添加实体json中配置的ComponentGroup

        :param groupName: str 实体行为包中定义的component_group的键名
        :return: bool 指令是否成功发出
        """
        comp = serverApi.GetEngineCompFactory().CreateEntityEvent(self.entityId)
        return comp.AddActorComponentGroup(groupName)

    def removeComponentGroup(self, groupName):
        # type: (str) -> bool
        """
        移除指定实体在实体json中配置的ComponentGroup

        :param groupName: str 实体行为包中定义的component_group的键名
        :return: bool 指令是否成功发出
        """
        comp = serverApi.GetEngineCompFactory().CreateEntityEvent(self.entityId)
        return comp.RemoveActorComponentGroup(groupName)

    def getComponents(self):
        # type: () -> dict
        """
        获取指定实体的生效Components

        :return: dict 指定实体的生效Components
        """
        comp = serverApi.GetEngineCompFactory().CreateEntityEvent(self.entityId)
        return comp.GetComponents()

    # Motion Methods
    def addAroundEntityMotion(self, eId, angularVelocity, axis=(0, 1, 0), lockDir=False, stopRad=0, radius=-1):
        # type: (str, float, tuple, bool, float, float) -> int
        """
        给实体添加对实体环绕运动器

        :param eId: str 要环绕的某个实体的ID
        :param angularVelocity: float 圆周运动的角速度（弧度/秒）
        :param axis: tuple(float, float, float) 圆周运动的轴，默认为(0, 1, 0)
        :param lockDir: bool 是否在运动器生效时锁定实体的朝向，默认为False
        :param stopRad: float 停止该运动器所需要的弧度，当stopRad为0时，该运动器会一直运行，默认为0
        :param radius: float 环绕半径，当设置为-1时环绕运动器使用启动时与目标的距离作为半径，默认为-1
        :return: int 运动器ID，添加失败时返回-1
        """
        motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(self.entityId)
        return motionComp.AddEntityAroundEntityMotion(eId, angularVelocity, axis, lockDir, stopRad, radius)

    def addAroundPointMotion(self, center, angularVelocity, axis=(0, 1, 0), lockDir=False, stopRad=0):
        # type: (tuple, float, tuple, bool, float) -> int
        """
        给实体添加对点环绕运动器

        :param center: tuple(float, float, float) 要环绕的圆心点坐标
        :param angularVelocity: float 圆周运动的角速度（弧度/秒）
        :param axis: tuple(float, float, float) 圆周运动的轴，默认为(0, 1, 0)
        :param lockDir: bool 是否在运动器生效时锁定实体的朝向，默认为False
        :param stopRad: float 停止该运动器所需要的弧度，当stopRad为0时，该运动器会一直运行，默认为0
        :return: int 运动器ID，添加失败时返回-1
        """
        motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(self.entityId)
        return motionComp.AddEntityAroundPointMotion(center, angularVelocity, axis, lockDir, stopRad)

    def addTrackMotion(self, targetPos, duraTime, startPos=None, relativeCoord=False, isLoop=False, targetRot=None, startRot=None, useVelocityDir=False, ease='linear'):
        # type: (tuple, float, tuple, bool, bool, tuple, tuple, bool, str) -> int
        """
        给实体添加轨迹运动器

        :param targetPos: tuple(float, float, float) 轨迹终点
        :param duraTime: float 到达终点所需要的时间
        :param startPos: tuple(float, float, float) 轨迹起点，默认为None，表示以调用StartEntityMotion的位置作为起点
        :param relativeCoord: bool 是否使用相对坐标设置起点和终点的位置以及朝向，默认为False
        :param isLoop: bool 是否循环，若设为True，则实体会在起点和终点之间往复运动，默认为False
        :param targetRot: tuple(float, float) 实体到达targetPos时的朝向，受参数relativeCoord影响，默认为None，表示使用调用StartEntityMotion时的朝向
        :param startRot: tuple(float, float) 实体到达startPos时的朝向，受参数relativeCoord影响，默认为None，表示使用调用StartEntityMotion时的朝向
        :param useVelocityDir: bool 是否使用运动中的速度方向作为朝向，默认为False，若为True，则参数targetRot和startRot无效
        :param ease: str 时间变化函数, 默认值为'linear'
        :return: int 运动器ID，添加失败时返回-1
        """
        motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(self.entityId)
        timeEaseType = getattr(serverApi.GetMinecraftEnum().TimeEaseType, ease, 'linear')
        return motionComp.AddEntityTrackMotion(targetPos, duraTime, startPos, relativeCoord, isLoop, targetRot, startRot, useVelocityDir, timeEaseType)

    def addVelocityMotion(self, velocity, accelerate=None, useVelocityDir=True):
        # type: (tuple, tuple, bool) -> int
        """
        给实体添加速度运动器

        :param velocity: tuple(float, float, float) 速度，包含大小、方向
        :param accelerate: tuple(float, float, float) 加速度，包含大小、方向，默认为None，表示没有加速度
        :param useVelocityDir: bool 是否使用当前速度的方向作为此刻实体的朝向，默认为True
        :return: int 运动器ID，添加失败时返回-1
        """
        motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(self.entityId)
        return motionComp.AddEntityVelocityMotion(velocity, accelerate, useVelocityDir)

    def removeMotion(self, motionId):
        # type: (int) -> bool
        """
        移除实体身上的运动器

        :param motionId: int 要移除的某个运动器的ID
        :return: bool 是否成功移除
        """
        motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(self.entityId)
        return motionComp.RemoveEntityMotion(motionId)

    def resetMotion(self):
        # type: () -> bool
        """
        重置生物的瞬时移动方向向量

        :return: bool 设置是否成功
        """
        motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(self.entityId)
        return motionComp.ResetMotion()

    def setMotion(self, motion):
        # type: (tuple) -> bool
        """
        设置生物的瞬时移动方向向量

        :param motion: tuple(float, float, float) 世界坐标系下的向量
        :return: bool 设置是否成功
        """
        motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(self.entityId)
        return motionComp.SetMotion(motion)

    def startMotion(self, motionId):
        # type: (int) -> bool
        """
        启动实体身上的某个运动器

        :param motionId: int 要启动的某个运动器的ID
        :return: bool 是否成功启动
        """
        motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(self.entityId)
        return motionComp.StartEntityMotion(motionId)

    def stopMotion(self, motionId):
        # type: (int) -> bool
        """
        停止实体身上的某个运动器

        :param motionId: int 要停止的某个运动器的ID
        :return: bool 是否成功停止
        """
        motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(self.entityId)
        return motionComp.StopEntityMotion(motionId)

    # Ride Methods
    def addSeat(self, pos, rot=0, lockRot=0):
        # type: (tuple, float, float) -> int
        """
        增加坐骑座位

        :param pos: tuple(float, float, float) 座位位置
        :param rot: float 座位旋转，默认为0
        :param lockRot: float 骑乘者允许旋转角度范围，默认不限制
        :return: int 当前最大座位序号，增加失败返回-1
        """
        rideComp = serverApi.GetEngineCompFactory().CreateRide(self.entityId)
        return rideComp.AddEntitySeat(pos, rot, lockRot)

    def deleteSeat(self, seatIndex):
        # type: (int) -> bool
        """
        删除坐骑座位

        :param seatIndex: int 座位序号，范围为0~最大座位序号
        :return: bool 设置结果
        """
        rideComp = serverApi.GetEngineCompFactory().CreateRide(self.entityId)
        return rideComp.DeleteEntitySeat(seatIndex)

    def setSeat(self, seatIndex, pos, rot=0, lockRot=0):
        # type: (int, tuple, float, float) -> bool
        """
        设置坐骑座位的位置、旋转以及允许实体旋转范围

        :param seatIndex: int 座位序号，范围为0~最大座位序号
        :param pos: tuple(float, float, float) 座位位置
        :param rot: float 座位旋转，默认为0
        :param lockRot: float 骑乘者允许旋转角度范围，默认不限制
        :return: bool 设置结果
        """
        rideComp = serverApi.GetEngineCompFactory().CreateRide(self.entityId)
        return rideComp.SetEntitySeat(seatIndex, pos, rot, lockRot)

    def setRidePos(self, pos):
        # type: (tuple) -> bool
        """
        设置生物骑乘位置

        :param pos: tuple(float, float, float) 骑乘时挂接点
        :return: bool 设置结果
        """
        rideComp = serverApi.GetEngineCompFactory().CreateRide(self.entityId)
        return rideComp.SetRidePos(pos)

    def setRiderRideEntity(self, riderId, riddenEntityId, riderIndex=None):
        # type: (str, str, int) -> bool
        """
        设置实体骑乘生物（或者船与矿车）

        :param riderId: str 骑乘生物id
        :param riddenEntityId: str 被骑乘生物id。要求被骑乘生物的定义中具有minecraft:rideable组件，且组件中family_types含有可骑乘者的类型声明
        :param riderIndex: int 指定实体成为第n个骑乘者，范围为0~SeatCount-1，默认不指定
        :return: bool 设置结果
        """
        rideComp = serverApi.GetEngineCompFactory().CreateRide(self.entityId)
        return rideComp.SetRiderRideEntity(riderId, riddenEntityId, riderIndex)

    def stopEntityRiding(self):
        # type: () -> bool
        """
        强制骑乘者下坐骑

        :return: bool 当骑乘者当前正在骑乘并成功下坐骑返回True，否则返回False
        """
        rideComp = serverApi.GetEngineCompFactory().CreateRide(self.entityId)
        return rideComp.StopEntityRiding()

    # Action Methods
    def setAttackTarget(self, targetId):
        # type: (str) -> bool
        """
        设置仇恨目标

        :param targetId: str 目标实体id
        :return: bool 设置结果
        """
        actionComp = serverApi.GetEngineCompFactory().CreateAction(self.entityId)
        return actionComp.SetAttackTarget(targetId)

    def resetAttackTarget(self):
        # type: () -> bool
        """
        清除仇恨目标

        :return: bool 设置结果
        """
        actionComp = serverApi.GetEngineCompFactory().CreateAction(self.entityId)
        return actionComp.ResetAttackTarget()

    def getAttackTarget(self):
        # type: () -> str
        """
        获取仇恨目标

        :return: str 返回仇恨目标的实体id。如果传入的实体id所对应的实体没有仇恨目标，则返回-1。如果传入的实体id所对应的实体不存在，则返回None
        """
        actionComp = serverApi.GetEngineCompFactory().CreateAction(self.entityId)
        return actionComp.GetAttackTarget()

    def setMobKnockback(self, xd, zd, power, height, heightCap):
        # type: (float, float, float, float, float) -> None
        """
        设置击退的初始速度

        :param xd: float x轴方向，用来控制角度
        :param zd: float z轴方向，用来控制角度
        :param power: float 用来控制水平方向的初速度
        :param height: float 竖直方向的初速度
        :param heightCap: float 向上速度阈值，当实体本身已经有向上的速度时需要考虑这个值，用来确保最终向上的速度不会超过heightCap
        """
        actionComp = serverApi.GetEngineCompFactory().CreateAction(self.entityId)
        actionComp.SetMobKnockback(xd, zd, power, height, heightCap)

    # Attribute Methods
    def getJumpPower(self):
        # type: () -> float
        """
        获取生物跳跃力度

        :return: float 返回生物跳跃力度
        """
        gravityComp = serverApi.GetEngineCompFactory().CreateGravity(self.entityId)
        return gravityComp.GetJumpPower()

    def setJumpPower(self, jumpPower):
        # type: (float) -> bool
        """
        设置生物跳跃力度

        :param jumpPower: float 跳跃力度，正常是0.42
        :return: bool 是否设置成功
        """
        gravityComp = serverApi.GetEngineCompFactory().CreateGravity(self.entityId)
        return gravityComp.SetJumpPower(jumpPower)

    def getStepHeight(self):
        # type: () -> float
        """
        返回玩家前进非跳跃状态下能上的最大台阶高度

        :return: float 台阶高度
        """
        attrComp = serverApi.GetEngineCompFactory().CreateAttr(self.entityId)
        return attrComp.GetStepHeight()

    def setStepHeight(self, stepHeight):
        # type: (float) -> bool
        """
        设置玩家前进非跳跃状态下能上的最大台阶高度

        :param stepHeight: float 最大高度，需要大于0
        :return: bool 是否设置成功
        """
        attrComp = serverApi.GetEngineCompFactory().CreateAttr(self.entityId)
        return attrComp.SetStepHeight(stepHeight)

    def resetStepHeight(self):
        # type: () -> bool
        """
        恢复引擎默认玩家前进非跳跃状态下能上的最大台阶高度

        :return: bool 是否设置成功
        """
        attrComp = serverApi.GetEngineCompFactory().CreateAttr(self.entityId)
        return attrComp.ResetStepHeight()

    # Damage Methods
    def hurt(self, damage, cause, attackerId=None, childAttackerId=None, knocked=True, customTag=None):
        # type: (int, str, str, str, bool, str) -> bool
        """
        设置实体伤害

        :param damage: int 伤害值
        :param cause: str 伤害来源，详见Minecraft枚举值文档的ActorDamageCause枚举
        :param attackerId: str 伤害来源的实体id，默认为None
        :param childAttackerId: str 伤害来源的子实体id，默认为None，比如玩家使用抛射物对实体造成伤害，该值应为抛射物Id
        :param knocked: bool 实体是否被击退，默认值为True
        :param customTag: str 标识自定义伤害来源，只在cause为Custom生效，可在ActorHurtServerEvent、ActuallyHurtServerEvent、DamageEvent、PlayerHurtEvent、PlayerDieEvent、MobDieEvent监听到标识
        :return: bool 是否设置成功
        """
        hurtComp = serverApi.GetEngineCompFactory().CreateHurt(self.entityId)
        return hurtComp.Hurt(damage, cause, attackerId, childAttackerId, knocked, customTag)

    def immuneDamage(self, immune):
        # type: (bool) -> bool
        """
        设置实体是否免疫伤害（该属性存档）

        :param immune: bool 是否免疫伤害
        :return: bool 是否设置成功
        """
        hurtComp = serverApi.GetEngineCompFactory().CreateHurt(self.entityId)
        return hurtComp.ImmuneDamage(immune)

    # Persistence Methods
    def setPersistence(self, isPersistent):
        # type: (bool) -> None
        """
        设置实体是否持久化

        :param isPersistent: bool True为设置实体持久化，False为设置实体不持久化
        """
        persistenceComp = serverApi.GetEngineCompFactory().CreatePersistence(self.entityId)
        persistenceComp.SetPersistence(isPersistent)

    # Control AI Methods
    def setBlockControlAi(self, isBlock, freezeAnim=False):
        # type: (bool, bool) -> bool
        """
        设置屏蔽生物原生AI

        :param isBlock: bool 是否保留AI，False为屏蔽
        :param freezeAnim: bool 屏蔽AI时是否冻结动作，默认为False，仅当isBlock为False时生效。重进世界会恢复成初始动作
        :return: bool 设置结果
        """
        controlAiComp = serverApi.GetEngineCompFactory().CreateControlAi(self.entityId)
        return controlAiComp.SetBlockControlAi(isBlock, freezeAnim)

    def getBlockControlAi(self):
        # type: () -> bool
        """
        获取生物原生AI是否被屏蔽

        :return: bool AI是否保留。False为AI被屏蔽
        """
        controlAiComp = serverApi.GetEngineCompFactory().CreateControlAi(self.entityId)
        return controlAiComp.GetBlockControlAi()

    # Interaction Methods
    def setEntityInteractFilter(self, index, interactFilter):
        # type: (int, str) -> bool
        """
        设置与生物可交互的条件

        :param index: int 交互列表下标
        :param interactFilter: str 可交互的条件
        :return: bool 设置结果
        """
        interactComp = serverApi.GetEngineCompFactory().CreateInteract(self.entityId)
        return interactComp.SetEntityInteractFilter(index, interactFilter)

    # Tame Methods
    def setEntityTamed(self, playerId, tamedId):
        # type: (str, str) -> bool
        """
        设置生物驯服

        :param playerId: str 驯服玩家Id
        :param tamedId: str 被驯服的生物Id
        :return: bool 设置结果
        """
        tameComp = serverApi.GetEngineCompFactory().CreateTame(tamedId)
        return tameComp.SetEntityTamed(playerId, tamedId)

    def getOwnerId(self):
        # type: () -> str
        """
        获取驯服生物的主人id

        :return: str 主人id，不存在时返回None
        """
        tameComp = serverApi.GetEngineCompFactory().CreateTame(self.entityId)
        return tameComp.GetOwnerId()

    # Entity Event Methods
    def triggerCustomEvent(self, eventName):
        # type: (str) -> bool
        """
        触发生物自定义事件

        :param eventName: str 事件名称
        :return: bool 设置结果
        """
        entityEventComp = serverApi.GetEngineCompFactory().CreateEntityEvent(self.entityId)
        return entityEventComp.TriggerCustomEvent(self.entityId, eventName)

    # Move To Methods
    def setMoveSetting(self, pos, speed=1.0, maxIteration=200, callback=None):
        # type: (tuple, float, int, function) -> None
        """
        寻路组件

        :param pos: tuple(float, float, float) 寻路目标位置
        :param speed: float 移动速度，指正常移动速度的倍率。如1.0表示正常速度，2.0表示两倍速
        :param maxIteration: int 寻路算法最大迭代次数 默认200
        :param callback: function 寻路结束回调函数
        """
        moveToComp = serverApi.GetEngineCompFactory().CreateMoveTo(self.entityId)
        moveToComp.SetMoveSetting(pos, speed, maxIteration, callback)

    # Other Methods
    def isEating(self):
        # type: () -> bool
        """
        判断非玩家实体是否在进食

        :return: bool 是否在进食
        """
        entityDefinitionsComp = serverApi.GetEngineCompFactory().CreateEntityDefinitions(self.entityId)
        return entityDefinitionsComp.IsEating()

    def isEntityOnFire(self):
        # type: () -> bool
        """
        获取实体是否着火

        :return: bool 是否着火
        """
        attrComp = serverApi.GetEngineCompFactory().CreateAttr(self.entityId)
        return attrComp.IsEntityOnFire()

    def setEntityOnFire(self, seconds, burnDamage=1):
        # type: (int, int) -> bool
        """
        设置实体着火

        :param seconds: int 着火时间（单位：秒），当传入参数seconds小于等于0时，将让着火的实体灭火
        :param burnDamage: int 着火状态下每秒扣的血量,不传的话默认是1
        :return: bool 是否设置成功
        """
        attrComp = serverApi.GetEngineCompFactory().CreateAttr(self.entityId)
        return attrComp.SetEntityOnFire(seconds, burnDamage)

    def getMotion(self):
        # type: () -> tuple
        """
        获取生物的瞬时移动方向向量

        :return: tuple(float, float, float) 瞬时移动方向向量，异常时返回None
        """
        motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(self.entityId)
        return motionComp.GetMotion()

    def getEntityMotions(self):
        # type: () -> dict
        """
        获取实体身上的所有运动器

        :return: dict 运动器集合，key值代表运动器mID，value值代表运动器类型0：轨迹运动器、1：速度运动器、2：环绕运动器
        """
        motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(self.entityId)
        return motionComp.GetEntityMotions()

    def setActorCollidable(self, isCollidable):
        # type: (bool) -> bool
        """
        设置实体是否可碰撞

        :param isCollidable: bool 0:可碰撞 1:不可碰撞
        :return: bool True表示设置成功
        """
        collidableComp = serverApi.GetEngineCompFactory().CreateActorCollidable(self.entityId)
        return collidableComp.SetActorCollidable(int(isCollidable))

    def setActorPushable(self, isPushable):
        # type: (bool) -> bool
        """
        设置实体是否可推动

        :param isPushable: bool 0:不可推动 1:可推动
        :return: bool True表示设置成功
        """
        pushableComp = serverApi.GetEngineCompFactory().CreateActorPushable(self.entityId)
        return pushableComp.SetActorPushable(int(isPushable))

    def getLeashHolder(self):
        # type: () -> str
        """
        获取实体被使用拴绳牵引时牵引者的ID

        :return: str 牵引者ID，调用失败或者没有则返回 -1
        """
        entityDefinitionsComp = serverApi.GetEngineCompFactory().CreateEntityDefinitions(self.entityId)
        return entityDefinitionsComp.GetLeashHolder()

    def setLeashHolder(self, holderId):
        # type: (str) -> bool
        """
        为实体添加牵引者

        :param holderId: str 牵引者Id
        :return: bool 是否成功
        """
        entityDefinitionsComp = serverApi.GetEngineCompFactory().CreateEntityDefinitions(self.entityId)
        return entityDefinitionsComp.SetLeashHolder(holderId)

    def getRiders(self):
        # type: () -> list
        """
        获取坐骑上的骑乘者信息

        :return: list(dict) 骑乘者信息，包括骑乘者的entityId，其在骑乘者列表中的序号riderIndex以及所坐的座位序号seatIndex
        """
        rideComp = serverApi.GetEngineCompFactory().CreateRide(self.entityId)
        return rideComp.GetRiders()

    def changeRiderSeatIndex(self, riderIndex):
        # type: (int) -> bool
        """
        设置骑乘者在当前坐骑上的序号

        :param riderIndex: int 指定实体成为第n个骑乘者，范围为0~SeatCount-1
        :return: bool 设置结果
        """
        rideComp = serverApi.GetEngineCompFactory().CreateRide(self.entityId)
        return rideComp.ChangeRiderSeat(riderIndex)

    def setEntityLockRider(self, isLock):
        # type: (bool) -> bool
        """
        设置坐骑上的实体是否锁定序号

        :param isLock: bool 是否锁定实体当前所处的序号
        :return: bool 设置结果
        """
        rideComp = serverApi.GetEngineCompFactory().CreateRide(self.entityId)
        return rideComp.SetEntityLockRider(isLock)

    def setCanOtherPlayerRide(self, canRide):
        # type: (bool) -> bool
        """
        设置其他玩家是否有权限骑乘

        :param canRide: bool True表示每个玩家都能骑乘，False只有驯服者才能骑乘
        :return: bool 设置结果
        """
        rideComp = serverApi.GetEngineCompFactory().CreateRide(self.entityId)
        return rideComp.SetCanOtherPlayerRide(canRide)

    def setControl(self, isControl):
        # type: (bool) -> bool
        """
        设置该生物无需装备鞍就可以控制行走跳跃

        :param isControl: bool 是否控制
        :return: bool 设置结果
        """
        rideComp = serverApi.GetEngineCompFactory().CreateRide(self.entityId)
        return rideComp.SetControl(isControl)

    def setEntityShareablesItems(self, items):
        # type: (list) -> bool
        """
        设置生物可分享/可拾取的物品列表

        :param items: list(dict) 可分享/可拾取的物品列表
        :return: bool 设置结果
        """
        shareableComp = serverApi.GetEngineCompFactory().CreateShareables(self.entityId)
        return shareableComp.SetEntityShareablesItems(items)

    def isLootDropped(self):
        # type: () -> bool
        """
        获取生物是否生成掉落物

        :return: bool 是否能生成战利品
        """
        entityDefinitionsComp = serverApi.GetEngineCompFactory().CreateEntityDefinitions(self.entityId)
        return entityDefinitionsComp.IsLootDropped()

    def setLootDropped(self, isLootDropped):
        # type: (bool) -> bool
        """
        设置生物是否生成掉落物

        :param isLootDropped: bool 设置生物是否生成掉落物
        :return: bool 是否设置成功
        """
        entityDefinitionsComp = serverApi.GetEngineCompFactory().CreateEntityDefinitions(self.entityId)
        return entityDefinitionsComp.SetLootDropped(isLootDropped)

    def isPersistent(self):
        # type: () -> bool
        """
        判断是否为持久性生物

        :return: bool 是否为持久性生物
        """
        entityDefinitionsComp = serverApi.GetEngineCompFactory().CreateEntityDefinitions(self.entityId)
        return entityDefinitionsComp.IsPersistent()

    def isRoaring(self):
        # type: () -> bool
        """
        判断是否处于咆哮状态，仅对劫掠兽有效

        :return: bool 是否处于咆哮状态
        """
        entityDefinitionsComp = serverApi.GetEngineCompFactory().CreateEntityDefinitions(self.entityId)
        return entityDefinitionsComp.IsRoaring()

    def isStunned(self):
        # type: () -> bool
        """
        判断是否处于眩晕状态，仅对劫掠兽有效

        :return: bool 是否处于眩晕状态
        """
        entityDefinitionsComp = serverApi.GetEngineCompFactory().CreateEntityDefinitions(self.entityId)
        return entityDefinitionsComp.IsStunned()

    def setEntityRide(self, playerId, tamedEntityId):
        # type: (str, str) -> bool
        """
        设置实体骑乘

        :param playerId: str 玩家id
        :param tamedEntityId: str 要驯服的可骑乘生物id
        :return: bool 设置结果
        """
        rideComp = serverApi.GetEngineCompFactory().CreateRide(tamedEntityId)
        return rideComp.SetEntityRide(playerId, tamedEntityId)

    def isAlive(self):
        # type: () -> bool
        """
        判断生物实体是否存活或非生物实体是否存在

        :return: bool true表示存活或存在, false表示死亡或销毁或区块未加载
        示例:
            alive = self.isEntityAlive(entityId)
        """
        gameComp = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
        return gameComp.IsEntityAlive(self.entityId)

    def kill(self):
        # type: () -> bool
        """
        杀死某个Entity

        :return: bool 是否杀死成功
        示例:
            self.killEntity(entityId)
        """
        gameComp = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
        return gameComp.KillEntity(self.entityId)