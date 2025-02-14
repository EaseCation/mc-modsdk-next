# -*- coding: utf-8 -*-
import mod.server.extraServerApi as serverApi
from modsdk_next.server.next.event.events import *
from modsdk_next.server.next.World import world

class ModSDKNextServerSystem(serverApi.GetServerSystemCls()):

    def __init__(self, namespace, name):
        super(ModSDKNextServerSystem, self).__init__(namespace, name)
        print("ModSDKNextServerSystem.__init__")
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
                            'LoadServerAddonScriptsAfter', self, self.OnLoadServerAddon)

    def OnLoadServerAddon(self, args):
        self.demo()
        print("ModSDKNextServerSystem.OnLoadServerAddon")

    def demo(self):
        def onEffectAdd(event):  # type: (AddEffectEvent) -> None
            entityId = event.entityId
            effectName = event.effectName
            entity = event.getEntity()
            motion = entity.getMotion()
            print("Entity {} has motion {}".format(entityId, str(motion)))
        world.events.entityEffectAdd.subscribe(onEffectAdd)