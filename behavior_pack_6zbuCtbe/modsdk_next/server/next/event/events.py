# -*- coding: utf-8 -*-
if False:
    from typing import Tuple, Dict, List, Any
from ..Entity import Entity
from ..Player import Player


class AchievementCompleteEvent(object):
    """
    触发时机：玩家完成自定义成就时触发该事件
    :param playerId: 玩家id
    :param rootNodeId: 所属的页面的根节点成就id
    :param achievementId: 达成的成就id
    :param title: 成就标题
    :param description: 成就描述
    """
    playerId = None  # type: str
    rootNodeId = None  # type: str
    achievementId = None  # type: str
    title = None  # type: str
    description = None  # type: str

    def getPlayer(self):
        return Player(self.playerId)


class AddEntityServerEvent(object):
    """
    触发时机：服务端侧创建新实体，或实体从存档加载时触发
    :param id: 实体id
    :param posX: 位置x
    :param posY: 位置y
    :param posZ: 位置z
    :param dimensionId: 实体维度
    :param isBaby: 是否为幼儿
    :param engineTypeStr: 实体类型
    :param itemName: 物品identifier（仅当物品实体时存在该字段）
    :param auxValue: 物品附加值（仅当物品实体时存在该字段）
    """
    id = None  # type: str
    posX = None  # type: float
    posY = None  # type: float
    posZ = None  # type: float
    dimensionId = None  # type: int
    isBaby = None  # type: bool
    engineTypeStr = None  # type: str
    itemName = None  # type: str or None
    auxValue = None  # type: int or None

    def getEntity(self):
        return Entity(self.id)


class AddServerPlayerEvent(object):
    """
    触发时机：玩家加入时触发该事件。
    :param id: 玩家id
    :param isTransfer: 是否是切服时进入服务器
    :param isReconnect: 是否是断线重连
    :param isPeUser: 是否从手机端登录
    :param transferParam: 切服传入参数
    :param uid: 玩家的netease uid
    :param proxyId: 当前客户端连接的proxy服务器id
    """
    id = None  # type: str
    isTransfer = None  # type: bool
    isReconnect = None  # type: bool
    isPeUser = None  # type: bool
    transferParam = None  # type: str or None
    uid = None  # type: int or None
    proxyId = None  # type: int or None

    def getPlayer(self):
        return Player(self.id)


class ChunkAcquireDiscardedServerEvent(object):
    """
    触发时机：服务端区块即将被卸载时触发
    :param dimension: 区块所在维度
    :param chunkPosX: 区块的x坐标
    :param chunkPosZ: 区块的z坐标
    :param entities: 随区块卸载而从世界移除的实体id的列表
    :param blockEntities: 随区块卸载而从世界移除的自定义方块实体的坐标的列表
    """
    dimension = None  # type: int
    chunkPosX = None  # type: int
    chunkPosZ = None  # type: int
    entities = None  # type: List[str]
    blockEntities = None  # type: List[Dict[str, Any]]


class ChunkGeneratedServerEvent(object):
    """
    触发时机：区块创建完成时触发
    :param dimension: 该区块所在的维度
    :param blockEntityData: 该区块中的自定义方块实体列表
    """
    dimension = None  # type: int
    blockEntityData = None  # type: List[Dict[str, Any]] or None


class ChunkLoadedServerEvent(object):
    """
    触发时机：服务端区块加载完成时
    :param dimension: 区块所在维度
    :param chunkPosX: 区块的x坐标
    :param chunkPosZ: 区块的z坐标
    :param blockEntities: 随区块加载而加载进世界的自定义方块实体的坐标的列表
    """
    dimension = None  # type: int
    chunkPosX = None  # type: int
    chunkPosZ = None  # type: int
    blockEntities = None  # type: List[Dict[str, Any]]


class ClientLoadAddonsFinishServerEvent(object):
    """
    触发时机：客户端mod加载完成时，服务端触发此事件
    :param playerId: 玩家id
    """
    playerId = None  # type: str

    def getPlayer(self):
        return Player(self.playerId)


class CommandEvent(object):
    """
    触发时机：玩家请求执行指令时触发
    :param entityId: 玩家ID
    :param command: 指令字符串
    :param cancel: 是否取消
    """
    entityId = None  # type: str
    command = None  # type: str
    cancel = None  # type: bool

    def getPlayer(self):
        return Player(self.entityId)


class CustomCommandTriggerServerEvent(object):
    """
    触发时机：自定义命令触发事件
    :param command: 自定义命令名称
    :param args: 自定义命令参数
    :param origin: 触发源的信息
    :param return_failed: 设置自定义命令是否执行失败
    :param return_msg_key: 设置返回给玩家或命令方块的信息
    """
    command = None  # type: str
    args = None  # type: List[Dict[str, Any]]
    origin = None  # type: Dict[str, Any]
    return_failed = None  # type: bool
    return_msg_key = None  # type: str

    def getPlayer(self):
        if 'entityId' in self.origin:
            return Player(self.origin['entityId'])


class DelServerPlayerEvent(object):
    """
    触发时机：删除玩家时触发该事件
    :param id: 玩家id
    :param isTransfer: 是否是切服时退出服务器
    :param uid: 玩家的netease uid
    """
    id = None  # type: str
    isTransfer = None  # type: bool
    uid = None  # type: int

    def getPlayer(self):
        return Player(self.id)


class EntityRemoveEvent(object):
    """
    触发时机：实体被删除时触发
    :param id: 实体id
    """
    id = None  # type: str

    def getEntity(self):
        return Entity(self.id)


class ExplosionServerEvent(object):
    """
    触发时机：当发生爆炸时触发
    :param blocks: 爆炸导致的被破坏方块坐标
    :param victims: 受伤实体id列表
    :param sourceId: 爆炸创建者id
    :param explodePos: 爆炸位置
    :param dimensionId: 维度id
    """
    blocks = None  # type: List[Tuple[int, int, int, bool]]
    victims = None  # type: List[str] or None
    sourceId = None  # type: str or None
    explodePos = None  # type: Tuple[int, int, int]
    dimensionId = None  # type: int


