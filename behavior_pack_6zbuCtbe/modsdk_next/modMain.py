# -*- coding: utf-8 -*-

from mod.common.mod import Mod
import mod.client.extraClientApi as clientApi
import mod.server.extraServerApi as serverApi

@Mod.Binding(name="ModSDKNext", version="1.0")
class HitMod(object):
    def __init__(self):
        pass

    @Mod.InitServer()
    def initMod(self):
        serverApi.RegisterSystem(
            "ModSDKNext",
            "ModSDKNextServerSystem",
            "modsdk_next.server.ModSDKNextServerSystem.ModSDKNextServerSystem"
        )

    @Mod.InitClient()
    def init(self):
        clientApi.RegisterSystem(
            "ModSDKNext",
            "ModSDKNextClientSystem",
            "modsdk_next.client.ModSDKNextClientSystem.ModSDKNextClientSystem"
        )
