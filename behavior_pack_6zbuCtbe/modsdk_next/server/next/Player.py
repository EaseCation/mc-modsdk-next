from modsdk_next.server.next.Entity import Entity


class Player(Entity):

    def __init__(self, playerId):
        super(Player, self).__init__(playerId)

