# -*- coding: utf-8 -*-
import mod.server.extraServerApi as serverApi

from modsdk_next.Util import Util

class EventCallback(object):
    def __init__(self, callback):
        self.callback = callback

    def call(self, args):
        self.callback(args)


class BaseEventSignal(object):

    __slots__ = ["_subscribedCallbacks", "eventName"]

    def __init__(self, eventName):
        self._subscribedCallbacks = {}
        self.eventName = eventName

    def _subscribe(self, callback, cb):
        eventCallback = EventCallback(cb)
        self._subscribedCallbacks[callback] = eventCallback
        Util.getServerSystem().ListenForEvent(
            serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
            self.eventName, eventCallback, eventCallback.call
        )

    def unsubscribe(self, callback):
        if callback in self._subscribedCallbacks:
            eventCallback = self._subscribedCallbacks[callback]
            Util.getServerSystem().UnListenForEvent(
                serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
                self.eventName, eventCallback, eventCallback.call
            )
            del self._subscribedCallbacks[callback]
