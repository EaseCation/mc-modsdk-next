import mod.server.extraServerApi as serverApi
if False:
    from server.ModSDKNextServerSystem import ModSDKNextServerSystem

class Util(object):

    serverSystem = None  # type: ModSDKNextServerSystem | None

    @staticmethod
    def getServerSystem():
        if Util.serverSystem is None:
            Util.serverSystem = serverApi.GetSystem("ModSDKNext", "ModSDKNextServerSystem")
        return Util.serverSystem