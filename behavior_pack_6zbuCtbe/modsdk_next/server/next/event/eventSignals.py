# -*- coding: utf-8 -*-

if False:
    from typing import Callable

from .events import *
from .BaseEventSignal import BaseEventSignal


class AchievementCompleteEventSignal(BaseEventSignal):
    def __init__(self):
        super(AchievementCompleteEventSignal, self).__init__("AchievementCompleteEvent")

    def subscribe(self, callback):
        # type: (Callable[[AchievementCompleteEvent], None]) -> None
        def cb(args):
            event = AchievementCompleteEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)

class AddEntityServerEventSignal(BaseEventSignal):
    def __init__(self):
        super(AddEntityServerEventSignal, self).__init__("AddEntityServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[AddEntityServerEvent], None]) -> None
        def cb(args):
            event = AddEntityServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)

class AddServerPlayerEventSignal(BaseEventSignal):
    def __init__(self):
        super(AddServerPlayerEventSignal, self).__init__("AddServerPlayerEvent")

    def subscribe(self, callback):
        # type: (Callable[[AddServerPlayerEvent], None]) -> None
        def cb(args):
            event = AddServerPlayerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)

class ChunkAcquireDiscardedServerEventSignal(BaseEventSignal):
    def __init__(self):
        super(ChunkAcquireDiscardedServerEventSignal, self).__init__("ChunkAcquireDiscardedServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[ChunkAcquireDiscardedServerEvent], None]) -> None
        def cb(args):
            event = ChunkAcquireDiscardedServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)

class ChunkGeneratedServerEventSignal(BaseEventSignal):
    def __init__(self):
        super(ChunkGeneratedServerEventSignal, self).__init__("ChunkGeneratedServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[ChunkGeneratedServerEvent], None]) -> None
        def cb(args):
            event = ChunkGeneratedServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)

class ChunkLoadedServerEventSignal(BaseEventSignal):
    def __init__(self):
        super(ChunkLoadedServerEventSignal, self).__init__("ChunkLoadedServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[ChunkLoadedServerEvent], None]) -> None
        def cb(args):
            event = ChunkLoadedServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)

class ClientLoadAddonsFinishServerEventSignal(BaseEventSignal):
    def __init__(self):
        super(ClientLoadAddonsFinishServerEventSignal, self).__init__("ClientLoadAddonsFinishServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[ClientLoadAddonsFinishServerEvent], None]) -> None
        def cb(args):
            event = ClientLoadAddonsFinishServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)

class CommandEventSignal(BaseEventSignal):
    def __init__(self):
        super(CommandEventSignal, self).__init__("CommandEvent")

    def subscribe(self, callback):
        # type: (Callable[[CommandEvent], None]) -> None
        def cb(args):
            event = CommandEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)

class CustomCommandTriggerServerEventSignal(BaseEventSignal):
    def __init__(self):
        super(CustomCommandTriggerServerEventSignal, self).__init__("CustomCommandTriggerServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[CustomCommandTriggerServerEvent], None]) -> None
        def cb(args):
            event = CustomCommandTriggerServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)

class DelServerPlayerEventSignal(BaseEventSignal):
    def __init__(self):
        super(DelServerPlayerEventSignal, self).__init__("DelServerPlayerEvent")

    def subscribe(self, callback):
        # type: (Callable[[DelServerPlayerEvent], None]) -> None
        def cb(args):
            event = DelServerPlayerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)

class EntityRemoveEventSignal(BaseEventSignal):
    def __init__(self):
        super(EntityRemoveEventSignal, self).__init__("EntityRemoveEvent")

    def subscribe(self, callback):
        # type: (Callable[[EntityRemoveEvent], None]) -> None
        def cb(args):
            event = EntityRemoveEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)

class ExplosionServerEventSignal(BaseEventSignal):
    def __init__(self):
        super(ExplosionServerEventSignal, self).__init__("ExplosionServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[ExplosionServerEvent], None]) -> None
        def cb(args):
            event = ExplosionServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)

class GlobalCommandServerEventSignal(BaseEventSignal):
    def __init__(self):
        super(GlobalCommandServerEventSignal, self).__init__("GlobalCommandServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[GlobalCommandServerEvent], None]) -> None
        def cb(args):
            event = GlobalCommandServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)

class NewOnEntityAreaEventSignal(BaseEventSignal):
    def __init__(self):
        super(NewOnEntityAreaEventSignal, self).__init__("NewOnEntityAreaEvent")

    def subscribe(self, callback):
        # type: (Callable[[NewOnEntityAreaEvent], None]) -> None
        def cb(args):
            event = NewOnEntityAreaEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)

class OnCommandOutputServerEventSignal(BaseEventSignal):
    def __init__(self):
        super(OnCommandOutputServerEventSignal, self).__init__("OnCommandOutputServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[OnCommandOutputServerEvent], None]) -> None
        def cb(args):
            event = OnCommandOutputServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)