class GlobalCommandServerEvent(object):
    """
    触发时机：服务端全局命令事件
    :param entityId: 执行命令的实体Id
    :param command: 命令
    :param blockPos: 执行命令的实体或方块的方块坐标
    :param dimension: 执行命令的实体或方块所在维度id
    :param cancel: 设置为True可以取消命令执行
    """
    entityId = None  # type: str or None
    command = None  # type: str
    blockPos = None  # type: Tuple[int, int, int]
    dimension = None  # type: int
    cancel = None  # type: bool

    def getPlayer(self):
        if self.entityId:
            return Player(self.entityId)


class NewOnEntityAreaEvent(object):
    """
    触发时机：通过RegisterEntityAOIEvent注册过AOI事件后，当有实体进入或离开注册感应区域时触发该事件
    :param name: 注册感应区域名称
    :param enteredEntities: 进入该感应区域的实体id列表
    :param leftEntities: 离开该感应区域的实体id列表
    """
    name = None  # type: str
    enteredEntities = None  # type: List[str]
    leftEntities = None  # type: List[str]

    def getEnteredEntities(self):
        return [Entity(entityId) for entityId in self.enteredEntities]

    def getLeftEntities(self):
        return [Entity(entityId) for entityId in self.leftEntities]


class OnCommandOutputServerEvent(object):
    """
    触发时机：Command命令执行成功事件
    :param command: 命令名称
    :param message: 命令返回的消息
    """
    command = None  # type: str
    message = None  # type: str


class OnContainerFillLoottableServerEvent(object):
    """
    触发时机：随机奖励箱第一次打开根据loottable生成物品时
    :param loottable: 奖励箱子所读取的loottable的json路径
    :param playerId: 打开奖励箱子的玩家的playerId
    :param itemList: 掉落物品列表
    :param dirty: 默认为False，如果需要修改掉落列表需将该值设为True
    """
    loottable = None  # type: str
    playerId = None  # type: str
    itemList = None  # type: List[Dict[str, Any]]
    dirty = None  # type: bool

    def getPlayer(self):
        return Player(self.playerId)


class OnLightningLevelChangeServerEvent(object):
    """
    触发时机：打雷强度发生改变
    :param oldLevel: 改变前的打雷强度
    :param newLevel: 改变后的打雷强度
    """
    oldLevel = None  # type: float
    newLevel = None  # type: float


class OnLocalLightningLevelChangeServerEvent(object):
    """
    触发时机：独立维度天气打雷强度发生改变时触发
    :param oldLevel: 改变前的打雷强度
    :param newLevel: 改变后的打雷强度
    :param dimensionId: 独立天气维度id
    """
    oldLevel = None  # type: float
    newLevel = None  # type: float
    dimensionId = None  # type: int


class OnLocalRainLevelChangeServerEvent(object):
    """
    触发时机：独立维度天气下雨强度发生改变时触发
    :param oldLevel: 改变前的下雨强度
    :param newLevel: 改变后的下雨强度
    :param dimensionId: 独立天气维度id
    """
    oldLevel = None  # type: float
    newLevel = None  # type: float
    dimensionId = None  # type: int


class OnRainLevelChangeServerEvent(object):
    """
    触发时机：下雨强度发生改变
    :param oldLevel: 改变前的下雨强度
    :param newLevel: 改变后的下雨强度
    """
    oldLevel = None  # type: float
    newLevel = None  # type: float


class OnScriptTickServer(object):
    """
    触发时机：服务器tick时触发,1秒有30个tick
    """
    pass


class PlaceNeteaseLargeFeatureServerEvent(object):
    """
    触发时机：网易版大型结构即将生成时服务端抛出该事件
    :param dimensionId: 维度id
    :param pos: 中心结构放置坐标
    :param rot: 中心结构顺时针旋转角度
    :param depth: 大型结构递归深度
    :param centerPool: 中心池的identifier
    :param ignoreFitInContext: 是否允许生成过结构的地方是否可以继续生成结构
    :param cancel: 设置为True时可阻止该大型结构的放置
    """
    dimensionId = None  # type: int
    pos = None  # type: Tuple[int, int]
    rot = None  # type: int
    depth = None  # type: int
    centerPool = None  # type: str
    ignoreFitInContext = None  # type: bool
    cancel = None  # type: bool


class PlaceNeteaseStructureFeatureEvent(object):
    """
    触发时机：首次生成地形时，结构特征即将生成时服务端抛出该事件
    :param structureName: 结构名称
    :param x: 结构坐标最小方块所在的x坐标
    :param y: 结构坐标最小方块所在的y坐标
    :param z: 结构坐标最小方块所在的z坐标
    :param biomeType: 该feature所放置区块的生物群系类型
    :param biomeName: 该feature所放置区块的生物群系名称
    :param dimensionId: 维度id
    :param cancel: 设置为True时可阻止该结构的放置
    """
    structureName = None  # type: str
    x = None  # type: int
    y = None  # type: int
    z = None  # type: int
    biomeType = None  # type: int
    biomeName = None  # type: str
    dimensionId = None  # type: int
    cancel = None  # type: bool


class PlayerIntendLeaveServerEvent(object):
    """
    触发时机：即将删除玩家时触发该事件
    :param playerId: 玩家id
    """
    playerId = None  # type: str

    def getPlayer(self):
        return Player(self.playerId)


class PlayerJoinMessageEvent(object):
    """
    触发时机：准备显示“xxx加入游戏”的玩家登录提示文字时服务端抛出的事件
    :param id: 玩家实体id
    :param name: 玩家昵称
    :param cancel: 是否显示提示文字
    :param message: 玩家加入游戏的提示文字
    """
    id = None  # type: str
    name = None  # type: str
    cancel = None  # type: bool
    message = None  # type: str

    def getPlayer(self):
        return Player(self.id)


