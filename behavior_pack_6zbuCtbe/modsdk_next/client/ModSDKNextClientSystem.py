# -*- coding: utf-8 -*-

import mod.client.extraClientApi as clientApi


class ModSDKNextClientSystem(clientApi.GetClientSystemCls()):

    def __init__(self, namespace, name):
        super(ModSDKNextClientSystem, self).__init__(namespace, name)