class OnContainerFillLoottableServerEventSignal(BaseEventSignal):
    def __init__(self):
        super(OnContainerFillLoottableServerEventSignal, self).__init__("OnContainerFillLoottableServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[OnContainerFillLoottableServerEvent], None]) -> None
        def cb(args):
            event = OnContainerFillLoottableServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)

class OnLightningLevelChangeServerEventSignal(BaseEventSignal):
    def __init__(self):
        super(OnLightningLevelChangeServerEventSignal, self).__init__("OnLightningLevelChangeServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[OnLightningLevelChangeServerEvent], None]) -> None
        def cb(args):
            event = OnLightningLevelChangeServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)

class OnLocalLightningLevelChangeServerEventSignal(BaseEventSignal):
    def __init__(self):
        super(OnLocalLightningLevelChangeServerEventSignal, self).__init__("OnLocalLightningLevelChangeServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[OnLocalLightningLevelChangeServerEvent], None]) -> None
        def cb(args):
            event = OnLocalLightningLevelChangeServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)

class OnLocalRainLevelChangeServerEventSignal(BaseEventSignal):
    def __init__(self):
        super(OnLocalRainLevelChangeServerEventSignal, self).__init__("OnLocalRainLevelChangeServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[OnLocalRainLevelChangeServerEvent], None]) -> None
        def cb(args):
            event = OnLocalRainLevelChangeServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)

class OnRainLevelChangeServerEventSignal(BaseEventSignal):
    def __init__(self):
        super(OnRainLevelChangeServerEventSignal, self).__init__("OnRainLevelChangeServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[OnRainLevelChangeServerEvent], None]) -> None
        def cb(args):
            event = OnRainLevelChangeServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)

class OnScriptTickServerEventSignal(BaseEventSignal):
    def __init__(self):
        super(OnScriptTickServerEventSignal, self).__init__("OnScriptTickServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[OnScriptTickServer], None]) -> None
        def cb(args):
            event = OnScriptTickServer()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)

class PlaceNeteaseLargeFeatureServerEventSignal(BaseEventSignal):
    def __init__(self):
        super(PlaceNeteaseLargeFeatureServerEventSignal, self).__init__("PlaceNeteaseLargeFeatureServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[PlaceNeteaseLargeFeatureServerEvent], None]) -> None
        def cb(args):
            event = PlaceNeteaseLargeFeatureServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)

class PlaceNeteaseStructureFeatureEventSignal(BaseEventSignal):
    def __init__(self):
        super(PlaceNeteaseStructureFeatureEventSignal, self).__init__("PlaceNeteaseStructureFeatureEvent")

    def subscribe(self, callback):
        # type: (Callable[[PlaceNeteaseStructureFeatureEvent], None]) -> None
        def cb(args):
            event = PlaceNeteaseStructureFeatureEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)

class PlayerIntendLeaveServerEventSignal(BaseEventSignal):
    def __init__(self):
        super(PlayerIntendLeaveServerEventSignal, self).__init__("PlayerIntendLeaveServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[PlayerIntendLeaveServerEvent], None]) -> None
        def cb(args):
            event = PlayerIntendLeaveServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)

class PlayerJoinMessageEventSignal(BaseEventSignal):
    def __init__(self):
        super(PlayerJoinMessageEventSignal, self).__init__("PlayerJoinMessageEvent")

    def subscribe(self, callback):
        # type: (Callable[[PlayerJoinMessageEvent], None]) -> None
        def cb(args):
            event = PlayerJoinMessageEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)

class PlayerLeftMessageServerEventSignal(BaseEventSignal):
    def __init__(self):
        super(PlayerLeftMessageServerEventSignal, self).__init__("PlayerLeftMessageServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[PlayerLeftMessageServerEvent], None]) -> None
        def cb(args):
            event = PlayerLeftMessageServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)

class ServerChatEventSignal(BaseEventSignal):
    def __init__(self):
        super(ServerChatEventSignal, self).__init__("ServerChatEvent")

    def subscribe(self, callback):
        # type: (Callable[[ServerChatEvent], None]) -> None
        def cb(args):
            event = ServerChatEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)

class ServerPostBlockPatternEventSignal(BaseEventSignal):
    def __init__(self):
        super(ServerPostBlockPatternEventSignal, self).__init__("ServerPostBlockPatternEvent")

    def subscribe(self, callback):
        # type: (Callable[[ServerPostBlockPatternEvent], None]) -> None
        def cb(args):
            event = ServerPostBlockPatternEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)

class ServerPreBlockPatternEventSignal(BaseEventSignal):
    def __init__(self):
        super(ServerPreBlockPatternEventSignal, self).__init__("ServerPreBlockPatternEvent")

    def subscribe(self, callback):
        # type: (Callable[[ServerPreBlockPatternEvent], None]) -> None
        def cb(args):
            event = ServerPreBlockPatternEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)