class PlayerLeftMessageServerEvent(object):
    """
    触发时机：准备显示“xxx离开游戏”的玩家离开提示文字时服务端抛出的事件
    :param id: 玩家实体id
    :param name: 玩家昵称
    :param cancel: 是否显示提示文字
    :param message: 玩家离开游戏的提示文字
    """
    id = None  # type: str
    name = None  # type: str
    cancel = None  # type: bool
    message = None  # type: str

    def getPlayer(self):
        return Player(self.id)


class ServerChatEvent(object):
    """
    触发时机：玩家发送聊天信息时触发
    :param username: 玩家名称
    :param playerId: 玩家id
    :param message: 玩家发送的聊天消息内容
    :param cancel: 是否取消这个聊天事件
    :param bChatById: 是否把聊天消息发送给指定在线玩家
    :param bForbid: 是否禁言
    :param toPlayerIds: 接收聊天消息的玩家id列表
    :param gameChatPrefix: 设置当前玩家在网易聊天界面中的前缀
    :param gameChatPrefixColorR: 设置当前玩家在网易聊天界面中前缀颜色rgb的r值
    :param gameChatPrefixColorG: 设置当前玩家在网易聊天界面中前缀颜色rgb的g值
    :param gameChatPrefixColorB: 设置当前玩家在网易聊天界面中前缀颜色rgb的b值
    """
    username = None  # type: str
    playerId = None  # type: str
    message = None  # type: str
    cancel = None  # type: bool
    bChatById = None  # type: bool
    bForbid = None  # type: bool
    toPlayerIds = None  # type: List[str]
    gameChatPrefix = None  # type: str
    gameChatPrefixColorR = None  # type: float
    gameChatPrefixColorG = None  # type: float
    gameChatPrefixColorB = None  # type: float

    def getPlayer(self):
        return Player(self.playerId)


class ServerPostBlockPatternEvent(object):
    """
    触发时机：用方块组合生成生物，生成生物之后触发该事件
    :param entityId: 生成生物的id
    :param entityGenerated: 生成生物的名字
    :param x: 方块x坐标
    :param y: 方块y坐标
    :param z: 方块z坐标
    :param dimensionId: 维度id
    """
    entityId = None  # type: str
    entityGenerated = None  # type: str
    x = None  # type: int
    y = None  # type: int
    z = None  # type: int
    dimensionId = None  # type: int

    def getEntity(self):
        return Entity(self.entityId)


class ServerPreBlockPatternEvent(object):
    """
    触发时机：用方块组合生成生物，在放置最后一个组成方块时触发该事件
    :param enable: 是否允许继续生成
    :param x: 方块x坐标
    :param y: 方块y坐标
    :param z: 方块z坐标
    :param dimensionId: 维度id
    :param entityWillBeGenerated: 即将生成生物的名字
    """
    enable = None  # type: bool
    x = None  # type: int
    y = None  # type: int
    z = None  # type: int
    dimensionId = None  # type: int
    entityWillBeGenerated = None  # type: str


class ServerSpawnMobEvent(object):
    """
    触发时机：游戏内自动生成生物，以及使用api生成生物时触发
    :param entityId: 实体id
    :param identifier: 生成实体的命名空间
    :param type: 生成实体的类型
    :param baby: 生成怪物是否是幼年怪
    :param x: 生成实体坐标x
    :param y: 生成实体坐标y
    :param z: 生成实体坐标z
    :param dimensionId: 生成实体的维度
    :param realIdentifier: 生成实体的命名空间
    :param cancel: 是否取消生成该实体
    """
    entityId = None  # type: str
    identifier = None  # type: str
    type = None  # type: int
    baby = None  # type: bool
    x = None  # type: float
    y = None  # type: float
    z = None  # type: float
    dimensionId = None  # type: int
    realIdentifier = None  # type: str
    cancel = None  # type: bool

    def getEntity(self):
        return Entity(self.entityId)


class ActorHurtEvent(object):
    """
    触发时机：生物（包括玩家）受伤时触发
    :param entityId: 生物Id
    :param cause: 伤害来源
    :param damage: 伤害值（被伤害吸收后的值）
    :param damage_f: 伤害值（被伤害吸收后的值）
    :param absorbedDamage: 被伤害吸收效果吸收的伤害值
    :param customTag: 使用Hurt接口传入的自定义伤害类型
    """
    entityId = None  # type: str
    cause = None  # type: str
    damage = None  # type: int
    damage_f = None  # type: float
    absorbedDamage = None  # type: int
    customTag = None  # type: str

    def getEntity(self):
        return Entity(self.entityId)


class ActuallyHurtEvent(object):
    """
    触发时机：实体实际受到伤害时触发
    :param srcId: 伤害源id
    :param projectileId: 投射物id
    :param entityId: 被伤害id
    :param damage: 伤害值（被伤害吸收后的值）
    :param damage_f: 伤害值（被伤害吸收后的值）
    :param cause: 伤害来源
    :param customTag: 使用Hurt接口传入的自定义伤害类型
    """
    srcId = None  # type: str
    projectileId = None  # type: str
    entityId = None  # type: str
    damage = None  # type: int
    damage_f = None  # type: float
    cause = None  # type: str
    customTag = None  # type: str

    def getEntity(self):
        return Entity(self.entityId)


class AddEffectEvent(object):
    """
    触发时机：实体获得状态效果时
    :param entityId: 实体id
    :param effectName: 实体获得状态效果的名字
    :param effectDuration: 状态效果的持续时间，单位秒
    :param effectAmplifier: 状态效果的放大倍数
    :param damage: 状态造成的伤害值（真实扣除生命值的量）。只有持续时间为0时有用
    """
    entityId = None  # type: str
    effectName = None  # type: str
    effectDuration = None  # type: int
    effectAmplifier = None  # type: int
    damage = None  # type: int

    def getEntity(self):
        return Entity(self.entityId)


class ChangeSwimStateEvent(object):
    """
    触发时机：实体开始或者结束游泳时
    :param entityId: 实体的唯一ID
    :param formState: 事件触发前，实体是否在游泳状态
    :param toState: 事件触发后，实体是否在游泳状态
    """
    entityId = None  # type: str
    formState = None  # type: bool
    toState = None  # type: bool

    def getEntity(self):
        return Entity(self.entityId)


