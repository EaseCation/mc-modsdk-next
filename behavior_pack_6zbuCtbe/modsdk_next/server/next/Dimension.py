# -*- coding: utf-8 -*-
import mod.server.extraServerApi as serverApi

class Dimension(object):

    __slots__ = ('dimensionId', 'levelId')

    def __init__(self, dimensionId):
        # type: (int) -> None
        """
        :param dimensionId: 维度id, 例如0-主世界, 1-地狱, 2-末地, 也可为自定义大于20的维度
        """
        self.dimensionId = dimensionId
        self.levelId = serverApi.GetLevelId()  # type: str

    def canSee(self, fromId, targetId, viewRange=8.0, onlySolid=True, angleX=180.0, angleY=180.0):
        # type: (str, str, float, bool, float, float) -> bool
        """
        判断起始对象(fromId)是否可看见目标对象(targetId)，基于两者Head位置判断
        :param fromId: str 起始对象ID
        :param targetId: str 目标对象ID
        :param viewRange: float 视野距离，默认8.0
        :param onlySolid: bool 是否只判断固体方块遮挡，默认为True；False则液体方块也会遮挡
        :param angleX: float 视野X轴角度，默认为180.0
        :param angleY: float 视野Y轴角度，默认为180.0
        :return: bool 是否可见
        备注：
          * 本API本身并未提供dimensionId参数，但此处可依赖fromId或targetId所处维度进行判断
        示例:
            comp = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            visible = comp.CanSee(entityId, targetId, 20.0, True, 180.0, 180.0)
        """
        gameComp = serverApi.GetEngineCompFactory().CreateGame(self.levelId)
        return gameComp.CanSee(fromId, targetId, viewRange, onlySolid, angleX, angleY)

    def checkBlockToPos(self, fromPos, toPos):
        # type: (tuple, tuple) -> int
        """
        判断同一维度(fromPos->toPos)之间是否有方块
        :param fromPos: tuple(float,float,float) 起始位置
        :param toPos: tuple(float,float,float) 终止位置
        :return: int result
                  -1：获取失败(可能区块未加载或传入的维度非法)
                   0：没有方块
                   1：有方块
        示例:
            comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
            result = comp.CheckBlockToPos((0,0,0), (1,1,1), dimensionId)
        """
        blockInfoComp = serverApi.GetEngineCompFactory().CreateBlockInfo(self.levelId)
        return blockInfoComp.CheckBlockToPos(fromPos, toPos, self.dimensionId)

    def checkChunkState(self, pos):
        # type: (tuple) -> bool
        """
        判断指定位置所在的chunk是否加载完成
        :param pos: tuple(int,int,int) 指定位置坐标
        :return: bool 该chunk是否加载完成
        示例:
            comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
            comp.CheckChunkState(dimensionId, (0,0,0))
        """
        chunkComp = serverApi.GetEngineCompFactory().CreateChunkSource(self.levelId)
        return chunkComp.CheckChunkState(self.dimensionId, pos)

    def createExplosion(self, pos, radius, fire, breaks, sourceId=None, playerId=None):
        # type: (tuple, int, bool, bool, str, str) -> bool
        """
        生成爆炸
        :param pos: tuple(float,float,float) 爆炸位置
        :param radius: int 爆炸威力
        :param fire: bool 是否带火
        :param breaks: bool 是否破坏方块
        :param sourceId: str 爆炸伤害源的实体id，可为空
        :param playerId: str 爆炸创造的实体id，可为空
        :return: bool 设置结果
        示例:
            comp = serverApi.GetEngineCompFactory().CreateExplosion(levelId)
            comp.CreateExplosion((50,50,50),10,True,True,sourceId,playerId)
        """
        explodeComp = serverApi.GetEngineCompFactory().CreateExplosion(self.levelId)
        return explodeComp.CreateExplosion(pos, radius, fire, breaks, sourceId, playerId)

    def deleteAllArea(self):
        # type: () -> int
        """
        删除所有常加载区域
        :return: int 删除的区域数目，错误时返回None
        示例:
            comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
            comp.DeleteAllArea()
        """
        chunkComp = serverApi.GetEngineCompFactory().CreateChunkSource(self.levelId)
        return chunkComp.DeleteAllArea()

    def deleteArea(self, key):
        # type: (str) -> bool
        """
        删除一个常加载区域
        :param key: str 常加载区域的名称
        :return: bool 删除是否成功
        示例:
            comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
            comp.DeleteArea('Area0')
        """
        chunkComp = serverApi.GetEngineCompFactory().CreateChunkSource(self.levelId)
        return chunkComp.DeleteArea(key)

    def detectStructure(self, pattern, defines, touchPos, pos):
        # type: (list, dict, list, tuple) -> tuple
        """
        检测自定义门的结构
        :param pattern: list(str) 传送门形状
        :param defines: dict 传送门定义(方块对应关系)
        :param touchPos: list(tuple(int,int)) 传送门可激活的位置(相对pattern)
        :param pos: tuple(int,int,int) 使用物品坐标(检测起点)
        :return: tuple(bool, tuple(int,int,int), tuple(int,int,int))
                 - 是否匹配, 传送门起始位置, 传送门方向
        示例:
            comp = serverApi.GetEngineCompFactory().CreatePortal(levelId)
            ret = comp.DetectStructure(None, pattern, defines, touchPos, (12,1,5), dimensionId)
        """
        portalComp = serverApi.GetEngineCompFactory().CreatePortal(self.levelId)
        # DetectStructure需要playerId, 但已废弃，用None
        return portalComp.DetectStructure(None, pattern, defines, touchPos, pos, self.dimensionId)

    def doTaskOnChunkAsync(self, posMin, posMax, callback):
        # type: (tuple, tuple, callable) -> bool
        """
        异步加载指定范围区块，加载完成后调用回调函数
        :param posMin: tuple(int,int,int) 范围最小值(需小于posMax)
        :param posMax: tuple(int,int,int) 范围最大值
        :param callback: function 回调函数(需能接收形如{'code':1}的dict)
        :return: bool 是否成功
        备注：
          * 仅在self.dimensionId表示的维度中进行异步加载
        示例:
            comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
            comp.DoTaskOnChunkAsync(dimensionId, (0,0,0), (100,0,100), callback)
        """
        chunkComp = serverApi.GetEngineCompFactory().CreateChunkSource(self.levelId)
        return chunkComp.DoTaskOnChunkAsync(self.dimensionId, posMin, posMax, callback)

    def getAllAreaKeys(self):
        # type: () -> list
        """
        获取所有常加载区域名称列表
        :return: list(str) 名称列表
        示例:
            comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
            comp.GetAllAreaKeys()
        """
        chunkComp = serverApi.GetEngineCompFactory().CreateChunkSource(self.levelId)
        return chunkComp.GetAllAreaKeys()

    def getBiomeInfo(self, biomeName):
        # type: (str) -> dict
        """
        获取某个生物群系的天气相关参数
        :param biomeName: str 群系名字
        :return: dict 群系天气相关参数, 获取失败返回None
        示例:
            comp = serverApi.GetEngineCompFactory().CreateBiome(levelId)
            info = comp.GetBiomeInfo("desert")
        """
        biomeComp = serverApi.GetEngineCompFactory().CreateBiome(self.levelId)
        return biomeComp.GetBiomeInfo(biomeName)

    def getBiomeName(self, pos):
        # type: (tuple) -> str
        """
        获取某一位置的生物群系名称(服务端接口)
        :param pos: tuple(int,int,int) 指定位置
        :return: str 生物群系名字
        备注：
          * 未加载区块将使用地形生成器计算群系
        示例:
            comp = serverApi.GetEngineCompFactory().CreateBiome(levelId)
            biomeName = comp.GetBiomeName((0, 80, 0), dimensionId)
        """
        biomeComp = serverApi.GetEngineCompFactory().CreateBiome(self.levelId)
        return biomeComp.GetBiomeName(pos, self.dimensionId)

    def getBlockLightLevel(self, pos):
        # type: (tuple) -> int
        """
        获取方块位置的光照等级
        :param pos: tuple(int,int,int) 方块坐标
        :return: int 光照等级(0~15)。-1说明失败(区块未加载等)
        示例:
            comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
            level = comp.GetBlockLightLevel((x,y,z), dimensionId)
        """
        blockInfoComp = serverApi.GetEngineCompFactory().CreateBlockInfo(self.levelId)
        return blockInfoComp.GetBlockLightLevel(pos, self.dimensionId)

    def getChunkEntites(self, pos):
        # type: (tuple) -> list
        """
        获取指定位置所在的区块中全部实体ID列表(不含区块未加载情况)
        :param pos: tuple(int,int,int) 指定位置坐标
        :return: list(str) 实体ID列表, 若区块不存在或未加载则返回None
        示例:
            comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
            entityList = comp.GetChunkEntites(dimensionId, (0,0,0))
        """
        chunkComp = serverApi.GetEngineCompFactory().CreateChunkSource(self.levelId)
        return chunkComp.GetChunkEntites(self.dimensionId, pos)

    def getChunkMaxPos(self, chunkPos):
        # type: (tuple) -> tuple
        """
        获取某区块最大点坐标
        :param chunkPos: tuple(int,int) 区块坐标
        :return: tuple(int,int,int) 或 None(输入非法)
        备注：
          * 调用时需确保使用具体实体id创建comp或使用维度信息，否则获取值可能不正确
        示例:
            comp = serverApi.GetEngineCompFactory().CreateChunkSource(entityId)
            maxPos = comp.GetChunkMaxPos((1, 3))
        """
        chunkComp = serverApi.GetEngineCompFactory().CreateChunkSource(self.levelId)
        return chunkComp.GetChunkMaxPos(chunkPos)

    def getChunkMinPos(self, chunkPos):
        # type: (tuple) -> tuple
        """
        获取某区块最小点坐标
        :param chunkPos: tuple(int,int) 区块坐标
        :return: tuple(int,int,int) 或 None(输入非法)
        备注：
          * 调用时需确保使用具体实体id创建comp或使用维度信息，否则获取值可能不正确
        示例:
            comp = serverApi.GetEngineCompFactory().CreateChunkSource(entityId)
            minPos = comp.GetChunkMinPos((1, 3))
        """
        chunkComp = serverApi.GetEngineCompFactory().CreateChunkSource(self.levelId)
        return chunkComp.GetChunkMinPos(chunkPos)

    def getChunkMobNum(self, chunkPos):
        # type: (tuple) -> int
        """
        获取某区块中的生物数量(不包括玩家，但包括盔甲架)
        :param chunkPos: tuple(int,int) 区块坐标
        :return: int 生物数量，-1说明区块未加载或维度不存在
        示例:
            comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
            num = comp.GetChunkMobNum(dimensionId, (1,3))
        """
        chunkComp = serverApi.GetEngineCompFactory().CreateChunkSource(self.levelId)
        return chunkComp.GetChunkMobNum(self.dimensionId, chunkPos)

    def getChunkPosFromBlockPos(self, blockPos):
        # type: (tuple) -> tuple
        """
        通过方块坐标获取所在区块坐标
        :param blockPos: tuple(int,int,int) 方块坐标
        :return: tuple(int,int) 或 None(输入非法)
        示例:
            comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
            chunkPos = comp.GetChunkPosFromBlockPos((90, 40, -4))
        """
        chunkComp = serverApi.GetEngineCompFactory().CreateChunkSource(self.levelId)
        return chunkComp.GetChunkPosFromBlockPos(blockPos)

    def getEntitiesAround(self, centerId, radius, filters=None):
        # type: (str, int, dict) -> list
        """
        获取以centerId为中心, 正方体区域半径=radius内的全部实体id列表(可选过滤器)
        :param centerId: str 区域中心实体id
        :param radius: int 范围半径(方形半径)
        :param filters: dict 过滤器设置,可选
        :return: list(str) 实体id列表
        示例:
            comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
            comp.GetEntitiesAround(entityId, 100, filters)
        """
        gameComp = serverApi.GetEngineCompFactory().CreateGame(self.levelId)
        return gameComp.GetEntitiesAround(centerId, radius, filters or {})

    def getEntitiesAroundByType(self, centerId, radius, entityType):
        # type: (str, int, int) -> list
        """
        获取指定类型实体列表,以centerId为中心的正方体区域半径=radius
        :param centerId: str 区域中心实体id
        :param radius: int 范围半径(方形)
        :param entityType: int EntityType枚举值
        :return: list(str) 实体id列表
        示例:
            comp.GetEntitiesAroundByType(entityId, 10, serverApi.GetMinecraftEnum().EntityType.ItemEntity)
        """
        gameComp = serverApi.GetEngineCompFactory().CreateGame(self.levelId)
        return gameComp.GetEntitiesAroundByType(centerId, radius, entityType)

    def getEntitiesInSquareArea(self, startPos, endPos):
        # type: (tuple, tuple) -> list
        """
        获取长方体区域[startPos, endPos]内的实体id列表(服务端接口)
        :param startPos: tuple(int,int,int) 区域最小坐标
        :param endPos: tuple(int,int,int) 区域最大坐标
        :return: list(str) 区域内实体id列表
        备注：
          * dimensionId由self.dimensionId
          * 表面相接不视为碰撞，需要AABB真正重合
        示例:
            comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
            comp.GetEntitiesInSquareArea(None, (0,0,0), (100,100,100), dimensionId)
        """
        gameComp = serverApi.GetEngineCompFactory().CreateGame(self.levelId)
        return gameComp.GetEntitiesInSquareArea(None, startPos, endPos, self.dimensionId)

    def getLoadedChunks(self):
        # type: () -> list
        """
        获取当前维度已加载的全部区块坐标列表
        :return: list(tuple(int,int)) 或 None(维度不存在/未创建)
        示例:
            comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
            result = comp.GetLoadedChunks(dimensionId)
        """
        chunkComp = serverApi.GetEngineCompFactory().CreateChunkSource(self.levelId)
        return chunkComp.GetLoadedChunks(self.dimensionId)

    def getSpawnDimension(self):
        # type: () -> int
        """
        获取世界出生维度
        :return: int 维度ID
        示例:
            comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
            spawnDimension = comp.GetSpawnDimension()
        """
        gameComp = serverApi.GetEngineCompFactory().CreateGame(self.levelId)
        return gameComp.GetSpawnDimension()

    def getSpawnPosition(self):
        # type: () -> tuple
        """
        获取世界出生点坐标
        :return: tuple(int,int,int) 出生点坐标
        备注：
          * 若未设置过worldspawn，则y轴可能是32767
        示例:
            comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
            spawnPos = comp.GetSpawnPosition()
        """
        gameComp = serverApi.GetEngineCompFactory().CreateGame(self.levelId)
        return gameComp.GetSpawnPosition()

    def getStructureSize(self, structureName):
        # type: (str) -> tuple
        """
        获取指定结构的长宽高
        :param structureName: str 结构名称
        :return: tuple(int,int,int) 或 None(失败)
        示例:
            comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
            comp.GetStructureSize("test:structureName")
        """
        gameComp = serverApi.GetEngineCompFactory().CreateGame(self.levelId)
        return gameComp.GetStructureSize(structureName)

    def isChunkGenerated(self, chunkPos):
        # type: (tuple) -> bool
        """
        判断某区块是否生成过(已存在于存档)
        :param chunkPos: tuple(int,int) 区块坐标
        :return: bool
        备注：
          * 设置常加载区块或玩家探索过的区块都算生成过
        """
        chunkComp = serverApi.GetEngineCompFactory().CreateChunkSource(self.levelId)
        return chunkComp.IsChunkGenerated(self.dimensionId, chunkPos)

    def isSlimeChunk(self, chunkPos):
        # type: (tuple) -> bool
        """
        判断某区块是否是史莱姆区块
        :param chunkPos: tuple(int,int) 区块坐标
        :return: bool
        示例:
            comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
            result = comp.IsSlimeChunk(dimensionId, chunkPos)
        """
        chunkComp = serverApi.GetEngineCompFactory().CreateChunkSource(self.levelId)
        return chunkComp.IsSlimeChunk(self.dimensionId, chunkPos)

    def locateNeteaseFeatureRule(self, ruleName, pos, mustBeInNewChunk=False):
        # type: (str, tuple, bool) -> tuple
        """
        类似/locate，用于定位网易自定义特征规则
        :param ruleName: str 特征规则名称
        :param pos: tuple(int,int,int) 起始查找位置
        :param mustBeInNewChunk: bool 是否只在未加载区块中寻找，默认False
        :return: tuple(float,float,float) 或 None
        备注：
          * 若找不到满足规则的位置或维度未加载，返回None
        示例:
            comp = serverApi.GetEngineCompFactory().CreateFeature(levelId)
            position = comp.LocateNeteaseFeatureRule("custombiomes:xxx", dimensionId, (0,64,0), False)
        """
        featureComp = serverApi.GetEngineCompFactory().CreateFeature(self.levelId)
        return featureComp.LocateNeteaseFeatureRule(ruleName, self.dimensionId, pos, mustBeInNewChunk)

    def locateStructureFeature(self, featureType, pos, useNewChunksOnly=False):
        # type: (int, tuple, bool) -> tuple
        """
        与/locate指令类似, 定位原版部分结构
        :param featureType: int 结构类型枚举(StructureFeatureType)
        :param pos: tuple(int,int,int) 起始查找位置
        :param useNewChunksOnly: bool 是否只在未生成的区块中寻找，默认False
        :return: tuple(float,float) 或 None
        示例:
            comp = serverApi.GetEngineCompFactory().CreateFeature(levelId)
            result = comp.LocateStructureFeature(serverApi.GetMinecraftEnum().StructureFeatureType.Village, dimensionId, (0,64,0), False)
        """
        featureComp = serverApi.GetEngineCompFactory().CreateFeature(self.levelId)
        return featureComp.LocateStructureFeature(featureType, self.dimensionId, pos, useNewChunksOnly)

    def mayPlace(self, identifier, blockPos, facing):
        # type: (str, tuple, int) -> bool
        """
        判断方块是否可以放置
        :param identifier: str 方块identifier，如minecraft:wheat
        :param blockPos: tuple(int,int,int) 放置的位置
        :param facing: int 朝向，Facing枚举
        :return: bool 是否可放置
        示例:
            comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
            canPlace = comp.MayPlace("minecraft:wheat", pos, facing, dimensionId)
        """
        blockInfoComp = serverApi.GetEngineCompFactory().CreateBlockInfo(self.levelId)
        return blockInfoComp.MayPlace(identifier, blockPos, facing, self.dimensionId)

    def mayPlaceOn(self, identifier, auxValue, blockPos, facing):
        # type: (str, int, tuple, int) -> bool
        """
        判断物品是否可以在指定位置放置(如染料, 并非生成实体的物品)
        :param identifier: str 物品identifier
        :param auxValue: int 物品附加值
        :param blockPos: tuple(int,int,int) 要放置的方块位置
        :param facing: int 朝向(Facing枚举)
        :return: bool 是否可放置
        备注：
          * 不支持常加载区块
          * 不支持放置会生成实体的物品(如船, 盔甲架等)
        示例:
            comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
            comp.MayPlaceOn("minecraft:dye", 3, (1,2,3), facing)
        """
        # 此接口在 itemCompServer 中，无 dimensionId 参数，但在此类中仅做代理
        itemComp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
        return itemComp.MayPlaceOn(identifier, auxValue, blockPos, facing)

    def mirror(self, fromId):
        # type: (int) -> bool
        """
        复制不同dimension的地形(将fromId维度复制到self.dimensionId)
        :param fromId: int 原dimensionId
        :return: bool 是否设置成功
        备注：
          * 仅复制源维度已生成区块至新的维度
        示例:
            comp = serverApi.GetEngineCompFactory().CreateDimension(levelId)
            comp.MirrorDimension(0, 1)
        """
        dimComp = serverApi.GetEngineCompFactory().CreateDimension(self.levelId)
        return dimComp.MirrorDimension(fromId, self.dimensionId)

    def openClientChunkGeneration(self, enable):
        # type: (bool) -> bool
        """
        开启/关闭客户端区块生成功能(LoadServerAddonScriptsAfter事件触发时调用)
        :param enable: bool True开启(默认)，False关闭
        :return: bool 是否成功
        备注：
          * 若使用netease:structure_feature或大幅修改地图，建议关闭客户端区块生成以防数据不一致
        示例:
            comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
            comp.OpenClientChunkGeneration(False)
        """
        chunkComp = serverApi.GetEngineCompFactory().CreateChunkSource(self.levelId)
        return chunkComp.OpenClientChunkGeneration(enable)

    def placeFeature(self, featureName, pos):
        # type: (str, tuple) -> bool
        """
        放置特征
        :param featureName: str 特征名称，如"test:pumpkins"
        :param pos: tuple(int,int,int) 放置位置
        :return: bool 是否放置成功
        示例:
            comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
            comp.PlaceFeature("test:pumpkins", dimensionId, (0,64,0))
        """
        gameComp = serverApi.GetEngineCompFactory().CreateGame(self.levelId)
        return gameComp.PlaceFeature(featureName, self.dimensionId, pos)

    def placeNeteaseLargeFeature(self, poolName, pos, rotation=0, maxDepth=5):
        # type: (str, tuple, int, int) -> bool
        """
        放置网易版大型结构特征
        :param poolName: str 中心池identifier，如"minecraft:centerPool"
        :param pos: tuple(int,int,int) 放置位置
        :param rotation: int 旋转角度(0,90,180,270)，默认0
        :param maxDepth: int 递归最大深度，默认5
        :return: bool 是否放置成功
        备注:
          * 需确保区块加载，否则可能部分缺失
        示例:
            comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
            comp.PlaceNeteaseLargeFeature("minecraft:centerPool", dimensionId, (0,65,0), 90, 5)
        """
        gameComp = serverApi.GetEngineCompFactory().CreateGame(self.levelId)
        return gameComp.PlaceNeteaseLargeFeature(poolName, self.dimensionId, pos, rotation, maxDepth)

    def placeStructure(self, structureName, pos, rotation=0, animationMode=0,
                       animationTime=0.0, includeEntity=True, removeBlock=False,
                       mirrorMode=0, integrity=100.0, seed=-1):
        # type: (str, tuple, int, int, float, bool, bool, int, float, int) -> bool
        """
        放置结构(同步执行,区块需已加载)
        :param structureName: str 结构名称
        :param pos: tuple(float,float,float) 放置位置
        :param rotation: int 旋转角度(0/90/180/270)，默认0
        :param animationMode: int 动画模式,AnimationModeType枚举,默认0
        :param animationTime: float 动画时长,默认0
        :param includeEntity: bool 是否包含实体,默认True
        :param removeBlock: bool 是否移除方块,默认False
        :param mirrorMode: int 镜像模式,MirrorModeType枚举,默认0
        :param integrity: float 完整度,默认100
        :param seed: int 随机种子,默认-1
        :return: bool 是否放置成功
        示例:
            comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
            comp.PlaceStructure(None,(100,70,100),"test:structureName",dimensionId,0)
        """
        gameComp = serverApi.GetEngineCompFactory().CreateGame(self.levelId)
        return gameComp.PlaceStructure(None, pos, structureName, self.dimensionId, rotation,
                                       animationMode, animationTime, includeEntity, removeBlock,
                                       mirrorMode, integrity, seed)

    def setAddArea(self, key, minPos, maxPos):
        # type: (str, tuple, tuple) -> bool
        """
        设置区块常加载区域(不会tick)
        :param key: str 常加载名称(需唯一)
        :param minPos: tuple(int,int,int) 加载区域最小坐标
        :param maxPos: tuple(int,int,int) 加载区域最大坐标
        :return: bool 设置是否成功
        备注:
          * 建议外扩80格, 以确保CheckChunkState可正常返回True
          * 需配合tick指令/原版tickingarea指令才会进行实体、方块等更新
        示例:
            comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
            comp.SetAddArea('Area0', dimensionId, (-80,0,-80), (80,0,80))
        """
        chunkComp = serverApi.GetEngineCompFactory().CreateChunkSource(self.levelId)
        return chunkComp.SetAddArea(key, self.dimensionId, minPos, maxPos)

    def setBiomeByPos(self, pos, biomeName):
        # type: (tuple, str) -> bool
        """
        设置某一位置的生物群系
        :param pos: tuple(int,int,int) 坐标
        :param biomeName: str 生物群系名称
        :return: bool 是否设置成功
        示例:
            comp = serverApi.GetEngineCompFactory().CreateBiome(levelId)
            result = comp.SetBiomeByPos((0,80,0), "desert", dimensionId)
        """
        biomeComp = serverApi.GetEngineCompFactory().CreateBiome(self.levelId)
        return biomeComp.SetBiomeByPos(pos, biomeName, self.dimensionId)

    def setBiomeByPosList(self, posList, biomeName):
        # type: (list, str) -> dict
        """
        设置posList中所有位置的生物群系
        :param posList: list(tuple(int,int,int)) 坐标列表
        :param biomeName: str 生物群系名称
        :return: dict 状态信息{"Update":bool, "BlockList":list}
        备注:
          * Update若有任意坐标设置失败即False
          * BlockList为设置失败的坐标列表(原对象)
        示例:
            comp = serverApi.GetEngineCompFactory().CreateBiome(levelId)
            info = comp.SetBiomeByPosList(posList, "desert", dimensionId)
        """
        biomeComp = serverApi.GetEngineCompFactory().CreateBiome(self.levelId)
        return biomeComp.SetBiomeByPosList(posList, biomeName, self.dimensionId)

    def setBiomeByVolume(self, minPos, maxPos, biomeName):
        # type: (tuple, tuple, str) -> bool
        """
        设置长方体区域[minPos, maxPos]的生物群系
        :param minPos: tuple(int,int,int)
        :param maxPos: tuple(int,int,int)
        :param biomeName: str 生物群系名称
        :return: bool 是否全部成功
        备注:
          * 超出范围会被忽略
          * 只支持已加载区块
        示例:
            comp = serverApi.GetEngineCompFactory().CreateBiome(levelId)
            res = comp.SetBiomeByVolume((0,0,0),(31,31,31),"desert",dimensionId)
        """
        biomeComp = serverApi.GetEngineCompFactory().CreateBiome(self.levelId)
        return biomeComp.SetBiomeByVolume(minPos, maxPos, biomeName, self.dimensionId)

    def setBiomeInfo(self, biomeName, snowAccumulation, temperature, downfall, isRain):
        # type: (str, tuple, float, float, bool) -> bool
        """
        设置群系天气相关参数(不存档)
        :param biomeName: str 群系名字
        :param snowAccumulation: tuple(float,float) (min,max)的积雪量
        :param temperature: float 温度, <=0.15下雪, >1无特殊意义
        :param downfall: float 降雨(雪)强度,会影响湿度
        :param isRain: bool 是否降雨(雪)
        :return: bool 是否设置成功
        示例:
            comp = serverApi.GetEngineCompFactory().CreateBiome(levelId)
            comp.SetBiomeInfo("desert",(0.125,1),0.15,1,True)
        """
        biomeComp = serverApi.GetEngineCompFactory().CreateBiome(self.levelId)
        return biomeComp.SetBiomeInfo(biomeName, snowAccumulation, temperature, downfall, isRain)

    def setMergeSpawnItemRadius(self, radius):
        # type: (float) -> bool
        """
        设置新生成物品的合堆检测半径
        :param radius: float 范围0~5,0表示不合堆
        :return: bool 是否成功
        示例:
            comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
            comp.SetMergeSpawnItemRadius(5.0)
        """
        gameComp = serverApi.GetEngineCompFactory().CreateGame(self.levelId)
        return gameComp.SetMergeSpawnItemRadius(radius)

    def setSpawnDimensionAndPosition(self, dimId=None, pos=None):
        # type: (int, tuple) -> bool
        """
        设置世界出生点维度与坐标
        :param dimId: int或None 维度id, None表示只设置坐标
        :param pos: tuple(int,int,int)或None 出生坐标, None表示只设置维度
        :return: bool 是否成功
        备注:
          * y=65535表示出生到xz最高实心方块上
          * 若与/spawnpoint冲突, spawnpoint优先级更高
        示例:
            comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
            comp.SetSpawnDimensionAndPosition(3,(0,60,0))
        """
        gameComp = serverApi.GetEngineCompFactory().CreateGame(self.levelId)
        return gameComp.SetSpawnDimensionAndPosition(dimId, pos)

    def upgradeMapVersion(self, version):
        # type: (int) -> bool
        """
        提升指定维度的地图版本号(存档不符则清理)
        :param version: int [1~999]
        :return: bool 是否成功
        备注:
          * 若区块已加载,则不会清理成功
        示例:
            comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
            comp.UpgradeMapDimensionVersion(dimensionId,10)
        """
        gameComp = serverApi.GetEngineCompFactory().CreateGame(self.levelId)
        return gameComp.UpgradeMapDimensionVersion(self.dimensionId, version)

    def createEngineEntityByNBT(self, nbtDict, pos=None, rot=None, dimensionId=None, isNpc=False, isGlobal=None):
        # type: (dict, tuple, tuple, int, bool, bool) -> str
        """
        根据给定的nbt数据创建实体

        :param nbtDict: dict 实体nbt数据，可通过GetEntityNBTTags获取
        :param pos: tuple(float,float,float) or None 生成坐标; 传None则使用nbt中的Pos
        :param rot: tuple(float,float) or None 实体旋转(上下角度,左右角度); 传None则使用nbt中的Rotation
                   注意：nbt中 Rotation=[y,x]
        :param dimensionId: int 生成维度, 若为None则默认为self.dimensionId
        :param isNpc: bool 是否生成npc, npc不会移动、转向、存档
        :param isGlobal: None or bool 是否全局实体；None表示沿用nbt中的值；True/False表示覆盖
        :return: str or None 新实体id或None(创建失败)

        备注：
          * 无法创建玩家实体
          * 若需要直接修改nbtDict["Rotation"]，注意数据顺序 (y,x)
        示例:
            comp = serverApi.GetEngineCompFactory().CreateEntityDefinitions(entityId)
            nbt = comp.GetEntityNBTTags()
            newEntityId = self.createEngineEntityByNBT(nbt, (0,5,0))
        """
        systemCls = serverApi.GetServerSystemCls()
        systemObj = systemCls()
        finalDim = dimensionId if (dimensionId is not None) else self.dimensionId
        return systemObj.CreateEngineEntityByNBT(nbtDict, pos, rot, finalDim, isNpc, isGlobal)

    def createEngineEntityByTypeStr(self, engineTypeStr, pos, rot=(0, 0), dimensionId=None, isNpc=False, isGlobal=False):
        # type: (str, tuple, tuple, int, bool, bool) -> str
        """
        创建指定identifier的实体

        :param engineTypeStr: str 实体identifier, 如 'minecraft:husk', 'minecraft:villager_v2'
        :param pos: tuple(float,float,float) 生成坐标
        :param rot: tuple(float,float) 生成旋转(上下角度, 左右角度)，单位:度
        :param dimensionId: int 生成的维度，若None则默认self.dimensionId
        :param isNpc: bool 是否生成npc, npc不会移动、转向、存档
        :param isGlobal: bool 是否生成全局实体, 默认False
        :return: str或None 实体Id或None表示创建失败

        备注：
          * 在未加载的chunk无法创建
          * 对村民使用"minecraft:villager_v2"
        示例:
            entityId = self.createEngineEntityByTypeStr(
                'minecraft:husk', (0, 5, 0), (0, 0), 0
            )
        """
        systemCls = serverApi.GetServerSystemCls()
        systemObj = systemCls()
        finalDim = dimensionId if (dimensionId is not None) else self.dimensionId
        return systemObj.CreateEngineEntityByTypeStr(engineTypeStr, pos, rot, finalDim, isNpc, isGlobal)

    def createEngineItemEntity(self, itemDict, pos, dimensionId=None):
        # type: (dict, tuple, int) -> str
        """
        用于创建物品实体(掉落物)，返回物品实体的entityId

        :param itemDict: dict 物品信息字典
        :param pos: tuple(float,float,float) 生成坐标
        :param dimensionId: int 生成维度，默认为None(使用self.dimensionId)
        :return: str或None entityId或None
        示例:
            itemDict = {
                'itemName': 'minecraft:bow',
                'count': 1,
                'enchantData': [(serverApi.GetMinecraftEnum().EnchantType.BowDamage, 1)],
                'auxValue': 0,
                'customTips':'§c new item §r',
                'extraId': 'abc',
                'userData': { 'color': { '__type__':8, '__value__':'gray'} },
            }
            entityId = self.createEngineItemEntity(itemDict, (0,5,0))
        """
        systemCls = serverApi.GetServerSystemCls()
        systemObj = systemCls()
        finalDim = dimensionId if (dimensionId is not None) else self.dimensionId
        return systemObj.CreateEngineItemEntity(itemDict, finalDim, pos)

    def createEntityAOI(self, name, aabb, func):
        # type: (str, tuple, callable) -> bool
        """
        在本维度注册感应区域(AOI)

        :param name: str 感应区域的名称
        :param aabb: tuple(float,float,float,float,float,float)
                     区域坐标范围(minX,minY,minZ, maxX,maxY,maxZ)
        :param func: function 回调函数, 参数为dict
                     {
                        "AOIName": str,
                        "entityType": int, #见EntityType枚举
                        "pos": tuple(float,float,float), #进入时有
                        "dimension": int,
                        "entityId": str,
                        "identifier": str,
                        "isEnter": bool # True进入,False离开
                     }
        :return: bool 是否注册成功
        备注：
          * 第一次创建AOI时, 区域内已有生物也会触发回调
          * 不支持区域长或宽大于2000
        示例:
            def myAOIFunc(args):
                print "entity trigger AOI", args

            self.createEntityAOI("myTest", (0, 0, 0, 10, 10, 10), myAOIFunc)
        """
        dimComp = serverApi.GetEngineCompFactory().CreateDimension(self.levelId)
        return dimComp.CreateEntityAOI(self.dimensionId, name, aabb, func)

    def createExperienceOrb(self, entityId, exp, position, isSpecial=False):
        # type: (str, int, tuple, bool) -> bool
        """
        创建专属经验球 (或普通经验球)

        :param entityId: str 经验球专属的玩家或生物ID(如专属,则只此实体可拾取)
        :param exp: int 经验球经验
        :param position: tuple(float,float,float) 生成位置
        :param isSpecial: bool 是否专属,默认False
        :return: bool 是否创建成功
        备注：
          * 如果是专属经验球, 只有entityId对应的实体能拾取
        示例:
            self.createExperienceOrb(playerId, 25, (10,10,10), False)
        """
        expComp = serverApi.GetEngineCompFactory().CreateExp(entityId)
        return expComp.CreateExperienceOrb(exp, position, isSpecial)

    def createProjectileEntity(self, spawnerId, entityIdentifier, param=None):
        # type: (str, str, dict) -> str
        """
        创建并发射抛射物

        :param spawnerId: str 创建者的entityId
        :param entityIdentifier: str 投掷物identifier，如'minecraft:snowball'
        :param param: dict
            {
              'position':(float,float,float),
              'direction':(float,float,float),
              'power':float,
              'gravity':float,
              'damage':float,
              'targetId':str,
              'isDamageOwner':bool,
              'auxValue':int
            }
        :return: str 创建的抛射物ID, 失败时返回"-1"
        示例:
            param = {
                'position': (1,1,1),
                'direction': (1,1,1),
                'power': 2.0
            }
            self.createProjectileEntity(playerId, "minecraft:snowball", param)
        """
        projComp = serverApi.GetEngineCompFactory().CreateProjectile(self.levelId)
        return projComp.CreateProjectileEntity(spawnerId, entityIdentifier, param)

    def deleteEntityAOI(self, name):
        # type: (str) -> bool
        """
        删除感应区

        :param name: str 要删除的AOI名称
        :return: bool 是否删除成功
        示例:
            self.deleteEntityAOI("myTest")
        """
        dimComp = serverApi.GetEngineCompFactory().CreateDimension(self.levelId)
        return dimComp.DeleteEntityAOI(self.dimensionId, name)

    def destroyEntity(self, entityId):
        # type: (str) -> bool
        """
        销毁实体

        :param entityId: str 待销毁的实体ID
        :return: bool 是否销毁成功
        备注：
          * 对玩家实体无效
        示例:
            self.destroyEntity(entityId)
        """
        systemCls = serverApi.GetServerSystemCls()
        systemObj = systemCls()
        return systemObj.DestroyEntity(entityId)

    def getDroppedItem(self, itemEntityId, getUserData=False):
        # type: (str, bool) -> dict
        """
        获取掉落物实体对应的物品信息

        :param itemEntityId: str 掉落物实体ID
        :param getUserData: bool 是否获取userData，默认False
        :return: dict or None 物品信息字典, 若实体不存在则None
        示例:
            comp = serverApi.GetEngineCompFactory().CreateItem(levelId)
            info = comp.GetDroppedItem(itemEntityId)
        """
        itemComp = serverApi.GetEngineCompFactory().CreateItem(self.levelId)
        return itemComp.GetDroppedItem(itemEntityId, getUserData)

    def getEngineActor(self):
        # type: () -> dict
        """
        获取所有已加载的非玩家实体信息(跨所有维度)

        :return: dict { entityId: { 'dimensionId': int, 'identifier': str }, ... }
                      若无实体则返回空dict
        示例:
            entityDicts = serverApi.GetEngineActor()
        """
        return serverApi.GetEngineActor()

    def getPlayerList(self):
        # type: () -> list
        """
        获取所有维度中已加载的全部玩家ID列表

        :return: list(str) 玩家ID列表
        备注：
          * 列表顺序不保证
        示例:
            players = serverApi.GetPlayerList()
        """
        return serverApi.GetPlayerList()

    def isEntityAlive(self, entityId):
        # type: (str) -> bool
        """
        判断生物实体是否存活或非生物实体是否存在

        :param entityId: str 实体id
        :return: bool true表示存活或存在, false表示死亡或销毁或区块未加载
        示例:
            alive = self.isEntityAlive(entityId)
        """
        gameComp = serverApi.GetEngineCompFactory().CreateGame(self.levelId)
        return gameComp.IsEntityAlive(entityId)

    def killEntity(self, entityId):
        # type: (str) -> bool
        """
        杀死某个Entity

        :param entityId: str 要杀死的目标实体id
        :return: bool 是否杀死成功
        示例:
            self.killEntity(entityId)
        """
        gameComp = serverApi.GetEngineCompFactory().CreateGame(self.levelId)
        return gameComp.KillEntity(entityId)

    def spawnItemToLevel(self, itemDict, pos, dimensionId=None):
        # type: (dict, tuple, int) -> bool
        """
        生成物品掉落物(不返回entityId)，若需要实体Id可用CreateEngineItemEntity

        :param itemDict: dict 物品信息
        :param pos: tuple(float,float,float) 生成位置
        :param dimensionId: int 若None则默认self.dimensionId
        :return: bool 是否成功
        示例:
            itemDict = {...}
            self.spawnItemToLevel(itemDict, (0,80,20))
        """
        itemComp = serverApi.GetEngineCompFactory().CreateItem(self.levelId)
        finalDim = dimensionId if (dimensionId is not None) else self.dimensionId
        return itemComp.SpawnItemToLevel(itemDict, finalDim, pos)

    def spawnLootTable(self, pos, identifier, playerKillerId=None, damageCauseEntityId=None):
        # type: (tuple, str, str, str) -> bool
        """
        使用生物类型模拟一次随机掉落并立即生成掉落物

        :param pos: tuple(int,int,int) 掉落位置
        :param identifier: str 生物identifier(如"minecraft:guardian")
        :param playerKillerId: str 玩家杀手id(可影响抢夺附魔、经验掉落等),默认None
        :param damageCauseEntityId: str 伤害来源id(影响抢夺)，默认None
        :return: bool 是否成功生成
        备注：
          * 需要在player实体附近，否则生成失败
          * 某些特殊生物可能需要用SpawnLootTableWithActor
        示例:
            self.spawnLootTable((1,4,5),'minecraft:guardian')
        """
        lootComp = serverApi.GetEngineCompFactory().CreateActorLoot(self.levelId)
        return lootComp.SpawnLootTable(pos, identifier, playerKillerId, damageCauseEntityId)

    def spawnLootTableWithActor(self, pos, entityId, playerKillerId=None, damageCauseEntityId=None):
        # type: (tuple, str, str, str) -> bool
        """
        使用生物实例模拟一次随机掉落并立即生成掉落物

        :param pos: tuple(int,int,int) 掉落位置
        :param entityId: str 模拟的生物entityId
        :param playerKillerId: str 玩家杀手, 默认None
        :param damageCauseEntityId: str 伤害来源, 默认None
        :return: bool 是否成功
        备注：
          * 需要在玩家实体附近，否则会生成失败
        示例:
            self.spawnLootTableWithActor((1,4,5), someEntityId)
        """
        lootComp = serverApi.GetEngineCompFactory().CreateActorLoot(self.levelId)
        return lootComp.SpawnLootTableWithActor(pos, entityId, playerKillerId, damageCauseEntityId)

    def spawnResources(self, identifier, pos, aux, probability=1.0, bonusLootLevel=0,
                       dimensionId=None, allowRandomness=True):
        # type: (str, tuple, int, float, int, int, bool) -> bool
        """
        产生方块随机掉落(不适用于实体方块)

        :param identifier: str 方块identifier,如"minecraft:gold_ore"
        :param pos: tuple(int,int,int) 掉落位置
        :param aux: int 方块Aux
        :param probability: float 掉落概率[0~1],默认1.0
        :param bonusLootLevel: int 时运等级,默认0
        :param dimensionId: int 若None则使用self.dimensionId
        :param allowRandomness: bool True则使用probability进行随机
        :return: bool 是否成功
        备注：
          * bonusLootLevel仅对部分方块生效
          * probability对部分农作物/树叶无效
          * 需区块已加载
        示例:
            self.spawnResources("minecraft:gold_ore",(1,1,1),7,1.0,10,0)
        """
        blockInfoComp = serverApi.GetEngineCompFactory().CreateBlockInfo(self.levelId)
        finalDim = dimensionId if dimensionId is not None else self.dimensionId
        return blockInfoComp.SpawnResources(identifier, pos, aux, probability, bonusLootLevel,
                                            finalDim, allowRandomness)

    def spawnResourcesSilkTouched(self, identifier, pos, aux, dimensionId=None):
        # type: (str, tuple, int, int) -> bool
        """
        模拟方块精准采集掉落

        :param identifier: str 方块identifier,如"minecraft:gold_ore"
        :param pos: tuple(int,int,int) 掉落位置
        :param aux: int 方块Aux
        :param dimensionId: int 若None则使用self.dimensionId
        :return: bool 是否成功
        备注：
          * 若该方块不属于可精准采集范畴,返回False
        示例:
            self.spawnResourcesSilkTouched("minecraft:gold_ore",(1,1,1),7)
        """
        blockInfoComp = serverApi.GetEngineCompFactory().CreateBlockInfo(self.levelId)
        finalDim = dimensionId if dimensionId is not None else self.dimensionId
        return blockInfoComp.SpawnResourcesSilkTouched(identifier, pos, aux, finalDim)

    def getEntitiesOrBlockFromRay(self, pos, rot, distance=16, isThrough=False, filterType=None):
        # type: (tuple, tuple, float, bool, object) -> list
        """
        从pos向rot方向发射一条射线，获取相交的实体或方块

        :param pos: tuple(float,float,float) 射线起点
        :param rot: tuple(float,float,float) 射线方向(单位向量)
        :param distance: float 射线长度(默认16)
        :param isThrough: bool 是否穿透(穿透时返回所有碰撞对象，否则返回第一个)
        :param filterType: RayFilterType枚举,可用serverApi.GetMinecraftEnum().RayFilterType.OnlyEntities等
        :return: list(dict)
                 若选中实体, dict结构:
                   {"type":"Entity","entityId":xxx,"identifier":xxx,"hitPos":(x,y,z)}
                 若选中方块, dict结构:
                   {"type":"Block","pos":(xx,yy,zz),"identifier":xxx,"hitPos":(x,y,z)}
                 若未选中,返回None
        备注：
          * 需指定dimensionId->使用self.dimensionId
          * 不检测无碰撞盒clip的方块(如火焰)
        示例:
            results = self.getEntitiesOrBlockFromRay((0,0,0), (1,0,0), 16, False, serverApi.GetMinecraftEnum().RayFilterType.OnlyEntities)
        """
        rayFilter = filterType if (filterType is not None) else serverApi.GetMinecraftEnum().RayFilterType.OnlyEntities
        return serverApi.getEntitiesOrBlockFromRay(
            self.dimensionId, pos, rot, distance, isThrough, rayFilter
        )

    def getBlockClip(self, pos):
        # type: (tuple) -> dict
        """
        获取某一位置方块当前clip的aabb
        :param pos: tuple(int,int,int) 方块位置
        :return: dict 方块clip的aabb字典
        备注：
          * 仅能获取已加载区块内方块信息
          * 由于方块的碰撞盒会随周围环境动态改变，此处返回的是当前时刻方块clip的aabb
        示例:
            comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
            blockDict = comp.GetBlockClip((0, 5, 0), dimensionId)
        """
        blockInfoComp = serverApi.GetEngineCompFactory().CreateBlockInfo(self.levelId)
        return blockInfoComp.GetBlockClip(pos, self.dimensionId)

    def getBlockCollision(self, pos):
        # type: (tuple) -> dict
        """
        获取某一位置方块当前collision的aabb
        :param pos: tuple(int,int,int) 方块位置
        :return: dict 方块collision的aabb字典
        备注：
          * 仅能获取已加载区块内方块信息
          * 由于方块的碰撞盒会随周围环境动态改变，此处返回的是当前时刻方块collision的aabb
        示例:
            comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
            blockDict = comp.GetBlockCollision((0, 5, 0), dimensionId)
        """
        blockInfoComp = serverApi.GetEngineCompFactory().CreateBlockInfo(self.levelId)
        return blockInfoComp.GetBlockCollision(pos, self.dimensionId)

    def getBlockNew(self, pos):
        # type: (tuple) -> dict
        """
        获取某一位置的方块信息
        :param pos: tuple(int,int,int) 方块位置
        :return: dict 方块信息字典
        备注：
          * 仅能获取已加载区块内方块信息
          * 若方块具有多种状态, auxValue 的计算较复杂，可结合GetBlockStates使用
        示例:
            comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
            blockDict = comp.GetBlockNew((0, 5, 0), dimensionId)
        """
        blockInfoComp = serverApi.GetEngineCompFactory().CreateBlockInfo(self.levelId)
        return blockInfoComp.GetBlockNew(pos, self.dimensionId)

    def getDestroyTotalTime(self, blockName, itemName=None, miningArgs=None):
        # type: (str, str, dict) -> float
        """
        获取使用物品破坏方块需要的时间
        :param blockName: str 方块标识符, 格式[namespace:name:aux], aux默认为0
        :param itemName: str 物品标识符, 同上, 默认为None表示不使用物品
        :param miningArgs: dict 模拟挖掘状态的参数,如{ 'haste':1, 'mining_fatigue':1, ... }
                           默认为None(所有参数为0)
        :return: float 破坏方块需要消耗的时间
        备注：
          * haste=急迫, conduit_power=潮涌能量, mining_fatigue=挖掘疲劳, mining_efficiency=效率附魔
          * 在服务器逻辑中，不需要传dimensionId
        示例:
            args = {
                "haste": 1,
                "conduit_power": 1,
                "mining_fatigue": 1,
                "mining_efficiency": 1
            }
            comp.GetDestroyTotalTime("minecraft:diamond_block","minecraft:stone_pickaxe", args)
        """
        blockInfoComp = serverApi.GetEngineCompFactory().CreateBlockInfo(self.levelId)
        return blockInfoComp.GetDestroyTotalTime(blockName, itemName, miningArgs)

    def getLiquidBlock(self, pos):
        # type: (tuple) -> dict
        """
        获取某位置的方块所含流体信息(仅服务器)
        :param pos: tuple(int,int,int) 方块位置
        :return: dict or None 流体信息dict, 不含水或非流体时为None
        备注：
          * 仅能获取已加载区块内方块信息
          * 含水方块(如含水栅栏)会在GetLiquidBlock中返回水的信息, 在GetBlockNew中返回栅栏的信息
        示例:
            comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
            liquidBlockDict = comp.GetLiquidBlock((0,5,0), dimensionId)
        """
        blockInfoComp = serverApi.GetEngineCompFactory().CreateBlockInfo(self.levelId)
        return blockInfoComp.GetLiquidBlock(pos, self.dimensionId)

    def getTopBlockHeight(self, xzPos):
        # type: (tuple) -> int
        """
        获取某一(x,z)位置最高的非空气方块的高度
        :param xzPos: tuple(int,int) x,z位置
        :return: int or None, 如果区块未加载则None
        备注：
          * dimension默认为self.dimensionId
        示例:
            comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
            height = comp.GetTopBlockHeight((5,5), dimensionId)
        """
        blockInfoComp = serverApi.GetEngineCompFactory().CreateBlockInfo(self.levelId)
        return blockInfoComp.GetTopBlockHeight(xzPos, self.dimensionId)

    def setBlockNew(self, pos, blockDict, oldBlockHandling=0, isLegacy=False, updateNeighbors=True):
        # type: (tuple, dict, int, bool, bool) -> bool
        """
        设置某一位置的方块
        :param pos: tuple(int,int,int) 方块位置
        :param blockDict: dict 包含 'name' 和 'aux'等字段的方块信息
        :param oldBlockHandling: int 0-替换,1-销毁,2-保留,默认为0
        :param isLegacy: bool 是否为传统aux设置,默认为False(建议True, 避免版本变化)
        :param updateNeighbors: bool 是否更新相邻方块,默认True
        :return: bool 是否成功改变方块(True表示方块确实发生了改变)
        备注：
          * 必须在已加载区块内操作
          * 如果前后方块相同,返回False
          * 若方块实体类型一致(如同为箱子)，则方块实体不被清空。若要清空可先放空气再放目标方块
        示例:
            blockDict = { 'name':'minecraft:wool', 'aux':5 }
            self.setBlockNew((0,5,0), blockDict, 0, True, False)
        """
        blockInfoComp = serverApi.GetEngineCompFactory().CreateBlockInfo(self.levelId)
        # dimensionId是必需参数, oldBlockHandling是命名第3个参数
        return blockInfoComp.SetBlockNew(pos, blockDict, oldBlockHandling, self.dimensionId, isLegacy, updateNeighbors)

    def setJigsawBlock(self, pos, blockDict):
        # type: (tuple, dict) -> bool
        """
        在某位置放置拼图方块
        :param pos: tuple(int,int,int) 方块位置
        :param blockDict: dict 拼图方块信息, 如{
            'name':'minecraft:jigsaw', 'aux':auxValue,
            'jigsaw_name':'minecraft:empty', ...
            'jigsaw_join_type':0/1
        }
        :return: bool 是否设置成功
        备注：
          * 必须在已加载区块内操作
        示例:
            blockDict = { 'name':'minecraft:jigsaw', 'aux':0, 'jigsaw_name':... }
            self.setJigsawBlock((0,100,0), blockDict)
        """
        blockInfoComp = serverApi.GetEngineCompFactory().CreateBlockInfo(self.levelId)
        return blockInfoComp.SetJigsawBlock(pos, blockDict, self.dimensionId)

    def setLiquidBlock(self, pos, blockDict):
        # type: (tuple, dict) -> bool
        """
        设置某一位置的流体方块(例如为方块注水)
        :param pos: tuple(int,int,int) 方块位置
        :param blockDict: dict { 'name':'minecraft:water','aux':5 }等
        :return: bool 设置结果
        备注：
          * 必须在已加载区块内
          * dimensionId需为player所在的维度, 此处将使用self.dimensionId
        示例:
            blockDict = { 'name': 'minecraft:water','aux':5 }
            self.setLiquidBlock((0,5,0), blockDict)
        """
        blockInfoComp = serverApi.GetEngineCompFactory().CreateBlockInfo(self.levelId)
        return blockInfoComp.SetLiquidBlock(pos, blockDict, self.dimensionId)

    def setSnowBlock(self, pos, height=1):
        # type: (tuple, int) -> bool
        """
        设置某一位置方块含雪
        :param pos: tuple(int,int,int) 方块位置
        :param height: int 雪的高度,默认1
        :return: bool 设置结果
        备注：
          * 必须在已加载区块内
        示例:
            self.setSnowBlock((0,5,0),1)
        """
        blockInfoComp = serverApi.GetEngineCompFactory().CreateBlockInfo(self.levelId)
        return blockInfoComp.SetSnowBlock(pos, self.dimensionId, height)

    # 时间相关

    def isUsingLocalTime(self):
        # type: () -> bool
        """
        当前维度是否使用本地时间
        :return: bool 是否使用本地时间
        示例:
            isUsing = self.isUsingLocalTime()
        """
        comp = serverApi.GetEngineCompFactory().CreateDimension(self.levelId)
        return comp.GetUseLocalTime(self.dimensionId)

    def setUseLocalTime(self, isUse):
        # type: (bool) -> bool
        """
        设置是否使用本地时间
        :param isUse: bool 是否使用本地时间
        :return: bool 是否设置成功
        示例:
            self.setUseLocalTime(True)
        """
        comp = serverApi.GetEngineCompFactory().CreateDimension(self.levelId)
        return comp.SetUseLocalTime(self.dimensionId, isUse)

    def getLocalAbsoluteTime(self):
        # type: () -> int
        """
        获取本地绝对时间
        :return: int 本地绝对时间
        示例:
            time = self.getLocalAbsoluteTime()
        """
        comp = serverApi.GetEngineCompFactory().CreateDimension(self.levelId)
        return comp.GetLocalTime(self.dimensionId)

    def getLocalDay(self):
        # type: () -> int
        """
        获取本地白天时间
        :return: int 本地白天时间
        示例:
            time = self.getLocalDayTime()
        """
        comp = serverApi.GetEngineCompFactory().CreateDimension(self.levelId)
        return int(comp.GetLocalTime(self.dimensionId) % 24000)

    def getLocalTimeOfDay(self):
        # type: () -> int
        """
        获取本地时间
        :return: str 本地时间
        示例:
            time = self.getLocalTimeOfDay()
        """
        comp = serverApi.GetEngineCompFactory().CreateDimension(self.levelId)
        return comp.GetLocalTime(self.dimensionId) % 24000

    # 天气相关

    def isUsingLocalWeather(self):
        # type: () -> bool
        """
        当前维度是否使用本地天气
        :return: bool 是否使用本地天气
        示例:
            isUsing = self.isUsingLocalWeather()
        """
        comp = serverApi.GetEngineCompFactory().CreateWeather(self.levelId)
        return comp.GetDimensionUseLocalWeather(self.dimensionId)

    def setUseLocalWeather(self, isUse):
        # type: (bool) -> bool
        """
        设置是否使用本地天气
        :param isUse: bool 是否使用本地天气
        :return: bool 是否设置成功
        示例:
            self.setUseLocalWeather(True)
        """
        comp = serverApi.GetEngineCompFactory().CreateWeather(self.levelId)
        return comp.SetDimensionUseLocalWeather(self.dimensionId, isUse)

    def getLocalWeather(self):
        # type: () -> dict
        """
        获取本地天气信息
        :return: dict 本地天气信息
        """
        comp = serverApi.GetEngineCompFactory().CreateWeather(self.levelId)
        return comp.GetDimensionLocalWeatherInfo(self.dimensionId)

    def setRaining(self, level, ticks):
        # type: (float, int) -> bool
        """
        设置是否下雨
        :param level: float 下雨强度，范围为0-1
        :param ticks: int 天气的持续时间，单位为帧，一秒20帧。持续时间结束后会自动转换为相反的天气。注意，需要在游戏设置中开启天气更替后该参数才会生效。

        """
        comp = serverApi.GetEngineCompFactory().CreateWeather(self.levelId)
        return comp.SetDimensionLocalRain(self.dimensionId, level, ticks)

    def setThundering(self, level, ticks):
        # type: (float, int) -> bool
        """
        设置是否打雷
        :param level: float 打雷强度，范围为0-1
        :param ticks: int 天气的持续时间，单位为帧，一秒20帧。持续时间结束后会自动转换为相反的天气。注意，需要在游戏设置中开启天气更替后该参数才会生效。
        """
        comp = serverApi.GetEngineCompFactory().CreateWeather(self.levelId)
        return comp.SetDimensionLocalThunder(self.dimensionId, level, ticks)