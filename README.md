# MC ModSDK Next

更加轻量化和易用的 我的世界中国版 ModSDK 框架!
模仿和学习国际版Scripting API的设计思路，从代码提示层面。

# 这只是一个思路 DEMO！实现了部分功能，但还未完工和测试。

## 解决的一些痛点

```python
from modsdk_next.server.next.World import world

def onEffectAdd(event):  # type: (AddEffectEvent) -> None
    # 通过event类型标注，可以轻松的知道event的内有哪些数据
    entityId = event.entityId
    effectName = event.effectName
    print("Entity {} has add effect {}".format(entityId, effectName))
    # 更直观且性能损失极小的面向对象写法
    entity = event.getEntity()
    motion = entity.getMotion()
    print("Entity motion: {}".format(motion))
    
# 链式调用，将整理后的事件名称显示在了代码提示中，无需查找文档即可找到自己要的事件
world.events.entityEffectAdd.subscribe(onEffectAdd)
```