class DamageEvent(object):
    """
    触发时机：实体受到伤害时触发
    :param srcId: 伤害源id
    :param projectileId: 投射物id
    :param entityId: 被伤害id
    :param damage: 伤害值（被伤害吸收前的值）
    :param damage_f: 伤害值（被伤害吸收前的值）
    :param absorption: 受到伤害时，扣除黄心前，实体拥有的黄心血量
    :param cause: 伤害来源
    :param knock: 是否击退被攻击者
    :param ignite: 是否点燃被伤害者
    :param customTag: 使用Hurt接口传入的自定义伤害类型
    """
    srcId = None  # type: str
    projectileId = None  # type: str
    entityId = None  # type: str
    damage = None  # type: int
    damage_f = None  # type: float
    absorption = None  # type: int
    cause = None  # type: str
    knock = None  # type: bool
    ignite = None  # type: bool
    customTag = None  # type: str

    def getEntity(self):
        return Entity(self.entityId)


class EntityChangeDimensionEvent(object):
    """
    触发时机：实体维度改变时服务端抛出
    :param entityId: 实体id
    :param fromDimensionId: 维度改变前的维度
    :param toDimensionId: 维度改变后的维度
    :param fromX: 改变前的位置x
    :param fromY: 改变前的位置Y
    :param fromZ: 改变前的位置Z
    :param toX: 改变后的位置x
    :param toY: 改变后的位置Y
    :param toZ: 改变后的位置Z
    """
    entityId = None  # type: str
    fromDimensionId = None  # type: int
    toDimensionId = None  # type: int
    fromX = None  # type: float
    fromY = None  # type: float
    fromZ = None  # type: float
    toX = None  # type: float
    toY = None  # type: float
    toZ = None  # type: float

    def getEntity(self):
        return Entity(self.entityId)


class EntityDefinitionsEvent(object):
    """
    触发时机：生物定义json文件中设置的event触发时同时触发。生物行为变更事件
    :param entityId: 生物id
    :param eventName: 触发的事件名称
    """
    entityId = None  # type: str
    eventName = None  # type: str

    def getEntity(self):
        return Entity(self.entityId)


class EntityDieLoottableAfterEvent(object):
    """
    触发时机：生物死亡掉落物品之后
    :param dieEntityId: 死亡实体的entityId
    :param attacker: 伤害来源的entityId
    :param itemList: 掉落物品列表
    :param itemEntityIdList: 掉落物品entityId列表
    """
    dieEntityId = None  # type: str
    attacker = None  # type: str
    itemList = None  # type: list
    itemEntityIdList = None  # type: list

    def getEntity(self):
        return Entity(self.dieEntityId)


class EntityDieLoottableEvent(object):
    """
    触发时机：生物死亡掉落物品时
    :param dieEntityId: 死亡实体的entityId
    :param attacker: 伤害来源的entityId
    :param itemList: 掉落物品列表
    :param dirty: 默认为False，如果需要修改掉落列表需将该值设为True
    """
    dieEntityId = None  # type: str
    attacker = None  # type: str
    itemList = None  # type: list
    dirty = None  # type: bool

    def getEntity(self):
        return Entity(self.dieEntityId)


class EntityDroppedItemEvent(object):
    """
    触发时机：生物扔出物品时触发
    :param entityId: 生物Id
    :param itemDict: 扔出的物品的物品信息字典
    :param itemEntityId: 物品实体Id
    """
    entityId = None  # type: str
    itemDict = None  # type: dict
    itemEntityId = None  # type: str

    def getEntity(self):
        return Entity(self.entityId)


class EntityEffectDamageEvent(object):
    """
    触发时机：生物受到状态伤害/回复事件
    :param entityId: 实体id
    :param damage: 伤害值（伤害吸收后实际扣血量），负数表示生命回复量
    :param attributeBuffType: 状态类型
    :param duration: 状态持续时间，单位秒
    :param lifeTimer: 状态生命时间，单位秒
    :param isInstantaneous: 是否为立即生效状态
    :param cause: 伤害来源
    """
    entityId = None  # type: str
    damage = None  # type: int
    attributeBuffType = None  # type: int
    duration = None  # type: float
    lifeTimer = None  # type: float
    isInstantaneous = None  # type: bool
    cause = None  # type: str

    def getEntity(self):
        return Entity(self.entityId)


class EntityLoadScriptEvent(object):
    """
    触发时机：数据库加载实体自定义数据时触发
    :param args: 该事件的参数为长度为2的list，而非dict，其中list的第一个元素为实体id
    """
    args = None  # type: list

    def getEntity(self):
        return Entity(self.args[0])


class EntityMotionStartEvent(object):
    """
    触发时机：实体运动器开始事件
    :param motionId: 运动器id
    :param entityId: 实体id
    """
    motionId = None  # type: int
    entityId = None  # type: str

    def getEntity(self):
        return Entity(self.entityId)


class EntityMotionStopEvent(object):
    """
    触发时机：实体运动器停止事件
    :param motionId: 运动器id
    :param entityId: 实体id
    :param remove: 是否移除该运动器
    """
    motionId = None  # type: int
    entityId = None  # type: str
    remove = None  # type: bool

    def getEntity(self):
        return Entity(self.entityId)


class EntityPickupItemEvent(object):
    """
    触发时机：有minecraft:behavior.pickup_items行为的生物拾取物品时触发该事件
    :param entityId: 生物Id
    :param itemDict: 拾取的物品的物品信息字典
    :param secondaryActor: 物品给予者id（一般是玩家）
    """
    entityId = None  # type: str
    itemDict = None  # type: dict
    secondaryActor = None  # type: str

    def getEntity(self):
        return Entity(self.entityId)


