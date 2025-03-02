# -*- coding: utf-8 -*-
from mod.common.utils.timer import CallLater
import mod.server.extraServerApi as serverApi

if False:
    from typing import Callable, Any, Union, Generator


class System(object):

    def runJob(self, coroutine_or_func, callback=None):
        # type: (Union[Generator, Callable[[], Generator]], Callable | None) -> Generator
        """
        启动协程任务，分段执行带 yield 的逻辑，避免一次性计算导致游戏卡顿。

        参数:
            coroutine_or_func: 带有 yield 的生成器对象，或者一个返回生成器的函数。
                               若传入函数，则从头开始执行协程。
            callback: 协程执行完毕后的回调函数，默认为 None。

        返回值:
            返回由 StartCoroutine 启动的协程对象，
            外部可将该对象传入 clearJob 停止协程。
        """
        # 调用网易 modsdk 的 StartCoroutine 接口启动协程
        coroutine = serverApi.StartCoroutine(coroutine_or_func, callback)
        return coroutine

    def clearJob(self, coroutine):
        """
        停止指定的协程任务。

        参数:
            coroutine: 通过 runJob 返回的协程对象。
        """
        serverApi.StopCoroutine(coroutine)

    def run(self, callback, args = None, kwargs = None):
        # type: (Callable[[], None], Any, Any) -> CallLater
        """
        在下一tick执行代码
        :param callback: 触发函数
        :param args: 变长参数，可以不设置
        :param kwargs: 字典变长参数，可以不设置
        :return: CallLater 返回单次触发的定时器实例，传入func不是函数类型时返回None
        """
        comp = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
        return comp.AddTimer(0.0, callback, args, kwargs)

    def runTimeout(self, callback, secondsDelay = 0.0, args = None, kwargs = None):
        # type: (Callable[[], None], float, Any, Any) -> CallLater
        """
        延迟执行
        :param callback: 定时器触发函数
        :param secondsDelay: 延迟时间，单位秒
        :param args: 变长参数，可以不设置
        :param kwargs: 字典变长参数，可以不设置
        :return: CallLater 返回单次触发的定时器实例，传入func不是函数类型时返回None
        """
        comp = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
        return comp.AddTimer(secondsDelay, callback,args, kwargs)

    def runInterval(self, callback, secondsInterval = 0.0, args = None, kwargs = None):
        # type: (Callable[[], None], float, Any, Any) -> CallLater
        """
        循环执行
        :param callback: 定时器触发函数
        :param secondsInterval: 间隔时间，单位秒
        :param args: 变长参数，可以不设置
        :param kwargs: 字典变长参数，可以不设置
        :return: CallLater 返回循环触发的定时器实例，传入func不是函数类型时返回None
        """
        comp = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
        return comp.AddRepeatedTimer(secondsInterval, callback, args, kwargs)

    def clearRun(self, callLater):
        """
        取消定时器
        :param callLater: 定时器实例
        """
        comp = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
        comp.CancelTimer(callLater)