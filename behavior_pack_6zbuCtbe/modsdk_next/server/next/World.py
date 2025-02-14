# -*- coding: utf-8 -*-
import mod.server.extraServerApi as serverApi
from .event.WorldEvents import WorldEvents

class World(object):

    def __init__(self):
        self.levelId = serverApi.GetLevelId()
        self.events = WorldEvents()

world = World()