class EntityStartRidingEvent(object):
    """
    触发时机：当实体骑乘上另一个实体时触发
    :param id: 乘骑者实体id
    :param rideId: 被乘骑者实体id
    """
    id = None  # type: str
    rideId = None  # type: str

    def getEntity(self):
        return Entity(self.id)


class EntityStopRidingEvent(object):
    """
    触发时机：当实体停止骑乘时
    :param id: 实体id
    :param rideId: 坐骑id
    :param exitFromRider: 是否下坐骑
    :param entityIsBeingDestroyed: 坐骑是否将要销毁
    :param switchingRides: 是否换乘坐骑
    :param cancel: 设置为True可以取消
    """
    id = None  # type: str
    rideId = None  # type: str
    exitFromRider = None  # type: bool
    entityIsBeingDestroyed = None  # type: bool
    switchingRides = None  # type: bool
    cancel = None  # type: bool

    def getEntity(self):
        return Entity(self.id)


class EntityTickEvent(object):
    """
    触发时机：实体tick时触发。该事件为20帧每秒
    :param entityId: 实体id
    :param identifier: 实体identifier
    """
    entityId = None  # type: str
    identifier = None  # type: str

    def getEntity(self):
        return Entity(self.entityId)


class HealthChangeBeforeEvent(object):
    """
    触发时机：生物生命值发生变化之前触发
    :param entityId: 实体id
    :param from: 变化前的生命值
    :param to: 将要变化到的生命值
    :param byScript: 是否通过SetAttrValue或SetAttrMaxValue调用产生的变化
    :param cancel: 是否取消该变化
    """
    entityId = None  # type: str
    from_ = None  # type: float
    to = None  # type: float
    byScript = None  # type: bool
    cancel = None  # type: bool

    def getEntity(self):
        return Entity(self.entityId)


class HealthChangeEvent(object):
    """
    触发时机：生物生命值发生变化时触发
    :param entityId: 实体id
    :param from_: 变化前的生命值
    :param to: 变化后的生命值
    :param byScript: 是否通过SetAttrValue或SetAttrMaxValue调用产生的变化
    """
    entityId = None  # type: str
    from_ = None  # type: float
    to = None  # type: float
    byScript = None  # type: bool

    def getEntity(self):
        return Entity(self.entityId)


class MobDieEvent(object):
    """
    触发时机：实体死亡时触发
    :param id: 实体id
    :param attacker: 伤害来源id
    :param cause: 伤害来源
    :param customTag: 使用Hurt接口传入的自定义伤害类型
    """
    id = None  # type: str
    attacker = None  # type: str
    cause = None  # type: str
    customTag = None  # type: str

    def getEntity(self):
        return Entity(self.id)


class MobGriefingBlockEvent(object):
    """
    触发时机：环境生物改变方块时触发
    :param cancel: 是否允许触发
    :param blockX: 方块x坐标
    :param blockY: 方块y坐标
    :param blockZ: 方块z坐标
    :param entityId: 触发的entity的唯一ID
    :param blockName: 方块的identifier
    :param dimensionId: 维度id
    """
    cancel = None  # type: bool
    blockX = None  # type: int
    blockY = None  # type: int
    blockZ = None  # type: int
    entityId = None  # type: str
    blockName = None  # type: str
    dimensionId = None  # type: int

    def getEntity(self):
        return Entity(self.entityId)


class OnFireHurtEvent(object):
    """
    触发时机：生物受到火焰伤害时触发
    :param victim: 受伤实体id
    :param src: 火焰创建者id
    :param fireTime: 着火时间，单位秒
    :param cancel: 是否取消此处火焰伤害
    :param cancelIgnite: 是否取消点燃效果
    """
    victim = None  # type: str
    src = None  # type: str
    fireTime = None  # type: float
    cancel = None  # type: bool
    cancelIgnite = None  # type: bool

    def getEntity(self):
        return Entity(self.victim)


class OnGroundEvent(object):
    """
    触发时机：实体着地事件
    :param id: 实体id
    """
    id = None  # type: str

    def getEntity(self):
        return Entity(self.id)


class OnKnockBackEvent(object):
    """
    触发时机：实体被击退时触发
    :param id: 实体id
    """
    id = None  # type: str

    def getEntity(self):
        return Entity(self.id)


class OnMobHitBlockEvent(object):
    """
    触发时机：生物（不包括玩家）碰撞到方块时触发该事件
    :param entityId: 碰撞到方块的生物Id
    :param posX: 碰撞方块x坐标
    :param posY: 碰撞方块y坐标
    :param posZ: 碰撞方块z坐标
    :param blockId: 碰撞方块的identifier
    :param auxValue: 碰撞方块的附加值
    :param dimensionId: 维度id
    """
    entityId = None  # type: str
    posX = None  # type: int
    posY = None  # type: int
    posZ = None  # type: int
    blockId = None  # type: str
    auxValue = None  # type: int
    dimensionId = None  # type: int

    def getEntity(self):
        return Entity(self.entityId)


class OnMobHitMobEvent(object):
    """
    触发时机：生物间（包含玩家）碰撞时触发该事件
    :param mobId: 当前生物的id
    :param hittedMobList: 当前生物碰撞到的其他所有生物id的list
    """
    mobId = None  # type: str
    hittedMobList = None  # type: list

    def getEntity(self):
        return Entity(self.mobId)


class ProjectileCritHitEvent(object):
    """
    触发时机：当抛射物与头部碰撞时触发该事件
    :param id: 抛射物id
    :param targetId: 碰撞目标id
    """
    id = None  # type: str
    targetId = None  # type: str

    def getEntity(self):
        return Entity(self.id)