class ActorHurtEventSignal(BaseEventSignal):
    """触发时机：生物（包括玩家）受伤时触发"""
    def __init__(self):
        super(ActorHurtEventSignal, self).__init__("ActorHurtServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[ActorHurtEvent], None]) -> None
        """订阅生物受伤事件
        :param callback: 回调函数，参数为ActorHurtEvent
        """
        def cb(args):
            event = ActorHurtEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class ActuallyHurtEventSignal(BaseEventSignal):
    """触发时机：实体实际受到伤害时触发"""
    def __init__(self):
        super(ActuallyHurtEventSignal, self).__init__("ActuallyHurtServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[ActuallyHurtEvent], None]) -> None
        """订阅实体实际受到伤害事件
        :param callback: 回调函数，参数为ActuallyHurtEvent
        """
        def cb(args):
            event = ActuallyHurtEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class AddEffectEventSignal(BaseEventSignal):
    """触发时机：实体获得状态效果时"""
    def __init__(self):
        super(AddEffectEventSignal, self).__init__("AddEffectServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[AddEffectEvent], None]) -> None
        """订阅实体获得状态效果事件
        :param callback: 回调函数，参数为AddEffectEvent
        """
        def cb(args):
            event = AddEffectEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class ChangeSwimStateEventSignal(BaseEventSignal):
    """触发时机：实体开始或者结束游泳时"""
    def __init__(self):
        super(ChangeSwimStateEventSignal, self).__init__("ChangeSwimStateServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[ChangeSwimStateEvent], None]) -> None
        """订阅实体游泳状态变化事件
        :param callback: 回调函数，参数为ChangeSwimStateEvent
        """
        def cb(args):
            event = ChangeSwimStateEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class DamageEventSignal(BaseEventSignal):
    """触发时机：实体受到伤害时触发"""
    def __init__(self):
        super(DamageEventSignal, self).__init__("DamageEvent")

    def subscribe(self, callback):
        # type: (Callable[[DamageEvent], None]) -> None
        """订阅实体受到伤害事件
        :param callback: 回调函数，参数为DamageEvent
        """
        def cb(args):
            event = DamageEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class EntityChangeDimensionEventSignal(BaseEventSignal):
    """触发时机：实体维度改变时服务端抛出"""
    def __init__(self):
        super(EntityChangeDimensionEventSignal, self).__init__("EntityChangeDimensionServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[EntityChangeDimensionEvent], None]) -> None
        """订阅实体维度改变事件
        :param callback: 回调函数，参数为EntityChangeDimensionEvent
        """
        def cb(args):
            event = EntityChangeDimensionEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class EntityDefinitionsEventSignal(BaseEventSignal):
    """触发时机：生物定义json文件中设置的event触发时同时触发。生物行为变更事件"""
    def __init__(self):
        super(EntityDefinitionsEventSignal, self).__init__("EntityDefinitionsEventServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[EntityDefinitionsEvent], None]) -> None
        """订阅生物行为变更事件
        :param callback: 回调函数，参数为EntityDefinitionsEvent
        """
        def cb(args):
            event = EntityDefinitionsEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class EntityDieLoottableAfterEventSignal(BaseEventSignal):
    """触发时机：生物死亡掉落物品之后"""
    def __init__(self):
        super(EntityDieLoottableAfterEventSignal, self).__init__("EntityDieLoottableAfterServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[EntityDieLoottableAfterEvent], None]) -> None
        """订阅生物死亡掉落物品之后事件
        :param callback: 回调函数，参数为EntityDieLoottableAfterEvent
        """
        def cb(args):
            event = EntityDieLoottableAfterEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class EntityDieLoottableEventSignal(BaseEventSignal):
    """触发时机：生物死亡掉落物品时"""
    def __init__(self):
        super(EntityDieLoottableEventSignal, self).__init__("EntityDieLoottableServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[EntityDieLoottableEvent], None]) -> None
        """订阅生物死亡掉落物品事件
        :param callback: 回调函数，参数为EntityDieLoottableEvent
        """
        def cb(args):
            event = EntityDieLoottableEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class EntityDroppedItemEventSignal(BaseEventSignal):
    """触发时机：生物扔出物品时触发"""
    def __init__(self):
        super(EntityDroppedItemEventSignal, self).__init__("EntityDroppedItemServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[EntityDroppedItemEvent], None]) -> None
        """订阅生物扔出物品事件
        :param callback: 回调函数，参数为EntityDroppedItemEvent
        """
        def cb(args):
            event = EntityDroppedItemEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class EntityEffectDamageEventSignal(BaseEventSignal):
    """触发时机：生物受到状态伤害/回复事件"""
    def __init__(self):
        super(EntityEffectDamageEventSignal, self).__init__("EntityEffectDamageServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[EntityEffectDamageEvent], None]) -> None
        """订阅生物受到状态伤害/回复事件
        :param callback: 回调函数，参数为EntityEffectDamageEvent
        """
        def cb(args):
            event = EntityEffectDamageEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class EntityLoadScriptEventSignal(BaseEventSignal):
    """触发时机：数据库加载实体自定义数据时触发"""
    def __init__(self):
        super(EntityLoadScriptEventSignal, self).__init__("EntityLoadScriptEvent")

    def subscribe(self, callback):
        # type: (Callable[[EntityLoadScriptEvent], None]) -> None
        """订阅数据库加载实体自定义数据事件
        :param callback: 回调函数，参数为EntityLoadScriptEvent
        """
        def cb(args):
            event = EntityLoadScriptEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class EntityMotionStartEventSignal(BaseEventSignal):
    """触发时机：实体运动器开始事件"""
    def __init__(self):
        super(EntityMotionStartEventSignal, self).__init__("EntityMotionStartServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[EntityMotionStartEvent], None]) -> None
        """订阅实体运动器开始事件
        :param callback: 回调函数，参数为EntityMotionStartEvent
        """
        def cb(args):
            event = EntityMotionStartEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class EntityMotionStopEventSignal(BaseEventSignal):
    """触发时机：实体运动器停止事件"""
    def __init__(self):
        super(EntityMotionStopEventSignal, self).__init__("EntityMotionStopServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[EntityMotionStopEvent], None]) -> None
        """订阅实体运动器停止事件
        :param callback: 回调函数，参数为EntityMotionStopEvent
        """
        def cb(args):
            event = EntityMotionStopEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class EntityPickupItemEventSignal(BaseEventSignal):
    """触发时机：有minecraft:behavior.pickup_items行为的生物拾取物品时触发该事件"""
    def __init__(self):
        super(EntityPickupItemEventSignal, self).__init__("EntityPickupItemServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[EntityPickupItemEvent], None]) -> None
        """订阅生物拾取物品事件
        :param callback: 回调函数，参数为EntityPickupItemEvent
        """
        def cb(args):
            event = EntityPickupItemEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class EntityStartRidingEventSignal(BaseEventSignal):
    """触发时机：当实体骑乘上另一个实体时触发"""
    def __init__(self):
        super(EntityStartRidingEventSignal, self).__init__("StartRidingServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[EntityStartRidingEvent], None]) -> None
        """订阅实体骑乘事件
        :param callback: 回调函数，参数为EntityStartRidingEvent
        """
        def cb(args):
            event = EntityStartRidingEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class EntityStopRidingEventSignal(BaseEventSignal):
    """触发时机：当实体停止骑乘时"""
    def __init__(self):
        super(EntityStopRidingEventSignal, self).__init__("EntityStopRidingEvent")

    def subscribe(self, callback):
        # type: (Callable[[EntityStopRidingEvent], None]) -> None
        """订阅实体停止骑乘事件
        :param callback: 回调函数，参数为EntityStopRidingEvent
        """
        def cb(args):
            event = EntityStopRidingEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class EntityTickEventSignal(BaseEventSignal):
    """触发时机：实体tick时触发。该事件为20帧每秒"""
    def __init__(self):
        super(EntityTickEventSignal, self).__init__("EntityTickServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[EntityTickEvent], None]) -> None
        """订阅实体tick事件
        :param callback: 回调函数，参数为EntityTickEvent
        """
        def cb(args):
            event = EntityTickEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class HealthChangeBeforeEventSignal(BaseEventSignal):
    """触发时机：生物生命值发生变化之前触发"""
    def __init__(self):
        super(HealthChangeBeforeEventSignal, self).__init__("HealthChangeBeforeServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[HealthChangeBeforeEvent], None]) -> None
        """订阅生物生命值变化之前事件
        :param callback: 回调函数，参数为HealthChangeBeforeEvent
        """
        def cb(args):
            event = HealthChangeBeforeEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class HealthChangeEventSignal(BaseEventSignal):
    """触发时机：生物生命值发生变化时触发"""
    def __init__(self):
        super(HealthChangeEventSignal, self).__init__("HealthChangeServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[HealthChangeEvent], None]) -> None
        """订阅生物生命值变化事件
        :param callback: 回调函数，参数为HealthChangeEvent
        """
        def cb(args):
            event = HealthChangeEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class MobDieEventSignal(BaseEventSignal):
    """触发时机：实体死亡时触发"""
    def __init__(self):
        super(MobDieEventSignal, self).__init__("MobDieEvent")

    def subscribe(self, callback):
        # type: (Callable[[MobDieEvent], None]) -> None
        """订阅实体死亡事件
        :param callback: 回调函数，参数为MobDieEvent
        """
        def cb(args):
            event = MobDieEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class MobGriefingBlockEventSignal(BaseEventSignal):
    """触发时机：环境生物改变方块时触发"""
    def __init__(self):
        super(MobGriefingBlockEventSignal, self).__init__("MobGriefingBlockServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[MobGriefingBlockEvent], None]) -> None
        """订阅环境生物改变方块事件
        :param callback: 回调函数，参数为MobGriefingBlockEvent
        """
        def cb(args):
            event = MobGriefingBlockEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class OnFireHurtEventSignal(BaseEventSignal):
    """触发时机：生物受到火焰伤害时触发"""
    def __init__(self):
        super(OnFireHurtEventSignal, self).__init__("OnFireHurtEvent")

    def subscribe(self, callback):
        # type: (Callable[[OnFireHurtEvent], None]) -> None
        """订阅生物受到火焰伤害事件
        :param callback: 回调函数，参数为OnFireHurtEvent
        """
        def cb(args):
            event = OnFireHurtEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class OnGroundEventSignal(BaseEventSignal):
    """触发时机：实体着地事件"""
    def __init__(self):
        super(OnGroundEventSignal, self).__init__("OnGroundServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[OnGroundEvent], None]) -> None
        """订阅实体着地事件
        :param callback: 回调函数，参数为OnGroundEvent
        """
        def cb(args):
            event = OnGroundEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class OnKnockBackEventSignal(BaseEventSignal):
    """触发时机：实体被击退时触发"""
    def __init__(self):
        super(OnKnockBackEventSignal, self).__init__("OnKnockBackServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[OnKnockBackEvent], None]) -> None
        """订阅实体被击退事件
        :param callback: 回调函数，参数为OnKnockBackEvent
        """
        def cb(args):
            event = OnKnockBackEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class OnMobHitBlockEventSignal(BaseEventSignal):
    """触发时机：生物（不包括玩家）碰撞到方块时触发该事件"""
    def __init__(self):
        super(OnMobHitBlockEventSignal, self).__init__("OnMobHitBlockServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[OnMobHitBlockEvent], None]) -> None
        """订阅生物碰撞到方块事件
        :param callback: 回调函数，参数为OnMobHitBlockEvent
        """
        def cb(args):
            event = OnMobHitBlockEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class OnMobHitMobEventSignal(BaseEventSignal):
    """触发时机：生物间（包含玩家）碰撞时触发该事件"""
    def __init__(self):
        super(OnMobHitMobEventSignal, self).__init__("OnMobHitMobServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[OnMobHitMobEvent], None]) -> None
        """订阅生物碰撞事件
        :param callback: 回调函数，参数为OnMobHitMobEvent
        """
        def cb(args):
            event = OnMobHitMobEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class ProjectileCritHitEventSignal(BaseEventSignal):
    """触发时机：当抛射物与头部碰撞时触发该事件"""
    def __init__(self):
        super(ProjectileCritHitEventSignal, self).__init__("ProjectileCritHitEvent")

    def subscribe(self, callback):
        # type: (Callable[[ProjectileCritHitEvent], None]) -> None
        """订阅抛射物与头部碰撞事件
        :param callback: 回调函数，参数为ProjectileCritHitEvent
        """
        def cb(args):
            event = ProjectileCritHitEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class ProjectileDoHitEffectEventSignal(BaseEventSignal):
    """触发时机：当抛射物碰撞时触发该事件"""
    def __init__(self):
        super(ProjectileDoHitEffectEventSignal, self).__init__("ProjectileDoHitEffectEvent")

    def subscribe(self, callback):
        # type: (Callable[[ProjectileDoHitEffectEvent], None]) -> None
        """订阅抛射物碰撞事件
        :param callback: 回调函数，参数为ProjectileDoHitEffectEvent
        """
        def cb(args):
            event = ProjectileDoHitEffectEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class RefreshEffectEventSignal(BaseEventSignal):
    """触发时机：实体身上状态效果更新时触发"""
    def __init__(self):
        super(RefreshEffectEventSignal, self).__init__("RefreshEffectServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[RefreshEffectEvent], None]) -> None
        """订阅实体状态效果更新事件
        :param callback: 回调函数，参数为RefreshEffectEvent
        """
        def cb(args):
            event = RefreshEffectEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class RemoveEffectEventSignal(BaseEventSignal):
    """触发时机：实体身上状态效果被移除时"""
    def __init__(self):
        super(RemoveEffectEventSignal, self).__init__("RemoveEffectServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[RemoveEffectEvent], None]) -> None
        """订阅实体状态效果移除事件
        :param callback: 回调函数，参数为RemoveEffectEvent
        """
        def cb(args):
            event = RemoveEffectEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class SpawnProjectileEventSignal(BaseEventSignal):
    """触发时机：抛射物生成时触发"""
    def __init__(self):
        super(SpawnProjectileEventSignal, self).__init__("SpawnProjectileServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[SpawnProjectileEvent], None]) -> None
        """订阅抛射物生成事件
        :param callback: 回调函数，参数为SpawnProjectileEvent
        """
        def cb(args):
            event = SpawnProjectileEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class WillAddEffectEventSignal(BaseEventSignal):
    """触发时机：实体即将获得状态效果前"""
    def __init__(self):
        super(WillAddEffectEventSignal, self).__init__("WillAddEffectServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[WillAddEffectEvent], None]) -> None
        """订阅实体即将获得状态效果事件
        :param callback: 回调函数，参数为WillAddEffectEvent
        """
        def cb(args):
            event = WillAddEffectEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class WillTeleportToEventSignal(BaseEventSignal):
    """触发时机：实体即将传送或切换维度"""
    def __init__(self):
        super(WillTeleportToEventSignal, self).__init__("WillTeleportToServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[WillTeleportToEvent], None]) -> None
        """订阅实体即将传送或切换维度事件
        :param callback: 回调函数，参数为WillTeleportToEvent
        """
        def cb(args):
            event = WillTeleportToEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)

class BaseEventSignal(object):
    def __init__(self, eventName):
        self.eventName = eventName

    def _subscribe(self, callback, cb):
        # 这里假设有一个内部机制来订阅事件
        pass

    def subscribe(self, callback):
        raise NotImplementedError("This method should be overridden by subclasses")


class AddExpEventSignal(BaseEventSignal):
    """触发时机：当玩家增加经验时触发该事件。"""
    def __init__(self):
        super(AddExpEventSignal, self).__init__("AddExpEvent")

    def subscribe(self, callback):
        # type: (Callable[[AddExpEvent], None]) -> None
        """订阅玩家增加经验事件
        :param callback: 回调函数，参数为AddExpEvent
        """
        def cb(args):
            event = AddExpEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class AddLevelEventSignal(BaseEventSignal):
    """触发时机：当玩家升级时触发该事件。"""
    def __init__(self):
        super(AddLevelEventSignal, self).__init__("AddLevelEvent")

    def subscribe(self, callback):
        # type: (Callable[[AddLevelEvent], None]) -> None
        """订阅玩家升级事件
        :param callback: 回调函数，参数为AddLevelEvent
        """
        def cb(args):
            event = AddLevelEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class ChangeLevelUpCostEventSignal(BaseEventSignal):
    """触发时机：获取玩家下一个等级升级经验时，用于重载玩家的升级经验，每个等级在重置之前都只会触发一次"""
    def __init__(self):
        super(ChangeLevelUpCostEventSignal, self).__init__("ChangeLevelUpCostServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[ChangeLevelUpCostServerEvent], None]) -> None
        """订阅获取玩家下一个等级升级经验事件
        :param callback: 回调函数，参数为ChangeLevelUpCostServerEvent
        """
        def cb(args):
            event = ChangeLevelUpCostServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class DimensionChangeEventSignal(BaseEventSignal):
    """触发时机：玩家维度改变时服务端抛出"""
    def __init__(self):
        super(DimensionChangeEventSignal, self).__init__("DimensionChangeServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[DimensionChangeServerEvent], None]) -> None
        """订阅玩家维度改变事件
        :param callback: 回调函数，参数为DimensionChangeServerEvent
        """
        def cb(args):
            event = DimensionChangeServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class DimensionChangeFinishEventSignal(BaseEventSignal):
    """触发时机：玩家维度改变完成后服务端抛出"""
    def __init__(self):
        super(DimensionChangeFinishEventSignal, self).__init__("DimensionChangeFinishServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[DimensionChangeFinishServerEvent], None]) -> None
        """订阅玩家维度改变完成事件
        :param callback: 回调函数，参数为DimensionChangeFinishServerEvent
        """
        def cb(args):
            event = DimensionChangeFinishServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class ExtinguishFireEventSignal(BaseEventSignal):
    """触发时机：玩家扑灭火焰时触发。下雨，倒水等方式熄灭火焰不会触发。"""
    def __init__(self):
        super(ExtinguishFireEventSignal, self).__init__("ExtinguishFireServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[ExtinguishFireServerEvent], None]) -> None
        """订阅玩家扑灭火焰事件
        :param callback: 回调函数，参数为ExtinguishFireServerEvent
        """
        def cb(args):
            event = ExtinguishFireServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class GameTypeChangedEventSignal(BaseEventSignal):
    """触发时机：当默认游戏模式或个人游戏模式发生变化时服务端触发，如果个人游戏模式不为默认时，修改默认游戏模式也会同时修改个人游戏模式，此时会触发两次该事件"""
    def __init__(self):
        super(GameTypeChangedEventSignal, self).__init__("GameTypeChangedServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[GameTypeChangedServerEvent], None]) -> None
        """订阅游戏模式变化事件
        :param callback: 回调函数，参数为GameTypeChangedServerEvent
        """
        def cb(args):
            event = GameTypeChangedServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class OnPlayerActionEventSignal(BaseEventSignal):
    """触发时机：玩家动作事件，当玩家开始/停止某些动作时触发该事件"""
    def __init__(self):
        super(OnPlayerActionEventSignal, self).__init__("OnPlayerActionServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[OnPlayerActionServerEvent], None]) -> None
        """订阅玩家动作事件
        :param callback: 回调函数，参数为OnPlayerActionServerEvent
        """
        def cb(args):
            event = OnPlayerActionServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class OnPlayerHitBlockEventSignal(BaseEventSignal):
    """触发时机：通过OpenPlayerHitBlockDetection打开方块碰撞检测后，当玩家碰撞到方块时触发该事件。监听玩家着地请使用客户端的OnGroundClientEvent。客户端和服务端分别作碰撞检测，可能两个事件返回的略有差异。"""
    def __init__(self):
        super(OnPlayerHitBlockEventSignal, self).__init__("OnPlayerHitBlockServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[OnPlayerHitBlockServerEvent], None]) -> None
        """订阅玩家碰撞方块事件
        :param callback: 回调函数，参数为OnPlayerHitBlockServerEvent
        """
        def cb(args):
            event = OnPlayerHitBlockServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class PlayerAttackEntityEventSignal(BaseEventSignal):
    """触发时机：当玩家攻击时触发该事件。"""
    def __init__(self):
        super(PlayerAttackEntityEventSignal, self).__init__("PlayerAttackEntityEvent")

    def subscribe(self, callback):
        # type: (Callable[[PlayerAttackEntityEvent], None]) -> None
        """订阅玩家攻击事件
        :param callback: 回调函数，参数为PlayerAttackEntityEvent
        """
        def cb(args):
            event = PlayerAttackEntityEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class PlayerCheatSpinAttackEventSignal(BaseEventSignal):
    """触发时机：玩家开始/结束快速旋转攻击并且不符合发送快速旋转攻击条件时触发（装备激流附魔的三叉戟、在水中或雨中，且未骑乘）"""
    def __init__(self):
        super(PlayerCheatSpinAttackEventSignal, self).__init__("PlayerCheatSpinAttackServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[PlayerCheatSpinAttackServerEvent], None]) -> None
        """订阅玩家快速旋转攻击事件
        :param callback: 回调函数，参数为PlayerCheatSpinAttackServerEvent
        """
        def cb(args):
            event = PlayerCheatSpinAttackServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class PlayerDieEventSignal(BaseEventSignal):
    """触发时机：当玩家死亡时触发该事件。"""
    def __init__(self):
        super(PlayerDieEventSignal, self).__init__("PlayerDieEvent")

    def subscribe(self, callback):
        # type: (Callable[[PlayerDieEvent], None]) -> None
        """订阅玩家死亡事件
        :param callback: 回调函数，参数为PlayerDieEvent
        """
        def cb(args):
            event = PlayerDieEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class PlayerDoInteractEventSignal(BaseEventSignal):
    """触发时机：玩家与有minecraft:interact组件的生物交互时触发该事件，例如玩家手持空桶对牛挤奶、玩家手持打火石点燃苦力怕"""
    def __init__(self):
        super(PlayerDoInteractEventSignal, self).__init__("PlayerDoInteractServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[PlayerDoInteractServerEvent], None]) -> None
        """订阅玩家交互事件
        :param callback: 回调函数，参数为PlayerDoInteractServerEvent
        """
        def cb(args):
            event = PlayerDoInteractServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class PlayerEatFoodEventSignal(BaseEventSignal):
    """触发时机：玩家吃下食物时触发"""
    def __init__(self):
        super(PlayerEatFoodEventSignal, self).__init__("PlayerEatFoodServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[PlayerEatFoodServerEvent], None]) -> None
        """订阅玩家吃食物事件
        :param callback: 回调函数，参数为PlayerEatFoodServerEvent
        """
        def cb(args):
            event = PlayerEatFoodServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class PlayerFeedEntityEventSignal(BaseEventSignal):
    """触发时机：玩家喂养生物时触发，例如玩家手持小麦喂养牛、玩家手持胡萝卜喂养幼年猪。"""
    def __init__(self):
        super(PlayerFeedEntityEventSignal, self).__init__("PlayerFeedEntityServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[PlayerFeedEntityServerEvent], None]) -> None
        """订阅玩家喂养生物事件
        :param callback: 回调函数，参数为PlayerFeedEntityServerEvent
        """
        def cb(args):
            event = PlayerFeedEntityServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class PlayerHungerChangeEventSignal(BaseEventSignal):
    """触发时机：玩家饥饿度变化时触发该事件"""
    def __init__(self):
        super(PlayerHungerChangeEventSignal, self).__init__("PlayerHungerChangeServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[PlayerHungerChangeServerEvent], None]) -> None
        """订阅玩家饥饿度变化事件
        :param callback: 回调函数，参数为PlayerHungerChangeServerEvent
        """
        def cb(args):
            event = PlayerHungerChangeServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class PlayerHurtEventSignal(BaseEventSignal):
    """触发时机：当玩家受伤害前触发该事件。"""
    def __init__(self):
        super(PlayerHurtEventSignal, self).__init__("PlayerHurtEvent")

    def subscribe(self, callback):
        # type: (Callable[[PlayerHurtEvent], None]) -> None
        """订阅玩家受伤害事件
        :param callback: 回调函数，参数为PlayerHurtEvent
        """
        def cb(args):
            event = PlayerHurtEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class PlayerInteractEventSignal(BaseEventSignal):
    """触发时机：玩家可以与实体交互时。如果是鼠标控制模式，则当准心对着实体时触发。如果是触屏模式，则触发时机与屏幕下方的交互按钮显示的时机相同。玩家真正与实体发生交互的事件见PlayerDoInteractServerEvent"""
    def __init__(self):
        super(PlayerInteractEventSignal, self).__init__("PlayerInteractServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[PlayerInteractServerEvent], None]) -> None
        """订阅玩家交互事件
        :param callback: 回调函数，参数为PlayerInteractServerEvent
        """
        def cb(args):
            event = PlayerInteractServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class PlayerNamedEntityEventSignal(BaseEventSignal):
    """触发时机：玩家用命名牌重命名实体时触发，例如玩家手持命名牌对羊修改名字、玩家手持命名牌对盔甲架修改名字。"""
    def __init__(self):
        super(PlayerNamedEntityEventSignal, self).__init__("PlayerNamedEntityServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[PlayerNamedEntityServerEvent], None]) -> None
        """订阅玩家命名实体事件
        :param callback: 回调函数，参数为PlayerNamedEntityServerEvent
        """
        def cb(args):
            event = PlayerNamedEntityServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class PlayerRespawnEventSignal(BaseEventSignal):
    """触发时机：玩家复活时触发该事件。"""
    def __init__(self):
        super(PlayerRespawnEventSignal, self).__init__("PlayerRespawnEvent")

    def subscribe(self, callback):
        # type: (Callable[[PlayerRespawnEvent], None]) -> None
        """订阅玩家复活事件
        :param callback: 回调函数，参数为PlayerRespawnEvent
        """
        def cb(args):
            event = PlayerRespawnEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class PlayerRespawnFinishEventSignal(BaseEventSignal):
    """触发时机：玩家复活完毕时触发"""
    def __init__(self):
        super(PlayerRespawnFinishEventSignal, self).__init__("PlayerRespawnFinishServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[PlayerRespawnFinishServerEvent], None]) -> None
        """订阅玩家复活完毕事件
        :param callback: 回调函数，参数为PlayerRespawnFinishServerEvent
        """
        def cb(args):
            event = PlayerRespawnFinishServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class PlayerSleepEventSignal(BaseEventSignal):
    """触发时机：玩家使用床睡觉成功"""
    def __init__(self):
        super(PlayerSleepEventSignal, self).__init__("PlayerSleepServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[PlayerSleepServerEvent], None]) -> None
        """订阅玩家睡觉事件
        :param callback: 回调函数，参数为PlayerSleepServerEvent
        """
        def cb(args):
            event = PlayerSleepServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class PlayerSpinAttackEventSignal(BaseEventSignal):
    """触发时机：玩家开始/结束快速旋转攻击时触发"""
    def __init__(self):
        super(PlayerSpinAttackEventSignal, self).__init__("PlayerSpinAttackServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[PlayerSpinAttackServerEvent], None]) -> None
        """订阅玩家快速旋转攻击事件
        :param callback: 回调函数，参数为PlayerSpinAttackServerEvent
        """
        def cb(args):
            event = PlayerSpinAttackServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class PlayerStopSleepEventSignal(BaseEventSignal):
    """触发时机：玩家停止睡觉"""
    def __init__(self):
        super(PlayerStopSleepEventSignal, self).__init__("PlayerStopSleepServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[PlayerStopSleepServerEvent], None]) -> None
        """订阅玩家停止睡觉事件
        :param callback: 回调函数，参数为PlayerStopSleepServerEvent
        """
        def cb(args):
            event = PlayerStopSleepServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class PlayerTeleportEventSignal(BaseEventSignal):
    """触发时机：当玩家传送时触发该事件，如：玩家使用末影珍珠或tp指令时。"""
    def __init__(self):
        super(PlayerTeleportEventSignal, self).__init__("PlayerTeleportEvent")

    def subscribe(self, callback):
        # type: (Callable[[PlayerTeleportEvent], None]) -> None
        """订阅玩家传送事件
        :param callback: 回调函数，参数为PlayerTeleportEvent
        """
        def cb(args):
            event = PlayerTeleportEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class PlayerTrySleepEventSignal(BaseEventSignal):
    """触发时机：玩家尝试使用床睡觉"""
    def __init__(self):
        super(PlayerTrySleepEventSignal, self).__init__("PlayerTrySleepServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[PlayerTrySleepServerEvent], None]) -> None
        """订阅玩家尝试睡觉事件
        :param callback: 回调函数，参数为PlayerTrySleepServerEvent
        """
        def cb(args):
            event = PlayerTrySleepServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class ServerPlayerGetExperienceOrbEventSignal(BaseEventSignal):
    """触发时机：玩家获取经验球时触发的事件"""
    def __init__(self):
        super(ServerPlayerGetExperienceOrbEventSignal, self).__init__("ServerPlayerGetExperienceOrbEvent")

    def subscribe(self, callback):
        # type: (Callable[[ServerPlayerGetExperienceOrbEvent], None]) -> None
        """订阅玩家获取经验球事件
        :param callback: 回调函数，参数为ServerPlayerGetExperienceOrbEvent
        """
        def cb(args):
            event = ServerPlayerGetExperienceOrbEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)


class StoreBuySuccEventSignal(BaseEventSignal):
    """触发时机:玩家游戏内购买商品时服务端抛出的事件"""
    def __init__(self):
        super(StoreBuySuccEventSignal, self).__init__("StoreBuySuccServerEvent")

    def subscribe(self, callback):
        # type: (Callable[[StoreBuySuccServerEvent], None]) -> None
        """订阅玩家购买商品事件
        :param callback: 回调函数，参数为StoreBuySuccServerEvent
        """
        def cb(args):
            event = StoreBuySuccServerEvent()
            event.__dict__ = args
            callback(event)
        self._subscribe(callback, cb)