import contextlib
import time


@contextlib.contextmanager
def 计时(名字):
    开始时间 = time.time()
    yield
    print(f'「{名字}」用时:', time.time()-开始时间)


帧率计冷却时间 = 3
帧率计平均用时 = {}
@contextlib.contextmanager
def 帧率计(名字):
    global 帧率计冷却时间, 帧率计平均用时
    开始时间 = time.time()
    yield
    用时 = time.time() - 开始时间
    if 名字 not in 帧率计平均用时:
        帧率计平均用时[名字] = 用时
    帧率计平均用时[名字] = 0.9*帧率计平均用时[名字] + 0.1*用时
    帧率计冷却时间 -= 用时
    if 帧率计冷却时间 < 0:
        帧率计冷却时间 += 1
        for k, v in 帧率计平均用时.items():
            print(f'「{k}」帧率: %.2f' % (1/v))