class ProjectileDoHitEffectEvent(object):
    """
    触发时机：当抛射物碰撞时触发该事件
    :param id: 抛射物id
    :param hitTargetType: 碰撞目标类型
    :param targetId: 碰撞目标id
    :param hitFace: 撞击在方块上的面id
    :param x: 碰撞x坐标
    :param y: 碰撞y坐标
    :param z: 碰撞z坐标
    :param blockPosX: 碰撞是方块时，方块x坐标
    :param blockPosY: 碰撞是方块时，方块y坐标
    :param blockPosZ: 碰撞是方块时，方块z坐标
    :param srcId: 创建者id
    :param cancel: 是否取消这个碰撞事件
    """
    id = None  # type: str
    hitTargetType = None  # type: str
    targetId = None  # type: str
    hitFace = None  # type: int
    x = None  # type: float
    y = None  # type: float
    z = None  # type: float
    blockPosX = None  # type: int
    blockPosY = None  # type: int
    blockPosZ = None  # type: int
    srcId = None  # type: str
    cancel = None  # type: bool

    def getEntity(self):
        return Entity(self.id)


class RefreshEffectEvent(object):
    """
    触发时机：实体身上状态效果更新时触发
    :param entityId: 实体id
    :param effectName: 更新状态效果的名字
    :param effectDuration: 更新后状态效果剩余持续时间
    :param effectAmplifier: 更新后的状态效果放大倍数
    :param damage: 状态造成的伤害值
    """
    entityId = None  # type: str
    effectName = None  # type: str
    effectDuration = None  # type: int
    effectAmplifier = None  # type: int
    damage = None  # type: int

    def getEntity(self):
        return Entity(self.entityId)


class RemoveEffectEvent(object):
    """
    触发时机：实体身上状态效果被移除时
    :param entityId: 实体id
    :param effectName: 被移除状态效果的名字
    :param effectDuration: 被移除状态效果的剩余持续时间
    :param effectAmplifier: 被移除状态效果的放大倍数
    """
    entityId = None  # type: str
    effectName = None  # type: str
    effectDuration = None  # type: int
    effectAmplifier = None  # type: int

    def getEntity(self):
        return Entity(self.entityId)


class SpawnProjectileEvent(object):
    """
    触发时机：抛射物生成时触发
    :param projectileId: 抛射物的实体id
    :param projectileIdentifier: 抛射物的identifier
    :param spawnerId: 发射者的实体id
    """
    projectileId = None  # type: str
    projectileIdentifier = None  # type: str
    spawnerId = None  # type: str

    def getEntity(self):
        return Entity(self.projectileId)


class StartRidingEvent(object):
    """
    触发时机：一个实体即将骑乘另外一个实体
    :param cancel: 是否允许触发
    :param actorId: 骑乘者的唯一ID
    :param victimId: 被骑乘实体的唯一ID
    """
    cancel = None  # type: bool
    actorId = None  # type: str
    victimId = None  # type: str

    def getEntity(self):
        return Entity(self.actorId)


class WillAddEffectEvent(object):
    """
    触发时机：实体即将获得状态效果前
    :param entityId: 实体id
    :param effectName: 实体获得状态效果的名字
    :param effectDuration: 状态效果的持续时间
    :param effectAmplifier: 状态效果的放大倍数
    :param cancel: 设置为True可以取消
    :param damage: 状态将会造成的伤害值
    """
    entityId = None  # type: str
    effectName = None  # type: str
    effectDuration = None  # type: int
    effectAmplifier = None  # type: int
    cancel = None  # type: bool
    damage = None  # type: int

    def getEntity(self):
        return Entity(self.entityId)


class WillTeleportToEvent(object):
    """
    触发时机：实体即将传送或切换维度
    :param cancel: 是否允许触发
    :param entityId: 实体的唯一ID
    :param fromDimensionId: 传送前所在的维度
    :param toDimensionId: 传送后的目标维度
    :param fromX: 传送前所在的x坐标
    :param fromY: 传送前所在的y坐标
    :param fromZ: 传送前所在的z坐标
    :param toX: 传送目标地点的x坐标
    :param toY: 传送目标地点的y坐标
    :param toZ: 传送目标地点的z坐标
    :param cause: 传送理由
    """
    cancel = None  # type: bool
    entityId = None  # type: str
    fromDimensionId = None  # type: int
    toDimensionId = None  # type: int
    fromX = None  # type: int
    fromY = None  # type: int
    fromZ = None  # type: int
    toX = None  # type: int
    toY = None  # type: int
    toZ = None  # type: int
    cause = None  # type: str

    def getEntity(self):
        return Entity(self.entityId)


class AddExpEvent(object):
    """
    触发时机：当玩家增加经验时触发该事件。
    :param playerId: 玩家id
    :param addExp: 增加的经验值
    """
    playerId = None  # type: str
    addExp = None  # type: int

    def getPlayer(self):
        return Player(self.playerId)


class AddLevelEvent(object):
    """
    触发时机：当玩家升级时触发该事件。
    :param playerId: 玩家id
    :param addLevel: 增加的等级值
    :param newLevel: 新的等级
    """
    playerId = None  # type: str
    addLevel = None  # type: int
    newLevel = None  # type: int

    def getPlayer(self):
        return Player(self.playerId)


class ChangeLevelUpCostServerEvent(object):
    """
    触发时机：获取玩家下一个等级升级经验时，用于重载玩家的升级经验，每个等级在重置之前都只会触发一次
    :param level: 玩家当前等级
    :param levelUpCostExp: 当前等级升级到下个等级需要的经验值
    :param changed: 设置为True，重载玩家升级经验才会生效
    """
    level = None  # type: int
    levelUpCostExp = None  # type: int
    changed = None  # type: bool


class DimensionChangeServerEvent(object):
    """
    触发时机：玩家维度改变时服务端抛出
    :param playerId: 玩家实体id
    :param fromDimensionId: 维度改变前的维度
    :param toDimensionId: 维度改变后的维度
    :param fromX: 改变前的位置x
    :param fromY: 改变前的位置Y
    :param fromZ: 改变前的位置Z
    :param toX: 改变后的位置x
    :param toY: 改变后的位置Y
    :param toZ: 改变后的位置Z
    """
    playerId = None  # type: str
    fromDimensionId = None  # type: int
    toDimensionId = None  # type: int
    fromX = None  # type: float
    fromY = None  # type: float
    fromZ = None  # type: float
    toX = None  # type: float
    toY = None  # type: float
    toZ = None  # type: float

    def getPlayer(self):
        return Player(self.playerId)


class DimensionChangeFinishServerEvent(object):
    """
    触发时机：玩家维度改变完成后服务端抛出
    :param playerId: 玩家实体id
    :param fromDimensionId: 维度改变前的维度
    :param toDimensionId: 维度改变后的维度
    :param toPos: 改变后的位置x,y,z,其中y值为脚底加上角色的身高值
    """
    playerId = None  # type: str
    fromDimensionId = None  # type: int
    toDimensionId = None  # type: int
    toPos = None  # type: Tuple[float, float, float]

    def getPlayer(self):
        return Player(self.playerId)


class ExtinguishFireServerEvent(object):
    """
    触发时机：玩家扑灭火焰时触发。下雨，倒水等方式熄灭火焰不会触发。
    :param pos: 火焰方块的坐标
    :param playerId: 玩家id
    :param cancel: 修改为True时，可阻止玩家扑灭火焰。需要与ExtinguishFireClientEvent一起修改。
    """
    pos = None  # type: Tuple[float, float, float]
    playerId = None  # type: str
    cancel = None  # type: bool

    def getPlayer(self):
        return Player(self.playerId)


class GameTypeChangedServerEvent(object):
    """
    触发时机：当默认游戏模式或个人游戏模式发生变化时服务端触发，如果个人游戏模式不为默认时，修改默认游戏模式也会同时修改个人游戏模式，此时会触发两次该事件
    :param playerId: 玩家Id，SetDefaultGameType接口改变游戏模式时该参数为空字符串
    :param oldGameType: 切换前的游戏模式
    :param newGameType: 切换后的游戏模式
    """
    playerId = None  # type: str
    oldGameType = None  # type: int
    newGameType = None  # type: int

    def getPlayer(self):
        return Player(self.playerId)


class OnPlayerActionServerEvent(object):
    """
    触发时机：玩家动作事件，当玩家开始/停止某些动作时触发该事件
    :param playerId: 玩家id
    :param actionType: 动作事件枚举
    """
    playerId = None  # type: str
    actionType = None  # type: int

    def getPlayer(self):
        return Player(self.playerId)


class OnPlayerHitBlockServerEvent(object):
    """
    触发时机：通过OpenPlayerHitBlockDetection打开方块碰撞检测后，当玩家碰撞到方块时触发该事件。监听玩家着地请使用客户端的OnGroundClientEvent。客户端和服务端分别作碰撞检测，可能两个事件返回的略有差异。
    :param playerId: 碰撞到方块的玩家Id
    :param posX: 碰撞方块x坐标
    :param posY: 碰撞方块y坐标
    :param posZ: 碰撞方块z坐标
    :param blockId: 碰撞方块的identifier
    :param auxValue: 碰撞方块的附加值
    :param dimensionId: 维度id
    """
    playerId = None  # type: str
    posX = None  # type: int
    posY = None  # type: int
    posZ = None  # type: int
    blockId = None  # type: str
    auxValue = None  # type: int
    dimensionId = None  # type: int

    def getPlayer(self):
        return Player(self.playerId)


class PlayerAttackEntityEvent(object):
    """
    触发时机：当玩家攻击时触发该事件。
    :param playerId: 玩家id
    :param victimId: 受击者id
    :param damage: 伤害值：引擎传过来的值是0 允许脚本层修改为其他数
    :param isValid: 脚本是否设置伤害值：1表示是；0 表示否
    :param cancel: 是否取消该次攻击，默认不取消
    :param isKnockBack: 是否支持击退效果，默认支持，当不支持时将屏蔽武器击退附魔效果
    :param isCrit: 本次攻击是否产生暴击,不支持修改
    """
    playerId = None  # type: str
    victimId = None  # type: str
    damage = None  # type: int
    isValid = None  # type: int
    cancel = None  # type: bool
    isKnockBack = None  # type: bool
    isCrit = None  # type: bool

    def getPlayer(self):
        return Player(self.playerId)


class PlayerCheatSpinAttackServerEvent(object):
    """
    触发时机：玩家开始/结束快速旋转攻击并且不符合发送快速旋转攻击条件时触发（装备激流附魔的三叉戟、在水中或雨中，且未骑乘）
    :param playerId: 玩家的entityId
    :param isStart: True时代表开始快速旋转攻击；False时代表结束快速旋转攻击
    """
    playerId = None  # type: str
    isStart = None  # type: bool

    def getPlayer(self):
        return Player(self.playerId)


class PlayerDieEvent(object):
    """
    触发时机：当玩家死亡时触发该事件。
    :param playerId: 玩家id
    :param attacker: 伤害来源id
    :param customTag: 使用Hurt接口传入的自定义伤害类型
    :param cause: 伤害来源
    """
    playerId = None  # type: str
    attacker = None  # type: str
    customTag = None  # type: str
    cause = None  # type: str

    def getPlayer(self):
        return Player(self.playerId)


class PlayerDoInteractServerEvent(object):
    """
    触发时机：玩家与有minecraft:interact组件的生物交互时触发该事件，例如玩家手持空桶对牛挤奶、玩家手持打火石点燃苦力怕
    :param playerId: 玩家id
    :param itemDict: 交互时使用物品的物品信息字典
    :param interactEntityId: 交互的生物entityId
    """
    playerId = None  # type: str
    itemDict = None  # type: Dict
    interactEntityId = None  # type: str

    def getPlayer(self):
        return Player(self.playerId)


class PlayerEatFoodServerEvent(object):
    """
    触发时机：玩家吃下食物时触发
    :param playerId: 玩家Id
    :param itemDict: 食物物品的物品信息字典
    :param hunger: 食物增加的饥饿值，可修改
    :param nutrition: 食物的营养价值，回复饱和度 = 食物增加的饥饿值 * 食物的营养价值 * 2，饱和度最大不超过当前饥饿值，可修改
    """
    playerId = None  # type: str
    itemDict = None  # type: Dict
    hunger = None  # type: int
    nutrition = None  # type: float

    def getPlayer(self):
        return Player(self.playerId)


class PlayerFeedEntityServerEvent(object):
    """
    触发时机：玩家喂养生物时触发，例如玩家手持小麦喂养牛、玩家手持胡萝卜喂养幼年猪。
    :param playerId: 主动喂养生物的玩家的唯一ID
    :param entityId: 被喂养生物的唯一ID
    :param itemDict: 当前玩家手持物品的物品信息字典
    :param cancel: 是否取消触发，默认为False，若设为True，可阻止触发后续的生物喂养逻辑
    """
    playerId = None  # type: str
    entityId = None  # type: str
    itemDict = None  # type: Dict
    cancel = None  # type: bool

    def getPlayer(self):
        return Player(self.playerId)


class PlayerHungerChangeServerEvent(object):
    """
    触发时机：玩家饥饿度变化时触发该事件
    :param playerId: 玩家id
    :param hungerBefore: 变化前的饥饿度
    :param hunger: 变化后的饥饿度
    :param cancel: 是否取消饥饿度变化
    """
    playerId = None  # type: str
    hungerBefore = None  # type: float
    hunger = None  # type: float
    cancel = None  # type: bool

    def getPlayer(self):
        return Player(self.playerId)


class PlayerHurtEvent(object):
    """
    触发时机：当玩家受伤害前触发该事件。
    :param playerId: 受击玩家id
    :param attacker: 伤害来源实体id，若没有实体攻击，例如高空坠落，id为-1
    :param customTag: 使用Hurt接口传入的自定义伤害类型
    :param cause: 伤害来源
    """
    playerId = None  # type: str
    attacker = None  # type: str
    customTag = None  # type: str
    cause = None  # type: str

    def getPlayer(self):
        return Player(self.playerId)


class PlayerInteractServerEvent(object):
    """
    触发时机：玩家可以与实体交互时。如果是鼠标控制模式，则当准心对着实体时触发。如果是触屏模式，则触发时机与屏幕下方的交互按钮显示的时机相同。玩家真正与实体发生交互的事件见PlayerDoInteractServerEvent
    :param cancel: 是否取消触发，默认为False，若设为True，可阻止触发后续的实体交互事件
    :param playerId: 主动与实体互动的玩家的唯一ID
    :param itemDict: 当前玩家手持物品的物品信息字典
    :param victimId: 被动的实体的唯一ID
    """
    cancel = None  # type: bool
    playerId = None  # type: str
    itemDict = None  # type: Dict
    victimId = None  # type: str

    def getPlayer(self):
        return Player(self.playerId)


class PlayerNamedEntityServerEvent(object):
    """
    触发时机：玩家用命名牌重命名实体时触发，例如玩家手持命名牌对羊修改名字、玩家手持命名牌对盔甲架修改名字。
    :param playerId: 主动命名实体的玩家的唯一ID
    :param entityId: 被命名实体的唯一ID
    :param preName: 实体当前的名字
    :param afterName: 实体重命名后的名字
    :param cancel: 是否取消触发，默认为False，若设为True，可阻止触发后续的实体命名逻辑
    """
    playerId = None  # type: str
    entityId = None  # type: str
    preName = None  # type: str
    afterName = None  # type: str
    cancel = None  # type: bool

    def getPlayer(self):
        return Player(self.playerId)


class PlayerRespawnEvent(object):
    """
    触发时机：玩家复活时触发该事件。
    :param playerId: 玩家id
    """
    playerId = None  # type: str

    def getPlayer(self):
        return Player(self.playerId)


class PlayerRespawnFinishServerEvent(object):
    """
    触发时机：玩家复活完毕时触发
    :param playerId: 玩家id
    """
    playerId = None  # type: str

    def getPlayer(self):
        return Player(self.playerId)


class PlayerSleepServerEvent(object):
    """
    触发时机：玩家使用床睡觉成功
    :param playerId: 玩家id
    """
    playerId = None  # type: str

    def getPlayer(self):
        return Player(self.playerId)


class PlayerSpinAttackServerEvent(object):
    """
    触发时机：玩家开始/结束快速旋转攻击时触发
    :param playerId: 玩家的entityId
    :param isInWaterOrRain: 是否在水中或雨中
    :param isRiding: 是否骑乘状态
    :param isStart: True时代表开始快速旋转攻击；False时代表结束快速旋转攻击
    """
    playerId = None  # type: str
    isInWaterOrRain = None  # type: bool
    isRiding = None  # type: bool
    isStart = None  # type: bool

    def getPlayer(self):
        return Player(self.playerId)


class PlayerStopSleepServerEvent(object):
    """
    触发时机：玩家停止睡觉
    :param playerId: 玩家id
    """
    playerId = None  # type: str

    def getPlayer(self):
        return Player(self.playerId)


class PlayerTeleportEvent(object):
    """
    触发时机：当玩家传送时触发该事件，如：玩家使用末影珍珠或tp指令时。
    :param playerId: 玩家id
    """
    playerId = None  # type: str

    def getPlayer(self):
        return Player(self.playerId)


class PlayerTrySleepServerEvent(object):
    """
    触发时机：玩家尝试使用床睡觉
    :param playerId: 玩家id
    :param cancel: 是否取消（开发者传入）
    """
    playerId = None  # type: str
    cancel = None  # type: bool

    def getPlayer(self):
        return Player(self.playerId)


class ServerPlayerGetExperienceOrbEvent(object):
    """
    触发时机：玩家获取经验球时触发的事件
    :param playerId: 玩家id
    :param experienceValue: 经验球经验值
    :param cancel: 是否取消（开发者传入）
    """
    playerId = None  # type: str
    experienceValue = None  # type: int
    cancel = None  # type: bool

    def getPlayer(self):
        return Player(self.playerId)


class StoreBuySuccServerEvent(object):
    """
    触发时机: 玩家游戏内购买商品时服务端抛出的事件
    :param playerId: 购买商品的玩家实体id
    """
    playerId = None  # type: str

    def getPlayer(self):
        return Player(self.playerId)